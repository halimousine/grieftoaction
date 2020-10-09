from flask import Flask, render_template, redirect, request, url_for
app = Flask(__name__)
app.config['DEBUG'] = True

comments = []
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main.html', comments=comments)
    comments.append(request.form["contents"])
    return redirect(url_for('index'))

@app.route('/about')
def about_index():
    return render_template('about.html')

@app.route('/elevate')
def projects_index():
    return render_template('elevate.html')

@app.route('/contact')
def contact_index():
    return render_template('contact.html')

@app.route('/elevate/dashboard')
def dashboard_index():
    return render_template('elevate/dashboard.html')

@app.route('/elevate/review')
def review_index():
    return render_template('elevate/review.html')

@app.route('/elevate/register')
def register_index():
    return render_template('elevate/register.html')