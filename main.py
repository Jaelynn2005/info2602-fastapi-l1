from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'

'''
@app.get('/students')
async def get_students():
    return data
'''

#route parameters
@app.get('/students/{id}') #path parameter to get a student with a specific ID
async def get_students(id):
    for student in data: #loops through every student in the json file and if it matches with the ID, it will return that student
        if student['id'] == id:
            return student
        
#query parameters
#GET all students or filter by preference
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students=[] #checks if pref is in the url and creates an empty list to store matches
        for student in data: #loops through every student and compared the student's pref value and once matched, it is added into the filtered_students list.
            if student['pref'] == pref:
                filtered_students.append(student) #adds the student into the list by using .append 
        return filtered_students #returns student with the preference
    return data #return all students if no preference provided

#exercise 1 
@app.get('/stats')
async def get_stats():
    stats={} 

    for student in data:
        meal = student['pref']
        if meal in stats:
            stats[meal]+=1
        else:
            stats[meal] = 1

        prog = student['programme']
        if prog in stats:
            stats[prog]+=1
        else:
            stats[prog] = 1
    return stats

#exercise 2
#addition
@app.get('/add/{a}/{b}')
async def add(a: int, b: int):
    return a+b

#subtraction
@app.get('/subtract/{a}/{b}')
async def subtract(a:int, b:int):
    return a-b

#multiply
@app.get('/multiply/{a}/{b}')
async def multiply(a:int, b:int):
    return a*b

#division
@app.get('/divide/{a}/{b}')
async def divide(a:int, b:int):
    return a/b




