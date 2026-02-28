# Hangman Game - Python Implementation 🎮

This is a classic **Hangman** game created as part of **Section 7** of the **"100 Days of Code™: The Complete Python Pro Bootcamp"** by **Angela Yu** on Udemy.

## 🎯 Project Overview
The objective was to build a fully functional Hangman game where the player tries to guess a hidden word letter by letter before the "hangman" is fully drawn.

## 🕹️ Features
* **Random Word Selection:** The game picks a challenging word from an extensive library (including difficult ones like 'absurd', 'glyph', or 'syndrome').
* **Visual Progress:** Displays underscores for hidden letters and reveals them as you guess correctly.
* **Lives System:** The player starts with 7 lives. Each incorrect guess removes a life and updates the ASCII hangman art.
* **Win/Loss Logic:** The game detects when all letters have been guessed or when the player runs out of attempts.

## 🛠️ Technical Implementation
* **Loops:** Utilizes `while` loops for the game state and `for` loops to check letter positions.
* **Lists & Strings:** Managing a collection of words and dynamically building the `display` string.
* **ASCII Art:** Custom visual feedback using raw strings (`r'''`) to represent the hanging stages.
* **User Input:** Captures and normalizes input to lowercase to prevent case-sensitivity issues.

## 📋 How to Play
1. Run the script.
2. Look at the number of underscores (representing the word length).
3. Type a letter and press Enter.
4. If the letter is in the word, it appears in the blanks.
5. If not, you lose a life and the hangman starts to appear!

---

**Course:** 100 Days of Code™: The Complete Python Pro Bootcamp  
**Instructor:** Angela Yu (Udemy)  
**Developed by:** Rusu Ioana
