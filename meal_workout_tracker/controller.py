"""
controller.py
by Patrick Hudson

json reading and writing from
Reading and Writing JSON to a File in Python
https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

"""
import json

def get_workouts():
    with open('data/workouts.json', 'r') as openfile:
        json_object = json.load(openfile)
    return json_object

if __name__ == "__main__":
    get_workouts()