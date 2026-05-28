# 🎮 Python Hangman Game

[![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)](https://www.python.org)


A classic, interactive Command Line Interface (CLI) Hangman game built using Python. The computer randomly selects an animal from a massive word bank, and the player has 6 attempts to guess it before the gallows are complete!

This project is tailored specifically for **beginner Python programmers** looking to see how core programming concepts come together in a functional application.

---

## ✨ Features

*   **Dynamic Visual Gallows:** The terminal updates line-by-line using a custom ASCII art dictionary corresponding to your remaining lives.
*   **Massive Word Bank:** Includes a diverse tuple of over 200 different animals to keep gameplay unpredictable.
*   **Robust Input Validation:** 
    *   Automatically rejects numbers, symbols, or multi-letter inputs.
    *   Prevents penalty loops by detecting when you repeat a previously guessed letter.
    *   Case-insensitive handling (typing `A` works perfectly for `a`).
*   **Clean Codebase:** Written using simple, readable logic without complex external libraries.

---

## 🛠️ Concepts Covered

If you are reviewing this code to learn, it covers the following foundational Python pillars:
*   **Data Structures:** Using `tuples` for static data (word bank), `dictionaries` for game assets (ASCII art), and `sets` for tracking unique user guesses.
*   **Control Flow:** Utilizing `while` loops for the continuous game loop and nested `if-elif-else` statements for rule enforcement.
*   **String Manipulation:** Implementing methods like `.lower()`, `.strip()`, and `" ".join()` to format user inputs and game displays cleanly.

---

## 🚀 Getting Started

### Prerequisites
Make sure you have Python 3 installed on your machine. You can download it from [python.org](https://www.python.org/).

### Installation & Execution

1. **Clone the repository** (or simply download the `.py` file):

2. **Navigate into the project directory:**
   ```bash
   cd hangman-python

  ### Run the game
  python hangman.py

 ### 🕹️ Gameplay Preview

<pre>
==============================
-------
|  o 
| /|\
| /  
|
=======

Word: a _ _ _ v a _ k
Guessed letters: a, e, o, r, v, x

❌ Oops! 'x' is not in the word.
Guess a letter: _
</pre>

### Enjoy Playing 
