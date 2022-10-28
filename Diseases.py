import pandas as pd
import numpy as np


class Disease:
    def __init__(self, name, cases_filename=None, death_filename=None):
        if cases_filename is None:
            cases_filename = f'Estimated number of {name} cases'
        if death_filename is None:
            death_filename = f'Estimated number of {name} deaths'

        cases_data = self.get_useful_data_from_csv(cases_filename)
        death_data = self.get_useful_data_from_csv(death_filename)

        self.name = name
        self.data = self.merge_cases_and_death_data(cases_data, death_data)

    @staticmethod
    def get_useful_data_from_csv(filename):
        return pd.read_csv(f'data/{filename}.csv')[
            ['Period', 'Location', 'FactValueNumericLow', 'FactValueNumeric', 'FactValueNumericHigh']
        ].sort_values(['Location', 'Period']).fillna(0)

    @staticmethod
    def merge_cases_and_death_data(cases_data, death_data):
        return pd.DataFrame(
            np.array([
                cases_data.Period,
                cases_data.Location,
                cases_data.FactValueNumericLow.astype(int),
                cases_data.FactValueNumeric.astype(int),
                cases_data.FactValueNumericHigh.astype(int),
                death_data.FactValueNumericLow.astype(int),
                death_data.FactValueNumeric.astype(int),
                death_data.FactValueNumericHigh.astype(int),
            ]).transpose(),
            columns=[
                'Year',
                'Region',
                'Cases(low)',
                'Cases',
                'Cases(high)',
                'Death(low)',
                'Death',
                'Death(high)',
            ]
        )


Malaria = Disease('Malaria')

DISEASES = [Malaria]
