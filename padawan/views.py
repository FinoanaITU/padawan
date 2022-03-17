from flask import Flask, jsonify
from padawan.sources.recherche import recherche
from flask_cors import CORS, cross_origin
app = Flask(__name__)
CORS(app, support_credentials=True)
# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

@app.route('/')
def index():
        return "Hello world !"

@app.route('/findListPeople',methods=['POST'])
@cross_origin(supports_credentials=True)
def find():
        result = recherche().peopleList()
        return jsonify(result)
        
if __name__ == "__main__":
        app.run()
