from flask import Flask
from systeminfo2 import main
from app import app

@app.route('/')
def displayMachineInfo():
    return "This is my machine info " + main.main()
