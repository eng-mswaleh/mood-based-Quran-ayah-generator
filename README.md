# Mood-based-Quran-ayah-generator
The **Mood-Based Qur’an Ayah Generator** is a Python program that displays a Qur’an verse (ayah) based on the user’s current mood.   It serves as a personalized spiritual reminder, combining simple programming concepts with meaningful daily reflection.

## Features
- Asks the user to input their current mood (e.g., happy, sad, anxious, grateful).
- Matches the mood with a relevant ayah from a predefined dataset.
- Displays the ayah reference (Surah and verse number).
- Shows the translation/meaning in English.
- Easy to expand by adding more moods and ayahs.

---

## How It Works
1. A dataset of ayahs is stored in a Python dictionary, organized by mood categories.  
   Example:
   ```python
   ayahs = {
       "happy": "16:18 - And if you should count the favors of Allah, you could not enumerate them...",
       "sad": "94:5 - So, verily, with hardship comes ease...",
       "anxious": "13:28 - Verily, in the remembrance of Allah do hearts find rest...",
       "grateful": "14:7 - If you are grateful, I will surely increase your favor..."
   }
2) The program asks the user to enter their mood.
3) It selects the corresponding ayah from the dataset.
4) The ayah reference and meaning are displayed on the console.
5) Optionally, you can expand the dataset or connect to an online Qur’an API for dynamic ayah retrieval.
