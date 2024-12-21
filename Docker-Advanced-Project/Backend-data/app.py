from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Database configuration
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "dockerdb")
DB_USER = os.getenv("DB_USER", "dockeruser")
DB_PASS = os.getenv("DB_PASS", "dockerpass")

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASS
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM items;")
        rows = cursor.fetchall()
        conn.close()
        return jsonify(rows)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
