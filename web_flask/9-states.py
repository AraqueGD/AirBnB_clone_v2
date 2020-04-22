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


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = storage.all(State).values()
    sort_states = sorted(list(states), key=lambda k: k.name)
    cities = storage.all(City).values()
    sort_cities = sorted(list(cities), key=lambda k: k.name)
    return render_template('8-cities_by_states.html', states=sort_states,
                           cities=sort_cities)


@app.route('/states')
@app.route('/states/<id>', strict_slashes=False)
def states_id(id=None):
    states = storage.all(State).values()
    state_sort = sorted(states, key=lambda k: k.name)
    flag_state = None
    if (id is None):
        states = None
    else:
        for idx_states in states:
            if (idx_states == id):
                flag_state = idx_states
        cities = storage.all(City).values()
        cities_sort = sorted(list(cities), key=lambda k: k.name)
        return render_template('9-states.html', states=state_sort,
                               cities=cities_sort, flag_state=flag_state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
