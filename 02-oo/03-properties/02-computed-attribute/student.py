#!/usr/bin/python3

class BMICalculator:
    def __init__(self, weight_in_kg: int, height_in_m: float) -> None:
        self.weight_in_kg = weight_in_kg
        self.height_in_m = height_in_m
    
    @property
    def bmi(self):
        return self.weight_in_kg / self.height_in_m ** 2

    @property
    def category(self):
        bmi = self.bmi

        if bmi < 18.5:
            return "underweight"

        if bmi >= 18.5 and bmi <= 25:
            return "normal"

        if bmi > 25:
            return "overweight"