# The coffee machine

![Python projects](https://media.giphy.com/media/1lvSuCaxJrmrvX1XAH/giphy.gif)

### About this project
This project simulates a virtual coffee machine.

It runs on 4 ingredients:
- Milk
- Water 
- Disposable cups
- Coffee beans

And it also manages money.

### Run

Requirements:
- Python 3.7
- To run the tests: https://github.com/hyperskill/hs-test-python

`python coffee_machine.py`

![Python projects](http://g.recordit.co/HQsqONNO48.gif)


# Code it yourself: 

## 1. Hello, coffee!
<h3 style="text-align: center;">Description</h3>

Let's start with a program that makes you a coffee – virtual coffee, of course. 
In this project, you will implement functionality that simulates a real coffee machine. 
It can run out of ingredients, such as milk or coffee beans, it can offer you various types of coffee, and, finally, it will take money for the prepared drink.

<h3 style="text-align: center;">Objective</h3>

The first version of the program just makes you a coffee. It should print to the standard output what it is doing as it makes the drink.

<h3 style="text-align: center;">Example</h3>

ake a look at the sample output below and print all the following lines.

Output:

```
Starting to make a coffee
Grinding coffee beans
Boiling water
Mixing boiled water with crushed coffee beans
Pouring coffee into the cup
Pouring some milk into the cup
Coffee is ready!
```

## 2. Machines have needs
<h3 style="text-align: center;">Description</h3>

<p>Now let's consider a case when you need a lot of coffee. Maybe you're hosting a party with a lot of guests! In these circumstances, it's better to make preparations in advance.</p>

<p>So, we will ask a user to enter the desired amount of coffee, in cups. Given this, you can adjust the program by calculating how much water, coffee, and milk are necessary to make the specified amount of coffee.</p>

<p>Of course, all this coffee is not needed <em>right</em> now, so at this stage, the coffee machine doesn't actually make any coffee yet.</p>

<h3 style="text-align: center;">Objectives</h3>

<p>Let's break the task into several steps:</p>

<ol>
	<li>First, read the numbers of coffee drinks from the input.</li>
	<li>Figure out how much of each ingredient the machine will need. Note that one cup of coffee made on this coffee machine contains <em>200 ml</em> of water, <em>50 ml</em> of milk, and <em>15 g</em> of coffee beans.</li>
	<li>Output the required ingredient amounts back to the user.</li>
</ol>

<h3 style="text-align: center;">Examples</h3>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Example 1:</strong> <em>a dialogue with a user might look like this</em></p>

<pre><code class="language-no-highlight">Write how many cups of coffee you will need:
&gt; 25
For 25 cups of coffee you will need:
5000 ml of water
1250 ml of milk
375 g of coffee beans</code></pre>

<p><strong>Example 2:</strong> <em>here is another dialogue</em></p>

<pre><code class="language-no-highlight">Write how many cups of coffee you will need:
&gt; 125
For 125 cups of coffee you will need:
25000 ml of water
6250 ml of milk
1875 g of coffee beans</code></pre>


## 3. Enough coffee for everyone
<h3 style="text-align: center;">Description</h3>

<p>A real coffee machine doesn't have an infinite supply of water, milk, or coffee beans. And if you input a really big number, it's almost certain that a real coffee machine wouldn't have the supplies needed to make all that coffee for you.</p>

<p>In this stage, you need to improve the previous program. Now you will check amounts of water, milk, and coffee beans available in your coffee machine at the moment.</p>

<h3 style="text-align: center;">Objectives</h3>

<p>Write a program that does the following:</p>

<ol>
	<li>It requests the amounts of water, milk, and coffee beans available at the moment, and then asks for the number of cups a user needs.</li>
	<li>If the coffee machine has enough supplies to make the specified amount of coffee, the program should print <code class="java">"Yes, I can make that amount of coffee"</code>.</li>
	<li>If the coffee machine can make more than that, the program should output <code class="java">"Yes, I can make that amount of coffee (and even N more than that)"</code>, where <em>N</em> is the number of additional cups of coffee that the coffee machine can make.</li>
	<li>If the amount of given resources is not enough to make the specified amount of coffee, the program should output <code class="java">"No, I can make only N cups of coffee"</code>.</li>
</ol>

<p>Like in the previous stage, the coffee machine needs <em>200 ml</em> of water, <em>50 ml</em> of milk, and <em>15 g</em> of coffee beans to make one cup of coffee.</p>

<h3 style="text-align: center;">Examples</h3>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre><code class="language-no-highlight">Write how many ml of water the coffee machine has:
&gt; 300
Write how many ml of milk the coffee machine has:
&gt; 65
Write how many grams of coffee beans the coffee machine has:
&gt; 100
Write how many cups of coffee you will need:
&gt; 1
Yes, I can make that amount of coffee</code></pre>

<p><strong>Example 2:</strong></p>

<pre><code class="language-no-highlight">Write how many ml of water the coffee machine has:
&gt; 500
Write how many ml of milk the coffee machine has:
&gt; 250
Write how many grams of coffee beans the coffee machine has:
&gt; 200
Write how many cups of coffee you will need:
&gt; 10
No, I can make only 2 cups of coffee</code></pre>

<p><strong>Example 3:</strong></p>

<pre><code class="language-no-highlight">Write how many ml of water the coffee machine has:
&gt; 1550
Write how many ml of milk the coffee machine has:
&gt; 299
Write how many grams of coffee beans the coffee machine has:
&gt; 300
Write how many cups of coffee you will need:
&gt; 3
Yes, I can make that amount of coffee (and even 2 more than that)</code></pre>

<p><strong>Example 4:</strong></p>

<pre><code class="language-no-highlight">Write how many ml of water the coffee machine has:
&gt; 0
Write how many ml of milk the coffee machine has:
&gt; 0
Write how many grams of coffee beans the coffee machine has:
&gt; 0
Write how many cups of coffee you will need:
&gt; 1
No, I can make only 0 cups of coffee</code></pre>

<p><strong>Example 5:</strong></p>

<pre><code class="language-no-highlight">Write how many ml of water the coffee machine has:
&gt; 0
Write how many ml of milk the coffee machine has:
&gt; 0
Write how many grams of coffee beans the coffee machine has:
&gt; 0
Write how many cups of coffee you will need:
&gt; 0
Yes, I can make that amount of coffee </code></pre>

<p><strong>Example 6:</strong></p>

<pre><code class="language-no-highlight">Write how many ml of water the coffee machine has:
&gt; 200
Write how many ml of milk the coffee machine has:
&gt; 50
Write how many grams of coffee beans the coffee machine has:
&gt; 15
Write how many cups of coffee you will need:
&gt; 0
Yes, I can make that amount of coffee (and even 1 more than that)</code></pre>

## 4. Action!
<h3 style="text-align: center;">Description</h3>

<p>Let's simulate an actual coffee machine! What do we need for that? This coffee machine will have a limited supply of water, milk, coffee beans, and disposable cups. Also, it will calculate how much money it gets for selling coffee.</p>

<p>There are several options for the coffee machine we want you to implement: first, it should sell coffee. It can make different types of coffee: espresso, latte, and cappuccino. Of course, each variety requires a different amount of supplies, however, in any case, you will need only one disposable cup for a drink. Second, the coffee machine must get replenished by a special worker. Third, another special worker should be able to take out money from the coffee machine.</p>

<h3 style="text-align: center;">Objectives</h3>

<p>Write a program that offers to buy one cup of coffee or to fill the supplies or to take its money out. Note that the program is supposed to do one of the mentioned actions at a time. It should also calculate how many ingredients and money have left. Display the number of supplies before and after purchase.</p>

<ol>
	<li>First, your program reads one option from the standard input, which can be <code class="java">"buy"</code>, <code class="java">"fill"</code>, <code class="java">"take"</code>. If a user wants to buy some coffee, the input is <code class="java">"buy"</code>. If a special worker thinks that it is time to fill out all the supplies for the coffee machine, the input line will be <code class="java">"fill"</code>. If another special worker decides that it is time to take out the money from the coffee machine, you'll get the input <code class="java">"take"</code>.</li>
	<li>If the user writes <code class="java">"buy"</code> then they must choose one of three types of coffee that the coffee machine can make: espresso, latte, or cappuccino.
	<ul>
		<li>For one espresso, the coffee machine needs <em>250 ml</em> of water and <em>16 g</em> of coffee beans. It costs <em>$4</em>.</li>
		<li>For a latte, the coffee machine needs <em>350 ml</em> of water, <em>75 ml</em> of milk, and <em>20 g</em> of coffee beans. It costs <em>$7</em>.</li>
		<li>And for a cappuccino, the coffee machine needs <em>200 ml</em> of water, <em>100 ml</em> of milk, and <em>12 g</em> of coffee. It costs <em>$6</em>.</li>
	</ul>
	</li>
	<li>If the user writes <code class="java">"fill"</code>, the program should ask them how much water, milk, coffee and how many disposable cups they want to add into the coffee machine.</li>
	<li>If the user writes <code class="java">"take"</code> the program should give all the money that it earned from selling coffee.</li>
</ol>

<p>At the moment, the coffee machine has <em>$550</em>, <em>400 ml</em> of water, <em>540 ml</em> of milk, <em>120 g</em> of coffee beans, and <em>9</em> disposable cups.</p>

<p><div class="alert alert-primary">To sum up, your program should print the coffee machine's state, process one query from the user, as well as print the coffee machine's state after that. Try to use functions for implementing every action that the coffee machine can do.</div></p>

<h3 style="text-align: center;">Examples</h3>

<p>An espresso should be as number <em>1</em> in the list, a latte as number <em>2</em> and a cappuccino as number <em>3</em>.<br>
Options are named as <code class="java">"buy"</code>, <code class="java">"fill"</code>, <code class="java">"take"</code>.</p>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre><code class="language-no-highlight">The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money

Write action (buy, fill, take):
&gt; buy
What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:
&gt; 3

The coffee machine has:
200 of water
440 of milk
108 of coffee beans
8 of disposable cups
556 of money</code></pre>

<p><strong>Example 2:</strong></p>

<pre><code class="language-no-highlight">The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money

Write action (buy, fill, take):
&gt; fill
Write how many ml of water do you want to add:
&gt; 2000
Write how many ml of milk do you want to add:
&gt; 500
Write how many grams of coffee beans do you want to add:
&gt; 100
Write how many disposable cups of coffee do you want to add:
&gt; 10

The coffee machine has:
2400 of water
1040 of milk
220 of coffee beans
19 of disposable cups
550 of money</code></pre>

<p><strong>Example 3:</strong></p>

<pre><code class="language-no-highlight">The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
550 of money

Write action (buy, fill, take):
&gt; take
I gave you $550

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
0 of money</code></pre>

## 5. On a coffee loop
<h3 style="text-align: center;">Description</h3>

<p>Just one action is not so interesting, is it? Let's improve the program so it can do multiple actions, one after another. It should repeatedly ask a user what they want to do. If the user types <code class="java">"buy"</code>, <code class="java">"fill"</code> or <code class="java">"take"</code>, then the program should do exactly the same thing it did in the previous step. However, if the user wants to switch off the coffee machine, they should type <code class="java">"exit"</code>. The program should terminate on this command. Also, when the user types <code class="java">"remaining"</code>, the program should output all the resources that the coffee machine has.</p>

<h3 style="text-align: center;">Objectives</h3>

<p>Write a program that will work endlessly to make coffee for all interested persons until the shutdown signal is given. Introduce two new options: <code class="java">"remaining"</code> and <code class="java">"exit"</code>.</p>

<p>Do not forget that you can be out of resources for making coffee. If the coffee machine doesn't have enough resources to make coffee, the program should output a message that says it can't make a cup of coffee.</p>

<p>And the last improvement to the program at this step — if the user types <code class="java">"buy"</code> to buy a cup of coffee and then changes his mind, they should be able to type <code class="java">"back"</code> to return into the main cycle.</p>

<h3 style="text-align: center;">Example</h3>

<p>Your coffee machine should have the the same initial resources as in the example (<em>400 ml</em> of water, <em>540 ml</em> of milk, <em>120 g</em> of coffee beans, <em>9</em> disposable cups, <em>$550</em> in cash.</p>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre><code class="language-no-highlight">Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
&gt; buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
&gt; 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
&gt; buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
&gt; 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
&gt; fill

Write how many ml of water do you want to add:
&gt; 1000
Write how many ml of milk do you want to add:
&gt; 0
Write how many grams of coffee beans do you want to add:
&gt; 0
Write how many disposable cups of coffee do you want to add:
&gt; 0

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
&gt; buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
&gt; 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit):
&gt; take

I gave you $564

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
0 of money

Write action (buy, fill, take, remaining, exit):
&gt; exit</code></pre>


## 6. Brush up your code
<h3 style="text-align: center;">Description</h3>

<p>Let's redesign our program and write a class that represents the coffee machine. The class should have a method that takes a string as input. Every time the user inputs a string to the console, the program invokes this method with one argument: the line that user input to the console. This system simulates pretty accurately how real-world electronic devices work. External components (like buttons on the coffee machine or tapping on the screen) generate events that pass into the single interface of the program.</p>

<p>The class should not use system input at all; it will only handle the input that comes to it via this method and its string argument.</p>

<p>The first problem that comes to mind: how to write that method in a way that it represents all that coffee machine can do? If the user inputs a single number, how can the method determine what that number is: a variant of coffee chosen by the user or the number of the disposable cups that a special worker added into the coffee machine?</p>

<p>The right solution to this problem is to store the current state of the machine. The coffee machine has several states it can be in. For example, the state could be "choosing an action" or "choosing a type of coffee". Every time the user inputs something and a program passes that line to the method, the program determines how to interpret this line using the information about the current state. After processing this line, the state of the coffee machine can be changed or can stay the same.</p>

<h3 style="text-align: center;">Objective</h3>

<p>Your final task is to refactor the program. Make it so that you can communicate with the coffee machine through a single method. Good luck!</p>

<h3 style="text-align: center;">Example</h3>

<p>Your coffee machine should have the the same initial resources as in the example (<em>400 ml</em> of water, <em>540 ml</em> of milk, <em>120 g</em> of coffee beans, <em>9</em> disposable cups, <em>$550</em> in cash.<br>
The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Example 1:</strong></p>

<pre><code class="language-no-highlight">Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
400 of water
540 of milk
120 of coffee beans
9 of disposable cups
$550 of money

Write action (buy, fill, take, remaining, exit):
&gt; buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
&gt; 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
50 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
&gt; buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
&gt; 2
Sorry, not enough water!

Write action (buy, fill, take, remaining, exit):
&gt; fill

Write how many ml of water do you want to add:
&gt; 1000
Write how many ml of milk do you want to add:
&gt; 0
Write how many grams of coffee beans do you want to add:
&gt; 0
Write how many disposable cups of coffee do you want to add:
&gt; 0

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
1050 of water
465 of milk
100 of coffee beans
8 of disposable cups
$557 of money

Write action (buy, fill, take, remaining, exit):
&gt; buy

What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:
&gt; 2
I have enough resources, making you a coffee!

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$564 of money

Write action (buy, fill, take, remaining, exit):
&gt; take

I gave you $564

Write action (buy, fill, take, remaining, exit):
&gt; remaining

The coffee machine has:
700 of water
390 of milk
80 of coffee beans
7 of disposable cups
$0 of money

Write action (buy, fill, take, remaining, exit):
&gt; exit</code></pre>

