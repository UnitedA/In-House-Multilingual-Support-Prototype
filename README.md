# Multilingual Support Prototype

## Overview
This project is a multilingual assistance system prototype based on pre-trained machine translation models. The prototype exhibits the fundamental capabilities of text translation across various languages and serves as a starting point for a more extensive multilingual support system.

## Objectives

### Main Goal
- Integrate pre-trained machine translation models to give precise translations across specific languages.

### Secondary Goals
- Create a user-friendly interface for text entry and display translations.
- Demonstrate the practical use of NLP in real-world systems.

## Minimum Requirements

- **Machine Translation Integration**: Use pre-trained models from libraries such as Hugging Face Transformers to translate text between certain languages.
- **User Interface Development**:Create a simple web interface for entering text and viewing its translation.

## Optional Enhancements
- **Additional Languages**: Increase language support by using extra pre-trained models.
- **Real-Time Translation Features**:Outline possible capabilities for real-time translation applications as future project extensions.

## Tools & Techniques
- **Backend**: Python, Flask
- **NLP Models**: Hugging Face Transformers
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. **Clone the repository**:
    ```bash
    cd multilingual_support
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    venv\Scripts\activate  # For Windows
    source venv/bin/activate  # For MacOS/Linux
    ```

3. **Install the required packages**:
    ```bash
    pip install flask transformers sentencepiece
    ```

4. **Directory structure**:
    ```plaintext
    multilingual_support/
    ├── app.py
    ├── templates/
    │   └── index.html
    ├── static/
    │   └── style.css
    ├── README.md
    └── venv/
    ```

## Usage

1. **Run the Flask application**:
    ```bash
    python app.py
    ```

2. **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:5000`.

3. **Translation**:
    - Enter the text you want to translate.
    - Select the language pair from the dropdown menu.
    - Click the "Translate" button to get the translated text.

## Supported Language Pairs

- English to French
- French to English
- English to Spanish
- Spanish to English
- English to German
- German to English

## Code Explanation

### `app.py`
- **Imports**: Imports the essential modules, including Flask for the web framework and Hugging Face's pipeline for translation models.
- **Initialization**: Initializes translation pipelines for several language pairs with pre-trained Hugging Face models.
- **Routes**:
  - **GET/POST `/`**: It renders the main page and handles translation requests. The input text is translated using the appropriate translation pipeline based on the language pair specified.

### `templates/index.html`
- Creates a simple HTML form for text input and language selection.
- JavaScript is used to process form submissions, send requests to the backend, and display translated content.

### `static/style.css`
- Simple styling for the HTML page to make it more user-friendly.

## Additional Files

- **`init.py`**: Initializes the Flask application and registers blueprints for routing.
- **`route.py`**: Defines routes and request handling logic for the Flask application.
- **`run.py`**: Entry point to run the Flask application.

## Note
The logic is currently encapsulated in `app.py` for simplicity. The additional files (`init.py`, `route.py`, `run.py`) are included to support future scalability and best practices in modular design.
