# Sheridan Dela Cruz
# Garrett Woods
# Megan Mosier
# Garvin Stewart
# May 13, 2026
# Module 10.1, Milestone 3

import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="Outdoor_Adventure"
)

def rental_sales_report():
    cursor = db.cursor()

    # Total rental transactions
    cursor.execute("SELECT COUNT(*) FROM EquipmentRental")
    total_rentals = cursor.fetchone()[0]

    # Total sale transactions
    cursor.execute("SELECT COUNT(*) FROM EquipmentSale")
    total_sales = cursor.fetchone()[0]

    # Customers who rented
    cursor.execute("SELECT DISTINCT CustomerID FROM EquipmentRental")
    rental_customers = {row[0] for row in cursor.fetchall()}

    # Customers who bought
    cursor.execute("SELECT DISTINCT CustomerID FROM EquipmentSale")
    sale_customers = {row[0] for row in cursor.fetchall()}

    # Customers who did both
    both = rental_customers.intersection(sale_customers)

    print("\n--- Equipment Sales vs Rentals Report ---")
    print(f"Total Equipment Rentals: {total_rentals}")
    print(f"Total Equipment Sales:   {total_sales}")
    print(f"Customers who both rented and bought: {len(both)}")

rental_sales_report()
