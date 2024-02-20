#!/usr/bin/python3

def process_data(string_data: list) -> dict:
    result = dict()

    for string in string_data:
        string = string.split(",")

        result[string[0]] = {"age":int(string[1]),"courses":string[2:]}

    return result

def average_age(data: dict):
    sum = 0
    
    for value in data.values():
        sum += int(value["age"])

    return sum / len(data)

def courses(data: dict):
    result = set()

    for value in data.values():
        for course in value["courses"]:
            result.add(course)

    return result

def most_common_courses(data: dict):
    courseDict = dict()

    for value in data.values():
        for course in value["courses"]:
            courseDict[course] = courseDict.get(course, 0) + 1

    return set(key for key, value in courseDict.items() if value == max(courseDict.values()))