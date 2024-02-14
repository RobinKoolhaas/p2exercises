#!/usr/bin/python3

def card_value(string):
    if(string == "Jack"):
        return 11
    
    if(string == "Queen"):
        return 12

    if(string == "King"):
        return 13
    
    if(string == "Ace"):
        return 1
    
    return int(string)