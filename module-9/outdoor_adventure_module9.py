"""
Outdoor Adventure Database - Table Display Script
Blue Team: Sheridan Dela Cruz, Megan Mosier, Garvin Stewart, Garrett Woods
Module 9.1 | May 10, 2026

Usage:
    pip install mysql-connector-python
    python display_tables.py

    Adjust HOST / USER / PASSWORD below to match your MySQL setup.
"""

import mysql.connector
from mysql.connector import Error

# ── Connection settings ──────────────────────────────────────────────────────
HOST     = "localhost"
USER     = "root"          # change if needed
PASSWORD = ""              # change if needed
DATABASE = "Outdoor_Adventure"
# ─────────────────────────────────────────────────────────────────────────────


def connect():
    """Return an open MySQL connection or exit with an error message."""
    try:
        conn = mysql.connector.connect(
            host=HOST, user=USER, password=PASSWORD, database=DATABASE
        )
        if conn.is_connected():
            return conn
    except Error as e:
        print(f"\n[ERROR] Could not connect to MySQL: {e}")
        print("  Check that MySQL is running and that HOST/USER/PASSWORD are correct.\n")
        raise SystemExit(1)


def get_tables(cursor):
    """Return an ordered list of table names from the current database."""
    cursor.execute("SHOW TABLES")
    return [row[0] for row in cursor.fetchall()]


def display_table(cursor, table_name):
    """Fetch all rows from a table and print them in a formatted grid."""
    cursor.execute(f"SELECT * FROM `{table_name}`")
    rows    = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]

    # ── column widths: max of header or any data value ─────────────────────
    col_widths = [len(col) for col in columns]
    for row in rows:
        for i, val in enumerate(row):
            col_widths[i] = max(col_widths[i], len(str(val) if val is not None else "NULL"))

    # ── helpers ────────────────────────────────────────────────────────────
    sep  = "+-" + "-+-".join("-" * w for w in col_widths) + "-+"
    fmt  = "| " + " | ".join(f"{{:<{w}}}" for w in col_widths) + " |"

    # ── render ─────────────────────────────────────────────────────────────
    record_label = f"{len(rows)} record{'s' if len(rows) != 1 else ''}"
    print(f"\n{'═' * (sum(col_widths) + 3 * len(col_widths) + 1)}")
    print(f"  TABLE: {table_name.upper()}  ({record_label})")
    print(f"{'═' * (sum(col_widths) + 3 * len(col_widths) + 1)}")
    print(sep)
    print(fmt.format(*columns))
    print(sep)

    if rows:
        for row in rows:
            display_row = [str(v) if v is not None else "NULL" for v in row]
            print(fmt.format(*display_row))
    else:
        total_width = sum(col_widths) + 3 * len(col_widths) - 1
        print(f"|  {'(no records)'.center(total_width)}  |")

    print(sep)


def main():
    print("\n" + "=" * 60)
    print("  OUTDOOR ADVENTURE DATABASE  —  Blue Team")
    print("  Sheridan Dela Cruz | Megan Mosier")
    print("  Garvin Stewart     | Garrett Woods")
    print("=" * 60)

    conn   = connect()
    cursor = conn.cursor()

    tables = get_tables(cursor)
    print(f"\n  Database: {DATABASE}")
    print(f"  Tables found: {len(tables)}")
    print(f"  {', '.join(tables)}")

    for table in tables:
        display_table(cursor, table)

    cursor.close()
    conn.close()
    print("\n  Done. Connection closed.\n")


if __name__ == "__main__":
    main()
