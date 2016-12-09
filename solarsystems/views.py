from flask import render_template
from solarsystems import app, get_db
import json

@app.route("/")
def hello():
    """
    Create a view function here that grabs the solar systems from the database
    and serves the info to the front-end
    """
    # your code goes here
    return render_template('index.html')

@app.route('/systems')
def getData():
    db = get_db()
    db = db.cursor()
    data = db.execute('SELECT * FROM SYSTEMS').fetchall()
    dataJson = json.dumps( [dict(ix) for ix in data] ) 
    return dataJson