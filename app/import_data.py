"""
This module contains functions to import data from CSV files into the database.
Assumptions:
1. The CSV files are located in the data/csv directory.
2. All files are named in the format <model_name>-<year>.csv,
    where <model_name> is the name of the model class and <year> is the year of the data.
    For example, DistanceTravelledToWork-2011.csv.
3. The first row of each CSV file contains the column names.
4. The column names in the CSV files match the attribute names of the model classes in this way:
    - Lower case
    - Replace spaces with underscores
"""
import os
import pandas as pd
from sqlalchemy.exc import IntegrityError
from app import db
from app.models import (DistanceTravelledToWork, MethodOfTravelToWork,
                        EconomicActivity, HoursWorked, NSSEC, Occupation)


def import_data_from_csv(model_class, year, csv_path):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_path)
    # Rules for column names: lower case and replace spaces with underscores
    df.columns = [col.strip().replace('-', ' ').replace(':', '').replace(';', '')
                  .replace(' ', '_').lower() for col in df.columns]
    # Add the year to the DataFrame
    df['year'] = year
    # Iterate over the rows of the DataFrame and add each row as a new item in the database
    for _, row in df.iterrows():
        try:
            item = model_class(**row.to_dict())
            db.session.add(item)
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


def import_all_data():
    csv_dir = 'data/csv'
    for filename in os.listdir(csv_dir):
        name, year = filename.split('-')
        year = year.split('.')[0]

        if name == 'DistanceTravelledToWork':
            model_class = DistanceTravelledToWork
        elif name == 'MethodOfTravelToWork':
            model_class = MethodOfTravelToWork
        elif name == 'EconomicActivity':
            model_class = EconomicActivity
        elif name == 'HoursWorked':
            model_class = HoursWorked
        elif name == 'NSSEC':
            model_class = NSSEC
        elif name == 'Occupation':
            model_class = Occupation
        else:
            continue
        print(f'Importing {filename} into {model_class.__name__}')
        import_data_from_csv(model_class, year, os.path.join(csv_dir, filename))
