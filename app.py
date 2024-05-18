
from flask import Flask, request, render_template, jsonify
from transformers import pipeline
app = Flask(__name__)
# Load the translation pipelines with explicit model names
translator_en_to_fr = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr")
translator_fr_to_en = pipeline("translation_fr_to_en", model="Helsinki-NLP/opus-mt-fr-en")
translator_en_to_es = pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")
translator_es_to_en = pipeline("translation_es_to_en", model="Helsinki-NLP/opus-mt-es-en")
translator_en_to_de = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
translator_de_to_en = pipeline("translation_de_to_en", model="Helsinki-NLP/opus-mt-de-en")
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_to_translate = request.json['text']
        lang = request.json.get('lang', 'en_to_fr')
        if lang == 'fr_to_en':
            translated_text = translator_fr_to_en(text_to_translate)[0]['translation_text']
        elif lang == 'en_to_fr':
            translated_text = translator_en_to_fr(text_to_translate)[0]['translation_text']
        elif lang == 'es_to_en':
            translated_text = translator_es_to_en(text_to_translate)[0]['translation_text']
        elif lang == 'en_to_es':
            translated_text = translator_en_to_es(text_to_translate)[0]['translation_text']
        elif lang == 'de_to_en':
            translated_text = translator_de_to_en(text_to_translate)[0]['translation_text']
        elif lang == 'en_to_de':
            translated_text = translator_en_to_de(text_to_translate)[0]['translation_text']
        return jsonify(translated_text=translated_text)
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)