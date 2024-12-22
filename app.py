from flask import Flask, render_template, request, jsonify
import sqlite3
import os
from datetime import datetime

app = Flask(__name__)

# Инициализация базы данных
def init_db():
    db_path = 'vibefit.db'
    
    # Проверяем, существует ли файл базы данных
    if not os.path.exists(db_path):
        print(f"База данных {db_path} не найдена, создаем...")  # Отладочное сообщение
        conn = sqlite3.connect(db_path)
        c = conn.cursor()

        # Создание таблицы для хранения данных о питании
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
        print("Таблица успешно создана!")  # Отладочное сообщение
    else:
        print("База данных уже существует.")

init_db()

# Получение списка приемов пищи из базы данных для конкретной даты
def get_meals_for_day(date):
    conn = sqlite3.connect('vibefit.db')
    c = conn.cursor()
    c.execute('SELECT * FROM meals WHERE date = ?', (date,))
    rows = c.fetchall()
    conn.close()
    return rows

# Добавление нового приема пищи в базу данных
def add_meal_to_db(meal):
    conn = sqlite3.connect('vibefit.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO meals (meal_type, name, calories, proteins, fats, carbs, date)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (meal['meal_type'], meal['name'], meal['calories'], meal['proteins'], meal['fats'], meal['carbs'], meal['date']))
    conn.commit()
    conn.close()

# Удаление приема пищи по ID
def delete_meal_from_db(meal_id):
    conn = sqlite3.connect('vibefit.db')
    c = conn.cursor()
    c.execute('DELETE FROM meals WHERE id = ?', (meal_id,))
    conn.commit()
    conn.close()

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/api/meals/<date>', methods=['GET'])
def get_meals(date):
    meals = get_meals_for_day(date)
    return jsonify(meals)

@app.route('/api/meals', methods=['POST'])
def add_meal():
    meal = request.get_json()

    # Ensure the 'date' key is provided
    if 'date' not in meal:
        meal['date'] = datetime.now().strftime('%Y-%m-%d')

    add_meal_to_db(meal)  # Add the meal to the database
    return jsonify({"message": "Meal added successfully!"}), 201

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

if __name__ == '__main__':
    app.run(debug=True)
