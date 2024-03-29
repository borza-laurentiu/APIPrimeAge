from flask import Flask, jsonify, Response 
import sys
from flask import jsonify
from flask import jsonify
import json
from flask import json


from datetime import datetime

app = Flask(__name__)

@app.route('/date/<birthDate>', methods=['GET', 'POST'])

def birthDate(birthDate):

    try:
        birthDate = int(float(birthDate))  

    except ValueError:
        return "ValueError: enter a number"

    year = datetime.utcnow().year
    ageInMonths = (int(year) - int(birthDate)) * 12
    
    if birthDate < 1:
        return 'value entered is less than 1'
    elif birthDate > 2022:
        return 'value exceed current year'
    else:
        ageInMonths = str(ageInMonths)
   

    return ageInMonths
