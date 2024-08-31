function dialogs() {
  Array.from(document.querySelectorAll('[for-dialog]')).forEach((trigger) => {
    trigger.addEventListener('click', () => {
      const dialog = document.getElementById(trigger.getAttribute('for-dialog'));
      const resetContainer = dialog.querySelector(trigger.getAttribute('with-reset'));
      const resetContent = trigger.getAttribute('with-reset-content');
      if (!dialog.open) {
        dialog.showModal();
        document.body.classList.add('dialog-open');
      } else {
        dialog.close();
        resetContainer && (resetContainer.innerHTML = resetContent ?? '');
        document.body.classList.remove('dialog-open');
      }
    })
  })
}

function theme() {
  const themes = {
    light: {
      icon: '&#x263D;',
      theme: 'light'
    },
    dark: {
      icon: '&#x2600;',
      theme: 'dark'
    },
  }
  const $html = document.querySelector('html');
  const loadedTheme = window.localStorage.getItem('theme') ?? 'light';

  function toggleTheme() {
    const currentTheme = themes[$html.getAttribute('data-theme')];
    $html.setAttribute(
      'data-theme',
      currentTheme.theme === themes.light.theme ? themes.dark.theme : themes.light.theme
    );
    this.innerHTML = themes[$html.getAttribute('data-theme')].icon;
    window.localStorage.setItem('theme', $html.getAttribute('data-theme'))
  }

  Array.from(document.querySelectorAll('[data-theme-switcher]')).forEach((trigger) => {
    trigger.addEventListener('click', toggleTheme)
    trigger.innerHTML = themes[loadedTheme].icon;
  });

  $html.setAttribute('data-theme', window.localStorage.getItem('theme') ?? 'light')
}

window.onload = () => {
  dialogs();
  theme();
};