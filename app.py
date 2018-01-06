import os
from flask import Flask

app=Flask(__name__)

@app.route('/')
def name():
   return("python is love ")

@app.route('/user')
def name1():
   return("python is Wonderfull language")

#if __name__ == '__main__':
 #      app.run(debug=True, host='0.0.0.0')
PORT =int( os.environ.get("PORT"))

app.run(debug=True,host='0.0.0.0',port=PORT)

print("app is run in thois port",PORT)