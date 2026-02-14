This is a simple, interactive flashcard application built with Python, Tkinter, and Pandas. It helps users learn French vocabulary by showing a French word, waiting a few seconds, and then flipping the card to reveal the English translation. Users can mark words as known, and the app will automatically remove them from the learning list.
  

Technologies used
- Python
- Tkinter — GUI framework
- Pandas — CSV handling
- Random — word selection

How it works
1. Loading the Data
The app first tries to load words_to_learn.csv. If it doesn’t exist or is empty, it falls back to french_words.csv.
The words are stored as a list of dictionaries for easy access.
2. Showing a New Word
switch_word() selects a random French word, updates the UI, and resets the flip timer.
3. Flipping the Card
After 3 seconds, the card flips to show the English translation.
4. Marking a Word as Known
When the user clicks the ✔️ button:
- The current word is removed from the learning list
- The updated list is saved to words_to_learn.csv
- A new word is shown
If all words are learned, the app displays a congratulatory message and closes.
