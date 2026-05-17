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

def booking_trends_report():
    cursor = db.cursor()

    regions = ["Africa", "Asia", "Southern Europe"]

    print("\n--- Booking Trends by Region ---")

    for region in regions:
        # Total bookings for region
        total_query = """
            SELECT COUNT(BookingID)
            FROM Booking
            INNER JOIN Trip ON Booking.TripID = Trip.TripID
            INNER JOIN Location ON Trip.LocationID = Location.LocationID
            WHERE Location.RegionName = %s
        """
        cursor.execute(total_query, (region,))
        total = cursor.fetchone()[0]

        print(f"\nTotal bookings for {region}: {total}")

        # Bookings per year
        yearly_query = """
            SELECT YEAR(BookingDate) AS Year, COUNT(BookingID)
            FROM Booking
            INNER JOIN Trip ON Booking.TripID = Trip.TripID
            INNER JOIN Location ON Trip.LocationID = Location.LocationID
            WHERE Location.RegionName = %s
            GROUP BY YEAR(BookingDate)
            ORDER BY Year DESC
        """
        cursor.execute(yearly_query, (region,))
        yearly_results = cursor.fetchall()

        for row in yearly_results:
            print(f"Year: {row[0]}, Total Bookings: {row[1]}")

booking_trends_report()
