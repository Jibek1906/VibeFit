from flask import Flask, render_template, request, jsonify
import sqlite3
import os

app = Flask(__name__)

print(os.path.exists('vibefit.db'))

def init_db():
    conn = sqlite3.connect('vibefit.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS workouts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            title TEXT,
            description TEXT,
            video_id TEXT
        )
    ''')

    conn.commit()
    conn.close()

init_db()

def get_workouts_from_db(date):
    conn = sqlite3.connect('vibefit.db')
    c = conn.cursor()
    c.execute('''
        SELECT title, description, video_id FROM workouts WHERE date = ?
    ''', (date,))
    rows = c.fetchall()
    conn.close()
    return [{"title": row[0], "description": row[1], "video_id": row[2]} for row in rows]

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

@app.route('/workouts')
def workouts():
    return render_template('workouts.html')

@app.route('/api/workouts', methods=['GET'])
def get_workouts():
    date = request.args.get('date')
    conn = sqlite3.connect('vibefit.db')
    cursor = conn.cursor()
    query = "SELECT title, description, video_id FROM workouts WHERE date = ?"
    cursor.execute(query, (date,))
    rows = cursor.fetchall()
    conn.close()

    workouts = []
    for row in rows:
        workouts.append({
            "title": row[0],
            "description": row[1],
            "video_id": row[2]
        })

    return jsonify(workouts)

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

if __name__ == '__main__':
    app.run(debug=True)
