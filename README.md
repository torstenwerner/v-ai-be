# Misc AI examples of vibe coding

## Sudoku solver

The solver is available at: [https://torstenwerner.github.io/v-ai-be/sudoku.html](https://torstenwerner.github.io/v-ai-be/sudoku.html).
For faster input the space key will delete the value of the current cell.
Just try an extreme example from [https://sudoku.com/extreme/](https://sudoku.com/extreme/).

It has been created with Google Gemini 2.5 pro and the following prompt.

### Prompt

Please create a solver for Sudoku puzzles. It should be a single HTML file with CSS and Javascript.
It should have a nice 9x9 grid of cells to input the puzzle, a button for solving it, a grid for rendering the solution when solved, and a button to reset the input to an empty puzzle. 
The input grid should initially contain a sample puzzle.

When typing a digit the value in the currently focused cell should be replaced and the focus should move to the next cell in the current row or if the last cell is focused then to the first cell in the next row. 
The space key should delete the value in the current cell and move the focus in the same way as described above.

### Older python example

An older python example is available in [sudoku.py](sudoku.py).


## Messaging web application

It is a design study for a web application that works with messages somewhat similar to email messages.
Initially the message overview should be designed.

The prototype is available at: [https://torstenwerner.github.io/v-ai-be/messaging.html](https://torstenwerner.github.io/v-ai-be/messaging.html).

### Prompt

Please create a web application where the user can read, create, and answer messages similar to email messages.
The design should resemble the gmail interface where it makes sense.
It should be a single HTML file with CSS and Javascript embedded.
The actual messages should be mocked.
The application should render the message overview.
At the top of the screen it should render a logo, a search input field, an action for creating a new message, the name of the mailbox e.g. "Tina Tisch", and a logout button.
In the main area it should render the message overview with one row per message and a maximum of 50 rows.
In case there are more than 50 messages the user should be able to navigate to the next page of messages.
For all pages except for the first page the user should be able to navigate to the previous page of messages.
For each message the sender and subject should be displayed.
The unread status of each message should be visualized e.g. by using more font weight.
Initially all messages should be unread.
When clicking a message its unread status should change into read.
Each message should have actions for answering, forwarding, exporting, and deleting it.
These actions should not do anything at the moment.
The search input field should provide a pull down menu with autocompletion items.
The menu items are grouped where each menu item group has a group label.
As soon as the user focuses the search field it should show these menu items.
- group 'messages' with menu items 'all', 'unread'
- group 'mailbox' with menu items 'Tina Tisch', 'Bernd Bank', 'Violeta Jarmusch'
- group 'folder' with menu items 'inbox', 'outbox', 'sent', 'trash'
- group 'label' with menu items 'urgent', 'done'
After the user has entered a search query e.g. 'Ban' the menu items should be filtered to show only the items matching 'Ban'.
In this example the group 'mailbox' with menu item 'Bernd Bank' should still be shown because it matches 'Ban'.
Other menu items not matching 'Ban' should be removed.
One more menu group should be added to the filtered drop down menu:
- group 'filter' with menu items 'sender: Ban', 'subject: Ban' where 'Ban' should be the search term.

The search field should have an icon button to reset the search term if it is not empty.


## Wordle

Please create an application for a Wordle puzzle.
It should be a single HTML file with CSS and Javascript embedded.
The language of the words should be german.
A random puzzle should be displayed initially.
There should be a button to reset the current puzzle and start with a now random puzzle.

It should support keyboard input.
The first cell in the currently active row should be focused by default.
The currently focused cell should have a colorful border.
Typing a letter should replace the current value of the cell and move the focus to the next cell.
At the last cell of the current row the focus should wrap to the first cell of the same row.
A hint should be displayed if all 5 cells of the current row are filled and it is not submitted yet: "Mit <Enter> abschicken."
Hitting Enter after filling all 5 cells of the current row should submit it.

Show a hint below the virtual keyboard: "Geben Sie bitte SS anstelle von ß ein."
