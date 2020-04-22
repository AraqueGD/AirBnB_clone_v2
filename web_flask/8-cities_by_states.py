#!/usr/bin/python3
from models import storage
from models.state import State
from models.city import City
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(error):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return (render_template('7-states_list.html', states=states))


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    cities = storage.all(City).values()
    cities = sorted(cities, key=lambda k: k.name)
    return (render_template('7-states_list.html', cities=cities))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
