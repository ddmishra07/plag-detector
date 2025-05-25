from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_similarity(text1, text2):
    # Dummy example for now (replace with real logic)
    common_words = set(text1.lower().split()) & set(text2.lower().split())
    return len(common_words) / max(len(set(text1.lower().split())), 1)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    percentage = None
    text1 = text2 = ''

    if request.method == 'POST':
        text1 = request.form.get('text1', '').strip()
        text2 = request.form.get('text2', '').strip()

        if not text1 or not text2:
            result = "Please enter text in both fields."
        else:
            similarity = calculate_similarity(text1, text2)
            percentage = round(similarity * 100, 2)
            result = f"{percentage}% plagiarized"

    return render_template('index.html', result=result, percentage=percentage, text1=text1, text2=text2)

if __name__ == '__main__':
    app.run(debug=True)
