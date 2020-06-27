# Tic Tac Toe with AI

![ai](https://media.giphy.com/media/l1Et6k00qp9fMTP8s/giphy.gif)

### About this project

Everybody remembers this paper-and-pencil game from childhood: Tic-Tac-Toe, also known as Noughts and crosses or Xs and Os. A single mistake usually costs you the game, but thankfully it is simple enough that most players discover the best strategy quickly. Let’s program Tic-Tac-Toe and get playing!

### Run

Requirements:
- Python 3.7
- To run the tests: https://github.com/hyperskill/hs-test-python

`python tictactoe.py`

![Python projects](http://g.recordit.co/NwdFWua8nl.gif)

# Project
## 1. Initial setup
<h2 style="text-align: center;">Description</h2>

<p>In this project, you'll write a game called Tic-Tac-Toe that you can play with your computer. The computer will have three levels of difficulty - easy, medium, hard.</p>

<p>But, for starters, let's write a program that knows how to work with coordinates and determine the state of the game.</p>

<p>Suppose the bottom left cell has the coordinates (1, 1) and the top right cell has the coordinates (3, 3) like in this table:<br>
<br>
(1, 3) (2, 3) (3, 3)<br>
(1, 2) (2, 2) (3, 2)<br>
(1, 1) (2, 1) (3, 1)</p>

<p>The program should ask to enter the coordinates where the user wants to make a move.</p>

<p>Keep in mind that the first coordinate goes from left to right and the second coordinate goes from bottom to top. Also, notice that coordinates start with 1 and can be 1, 2 or 3.</p>

<p>But what if the user enters incorrect coordinates? The user could enter symbols instead of numbers or enter coordinates representing occupied cells. You need to prevent all of that by checking a user's input and catching possible exceptions.</p>

<h2 style="text-align: center;">Objectives</h2>

<p>The program should work in the following way:</p>

<ol>
	<li>Get the 3x3 field from the first input line (it contains 9 symbols containing <code class="java">X</code>, <code class="java">O</code> and <code class="java">_</code>, the latter means it's an empty cell),</li>
	<li>Output this 3x3 field with cells before the user's move,</li>
	<li>Then ask the user about his next move,</li>
	<li>Then the user should input 2 numbers that represent the cell on which user wants to make his X or O. (9 symbols representing the field would be on the first line and these 2 numbers would be on the second line of the user input). Since the game always starts with X, if the number of X's and O's on the field is the same, the user should make a move with X, and if X's is one more than O's,  then the user should make a move with O.</li>
	<li>Analyze user input and show messages in the following situations:<br>
	•<code class="java">"This cell is occupied! Choose another one!"</code> - if the cell is not empty;<br>
	•<code class="java">"You should enter numbers!"</code> - if the user enters other symbols;<br>
	•<code class="java">"Coordinates should be from 1 to 3!"</code> - if the user goes beyond the field.</li>
	<li>Then output the table including the user's most recent move.</li>
	<li>Then output the state of the game.</li>
</ol>

<p>Possible states:</p>

<ul>
	<li><code class="java">"Game not finished"</code> - when no side has a three in a row but the field has empty cells;</li>
	<li><code class="java">"Draw"</code> - when no side has a three in a row and the field has no empty cells;</li>
	<li><code class="java">"X wins"</code> - when the field has three X in a row;</li>
	<li><code class="java">"O wins"</code> - when the field has three O in a row;</li>
</ul>

<p>If the user input wrong coordinates, the program should keep asking until the user enters coordinate that represents an empty cell on the field and after that output the field with that move. You should output the field only 2 times - before the move and after a legal move.</p>

<h2 style="text-align: center;">Examples</h2>

<p>The examples below show how your program should work.<br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre><code class="language-no-highlight">Enter cells: &gt; _XXOO_OX_

---------
|   X X |
| O O   |
| O X   |
---------
Enter the coordinates: &gt; 1 1
This cell is occupied! Choose another one!
Enter the coordinates: &gt; one
You should enter numbers!
Enter the coordinates: &gt; one three
You should enter numbers!
Enter the coordinates: &gt; 4 1
Coordinates should be from 1 to 3!
Enter the coordinates: &gt; 1 3
---------
| X X X |
| O O   |
| O X   |
---------
X wins</code></pre>

<p><strong>Example 2: </strong></p>

<pre><code class="language-no-highlight">Enter cells: &gt; XX_XOXOO_

---------
| X X   |
| X O X |
| O O   |
---------
Enter the coordinates: &gt; 3 1
---------
| X X   |
| X O X |
| O O O |
---------
O wins</code></pre>

<p><strong>Example 3: </strong></p>

<pre><code class="language-no-highlight">Enter cells: &gt; OX_XOOOXX

---------
| O X   |
| X O O |
| O X X |
---------
Enter the coordinates: &gt; 3 3
---------
| O X X |
| X O O |
| O X X |
---------
Draw</code></pre>

<p><strong>Example 4:</strong></p>

<pre><code class="language-no-highlight">Enter cells: &gt;  _XO_OX___

---------
|   X O |
|   O X |
|       |
---------
Enter the coordinates: &gt; 1 1
---------
|   X O |
|   O X |
| X     |
---------
Game not finished</code></pre>

## 2. Easy does it

<h2 style="text-align: center;">Description</h2>

<p>Now it is time to make a working game. Let's create our first opponent! In this version of the program, the user will be playing as X, and the <code class="java">"easy"</code> level computer will be playing as O. This will be our first small step to the AI!</p>

<p>Let's make it so that at this level the computer will make random moves. This level will be perfect for those who play this game for the first time! Well, though... You can create a level of difficulty that will always give in and never win the game. You can implement such a level along with "easy" level, if you want, but it will not be tested.</p>

<h2 style="text-align: center;">Objectives</h2>

<p>In this stage you should implement the following:</p>

<ol>
	<li>When starting the program, an empty field should be displayed.</li>
	<li>The first to start the game should be the user as <code class="java">X</code>. The program should ask the user to enter the cell coordinates.</li>
	<li>Next the computer should make its move as <code class="java">O</code>. And so on until someone will win or there will be a draw.</li>
	<li>At the very end of the game you need to print the final result of the game.</li>
</ol>

<h2 style="text-align: center;">Example</h2>

<p>The example below shows how your program should work.<br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">---------
|       |
|       |
|       |
---------
Enter the coordinates: &gt; 2 2
---------
|       |
|   X   |
|       |
---------
Making move level "easy"
---------
| O     |
|   X   |
|       |
---------
Enter the coordinates: &gt; 3 1
---------
| O     |
|   X   |
|     X |
---------
Making move level "easy"
---------
| O     |
| O X   |
|     X |
---------
Enter the coordinates: &gt; 1 1
---------
| O     |
| O X   |
| X   X |
---------
Making move level "easy"
---------
| O     |
| O X O |
| X   X |
---------
Enter the coordinates: &gt; 2 1
---------
| O     |
| O X O |
| X X X |
---------
X wins</code></pre>

## 3. Watch 'em fight
<h2 style="text-align: center;">Description</h2>

<p>It is time to make some variations of the game possible. What if you want to play with a friend and not with AI? What if you get tired of playing the game and want to see a match between two AI? Finally, you need to be able to play either the first move or the second move playing against AI. </p>

<p>You should also be able to finish the game after receiving the result.</p>

<h2 style="text-align: center;">Objectives</h2>

<p>Your tasks for this stage:</p>

<ol>
	<li>Write a menu loop, which can interpret two commands: <code class="java">"start"</code> and <code class="java">"exit"</code>.</li>
	<li>Implement the command <code class="java">"start"</code> , which should take two parameters: who will play <code class="java">X</code> and who will play <code class="java">O</code>. Two parameters are possible for now: <code class="java">"user"</code> to play as a human and <code class="java">"easy"</code> to play as an easy level AI.</li>
	<li>The command <code class="java">"exit"</code> should simply terminate the program.</li>
</ol>

<p>In the next steps, you will add "medium" and "hard" parameters.</p>

<p>Do not forget to handle incorrect input! Print <code class="java">"Bad parameters"</code> if something is wrong.</p>

<h2 style="text-align: center;">Example</h2>

<p>The example below shows how your program should work.<br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">Input command: &gt; start
Bad parameters!
Input command: &gt; start easy
Bad parameters!
Input command: &gt; start easy easy
---------
|       |
|       |
|       |
---------
Making move level "easy"
---------
|       |
|     X |
|       |
---------
Making move level "easy"
---------
|       |
| O   X |
|       |
---------
Making move level "easy"
---------
|       |
| O   X |
|     X |
---------
Making move level "easy"
---------
|       |
| O   X |
|   O X |
---------
Making move level "easy"
---------
|       |
| O X X |
|   O X |
---------
Making move level "easy"
---------
|     O |
| O X X |
|   O X |
---------
Making move level "easy"
---------
| X   O |
| O X X |
|   O X |
---------
X wins

Input command: &gt; start easy user
---------
|       |
|       |
|       |
---------
Making move level "easy"
---------
|       |
|       |
|     X |
---------
Enter the coordinates: &gt; 2 2
---------
|       |
|   O   |
|     X |
---------
Making move level "easy"
---------
|   X   |
|   O   |
|     X |
---------
Enter the coordinates: &gt; 1 1
---------
|   X   |
|   O   |
| O   X |
---------
Making move level "easy"
---------
|   X X |
|   O   |
| O   X |
---------
Enter the coordinates: &gt; 3 2
---------
|   X X |
|   O O |
| O   X |
---------
Making move level "easy"
---------
| X X X |
|   O O |
| O   X |
---------
X wins

Input command: &gt; start user user
---------
|       |
|       |
|       |
---------
Enter the coordinates: &gt; 1 1
---------
|       |
|       |
| X     |
---------
Enter the coordinates: &gt; 2 2
---------
|       |
|   O   |
| X     |
---------
Enter the coordinates: &gt; 1 2
---------
|       |
| X O   |
| X     |
---------
Enter the coordinates: &gt; 2 1
---------
|       |
| X O   |
| X O   |
---------
Enter the coordinates: &gt; 1 3
---------
| X     |
| X O   |
| X O   |
---------
X wins

Input command: &gt; exit</code></pre>

## 4. Signs of intelligence
<h2 style="text-align: center;">Description</h2>

<p>Let's write a <code class="java">"medium"</code> level difficulty. It's time to add awareness to our AI. Compared to randomly picking a cell to take a move, this level is considerably smarter.</p>

<p>Despite the randomness in the first moves, its level is a lot harder to beat. This level stops all simple attempts to beat it due to the second rule, and always wins when it can due to the first rule.</p>

<p>Let's take a look at these rules.</p>

<h2 style="text-align: center;">Objectives</h2>

<p>The <code class="java">"medium"</code> level difficulty makes a move using the following process:</p>

<ol>
	<li>If it can win in one move (if it has two in a row), it places a third to get three in a row and win.</li>
	<li>If the opponent can win in one move, it plays the third itself to block the opponent to win.</li>
	<li>Otherwise, it makes a random move.</li>
</ol>

<p>You also should add <code class="java">"medium"</code> parameter to be able to play against this level. And, of course, it should be possible to make "easy" vs "medium" matchup!</p>

<h2 style="text-align: center;">Example</h2>

<p>The example below shows how your program should work.<br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">Input command: &gt; start user medium

---------
|       |
|       |
|       |
---------
Enter the coordinates: &gt; 2 2
---------
|       |
|   X   |
|       |
---------
Making move level "medium"
---------
|       |
|   X   |
| O     |
---------
Enter the coordinates: &gt; 1 3
---------
| X     |
|   X   |
| O     |
---------
Making move level "medium"
---------
| X     |
|   X   |
| O   O |
---------
Enter the coordinates: &gt; 2 1
---------
| X     |
|   X   |
| O X O |
---------
Making move level "medium"
---------
| X O   |
|   X   |
| O X O |
---------
Enter the coordinates: &gt; 1 2
---------
| X O   |
| X X   |
| O X O |
---------
Making move level "medium"
---------
| X O   |
| X X O |
| O X O |
---------
Enter the coordinates: &gt; 3 3
---------
| X O X |
| X X O |
| O X O |
---------
Draw

Input command: &gt; start medium user
---------
|       |
|       |
|       |
---------
Making move level "medium"
---------
|       |
|       |
|   X   |
---------
Enter the coordinates: &gt; 2 2
---------
|       |
|   O   |
|   X   |
---------
Making move level "medium"
---------
|       |
|   O   |
| X X   |
---------
Enter the coordinates: &gt; 3 1
---------
|       |
|   O   |
| X X O |
---------
Making move level "medium"
---------
| X     |
|   O   |
| X X O |
---------
Enter the coordinates: &gt; 1 2
---------
| X     |
| O O   |
| X X O |
---------
Making move level "medium"
---------
| X     |
| O O X |
| X X O |
---------
Enter the coordinates: &gt; 3 3
---------
| X   O |
| O O X |
| X X O |
---------
Making move level "medium"
---------
| X X O |
| O O X |
| X X O |
---------
Draw

Input command: &gt; exit</code></pre>

## 5. An undefeated champion
<h2 style="text-align: center;">Description</h2>

<p>Congratulations, you're at the finish line! After all, our task is to create an AI that will become a strong opponent.</p>

<p>Let's write the <code class="java">"hard"</code> level difficulty.</p>

<p>Compared to the "medium" level difficulty, this level not just go one move ahead to see an immediate win or prevent an immediate loss. This level can see two moves ahead, three moves ahead and so on. Basically, it can see all possible outcomes till the end of the game and choose the best of them considering his opponent also would play perfectly. So, it doesn't rely on the blunders of the opponent, it plays perfectly regardless of the opponent's skill.</p>

<p>The algorithm that implements this is called Minimax. This is the brute force algorithm that maximizes the value of the own position and minimizes the value of the opponent's position. It's not only an algorithm for Tic-Tac-Toe, but for every game with two players with alternate move order, for example, chess.</p>

<h2 style="text-align: center;">Objectives</h2>

<p>In the last stage you need to implement Minimax algorithm as the "hard" difficulty level. <a target="_blank" href="https://medium.freecodecamp.org/how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37" rel="nofollow noopener noreferrer">This</a> link will help to understand details.</p>

<p>You also should add <code class="java">"hard"</code> parameter to be able to play against this level.</p>

<h2 style="text-align: center;">Example</h2>

<p>The example below shows how your program should work.<br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">Input command: &gt; start hard user
Making move level "hard"
---------
|       |
| X     |
|       |
---------
Enter the coordinates: &gt; 2 2
---------
|       |
| X O   |
|       |
---------
Making move level "hard"
---------
|   X   |
| X O   |
|       |
---------
Enter the coordinates: &gt; 2 1
---------
|   X   |
| X O   |
|   O   |
---------
Making move level "hard"
---------
| X X   |
| X O   |
|   O   |
---------
Enter the coordinates: &gt; 1 1
---------
| X X   |
| X O   |
| O O   |
---------
Making move level "hard"
---------
| X X X |
| X O   |
| O O   |
---------
X wins

Input command: &gt; exit</code></pre>
