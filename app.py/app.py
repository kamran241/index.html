from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    age = None
    if request.method == 'POST':
        year = int(request.form['year'])
        age = 2024 - year
        return render_template('index.html', year=year, age=age)
    return render_template('index.html', year=None, age=None)

if __name__ == '__main__':
    app.run(debug=True)