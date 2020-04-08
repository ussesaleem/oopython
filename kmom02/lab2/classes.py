"""
Classes to be used in lab2.
"""

class Person():
    """
    Class for a Person.
    """
    def __init__(self, name, ssn, address=""):
        """
        Initiate a new person with name, ssn and address.
        """
        self.name = name
        self._ssn = ssn
        self.set_address(address)

    def get_ssn(self):
        """
        Get the hidden ssn.
        """
        return self._ssn

    def set_address(self, address):
        """
        Set the person's address
        """
        if address == "":
            self.address = Address("", "", "")
        else:
            self.address = address

    def to_string(self):
        """
        Return the information in a string.
        """
        return "Name: {name} SSN: {ssn} {address}".format(
            name=self.name,
            ssn=self.get_ssn(),
            address=self.address.to_string()
        )


class Address():
    """
    Class to add an address.
    """
    def __init__(self, city, state, country):
        """
        Initiate a new address.
        """
        self.city = city
        self.state = state
        self.country = country

    def to_string(self):
        """
        Return the address in a string.
        """
        return "Address: {city} {state} {country}".format(
            city=self.city,
            state=self.state,
            country=self.country
        )



class Teacher(Person):
    """
    Class for a Teacher.
    """
    def __init__(self, name, ssn, address, courses=None):
        """
        Initiate a new Teacher object using information from Person class.
        """
        super().__init__(name, ssn, address)
        if courses is None:
            courses = []
            if courses == isinstance(courses, list):
                self.courses = courses
            else:
                self.courses = list(courses)

    def add_course(self, course):
        """
        Add courses to the courses list.
        """
        if course == isinstance(course, list):
            self.courses.extend(course)
        else:
            self.courses.append(course)

    def remove_course(self, course):
        """
        Remove courses to the courses list.
        """
        if course == isinstance(course, list):
            for c in course:
                if c in self.courses:
                    self.courses.remove(c)
        else:
            self.courses.remove(course)

    def courses_string(self):
        """
        Create a string with the courses from courses list.
        """
        course_string = ""
        for c in self.courses[0]:
            course_string += c + ", "
        course_string = course_string[:-2]
        return course_string

    def to_string(self):
        """
        Return a string with the information from Person, Address and courses.
        """
        return "{base_msg} Courses: {courses}".format(
            base_msg=super().to_string(),
            courses=self.courses_string()
        )

class Student(Person):
    """
    Class for Student.
    """
    def __init__(self, name, ssn, address, courses_grades=None):
        """
        Initiate a new Student object using information from Person class.
        """
        super().__init__(name, ssn, address)
        if courses_grades is None:
            courses_grades = []
            if courses_grades == isinstance(courses_grades, list):
                self.courses_grades = courses_grades
            else:
                self.courses_grades = list(courses_grades)

    def add_course_grade(self, course, grade):
        """
        Add courses and grades and turn them into tuples.
        """
        course_grade_tuple = (course, grade)
        self.courses_grades.append(course_grade_tuple)

    def average_grade(self):
        """
        Calculate the average grade of a Student.
        """
        grade_sum = 0
        grades_length = 0
        for c in self.courses_grades:
            if c[1] != "-":
                grade_sum += int(c[1])
                grades_length += 1
        average = grade_sum / grades_length
        return average
