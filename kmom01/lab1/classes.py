"""
File with classes for lab1.
"""

class Cat():
    """
    Create cat objects.
    """
    eye_color = "blue"
    name = "Soft Kitty"

    def __init__(self, eye_color, name):
        """
        Create new cat objects.
        """
        self.eye_color = eye_color
        self.name = name
        self._lives_left = -1

    def get_lives_left(self):
        """
        Returns how many lives the cats have left.
        """
        return self._lives_left

    def set_lives_left(self, x):
        """
        To set the lives a cat has.
        """
        self._lives_left = x

    def description(self):
        """
        Describes the cat; name, eye-color and lives.
        """
        return ("My cats name is {n}, has ".format(n=self.name) +
                "{e} eyes and ".format(e=self.eye_color) +
                "{l} lives left to live.".format(l=self._lives_left))

    @staticmethod
    def nr_of_paws(paws=4):
        """
        Returns how many paws the cat has.
        """
        return paws

class Duration():
    """
    Create duration objects.
    """
    hours = 0
    minutes = 0
    seconds = 0

    def __init__(self, hours, minutes, seconds):
        """
        Creates new durations.
        """
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self.hours_string = ""
        self.minutes_string = ""
        self.seconds_string = ""

    def display(self):
        """
        Returns the time in the format hh-mm-ss.
        """
        if int(self.hours) < 10:
            self.hours_string = str(0) + str(self.hours)
        else:
            self.hours_string = str(self.hours)
        if int(self.minutes) < 10:
            self.minutes_string = str(0) + str(self.minutes)
        else:
            self.minutes_string = str(self.minutes)
        if int(self.seconds) < 10:
            self.seconds_string = str(0) + str(self.seconds)
        else:
            self.seconds_string = str(self.seconds)
        time = (self.hours_string + "-" + self.minutes_string + "-" +
                self.seconds_string)
        return time

    @staticmethod
    def duration_to_sec(time):
        """
        Converts the duration into seconds.
        """
        time = time.split("-")
        hours = int(time[0])
        minutes = int(time[1])
        seconds = int(time[2])

        hours_to_sec = hours * 3600
        minutes_to_sec = minutes * 60
        all_seconds = hours_to_sec + minutes_to_sec + seconds
        return all_seconds

    def __add__(self, other):
        """
        Addition of durations in seconds.
        """
        return (self.duration_to_sec(self.display()) +
                other.duration_to_sec(other.display()))

    def __iadd__(self, other):
        """
        Changes the self-duration by adding the other duration.
        """
        self.hours += other.hours
        self.minutes += other.minutes
        self.seconds += other.seconds
        return self
