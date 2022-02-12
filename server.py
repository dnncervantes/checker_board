from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template("index.html", width = 8, length = 8)

@app.route('/4')
def eight_four():
    return render_template("index.html", width = 8, length = 4)

@app.route('/<int:x>/<int:y>')
def var_var(x,y):
    return render_template("index.html", width = x, length = y)



if __name__ == '__main__':
    app.run(debug=True) 



