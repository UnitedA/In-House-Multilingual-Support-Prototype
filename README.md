# Multilingual Support Prototype

## Overview
This project is a prototype of a multilingual support system that leverages pre-trained machine translation models. The prototype demonstrates the basic functionality of text translation between multiple languages and serves as a foundational step toward a more comprehensive multilingual support system.

## Objectives

### Main Goal
- Integrate pre-trained machine translation models to provide accurate translations between selected languages.

### Secondary Goals
- Develop a user-friendly interface for text input and display translations.
- Showcase the practical application of NLP in real-world systems.

## Minimum Requirements

- **Machine Translation Integration**: Utilize pre-trained models from libraries like Hugging Face Transformers to translate text between selected languages.
- **User Interface Development**: Create a basic web interface for inputting text and displaying its translation.

## Optional Enhancements
- **Additional Languages**: Add support for more languages by utilizing additional pre-trained models.
- **Real-Time Translation Features**: Outline potential features for real-time translation applications as future project expansions.

## Tools & Techniques
- **Backend**: Python, Flask
- **NLP Models**: Hugging Face Transformers
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
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
- **Imports**: Imports necessary modules including Flask for web framework and pipeline from Hugging Face for translation models.
- **Initialization**: Initializes translation pipelines for different language pairs using pre-trained models from Hugging Face.
- **Routes**:
  - **GET/POST `/`**: Renders the main page and handles translation requests. Based on the selected language pair, the appropriate translation pipeline is used to translate the input text.

### `templates/index.html`
- Provides a simple HTML form for text input and language selection.
- Uses JavaScript to handle form submission, send a request to the backend, and display the translated text.

### `static/style.css`
- Basic styling for the HTML page to make it user-friendly.

## Future Work

- Add more language pairs.
- Implement real-time translation features.
- Enhance the UI for better user experience.

## Acknowledgements
- [Hugging Face](https://huggingface.co/) for providing state-of-the-art NLP models.
- [Flask](https://flask.palletsprojects.com/) for the web framework.

<!-- ## License
This project is licensed under the MIT License. See the LICENSE file for details. -->

