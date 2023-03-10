from flask import Flask, request, render_template
import ai

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        code = request.form['description']
        topics = ai.code_explain(code)
        topics = topics.splitlines()
        return render_template("index.html", topics=topics)

@app.route('/404')
def error404():
    return render_template("404.html")
if __name__ == '__main__':
    app.run()
