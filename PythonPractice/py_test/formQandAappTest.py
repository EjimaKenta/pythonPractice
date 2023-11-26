from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form['question']
    # ここで質問をデータベースに保存します
    return render_template('ask.html', question=question)

@app.route('/answer', methods=['POST'])
def answer():
    answer = request.form['answer']
    # ここで回答をデータベースに保存します
    return render_template('answer.html', answer=answer)

if __name__ == "__main__":
    app.run(debug=True)