###################################
#INICIAR APP flask = set FLASK_APP = main.py
#set FLASK_DEBUG=1 --> crear web con habilidad de debug
#flask run --> ejecutar el servidor flask
###################################
from flask import Flask
from flask import render_template,jsonify

# __name__ = file that is running directly from the file that i am in
app = Flask(__name__)

# Flask works with function and the values you return might be visualized on the web server
#Pieces of code that that are running prior the function and its helpful beecause the code next the @
# will be executed before the function
@app.route('/data_json')
def data_json():
    dummy_data = [
        {
            "id": 1,
            "starting_time": "09:00",
            "team_a": "Random Team 1",
            "score": "5 - 1",
            "team_b": "Random Team 2",
            "minute": "05:00",
        },
        {
            "id": 2,
            "starting_time": "20:05",
            "team_a": "Random Team 3",
            "score": "4 - 3",
            "team_b": "Random Team 4",
            "minute": "05:00",
        },
    ]
    return jsonify(dummy_data)

@app.route('/') # / = direction of the website
def index():
    dummy_data = data_json()

    return  render_template(
        'index.html',
        matches = dummy_data.json
    )
