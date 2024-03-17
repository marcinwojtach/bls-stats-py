from flask import redirect, render_template, make_response


from . import app
from .scraping.profile_page import ProfilePage
from .services.bls_page_http import BlsPageHttp


@app.route('/')
def index():
    # TODO: think about starting page
    return redirect('/profile/869')




@app.route('/profile', defaults={ 'profile_id': -1 })
@app.route('/profile/<profile_id>')
def profile_user_stats(profile_id: int):
    if profile_id == -1:
        return 'Handle default profile_id : )'

    profile_information_response = BlsPageHttp.get_profile_information(profile_id)
    profile_career_response = BlsPageHttp.get_profile_career(profile_id)
    profile_page = ProfilePage(profile_id, profile_information_response.text, profile_career_response.text).call()
    return render_template(
        'profile.html',
        player=profile_page['player'],
        season_details=profile_page['season_details'],
        career_details=profile_page['career_details'],
    )


@app.route('/clicked')
def click_me_test():
    return make_response('Jest git!', 200)
