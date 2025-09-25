# frontend.py
import streamlit as st
import requests
import json

# Set the title of the web app
st.title("🤖 ConvoSchedule - AI Interview Scheduler")

# Create the input fields for the form
st.write("Enter the candidate's details below to schedule an interview.")
candidate_name = st.text_input("Candidate Name")
availability_text = st.text_area("Candidate's Availability (e.g., 'I am free next Tuesday afternoon')")

# Create a button to submit the form
if st.button("Schedule Interview"):
    # Check if the inputs are not empty
    if candidate_name and availability_text:
        # The URL for our Flask API endpoint
        api_url = "http://127.0.0.1:5000/schedule"
        
        # The data to send in the POST request
        payload = {
            "name": candidate_name,
            "availability": availability_text
        }
        
        # Send the POST request to the API
        try:
            response = requests.post(api_url, json=payload)
            
            # Check the response from the server
            if response.status_code == 201:
                st.success("✅ Interview scheduled successfully!")
                st.json(response.json())
            else:
                st.error("❌ Error from server:")
                st.json(response.json())
                
        except requests.exceptions.ConnectionError:
            st.error("❌ Connection Error: Could not connect to the backend server. Is it running?")
            
    else:
        st.warning("Please fill in both fields.")