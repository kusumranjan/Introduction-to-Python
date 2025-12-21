from flask import Flask, jsonify,request
from flask_cors import CORS
from operator import index
import pandas as pd
import pymysql
import logging
app = Flask(__name__)
CORS(app)  # Allow React frontend to call Flask API


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s - %(message)s',
)

def get_db():
    logging.info("Connecting to MySQL database")
    try:
        db = pymysql.connect(
            host="localhost",
            user="root",
            passwd="root",
            database="todo"
        )
        logging.debug("Connected to MySQL database")
        return db
    except Exception as e:
        logging.error(e)
        raise
@app.route('/tasks', methods=['GET'])
def get_data():
    logging.info("Getting Data")
    try:
        db=get_db()
        cursor = db.cursor()
        cursor.execute("select * from tasks")
        rows = cursor.fetchall()
        logging.info("Fetched Data")
        db.close()
        return jsonify(rows)
    except Exception as e:
        logging.error(e)
        raise
@app.route('/tasks', methods=['POST'])
def add_task():
    logging.info("Adding Task")
    try:
        db=get_db()
        cursor = db.cursor()
        data=request.get_json()
        cursor.execute(
            "INSERT INTO tasks ( title, description, status) VALUES ( %s, %s, %s)",
            ( data.get('title'), data.get('description'), data.get('status'))
        )
        db.commit()
        db.close()
        logging.info("Added Task")
        row = cursor.fetchone()
        return jsonify(row), 201
    except Exception as e:
        logging.error(e)
        raise
@app.route('/tasks/<int:id>', methods=['PUT'])
def edit_task(id):
    logging.info("Editing Task")
    try:
        db=get_db()
        cursor = db.cursor()
        data=request.get_json()
        cursor.execute( "UPDATE tasks SET title = %s, description = %s, status = %s WHERE id = %s",
        (data.get("title"), data.get("description"), data.get("status"), id))
        db.commit()
        db.close()
        logging.info("Edited Task")
        row = cursor.fetchone()
        return jsonify(row), 201
    except Exception as e:
        logging.error(e)
        raise

@app.route('/tasks/<int:id>', methods=['PATCH'])
def complete_task(id):
    logging.info("Completing Task")
    try:
        db=get_db()
        data = request.get_json()
        cursor = db.cursor()
        cursor.execute("UPDATE tasks SET status=%s WHERE id=%s",(data.get("status"),id))
        db.commit()
        db.close()
        logging.info("Completed Task")

        row = cursor.fetchone()
        return jsonify(row), 201

    except Exception as e:
        logging.error(e)
        raise


@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    logging.info("Deleting Task")
    try:
        db=get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = %s", (id,))
        db.commit()
        db.close()
        logging.info("Deleted Task")
        row = cursor.fetchone()
        return jsonify(row), 201

    except Exception as e:
        logging.error(e)
        raise

if __name__ == '__main__':
    app.run(debug=True)
