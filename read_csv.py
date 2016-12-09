import csv
from solarsystems import connect_db
import pandas

def read_csv():
    """ Read in the csv from data/solardata.csv and import it into the
    (currently empty) SQLite database, solar.db
    See schema.sql for what the database schema should look like"""
    FILEPATH = 'data/solar_data.csv'
    connection = connect_db()

    dataFile = pandas.read_csv(FILEPATH)
    dataFile.to_sql('systems', connection, if_exists='append', index=False)

if __name__ == "__main__":
    read_csv()