import os
import sqlite3
from flask import Flask, g

app = Flask(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'solar.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default',
    GMAPS_API_KEY='AIzaSyDXnvvP3ZBMRscLUy12TKQCpuXE6s8kiQc'
))
app.config.from_envvar('SOLARSYSTEMS_SETTINGS', silent=True)

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def init_db():
    """Initializes the database."""
    db = get_db()
    schema_path = os.path.join(app.root_path, 'schema.sql')
    with app.open_resource(schema_path, mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    print "Database initialized"


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db



print __name__
@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

import solarsystems.views
