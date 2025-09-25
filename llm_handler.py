# llm_handler.py
import os
import google.generativeai as genai
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Generative Model
model = genai.GenerativeModel('gemini-2.5-flash')

def create_prompt(user_text: str) -> str:
    """Creates a highly reliable, few-shot prompt for extracting schedule data."""
    today_date = datetime.now().strftime("%Y-%m-%d")
    master_prompt = f"""
    You are an expert scheduling assistant. Your task is to analyze the user's text and return ONLY a valid JSON object. Do not add ```json``` markdown or any other text. Let's think step by step.

    First, determine the date based on the user's text. Today's date is {today_date}.
    Second, determine the start and end times in 24-hour HH:MM format.
    Third, construct the JSON object. If a value is missing, use null.

    ---
    Here are some examples:

    Example 1:
    User text: "I can do next Wednesday morning, maybe from 9 to 11am."
    JSON Output:
    {{"date": "2025-10-01", "start_time": "09:00", "end_time": "11:00"}}

    Example 2:
    User text: "How about tomorrow afternoon?"
    JSON Output:
    {{"date": "2025-09-27", "start_time": "13:00", "end_time": "17:00"}}

    Example 3:
    User text: "I'm not sure yet."
    JSON Output:
    {{"date": null, "start_time": null, "end_time": null}}
    ---

    Now, process the following user text:

    User text: "{user_text}"
    JSON Output:
    """
    return master_prompt

def get_llm_response(prompt: str) -> str:
    """Sends a prompt to the Gemini API and returns the text response."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error: Unable to get response from the model."