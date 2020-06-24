import os
import platform
import subprocess
from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
     return 'Welcome to my first API/container'

@app.route('/hostname', methods=['POST','GET'])
def hostnm():
    hn = subprocess.run('hostname',capture_output=True,text=True,shell=True)
    return hn.stdout

@app.route('/systeminfo',methods=['POST','GET'])
def sysinfo():
    systype = platform.system()
    if systype == 'Windows':
        si = subprocess.run('systeminfo', capture_output=True, text=True, shell=True)
        return si.stdout
    else:
        cp = subprocess.run('lscpu', capture_output=True, text=True, shell=True)
        return cp.stdout