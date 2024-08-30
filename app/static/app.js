function dialogs() {
  Array.from(document.querySelectorAll('[for-dialog]')).forEach((trigger) => {
    trigger.addEventListener('click', () => {
      const dialog = document.getElementById(trigger.getAttribute('for-dialog'));
      !dialog.open ? dialog.showModal() : dialog.close();
    })
  })
}

window.onload = () => {
  dialogs();
};