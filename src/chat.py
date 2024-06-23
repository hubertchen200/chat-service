from src.utils import get_connection
import datetime
import json
from flask import jsonify


def send_message(sender, receiver, content, status="", is_group=False):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        insert_query = "insert into chat (sender, receiver, content, ts, status, is_group) values (%s, %s, %s, %s, %s, %s)"
        user_data = (sender, receiver, content, datetime.datetime.now(), status, is_group)
        cursor.execute(insert_query, user_data)
        conn.commit()
        return jsonify(user_data), 201
    except Exception as e:
        return jsonify({"error": f"message: {e}"})


# send_message(3, 1, "Hi")


def get_message(user_id, count):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        select_query = "select sender, receiver, content, ts from chat where receiver = %s or sender = %s order by ts desc limit %s"
        select_data = (user_id, user_id, count)
        cursor.execute(select_query, select_data)
        rows = cursor.fetchall()
        messages = []
        for row in rows:
            message = {
                "sender": row[0],
                "receiver": row[1],
                "content": row[2],
                "ts": row[3].isoformat()
            }
            messages.append(message)
        print(json.dumps(messages, indent=4))
        return json.dumps(messages)
    except Exception as e:
        print(f"failed: {e}")
        return jsonify({"error": f"message: {e}"})



def delete_message(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        delete_query = "DELETE from chat where id = %s"
        delete_data = (id,)
        cursor.execute(delete_query, delete_data)
        conn.commit()
        return jsonify({"status": "success"})
    except Exception as e:
        return jsonify({"error": f"message: {e}"})


