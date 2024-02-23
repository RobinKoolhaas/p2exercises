#!/usr/bin/python3

class Queue:
    def __init__(self) -> None:
        self.__queue = list()

    def add(self, item):
        self.__queue.append(item)

    def next(self):
        current = self.__queue[0]
        del self.__queue[0]
        return current

    def is_empty(self):
        return len(self.__queue) == 0