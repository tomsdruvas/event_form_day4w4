from flask import render_template
from app import app
from models.event import Event
from models.events import events


@app.route('/events')
def index():
    return render_template('index.html', title='Event Home', events=events)
