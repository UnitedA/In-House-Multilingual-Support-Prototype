from flask import Blueprint, request, render_template, jsonify
from transformers import pipeline

# Create a blueprint named 'main'
main = Blueprint('main', __name__)

# Load the translation pipeline with a pre-trained model for English to French translation
translator = pipeline("translation_en_to_fr")  # Change this to your desired languages

@main.route('/', methods=['GET', 'POST'])
def index():
    """
    Handle requests to the root URL ('/').

    GET requests:
        Render and return the index.html template for the user interface.

    POST requests:
        - Retrieve the text to translate from the form data.
        - Use the translation pipeline to translate the text.
        - Return the translated text as a JSON response.

    Returns:
        - If GET request: Renders the 'index.html' template.
        - If POST request: Returns a JSON object containing the translated text.
    """
    if request.method == 'POST':
        # Get the text to translate from the form data
        text_to_translate = request.form['text']
        # Use the translation pipeline to translate the text
        translated_text = translator(text_to_translate)[0]['translation_text']
        # Return the translated text as a JSON response
        return jsonify(translated_text=translated_text)
    
    # Render the index.html template for GET requests
    return render_template('index.html')
