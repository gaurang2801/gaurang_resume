from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/experience')
def experience():
    return render_template('experience.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/certificates')
def certificates():
    return render_template('certificates.html')

@app.route('/achievements')
def achievements():
    return render_template('achievements.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 