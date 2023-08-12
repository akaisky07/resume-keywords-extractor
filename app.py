from flask import Flask, request, render_template
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def extract_skills():
    if request.method == 'POST':
        resume = request.form.get('resume')
        words = word_tokenize(resume)
        tagged_words = pos_tag(words)
        skills = [word for word, pos in tagged_words if pos == "NN"]
        return render_template('index.html', skills=skills, resume=resume)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

