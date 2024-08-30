from flask import redirect, render_template, Response
from . import app
from app.shared import state
from .controllers import HomeController, PlayerController


@app.route('/')
def index():
    # TODO: think about starting page
    controller = HomeController(state['default_team_id'])
    return render_template('index.html', data=controller.index())


@app.route('/profile/<profile_id>')
def profile_user_stats(profile_id):
    controller = PlayerController(profile_id)
    return render_template('profile.html', data=controller.index())


@app.route('/hx/profile/<profile_id>/scores/highest')
def profile_scores_highest(profile_id):
    controller = PlayerController(profile_id)
    return Response(
        f'<img src="data:image/png;base64,{controller.highest_scores_chart_base64()}">',
        mimetype='text/html'
    )
