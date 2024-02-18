# Number Guessing Game

This is a simple number guessing game implemented in Python. The player needs to guess a number between 1 and 10. They have a limited number of attempts to guess the correct number.

## How to Play
1. The game will display ASCII art representing "Number Guessing Game".
2. The player will be prompted to enter a number between 1 and 10.
3. After each guess, the game will provide feedback:
   - If the guessed number is correct, the player wins.
   - If the guessed number is smaller than the correct number, the game will indicate that the player should enter a larger number.
   - If the guessed number is larger than the correct number, the game will indicate that the player should enter a smaller number.
4. The player has a total of 4 attempts to guess the correct number.
5. If the player fails to guess the correct number within the allowed attempts, the game is over, and the player loses.

## Features
- ASCII art representation of "Number Guessing Game"
- Limited attempts for guessing the correct number
- Feedback on each guess
- Win/lose indication

## Requirements
- Python 3.x
- `art` library (for ASCII art)

## How to Run
1. Ensure you have Python installed on your system.
2. Install the `art` library using pip:
   ```
   pip install art
   ```
3. Clone or download this repository to your local machine.
4. Open a terminal or command prompt and navigate to the project directory.
5. Run the following command:
   ```
   python main.py
   ```
6. Follow the on-screen instructions to play the game.

Feel free to contribute to this project by submitting pull requests or reporting issues. Thank you for playing the Number Guessing Game!