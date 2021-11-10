from flask import Flask, render_template, request, redirect
import os
import random

from flask.helpers import url_for

# Configuration

app = Flask(__name__)

# Routes 

def generate_name(amount):
    response = open('response.txt', 'w')
    amount = int(amount)
    ret_list = []

    names = ["Aaron", "Adam", "Adlai", "Adian", "Agatha", "Ahmed", "Ahmet", "Aimee", "Amy", "Al", "Alain", "Alastair", "Albert", "Alberto", "Alex", "Alexander"
             ]


    for i in range(amount):
        full_name = random.choice(names) + " " + random.choice(names) + " " + str(randomID())
        ret_list.append(full_name)

    for element in ret_list:
        response.write(element + "\n")

    response.close()

    return ret_list


def randomID():
    rand = random.randint(1000, 9999)
    return rand



@app.route('/', methods =['POST', 'GET'])
def my_form_post():
    if request.method == "POST":
        text = request.form["num"]
        converted = generate_name(text)
        return render_template("display.j2", data=converted)
        
    
    else: 
        return render_template("namegenerator.j2")


# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 1609)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port) 