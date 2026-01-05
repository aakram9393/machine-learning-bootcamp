### Building Url Dynamically
## Variable Rule
### Jinja 2 Template Engine

### Jinja 2 Template Engine
'''
    {{ }} expresisons to print output in html
    {%...%} conditions, for loops
    {#...#} this for comments
'''

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<html><h1>Welcome to the flask course</h1><html/>"

@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

# @app.route('/submit', methods=['GET', 'POST'])
# def submit():
#     if request.method=='POST':
#         name=request.form['name']
#         return f'Hello {name}'
#     return render_template('form.html')

## Variable Rule
@app.route('/success/<int:score>')
def success(score):
    if score >= 50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score': score, 'res':res}

    return render_template('result1.html',results=exp)

@app.route('/successif/<int:score>')
def successif(score):
    if score >= 50:
        res="PASSED"
    else:
        res="FAILED"

    exp={'score': score, 'res':res}

    return render_template('result.html',results=score)

@app.route('/fail/<int:score>')
def fail(score):

    return render_template('result.html',results=score)

@app.route('/submit', methods=['GET','POST'])
def submit():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        data_science=float(request.form['datascience'])
        total_score = (total_score + science + maths + data_science)/4
    else:
        return render_template('getresult.html')        
    return redirect(url_for('successif', score=total_score))



    


if __name__ == "__main__":
    app.run(debug=True, port=5050)