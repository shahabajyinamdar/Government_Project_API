
from flask import Flask,request,jsonify
import re,json,os,platform,sys
from flask_cors import CORS, cross_origin
from datetime import datetime
platform=platform.system()
sys.path.append(os.getcwd())
from service import CreateProject,FetchProject,FetchProjectDetails,SearchProject
from config import connect



app = Flask(__name__)
CORS(app, origins="*")

@app.route("/")
def post_welcome() -> json:
    return json.dumps("APIs Are running")

    
@app.route("/api/searchProject",methods=["POST"])
@cross_origin()
def search_project() -> json:
    try:
        if request.method == "POST":
            r = request.data
            r = json.loads(r)

            response = SearchProject(r)

            return response
    except Exception as e:
        print(e)

        return (
            jsonify({
                "status" : "Error 707: An unexpected error occured."
            }),
            500,
        )

@app.route("/api/createProject",methods=["POST"])
@cross_origin()
def create_project() -> json:
    try:
        if request.method == "POST":
            r = request.data
            r = json.loads(r)

            response = CreateProject(r)

            return response
    except Exception as e:
        print(e)

        return (
            jsonify({
                "status" : "Error 707: An unexpected error occured."
            }),
            500,
        )

@app.route("/api/fetchProject",methods=["GET"])
@cross_origin()
def fetch_project() -> json:
    try:
        if request.method == "GET":
           
            response = FetchProject()

            return response
    except Exception as e:
        print(e)

        return (
            jsonify({
                "status" : "Error 707: An unexpected error occured."
            }),
            500,
        )
    
@app.route("/api/fetchProjectinfo",methods=["POST"])
@cross_origin()
def fetch_projectdetails() -> json:
    try:
        if request.method == "POST":
            r = request.data
            r = json.loads(r)
            print('here-->>',r)
            response = FetchProjectDetails(r)

            return response
    except Exception as e:
        print(e)

        return (
            jsonify({
                "status" : "Error 707: An unexpected error occured."
            }),
            500,
        )
    

if __name__ == "__main__":
    app.run()
