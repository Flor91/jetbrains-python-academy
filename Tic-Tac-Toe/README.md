# Tic Tac Toe

![Python projects](https://media.giphy.com/media/3oriNKQe0D6uQVjcIM/giphy.gif)

### About this project

Tic-tac-toe is a game played by two players on a 3x3 field where the duel takes place. One of the players plays as 'X', and the other player is 'O'. 'X' plays first, then the 'O' side plays, and so on.

The first player that writes 3 'X' or 3 'O' in a straight line (including diagonals) wins.

### Run

Requirements:
- Python 3.7
- To run the tests: https://github.com/hyperskill/hs-test-python

`python tictactoe.py`

![Python projects](http://g.recordit.co/NwdFWua8nl.gif)

# Code it yourself

## 1. Welcome to the battlefield!

<h4 style="text-align: center;">Description</h4>

<p>Nowadays, this game is known all over the world. Each country may have its own version of the name, sometimes the rules are different, but the meaning of the game remains the same.</p>

<h4 style="text-align: center;">Objectives</h4>

<p>Your first task in this project is to print any state of the field in the console output. Do not forget to show the moves for both players.</p>

<h4 style="text-align: center;">Example</h4>

<p>The example below shows how your output might look.</p>

<pre><code class="language-no-highlight">X O X
O X O
X X O </code></pre>

## The user is the gamemaster

<h4 style="text-align: center;">Description</h4>

<p>However, our game should show the field in an "intermediate" states too. Let's try to visualize different combinations that the user will determine from the input. It is also important to think about the interface and set boundaries for our field.</p>

<h4 style="text-align: center;">Objectives</h4>

<p>In this stage, you should write a program that:</p>

<ol>
	<li>Reads 9 symbols from the input and writes an appropriate 3x3 field. Elements of the field can contain only <code class="java">'X'</code>, <code class="java">'O'</code> and <code class="java">'_'</code> symbols.</li>
	<li> Sets the field to a specific format, i.e. field should start and end with <code class="java">---------</code>, all lines in between should start and end with <code class="java">'|'</code> symbol and everything in the middle should be separated with a single space.  </li>
</ol>

<h4 style="text-align: center;">Examples</h4>

<p>Examples below show how your output should look. <br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

Example 1:

Enter cells: &gt; O_OXXO_XX

```
---------
| O _ O |
| X X O |
| _ X X |
---------
```

<p><strong>Example 2: </strong></p>


Enter cells: &gt; OXO__X_OX

```
---------
| O X O |
| _ _ X |
| _ O X |
---------
```

<p><strong>Example 3: </strong></p>

Enter cells: &gt; _XO__X___

```
---------
| _ X O |
| _ _ X |
| _ _ _ |
---------
```

## What's up on the field?

<h4 style="text-align: center;">Description</h4>

<p>It is time to learn to see the result (or lack thereof) of the game. In this stage, you should analyze a Tic-Tac-Toe field.  </p>

<p>Is the winner already known or is the game not over yet?  Is it a draw or an impossible combination of moves?  Let's find out!</p>

<p><strong>Note.</strong> In this stage either 'X' or 'O' can start the game.</p>

<h4 style="text-align: center;">Objectives</h4>

<p>In this stage, your program should:</p>

<ol>
	<li> Fill the field from the input and print it as in the previous stage.</li>
	<li> Find the state in which the game is at the moment and print it. Possible states:</li>
</ol>

<ul>
	<li><code class="java">"Game not finished"</code> - when no side has a three in a row but the field has empty cells;</li>
	<li><code class="java">"Draw"</code> - when no side has a three in a row and the field has no empty cells;</li>
	<li><code class="java">"X wins"</code> - when the field has three X in a row;</li>
	<li><code class="java">"O wins"</code> - when the field has three O in a row;</li>
	<li><code class="java">"Impossible"</code> - when the field has three X in a row as well as three O in a row. Or the field has a lot more X's that O's or vice versa (if the difference is 2 or more, should be 1 or 0). For this stage, consider that the game can be started both as X's or as O's. </li>
</ul>

<p>Also, you can use <code class="java">' '</code> or <code class="java">'_'</code> to print empty cells - it's up to you.</p>

<h4 style="text-align: center;">Examples</h4>

<p>The examples below show outputs for some predefined states. Your program should work in the same way. <br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Example 1:</strong></p>



<pre><code class="language-no-highlight">
Enter cells: &gt; XXXOO__O_
---------
| X X X |
| O O _ |
| _ O _ |
---------
X wins
</code></pre>



<p><strong>Example 2:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; XOXOXOXXO
---------
| X O X |
| O X O |
| X X O |
---------
X wins</code></pre>

<p><strong>Example 3:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; XOOOXOXXO
---------
| X O O |
| O X O |
| X X O |
---------
O wins</code></pre>

<p><strong>Example 4:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; XOXOOXXXO
---------
| X O X |
| O O X |
| X X O |
---------
Draw</code></pre>

<p><strong>Example 5:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; XO_OOX_X_
---------
| X O   |
| O O X |
|   X   |
---------
Game not finished</code></pre>

<p><strong>Example 6:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; XO_XO_XOX
---------
| X O _ |
| X O _ |
| X O X |
---------
Impossible</code></pre>

<p><strong>Example 7:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; _O_X__X_X
---------
|   O   |
| X     |
| X   X |
---------
Impossible</code></pre>

<p><strong>Example 8:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; _OOOO_X_X
---------
|   O O |
| O O   |
| X   X |
---------
Impossible</code></pre>

## First move!

<h4 style="text-align: center;">Description</h4>

<p>In addition to analyzing the field, it is equally important to add the ability to select a cell for your move. Now you need to implement human moves. Let's divide the field into cells.</p>

<p>Suppose the bottom left cell has the coordinates (1, 1) and the top right cell has the coordinates (3, 3) like in this table:<br>
<br>
(1, 3) (2, 3) (3, 3)<br>
(1, 2) (2, 2) (3, 2)<br>
(1, 1) (2, 1) (3, 1)</p>

<p>The program should ask to enter the coordinates where the user wants to make a move.</p>

<p><strong>Note</strong> that in this stage user moves as X, not O. Keep in mind that the first coordinate goes from left to right and the second coordinate goes from bottom to top. Also, notice that coordinates start with 1 and can be 1, 2 or 3.</p>

<p>But what if the user enters incorrect coordinates? The user could enter symbols instead of numbers or enter coordinates representing occupied cells. You need to prevent all of that by checking a user's input and catching possible exceptions.</p>

<p> </p>

<h4 style="text-align: center;">Objectives</h4>

<p>The program should work in the following way:</p>

<ol>
	<li>Get the 3x3 field from the input as in the previous stages.</li>
	<li>Output this 3x3 field with cells before the user's move.</li>
	<li>Then ask the user about his next move.</li>
	<li>Then the user should input 2 numbers that represent the cell on which user wants to make his X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user input)</li>
	<li>Analyze user input and show messages in the following situations:<br>
	-<code class="java">"This cell is occupied! Choose another one!"</code> - if the cell is not empty;<br>
	-<code class="java">"You should enter numbers!"</code> - if the user enters other symbols;<br>
	-<code class="java">"Coordinates should be from 1 to 3!"</code> - if the user goes beyond the field.</li>
	<li>Then output the table including the user's most recent move.</li>
</ol>

<p>The program should also check user input. If the user input is unsuitable, the program should ask him to enter coordinates again. </p>

<p>So, you need to output a field from the first line of the input and then ask the user to enter a move. Keep asking until the user enters coordinate that represents an empty cell on the field and after that output the field with that move. You should output the field only 2 times - before the move and after a legal move.</p>

<p><em>Do not delete code</em> that checks for table state; it will be useful in the future.</p>

<h4 style="text-align: center;">Examples</h4>

<p>The examples below shows how your program should work. <br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; X_X_O____
---------
| X   X |
|   O   |
|       |
---------
Enter the coordinates: &gt; 1 1
---------
| X   X |
|   O   |
| X     |
---------</code></pre>

<p><strong>Example 2: </strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: &gt; 1 3
---------
| X X X |
| O O   |
| O X   |
---------</code></pre>

<p><strong>Example 3: </strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: &gt; 3 1
---------
|   X X |
| O O   |
| O X X |
---------</code></pre>

<p><strong>Example 4:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: &gt; 3 2
---------
|   X X |
| O O X |
| O X   |
---------</code></pre>

<p><strong>Example 5:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: &gt; 1 1
This cell is occupied! Choose another one!
Enter the coordinates: &gt; 1 3
---------
| X X X |
| O O   |
| O X   |
---------</code></pre>

<p><strong>Example 6:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: &gt; one
You should enter numbers!
Enter the coordinates: &gt; one three
You should enter numbers!
Enter the coordinates: &gt; 1 3
---------
| X X X |
| O O   |
| O X   |
---------</code></pre>

<p><strong>Example 7:</strong></p>

<pre><code class="language-no-highlight">
Enter cells: &gt; _XXOO_OX_
---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: &gt; 4 1
Coordinates should be from 1 to 3!
Enter the coordinates: &gt; 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: &gt; 1 3
---------
| X X X |
| O O   |
| O X   |
---------</code></pre>

## Fight!

<h4 style="text-align: center;">Description</h4>

<p>We are at the finish line! But playing alone is not so interesting, is it? Let's combine our successes in past stages and get Tic-Tac-Toe with the ability to play from the beginning (empty field) to the result (win or draw).</p>

<p>Now it is time to make a working game!</p>

<p>In the last stage, make it so you can play a full game with a friend. First one of you moves as X, and then the other one moves as O.</p>

<h4 style="text-align: center;">Objectives</h4>

<p>In this stage, you should write a program that:</p>

<ol>
	<li>Prints an empty field at the beginning of the game.</li>
	<li>Creates a game loop where the program asks the user to enter the cell coordinates, analyzes the move for correctness and shows a field with the changes if everything is ok.</li>
	<li>Ends the game when someone wins or there is a draw.</li>
</ol>

<p>You need to output the final result after the end of the game.</p>

<p>Good luck gaming!</p>

<h4 style="text-align: center;">Example</h4>

<p>The example below shows how your program should work.<br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">

---------
|       |
|       |
|       |
---------
Enter the coordinates: &gt; 2 2
---------
|       |
|   X   |
|       |
---------
Enter the coordinates: &gt; 2 2
This cell is occupied! Choose another one!
Enter the coordinates: &gt; two two
You should enter numbers!
Enter the coordinates: &gt; 1 4
Coordinates should be from 1 to 3!
Enter the coordinates: &gt; 1 3
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: &gt; 3 1
---------
| O     |
|   X   |
|     X |
---------
Enter the coordinates: &gt; 1 2
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: &gt; 1 1
---------
| O     |
| O X   |
| X   X |
---------
Enter the coordinates: &gt; 3 2
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: &gt; 2 1
---------
| O     |
| O X O |
| X X X |
---------
X wins
</code></pre>
