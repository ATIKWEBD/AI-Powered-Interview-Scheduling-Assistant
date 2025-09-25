# app.py
from flask import Flask, request, jsonify
import json
import llm_handler
import db_handler

app = Flask(__name__)
@app.route('/')
def home():
    return "The ConvoSchedule server is running!"

@app.route('/schedule', methods=['POST'])
def schedule_interview():
    # 1. Get data from the incoming request
    request_data = request.json
    candidate_name = request_data.get('name')
    availability_text = request_data.get('availability')

    if not candidate_name or not availability_text:
        return jsonify({"error": "Missing 'name' or 'availability' in request body"}), 400

    # 2. Create the prompt and get the LLM's response
    prompt = llm_handler.create_prompt(availability_text)
    llm_response_str = llm_handler.get_llm_response(prompt)

    # 3. Parse the LLM's JSON response
    try:
        schedule_json = json.loads(llm_response_str)
    except json.JSONDecodeError:
        return jsonify({"error": "Failed to parse LLM response as JSON", "raw_response": llm_response_str}), 500

    # 4. Save the schedule to the MySQL database
    success = db_handler.save_interview(candidate_name, schedule_json)

    if success:
        return jsonify({"message": "Interview scheduled successfully!", "data": schedule_json}), 201
    else:
        return jsonify({"error": "Failed to save the interview to the database"}), 500



if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)