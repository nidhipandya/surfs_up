import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#2. Create an app, being sure to pass __name__
app = Flask(__name__)

#3. Define what to do when a user goes to the index
@app.route('/')
def hello_world():
    return 'Hello world'

export FLASK_APP=app.py

set FLASK_APP=app.py