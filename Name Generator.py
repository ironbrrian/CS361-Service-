from flask import Flask, render_template, request, redirect
import os
import random
from time import sleep 

from flask.helpers import url_for

# Configuration

app = Flask(__name__)

# Routes 
def randomID():
    rand = random.randint(1000, 9999)
    return rand


while True: 

    response = open('response.txt', 'w')
    ret_list = []

    names = ["Aaron", "Adam", "Adlai", "Adian", "Agatha", "Ahmed", "Ahmet", "Aimee", "Amy", "Al", "Alain", "Alastair", "Albert", "Alberto", "Alex", "Alexander"
             , "Barney", "Barrett","Bart","Barton", "Bob","Calvin", "Carl", "Carlos", "Carol", "Cathy","Dana", "Daren", "Dave", "David", 
             "Richard", "Ed", "Eva", "Eileen","Elsa","Guy", "Hans", "Hank","Harold","Harry", "Jacob","Jenny","Jason", "Jones","Kiki","Jones","Linda"
             , "Neville", "Oleg","Ralph", "Rodger", "Terry","Tuan","Lee", "Nguyen","Victoria","Winnie", "Woody"]


    full_name = random.choice(names) + " " + random.choice(names) + " " + str(randomID())
    ret_list.append(full_name)
    print(full_name)

    for element in ret_list:
        response.write(element + "\n")

    response.close()

    sleep(5) 


# def randomID():
#     rand = random.randint(1000, 9999)
#     return rand



# @app.route('/', methods =['POST', 'GET'])
# def my_form_post():
#     if request.method == "POST":
#         text = request.form["num"]
#         converted = generate_name(text)
#         return render_template("display.j2", data=converted)
        
    
#     else: 
#         return render_template("namegenerator.j2")


# # Listener

# if __name__ == "__main__":
#     port = int(os.environ.get('PORT', 1609)) 
#     #                                 ^^^^
#     #              You can replace this number with any valid port
    
#     app.run(port=port) 