Import the libraries we need
import sqlite3   # For connecting to and working with a local SQLite database
import requests  # For making requests to the Qur'an API (to fetch ayah text)
import random    # For picking a random ayah from the database results

# Define a function that fetches an ayah based on the user's mood
def get_ayah(mood):
    # Connect to the SQLite database file (moods.db)
    conn = sqlite3.connect("moods.db")
    cursor = conn.cursor()

    # Look up all ayah references that match the given mood
    cursor.execute("SELECT ayah_ref FROM moods WHERE mood = ?", (mood,))
    results = cursor.fetchall()  # Get all matching rows
    conn.close()  # Close the database connection

    # If no ayahs were found for that mood, tell the user
    if not results:
        return "Mood not found. Try another mood."

    # Pick one random ayah reference from the results
    # Example ayah_ref looks like "2:255" (Surah 2, Ayah 255)
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

# Define the main function that runs the program
def main():
    print(" Mood-Based Qur’an Ayah Generator ")

    # Keep running until the user types 'quit'
    while True:
        # Ask the user for their mood
        mood = input("\nEnter your mood (happy/sad/anxious/grateful/hope/fear/patience/contented/forgiveness)(or type 'quit' to exit): ").strip().lower()

        # If the user types 'quit', stop the program
        if mood == "quit":
            print("Goodbye! May you always find guidance")
            break

        # Otherwise, fetch and display an ayah for that mood
        print("\nHere is your ayah of the day:")
        print(get_ayah(mood))

# This line makes sure the program runs only when executed directly
if __name__ == "__main__":
    main()