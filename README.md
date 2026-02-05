# Mood-based-Quran-ayah-generator
The **Mood-Based Qur’an Ayah Generator** is a Python program that displays a Qur’an verse (ayah) based on the user’s current mood.  
It connects to a local SQLite database where moods and ayah references are stored, then fetches the actual ayah text dynamically from the [AlQuran Cloud API](https://alquran.cloud/api).  
It serves as a personalized spiritual reminder, combining simple programming concepts with meaningful daily reflection.

## Features
- Stores moods and ayah references in a database (SQLite).
- Asks the user to input their mood.
- Fetches a random ayah reference linked to that mood.
- Calls the Qur’an API to retrieve the ayah text and translation.
- Keeps running until the user chooses to quit.
- Easy to expand by adding more moods and ayahs.

## How It Works
1. **Database Setup**  
   - A SQLite database (`moods.db`) contains a table `moods` with two columns:
     - `mood` → the mood name (e.g., "happy", "sad")
     - `ayah_ref` → the Surah:Ayah reference (e.g., "2:255")
   - Example rows:
     mood  	ayah_ref
     happy	10:58
     sad	94:5
     grateful 	14:7

2. **Program Flow**  
   - User enters their mood (e.g., `sad`).
   - Program queries the database for ayahs linked to that mood.
   - Picks one ayah at random.
   - Calls the Qur’an API to fetch the ayah text in English.
   - Displays the ayah reference and translation.

## Project Structure
mood-ayah-generator/
│
├── moods.db                # SQLite database storing moods and ayah references
├── main.py  # Main program logic (fetches ayahs based on mood)
└── README.md               # Project documentation

## Project documentation
# How to Run
1. Clone or download this repository.
2. Make sure you have Python 3 installed.
3. Install required libraries:
   ```bash
   pip install requests
4. Run the program:
     python main.py
5.  Enter your mood when prompted.
        Example:
Enter your mood (or type 'quit' to exit): happy
Output
10:58 - Say, "In the bounty of Allah and in His mercy—in that let them rejoice; it is better than what they accumulate."
6. The interface remains open until you type in 'quit' to exit the interface

## Future Improvements
o Add more moods and ayahs to the database.
o Display ayahs in both Arabic and English.
o Save user moods and ayahs shown into a file for reflection history.
o Build a graphical interface (Tkinter or PyQt).

## Learning Goals
This project helps beginners practice:
o	Databases (SQLite) → storing and retrieving data.
o	SQL queries → selecting, inserting, and deleting rows.
o	Random module → picking one ayah at random.
o	Requests library → calling an external API.
o	Loops & conditionals → keeping the program interactive.
o	Functions → organizing code neatly.

## Why It’s Unique
Unlike generic beginner projects, this one is spiritual and personalized.
It blends programming practice with emotional awareness and Qur’anic reflection, making it both meaningful and technically educational.

