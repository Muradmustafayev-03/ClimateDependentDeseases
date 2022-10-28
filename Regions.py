from Diseases import DISEASES


class Region:
    def __init__(self, name, population, super_region: object = None, subregions: list[object] = None):
        self.name = name
        self.population = population

        self.diseases_data = {
            disease.name: disease.data[disease.data.Region == name]
            for disease in DISEASES
        }
        self.climate_data = self.get_climate_data()
        self.coordinates = self.get_coordinates()

        self.super_region = super_region
        self.subregions = subregions

    @staticmethod
    def get_climate_data():
        return

    @staticmethod
    def get_coordinates():
        return
