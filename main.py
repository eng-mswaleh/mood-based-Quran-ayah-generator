# Import the libraries we need
import sqlite3        # For connecting to and working with a local SQLite database
import requests       # For making requests to the Qur'an API (to fetch ayah text)
import random         # For picking a random ayah from the database results
import tkinter as tk  # For building the GUI (Graphical User Interface)
from tkinter import messagebox  # For showing pop-up messages
import datetime       # For tracking today's date (used in daily ayah feature)

# Dictionary to keep track of how many times each mood is searched
mood_counter = {}

# Function to fetch ayah based on mood
def get_ayah(mood):
    # Connect to the SQLite database file (moods.db)
    conn = sqlite3.connect("moods.db")
    cursor = conn.cursor()

    # Look up all ayah references that match the given mood
    cursor.execute("SELECT ayah_ref FROM moods WHERE mood = ?", (mood,))
    results = cursor.fetchall()
    conn.close()  # Close the database connection

    # If no ayahs were found for that mood, tell the user
    if not results:
        return "Mood not found. Try another mood."

    # Pick one random ayah reference from the results
    ayah_ref = random.choice(results)[0]
    surah, ayah = ayah_ref.split(":")  # Split into surah number and ayah number

    # Build the API URL to fetch the ayah text in English (translation by Asad)
    url = f"http://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.asad"
    response = requests.get(url)  # Send the request to the API

    # If the request worked (status code 200 means "OK")
    if response.status_code == 200:
        data = response.json()  # Convert the response into Python dictionary format
        # Return the ayah reference and the text from the API
        return f"{surah}:{ayah} - {data['data']['text']}"
    else:
        # If something went wrong with the API request
        return "Error fetching ayah. Please try again."

# Function triggered when "Get Ayah" button is clicked
def show_ayah():
    # Get the mood entered by the user
    mood = mood_entry.get().strip().lower()
    if mood == "":
        # Show a warning if the user forgot to type a mood
        messagebox.showwarning("Input Error", "Please enter a mood.")
        return

    # Fetch the ayah for the given mood
    ayah_text = get_ayah(mood)

    # Display the ayah text in the result label
    result_label.config(text=ayah_text, wraplength=400)

    # Update mood counter (track how many times each mood is searched)
    if mood in mood_counter:
        mood_counter[mood] += 1
    else:
        mood_counter[mood] = 1

    # Update summary label with search history
    summary_text = "\n".join([f"You searched for '{m}' {c} times this week." for m, c in mood_counter.items()])
    summary_label.config(text=summary_text)

# Function to show a random ayah once per day
def get_daily_ayah():
    # Pick a random ayah from the database (ignores mood)
    conn = sqlite3.connect("moods.db")
    cursor = conn.cursor()
    cursor.execute("SELECT ayah_ref FROM moods")
    results = cursor.fetchall()
    conn.close()

    if not results:
        return "No ayahs found in database."

    # Choose one random ayah reference
    ayah_ref = random.choice(results)[0]
    surah, ayah = ayah_ref.split(":")
    url = f"http://api.alquran.cloud/v1/ayah/{surah}:{ayah}/en.asad"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return f"{surah}:{ayah} - {data['data']['text']}"
    else:
        return "Error fetching daily ayah."

# Create the main window
root = tk.Tk()
root.title("Mood-Based Qur’an Ayah Generator")  # Window title
root.geometry("600x400")  # Window size (width x height)

# Title label at the top
title_label = tk.Label(root, text="Mood-Based Qur’an Ayah Generator", font=("Arial", 14, "bold"))
title_label.pack(pady=10)

# Show today's ayah once per day (Daily Ayah feature)
today = datetime.date.today()
daily_ayah = get_daily_ayah()
daily_label = tk.Label(root, text=f"Today's Ayah ({today}):\n{daily_ayah}", font=("Arial", 12), wraplength=500, justify="center")
daily_label.pack(pady=10)

# Mood input section
mood_label = tk.Label(root, text="Enter your mood:")
mood_label.pack()
mood_entry = tk.Entry(root, width=30)
mood_entry.pack(pady=5)

# Button to fetch ayah based on mood
fetch_button = tk.Button(root, text="Get Ayah", command=show_ayah)
fetch_button.pack(pady=10)

# Quit button to close the application
quit_button = tk.Button(root, text="Quit", command=root.destroy)
quit_button.pack(pady=10)

# Label to display the result (ayah text for the chosen mood)
result_label = tk.Label(root, text="", font=("Arial", 12), justify="center")
result_label.pack(pady=20)

# Label to display mood search summary (history tracker)
summary_label = tk.Label(root, text="", font=("Arial", 10), justify="left")
summary_label.pack(pady=10)

# Run the GUI loop (keeps the window open until user closes it)
root.mainloop()
