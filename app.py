import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
   return "Welcome pythn flask from Docker!!"

@app.route('/how are you')
def hello():
   return "I'm good, how are you?"


if __name__ == '__main__':
    app.run()