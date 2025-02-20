from flask import Flask, request, render_template, redirect, url_for
import pyodbc
import os

app = Flask(__name__)

# Get database connection details from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to Azure SQL Database
conn = pyodbc.connect(DATABASE_URL)

@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    tasks = cursor.fetchall()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete_task(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
