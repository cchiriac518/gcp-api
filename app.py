import os
import platform
import subprocess
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
     return 'Welcome to my first API/container'