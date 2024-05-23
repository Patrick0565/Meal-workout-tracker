"""
controller.py
by Patrick Hudson

json reading and writing from
Reading and Writing JSON to a File in Python
https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

"""
import json

def get_workout_list():
    output = ""
    with open('data/workouts.json', 'r') as openfile:
        workout_list = json.load(openfile)
    output = format_workout_list(workout_list)
    return output

def format_workout_list(workout_list):
    output = ""
    for workout in workout_list:
        title, workout_type, start, notes = workout.values()
        output += f"<h2>Title: {title}</h2>"
        output += f"<p><b>Workout type: {workout_type}</b></p>"
        output += f"<p><b>Start time: {start}</b></p>"
        output += f"<p><b>Notes:</b> {notes}</p>"
    return output



if __name__ == "__main__":
    get_workout_list()

