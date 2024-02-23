#!/usr/bin/python3

class Time:
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    @property
    def hours(self):
        return self.__hours

    @hours.setter
    def hours(self, hours):
        if hours < 0 or hours > 23:
            raise ValueError()

        self.__hours = hours

    @property
    def minutes(self):
        return self.__minutes

    @minutes.setter
    def minutes(self, minutes):
        if minutes < 0 or minutes > 59:
            raise ValueError()

        self.__minutes = minutes

    @property
    def seconds(self):
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds):
        if seconds < 0 or seconds > 59:
            raise ValueError()

        self.__seconds = seconds