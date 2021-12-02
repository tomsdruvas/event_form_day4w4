from flask import render_template, request
from app import app
from models.event import Event
from models.events import events, add_new_event


@app.route('/events')
def index():
    return render_template('index.html', title='Event Home', events=events)


@app.route('/events', methods=['POST'])
def add_event():
    name_event = request.form['name_event']
    date = request.form['date']
    num_guests = request.form['num_guests']
    location = request.form['location']
    description = request.form['description']
    recurring = request.form['recurring']
    new_event = Event(date, name_event, num_guests, location, description, recurring)

    add_new_event(new_event)
    return render_template('index.html', title='Event Home', events=events)


