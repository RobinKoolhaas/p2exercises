class Student:
    def __init__(self, name):
        self.name = name
        self.__courses = dict()

    def calculate_letter_grade(self, score):
        if score >= 90:
            return "A"
        if score >= 80 and score <= 89:
            return "B"
        if score >= 70 and score <= 79:
            return "C"
        if score >= 60 and score <= 69:
            return "D"
        
        return "F"

    def add_course(self, course_name, score):
        self.__courses[course_name] = self.calculate_letter_grade(score)

    def get_courses(self):
        return self.__courses