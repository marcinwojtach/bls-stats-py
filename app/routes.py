from flask import redirect, render_template, Response, request
from . import app
from .controllers import PlayerController, TeamController, HomeController


@app.route('/')
def index():
    return render_template('index.html', data=HomeController().index())


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/profile/<profile_id>')
def profile_user_stats(profile_id):
    return render_template('profile.html', data=PlayerController(profile_id).index())


@app.get('/hx/team/<team_id>/modal-body')
def get_team_modal_body(team_id):
    return render_template('partials/team_dialog_body.html', data=TeamController().index(team_id))


@app.get('/hx/profile/<profile_id>/scores/highest')
def get_profile_scores_highest(profile_id):
    return Response(
        f'<img src="data:image/png;base64,{PlayerController(profile_id).highest_scores_chart_base64(PlayerController.serialize_params(request.args))}">',
        mimetype='text/html'
    )
