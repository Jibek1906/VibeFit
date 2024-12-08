from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/register')
def register():
    return render_template('registration.html')

@app.route('/user-details')
def user_details():
    return render_template('user_details.html')

if __name__ == '__main__':
    app.run(debug=True)