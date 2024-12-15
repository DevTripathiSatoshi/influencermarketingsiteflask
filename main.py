from flask import Flask, render_template
import requests
#from threading import Thread
app = Flask(__name__)
from flask import request
from flask import jsonify
#from pymongo import MongoClient
#client = MongoClient('mongodb+srv://satosi:<satosi>@cluster0.qnronfw.mongodb.net/?retryWrites=true&w=majority')
#db = client['website']
'''lient = MongoClient("mongodb+srv://satosi:satosi@cluster0.qnronfw.mongodb.net/?retryWrites=true&w=majority")
db = client.website
data = db.wmail
req = db.botreq '''

from flask import send_from_directory

@app.route('/static/<path:filename>')
def custom_static(filename):
    return send_from_directory('static', filename, mimetype='audio/mpeg')


@app.route('/',methods=('GET', 'POST'))
def main():
  return render_template('index.html')

@app.route('/aboutus',methods=('GET', 'POST'))
def aboutus():
  return render_template('aboutus.html')



'''

@app.errorhandler(404)
def pagenotfound(e):
 return render_template('404.html')

@app.route('/UD/')
def UD():
    return render_template('underdevelopment.html')

'''

app.run(host='0.0.0.0', port=8080)