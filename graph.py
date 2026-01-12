import sqlite3
import matplotlib.pyplot as plt

# Labels for the services
labels = [
    "XML Conversion (PDF, DOC, HTML to XML)",
    "XML Tagging & Structuring",
    "DTD / XSD Validation",
    "Content Digitization",
    "Data Quality & Validation Services"
]

# Example usage values (you can change these dynamically)
usage_values = [50,10, 10, 20, 10]

# Colors for each slice
colors = ["#4e79a7", "#f28e2b", "#e15759", "#76b7b2", "#59a14f"]

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(
    usage_values,
    labels=labels,
    autopct="%1.1f%%",
    startangle=140,
    colors=colors
)
plt.title("User Usage Distribution Across XML Services")
plt.axis("equal")  # Equal aspect ratio ensures pie is drawn as a circle
plt.show()
