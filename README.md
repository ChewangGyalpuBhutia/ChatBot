# Culture: Django Chatbot Application

This is a Django-based chatbot application.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/PointX-Lab/Culture.git
    cd Culture
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. Create a .env file in the Culture directory and add your OpenAI API key:

     ```bash
    OPENAI_API_KEY="your_openai_api_key_here"
    ```
     
5. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

6. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000/chatbot/homepage/
    ```
