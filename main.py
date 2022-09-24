from flask import Flask, render_template, request, redirect
app = Flask(__name__)
import pymongo
client = pymongo.MongoClient("")
newsdb = client['news']['news']
sessiondb = client['session']['session']
admindb = client['admin']['admin']
from datetime import datetime
import time
@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port=80 , debug=True)