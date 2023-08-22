import imp
from flask import Flask, jsonify, render_template, request
import joblib
import numpy as np
import requests
from flask_restful import Resource, Api,reqparse
from fire import Uploader
from realtime import RealTimeDataCall

app = Flask(__name__)
upl = Uploader()
obj = RealTimeDataCall()

# apis
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('message', type=str, location='json')
class HelloWorld(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        msg = json_data['message']
        API_URL = "https://api-inference.huggingface.co/models/ANIKEThash/DialoGPT-medium-character"
        headers = {"Authorization": "Bearer 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"}

        form_data = request.form
        input = msg 

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.json()
        
        output = query({
            "inputs": input
        })
        # take input output here


        print(output['generated_text'])
        return {'data': output['generated_text']}

api.add_resource(HelloWorld, '/api')


@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/speak")
def speak_expert():
    return render_template("speak_to_an_expert.html")

# Carrer choice
@app.route("/forms")
def forms():
    return render_template("forms.html")

@app.route("/form-action", methods = ['POST', 'GET'])
def form_action():
    model = joblib.load("Model.joblib")
    form_data = request.form
    pred_arr = [form_data["location"],form_data["branch"],form_data["Marks"]]
    upl.upload_career(pred_arr)
    pred_arr = [int(elem) for elem in pred_arr]
    pred_arr = np.array(pred_arr).reshape(1, -1)
    pred = model.predict(pred_arr)[0]

    pred = pred[0].upper() + pred[1:]
    obj.runtimeCall()
    return render_template("display.html", pred=pred)

# Job
@app.route("/forms1")
def forms1():
    return render_template("forms1.html")

@app.route("/form-action1", methods = ['POST', 'GET'])
def form_action1():
    model = joblib.load("ModelJob.joblib")
    form_data = request.form
    pred_arr = [form_data["Age"], form_data["Location"], form_data["Current Qualification"], form_data["Strength"], form_data["Experience"],
                form_data["Salary Expectation"], form_data["Hobbies"]]
    upl.upload_job(pred_arr)
    pred_arr = [int(elem) for elem in pred_arr]
    pred_arr = np.array(pred_arr).reshape(1, -1)
    pred = model.predict(pred_arr)[0]

    pred = pred[0].upper() + pred[1:]
    obj.runtimeCall()
    return render_template("display1.html", pred=pred)

# Courses
@app.route("/forms2")
def forms2():
    return render_template("forms2.html")

@app.route("/form-action2", methods = ['POST', 'GET'])
def form_action2():
    model = joblib.load("Modelcourse.joblib")
    form_data = request.form
    pred_arr = [form_data["Interested"], form_data["Location"], form_data["Duration"]]
    upl.upload_courses(pred_arr)
    pred_arr = [int(elem) for elem in pred_arr]
    pred_arr = np.array(pred_arr).reshape(1, -1)
    pred = model.predict(pred_arr)[0]

    # pred = pred[0].upper() + pred[1:]
    obj.runtimeCall()
    return render_template("display2.html", pred=pred)

@app.route("/api-call", methods=["GET", "POST"])
def apiCall():
    API_URL = "https://api-inference.huggingface.co/models/ANIKEThash/DialoGPT-medium-character"
    headers = {"Authorization": "Bearer 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"}

    form_data = request.form
    input = form_data["msg"]

    def query(payload):
        response = requests.post(API_URL, headers=headers, json=payload)
        return response.json()
    
    output = query({

	    "inputs": input
    })

    return render_template("ouput.html", output=output)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/send-data", methods=["GET", "POST"])
def send():
    form_data = request.form
    upl.upload(form_data["name"], 
               form_data["email"], 
               form_data["phone"], 
               form_data["mssg"])
    return render_template("index.html")


@app.route("/signup")
def signup():
    return render_template("signup.html")


if __name__ == "__main__":
    app.run(debug=True)