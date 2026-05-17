# Sheridan Dela Cruz
# Garrett Woods
# Megan Mosier
# Garvin Stewart
# May 13, 2026
# Module 10, Milestone 3

import mysql.connector

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    passwd="",
    database="Outdoor_Adventure"
)

def aging_inventory_report():
    cursor = db.cursor()

    query = """
        SELECT EquipmentID, EquipmentType, PurchaseDate, ConditionStatus, QuantityAvailable
        FROM Equipment
        WHERE PurchaseDate <= DATE_SUB(CURDATE(), INTERVAL 5 YEAR)
    """

    cursor.execute(query)
    results = cursor.fetchall()

    print("\n--- Aging Inventory Report (5+ Years Old) ---")

    if not results:
        print("No equipment older than 5 years.")
        return

    for row in results:
        print(f"\nEquipment ID:      {row[0]}")
        print(f"Equipment Type:    {row[1]}")
        print(f"Purchase Date:     {row[2]}")
        print(f"Condition Status:  {row[3]}")
        print(f"Quantity Available:{row[4]}")

aging_inventory_report()

