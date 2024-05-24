"""
controller.py
by Patrick Hudson

json reading and writing from
Reading and Writing JSON to a File in Python
https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/

"""
import json

def get_workouts():
    output = get_workout_list() 
    output = format_workout_list(output)
    return output

def get_workout_list():
    with open('data/workouts.json', 'r') as openfile:
        workout_list = json.load(openfile)
    return workout_list

def format_workout_list(workout_list):
    output = ""
    for workout in workout_list:
        title, workout_type, start, notes = workout.values()
        output += f"<h2 style='color: #76ABAE;'> {title}</h2>"
        output += f"<p><b style='color: #76ABAE;'>Exercises: </b>{workout_type}</p>"
        output += f"<p><b style='color: #76ABAE;'>Start time: </b>{start}</p>"
        output += f"<p><b style='color: #76ABAE;'>Notes:</b> {notes}</p>"
        
    return output

def store_workout(title, exercise, start_time, notes):
    # create dictionary
    workout = {"title": title, 
               "type": exercise,
               "start_time": start_time,
               "notes": notes,
               }
  
    # get all workouts
    workouts = get_workout_list()
    workouts = edit_workouts(workouts, workout)
    save_workouts(workouts)

def edit_workouts(workouts, new_workout):
    # add new workout
    workouts.append(new_workout)

    # loop through workouts and remove sample
    has_sample = False
    for i in range(len(workouts)):
        title = workouts[i].get("title")
        if "Sample" in title:
            has_sample = True
            break
    if has_sample:
        workouts.pop(i)
    return workouts

# 
def save_workouts(workouts):
    with open('data/workouts.json', 'w') as openfile:
        json.dump(workouts, openfile)
        openfile.close()
      
        
    

if __name__ == "__main__":
    get_workout_list()

