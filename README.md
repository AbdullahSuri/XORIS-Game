# XORIS

**XORIS** is a multiplayer board game designed to bring friends and family together in a thrilling competition. The game allows up to 5 players to compete by placing their checkers on a grid, with the ultimate goal of connecting 4 checkers in a horizontal, vertical, or diagonal sequence.

---

## 🎮 Features

- **Customizable Players**: Supports 2 to 5 players, each assigned a unique checker (`X`, `O`, `R`, `I`, or `S`).
- **Dynamic Board Size**:
  - 11x11 board for 2 players.
  - 15x15 board for 3–5 players.
- **Winning Conditions**: Connect 4 checkers in a row to win (horizontal, vertical, or diagonal).
- **Draw Condition**: Ends the game as a draw when all positions are filled with no winner.
- **Randomized Turn Order**: Player order is randomized at the start of the game.
- **Clear Input Validation**: Ensures valid moves by checking for valid inputs and occupied cells.
- **Interactive Board Display**: A clean, responsive board that updates after every move.

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your machine.
- Terminal or Command Prompt.

### Instructions
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/AbdullahSuri/XORIS-Game.git
2. **Navigate to the Project Directory:**
   cd XORIS-Game
3. **Run the Game:**
   python XORIS.py
4. **Play the Game:**
   Follow the on-screen instructions and Enter moves in the format A1, C3, etc

## 📖 How to Play
1. **Start the Game:**
    - The game begins by asking the number of players (2 to 5).
    - Each player is assigned a unique checker.
2. **Make a Move:**
    - Players take turns entering their moves (e.g., A1 for column A, row 1).
    - The board updates automatically after each valid move.
3. **Win or Draw:**
    - Players take turns entering their moves (e.g., A1 for column A, row 1).
4. **Restart:**
    - Re-run the script to start a new game.   

## 🛠️ Built With
- Python: The game logic and board are implemented in Python.
- OS Module: Used to clear the terminal for a clean interface.
- Random Module: Used to shuffle player order.

## 📝 Notes
- The input format is case-insensitive (e.g., A9 or a9 are both valid).
- Ensure your terminal window is large enough to display the board correctly.
- Invalid moves or inputs prompt error messages and allow retries.

