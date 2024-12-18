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

@app.route('/personal-office')
def personal_office():
    return render_template('personal_office.html')

@app.route('/workout')
def workout():
    return render_template('workout.html')

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

if __name__ == '__main__':
    app.run(debug=True)