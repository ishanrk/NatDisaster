from flask import Flask, request, jsonify

from dowhy import gcm
import json

import networkx as nx, numpy as np, pandas as pd

import matplotlib.pyplot as plt
from flask import Flask, request, jsonify
from flask_cors import CORS

import pymongo
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def cf_predict():
    try:
        data = request.json
        

        return True
    except:
        return False
    
       