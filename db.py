import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='peeush10',
        database='rule_engine'
    )

def store_rule(rule_string):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rules (rule_string) VALUES (%s)", (rule_string,))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_rules():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM rules")
    rules = cursor.fetchall()
    cursor.close()
    conn.close()
    return rules
