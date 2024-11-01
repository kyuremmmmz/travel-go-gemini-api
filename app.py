import google.generativeai as genai
import os
from flask import Flask, request, jsonify
app = Flask(__name__)
api_key = os.getenv("AIzaSyClrc7hKPwYWPsvyMds4Y48ltUakzCFau8")
genai.configure(api_key="AIzaSyClrc7hKPwYWPsvyMds4Y48ltUakzCFau8")
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_contentresponse = model.generate_content(f"Calculate the hrs trip from Manila to Pangasinan and calculate the price dont include any other text just estimate it and calculate the budget that will be spent even not accurate")

@app.route("/calculate", methods=["POST"])
def calculate_trip():
    data = request.get_json()
    origin = data.get("origin")
    destination = data.get("destination")
    vehicle = data.get("vehicle");
    response = model.generate_content(f"Using the vehicle of {vehicle} Calculate the hrs trip from {origin} to {destination} and calculate the price include the place where ako sasakay na bus or jeep, and include google map link dont include any other text just estimate it and calculate the budget that will be spent even not accurate")
    return jsonify({"estimated_time": response.text})
    

