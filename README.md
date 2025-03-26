# Misc AI examples of vibe coding

## Sudoku solver

The solver is available at: https://torstenwerner.github.io/v-ai-be/sudoku.html
For faster input the space key will delete the value of the current cell.

It has been created with Google Gemini 2.5 pro and the following prompt.

### Prompt

Please create a solver for Sudoku puzzles. It should be a single HTML file with CSS and Javascript.
It should have a nice 9x9 grid of cells to input the puzzle, a button for solving it, a grid for rendering the solution when solved, and a button to reset the input to an empty puzzle. 
The input grid should initially contain a sample puzzle.

When typing a digit the value in the currently focused cell should be replaced and the focus should move to the next cell in the current row or if the last cell is focused then to the first cell in the next row. 
The space key should delete the value in the current cell and move the focus in the same way as described above.

### Older python example

An older python example is available in [sudoku.py](sudoku.py).
