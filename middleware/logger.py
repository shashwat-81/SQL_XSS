import sqlite3
from datetime import datetime

def log_attack(ip_address, payload, input_data):
    """
    Log the details of a blocked malicious request.
    """
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('logs/attack_logs.db')
        cursor = conn.cursor()

        # Insert the attack details into the database
        cursor.execute('''
            INSERT INTO attack_logs (ip_address, payload, timestamp)
            VALUES (?, ?, ?)
        ''', (ip_address, payload, datetime.now()))

        conn.commit()
        conn.close()
        print(f"Attack logged: IP {ip_address}, Payload: {payload}, Input: {input_data}")
    except Exception as e:
        print(f"Error logging attack: {e}")
