#!/usr/bin/python3

class CircularBuffer:
    def __init__(self, maxSize) -> None:
        self.__maxSize = maxSize
        self.__buffer = list()

    def add(self, value):
        self.__buffer.append(value)
        if len(self.__buffer) > self.__maxSize:
            del self.__buffer[0]

    def __len__(self):
        return len(self.__buffer)

    def __getitem__(self, value):
        return self.__buffer[value]