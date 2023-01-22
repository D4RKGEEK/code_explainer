from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        print(description)
    return render_template("index.html")

@app.route('/404')
def error404():
    return render_template("404.html")
if __name__ == '__main__':
    app.run()
