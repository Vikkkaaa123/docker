from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn

@app.route('/students', methods=['GET'])
def get_students():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM students;')
    students = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(students)

@app.route('/flask', methods=['GET'])
def flask_endpoint():
    return "Сервер успешно запущен 🚀", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
