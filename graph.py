import sqlite3
import matplotlib.pyplot as plt

# Connect to the SQLite database
conn = sqlite3.connect("reviews.db")
cur = conn.cursor()

# Fetch ratings from the reviews table
cur.execute("SELECT * FROM reviews")
ratings = [row[0] for row in cur.fetchall()]
conn.close()

# Plot histogram of ratings
plt.figure(figsize=(6,4))
plt.hist(ratings, bins=range(1,7), edgecolor="white", align="left")
plt.title("Rating Distribution")
plt.xlabel("Rating (1-5)")
plt.ylabel("Number of Reviews")
plt.xticks(range(1,6))

# Show the plot
plt.show()
