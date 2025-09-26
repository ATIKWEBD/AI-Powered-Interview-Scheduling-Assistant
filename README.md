<img width="1054" height="808" alt="image" src="https://github.com/user-attachments/assets/04ca2cab-c7b4-4f35-ab26-20dd380f142c" />
# 🤖 AI-Powered Interview Scheduling Assistant

![Streamlit App Screenshot](https://i.imgur.com/your-screenshot-url.png) This project is a full-stack web application that acts as an intelligent assistant for scheduling interviews. It uses a Large Language Model (LLM) to understand a candidate's availability from natural language and saves the structured data to a MySQL database.



## ✨ Features

-   **Conversational AI**: Parses unstructured text (e.g., "I'm free next Tuesday afternoon") into structured date and time data.
-   **Deterministic Outcomes**: Uses advanced prompt engineering to ensure reliable and predictable JSON output from the LLM.
-   **Web Interface**: A user-friendly frontend built with Streamlit to allow for easy input of candidate details.
-   **Data Persistence**: All scheduled interviews are saved to and managed in a MySQL database.

## 🛠️ Tech Stack

-   **Frontend**: Streamlit
-   **Backend Logic**: Python
-   **AI**: Google Gemini  (via API)
-   **Database**: MySQL
-   **Libraries**: `google-generativeai`, `mysql-connector-python`, `streamlit`

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   MySQL Server installed and running

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Create a virtual environment and install dependencies:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3.  **Set up the MySQL Database:**
    Log in to your MySQL instance and run the following commands:
    ```sql
    CREATE DATABASE sense_project;
    CREATE USER 'sense_user'@'localhost' IDENTIFIED BY 'your_secure_password';
    GRANT ALL PRIVILEGES ON sense_project.* TO 'sense_user'@'localhost';
    FLUSH PRIVILEGES;
    USE sense_project;
    CREATE TABLE interviews (
        id INT AUTO_INCREMENT PRIMARY KEY,
        candidate_name VARCHAR(255) NOT NULL,
        scheduled_date DATE,
        start_time TIME,
        end_time TIME,
        status VARCHAR(50) DEFAULT 'pending',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    ```

4.  **Set up Environment Variables:**
    Create a `.env` file in the root of the project directory and add your credentials:
    ```
    # .env file
    GOOGLE_API_KEY="YOUR_GOOGLE_AI_API_KEY"
    DB_HOST="localhost"
    DB_USER="sense_user"
    DB_PASSWORD="your_secure_password"
    DB_NAME="sense_project"
    ```

### Running the Application

With your virtual environment activated, run the Streamlit app from your terminal:
```bash
streamlit run frontend.py
# AI-Powered-Interview-Scheduling-Assistant
