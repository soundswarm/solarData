# README #

### Project instructions ###
For this project, we are giving you a small Flask webapp with a data CSV. We want you to do the following:

1. Import the CSV into a SQLite database
2. Display information about the solar panel systems in a meaningful way.

For #2, some ideas for this might be:

* a small chart comparing panel performance between systems
* a map showing where the solar panels are, with some information about the panels.

You'll want to edit the following files:

* `read_csv.py`
* `solarsystems/views.py`
* `solarsystems/templates/index.html`
* `solarsystems/static/css/style.css` (optional)
* `solarsystems/static/js/index.js` (optional)



### Setup instructions ###
 * install virtualenv on your laptop, if you don't already have it: [https://virtualenv.pypa.io/en/stable/installation/](https://virtualenv.pypa.io/en/stable/installation/)
 * activate your virtual environment with `source env/bin/activate`
 * once inside your virtual environment, run `pip install flask` to install the Flask web framework
 * in the fullstack-takehome folder, run `python runserver.py`. Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000), and you should see a website there that just says "My Demo".
 * To initialize the solar database, run `python init_db.py`. This initializes a sqlite3 database in the file `solarsystems/solar.db`. To browse the database, type `sqlite3 solarsystems/solar.db` (and `.quit` to get out)


### Helpful hints ###
 * [https://docs.python.org/2/library/sqlite3.html](https://docs.python.org/2/library/sqlite3.html)
 * An AJAX call to a URL that has your data is ideal, but for this exercise, in the interest of time it's fine to JSON-encode the data and pass it in as a Jinja2 template variable. An example of how to do this would be:

    **views.py**

        from flask import render_template
        import json
        mydict = {
            "a": 1,
            "b": 2,
            "c": 3,
        }
        json.dumps(mydict)
        return render_template('index.html', mydict=mydict)


    **index.html**

        <script>
            var django_data = {{mydict|safe}};
            console.log(django_data);
        </script>


    Bonus points: What could go wrong here?