"""
Contains classes to be used in Flask assignment.
"""

import json
import datetime


class Person():
    """
    Creates a person
    """
    def __init__(self, name):
        """
        Gets the person's name.
        """
        self.set_person(name)

    def set_person(self, name):
        """
        Open json file and get data
        """
        file_name = name + ".json"
        data_from_json = json.load(open(file_name, encoding="UTF-8"))
        self.first_name = data_from_json["firstname"]
        self.sur_name = data_from_json["surname"]
        self.name = self.first_name + " " + self.sur_name
        self._birthdate = data_from_json["dob"]
        self.image = data_from_json["img"]

    def age(self):
        """
        Calculates the age of the person
        """
        birth = self._birthdate.split("-")
        birth_year = int(birth[0])
        birth_month = int(birth[1])
        datenow = datetime.datetime.now()
        age = datenow.year - birth_year
        age_month = datenow.month - birth_month

        if age_month <= 1:
            age = age - 1
        else:
            age = age
        return age

    def get_dp(self):
        """
        Returns the profile picture.
        """
        return "static/images/" + self.image

if __name__ == "__main__":
    pers = Person('usama')
