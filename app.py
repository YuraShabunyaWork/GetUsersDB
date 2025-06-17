from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_connection():
    return psycopg2.connect("dbname=demo user=user password=pass host=db")

@app.route("/")
def hello():
    return "Hello from Docker!"

@app.route('/users')
def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(rows)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
