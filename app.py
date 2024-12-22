from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

def init_db():
    db_path = 'vibefit.db'

    if not os.path.exists(db_path):
        print(f"База данных {db_path} не найдена, создаем...")
        conn = sqlite3.connect(db_path)
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

        c.execute('''
            CREATE TABLE IF NOT EXISTS meals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                meal_type TEXT,
                name TEXT,
                calories INTEGER,
                proteins INTEGER,
                fats INTEGER,
                carbs INTEGER,
                date DATE
            )
        ''')

        conn.commit()
        conn.close()
        print("Таблицы успешно созданы!")
    else:
        print("База данных уже существует.")

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

def get_meals_for_day(date):
    conn = sqlite3.connect('vibefit.db')
    c = conn.cursor()
    c.execute('SELECT * FROM meals WHERE date = ?', (date,))
    rows = c.fetchall()
    conn.close()
    return rows

def add_meal_to_db(meal):
    conn = sqlite3.connect('vibefit.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO meals (meal_type, name, calories, proteins, fats, carbs, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (meal['meal_type'], meal['name'], meal['calories'], meal['proteins'], meal['fats'], meal['carbs'], meal['date']))
    conn.commit()
    conn.close()

def delete_meal_from_db(meal_id):
    conn = sqlite3.connect('vibefit.db')
    c = conn.cursor()
    c.execute('DELETE FROM meals WHERE id = ?', (meal_id,))
    conn.commit()
    conn.close()

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

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html')

@app.route('/api/workouts', methods=['GET'])
def get_workouts():
    date = request.args.get('date')
    workouts = get_workouts_from_db(date)
    return jsonify(workouts)

@app.route('/api/meals/<date>', methods=['GET'])
def get_meals(date):
    meals = get_meals_for_day(date)
    return jsonify(meals)

@app.route('/api/meals', methods=['POST'])
def add_meal():
    meal = request.get_json()

    if 'date' not in meal:
        meal['date'] = datetime.now().strftime('%Y-%m-%d')

    add_meal_to_db(meal)
    return jsonify({"message": "Meal added successfully!"}), 201

if __name__ == '__main__':
    app.run(debug=True)
