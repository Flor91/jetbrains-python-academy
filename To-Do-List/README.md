# To-Do List

![todo](https://media.giphy.com/media/l49K0MP1EQ579QTII/giphy.gif)

### About this project
To-Do list can improve your work and personal life. You can use it to reduce the stress in your life and get more done in less time. It also helps you become more reliable for other people and save time for the best things in life.

### Run

Requirements:
- Python 3.7
- To run the tests: https://github.com/hyperskill/hs-test-python
- SQLAlchemy

`python todolist.py`

# Project
## 1. Plan it
<h2>Description</h2>

<p>Do you have 10 minutes a day to add $4000 to your monthly income? </p>

<p>This is the average income difference between people who write down their goals and those who don’t. That’s one of many reasons why having a To-Do list can improve your work and personal life. You can use it to reduce the stress in your life and get more done in less time. It also helps you become more reliable for other people and save time for the best things in life. </p>

<p>In this project, you will create a To-Do list that will help you organize your life.</p>

<h2>Objectives</h2>

<p>To begin with, develop a simple list of 4 tasks. Your program must print exactly the same list as given in the example.</p>

<h2>Example</h2>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Output:</strong></p>

<pre><code class="language-no-highlight">Today:
1) Do yoga
2) Make breakfast
3) Learn basics of SQL
4) Learn what is ORM</code></pre>


## 2. I am an Alchemist!
<h2>Description</h2>

<p>It's very upsetting when the data about your to-do tasks disappears after the program is completed. To avoid this problem, you need to create a database where you can store all the necessary information about your tasks. We will use <strong>SQLite</strong> to create the database and <strong>SQLAlchemy </strong>to manage the database from Python.</p>

<p>SQLAlchemy is the Python SQL toolkit and Object Relational Mapper (ORM) that gives developers the full power and flexibility of SQL.</p>

<p>First, you need to create your database file. To create it, you should use the <code class="language-python">create_engine()</code> method, where <code class="language-python">file_name</code> is the database file name:</p>

<pre><code class="language-python">from sqlalchemy import create_engine

engine = create_engine('sqlite:///file_name?check_same_thread=False')</code></pre>

<p><code class="language-python">check_same_thread=False</code> argument allows connecting to the database from another thread. It's <strong>required</strong> for the test purpose otherwise, you will get an exception.</p>

<p>Once you've created your database file, you need to create a table in it. First, create a model class that describes the table in the database. All model classes should inherit from the <code class="language-python">DeclarativeMeta</code> class that is returned by <code class="language-python">declarative_base()</code>:</p>

<pre><code class="language-python">from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime

Base = declarative_base()


class Table(Base):
    __tablename__ = 'table_name'
    id = Column(Integer, primary_key=True)
    string_field = Column(String, default='default_value')
    date_field = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.string_field</code></pre>

<p>All information about the table is described in its model class.</p>

<ul>
	<li><code class="language-python">Table</code> is the name of the model class. It is used to access data from the table it describes. The name of the class can be anything.</li>
	<li><code class="language-python">__tablename__</code> specifies the table name in the database.</li>
	<li><code class="language-python">id</code> is an integer column of the table; <code class="language-python">primary_key=True</code> says that this column is the primary key.</li>
	<li><code class="language-python">string_field</code> is a string column; <code class="language-python">default='default_value'</code> says that the default value of this column is <code class="language-python">'default_value'</code>.</li>
	<li><code class="language-python">date_field</code> is a column that stores the date. SQLAlchmey automatically converts SQL <code class="language-python">date</code> into a Python <code class="language-python">datetime</code> object.</li>
	<li><code class="language-python">__repr__</code> method returns a string representation of the class object. In the ORM concept, each row in the table is an object of a class.</li>
</ul>

<p>After we've described our table, it's time to create it in our database. All we need is to call the <code class="language-python">create_all()</code> method and pass <code class="language-python">engine</code> to it:</p>

<pre><code class="language-python">Base.metadata.create_all(engine)</code></pre>

<p>This method creates a table in our database by generating SQL queries according to the models we described.</p>

<p>Now we can access the database and store data in it. To access the database, we need to create a session:</p>

<pre><code class="language-python">from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()</code></pre>

<p>The <code class="language-python">session</code> object is the only thing you need to manage the database. To create a row in our table, you need to create an object of the model class and pass it to the <code class="language-python">add()</code> method:</p>

<pre><code class="language-python">new_row = Table(string_field='This is string field!',
         date_field=datetime.strptime('01-24-2020', '%m-%d-%Y').date())
session.add(new_row)
session.commit()</code></pre>

<p>To get all rows from the table, you can pass the model class to the <code class="language-python">query()</code> method that selects all rows from the table represented by a model class:</p>

<pre><code class="language-python">rows = session.query(Table).all()</code></pre>

<p>The <code class="language-python">all()</code> method returns all rows from the table as a Python list. Each element of this list is an object of the model class. You can access the row fields by their names:</p>

<pre><code class="language-python">first_row = rows[0] # In case rows list is not empty

print(first_row.string_field) # Will print value of the string_field
print(first_row.id) # Will print the id of the row.
print(first_row) # Will print the string that was returned by __repr__ method</code></pre>

<h2>Objectives</h2>

<p>Let's store the data about our tasks in the database. Here's what you need to do:</p>

<ul>
	<li>Create a database file. Its name should be <code class="language-python">todo.db</code>.</li>
	<li>Create a table in this database. The table name should be <code class="language-python">task</code>. </li>
</ul>

<p>The table <code class="language-python">task</code> should have the following columns:</p>

<ul>
	<li>Integer column named <code class="language-python">id</code>. It should be the <code class="language-python">primary key</code>.</li>
	<li>String column named <code class="language-python">task</code>.</li>
	<li>Date column named <code class="language-python">deadline</code>. It should have the date when the task was created by default. You can use <code class="language-python">datetime.today()</code> method.</li>
</ul>

<p>Also, you need to implement a menu that will make your program more convenient. The menu should have the following items:</p>

<ol>
	<li><strong>Today's tasks</strong>. Prints all tasks for today.</li>
	<li><strong>Add task</strong>. Asks for task description and saves it in the database.</li>
	<li><strong>Exit.</strong></li>
</ol>

<h2>Example</h2>

<p>The greater-than symbol followed by space (<code class="language-python">&gt; </code>) represents the user input. Note that it's not the part of the input.</p>

<p><strong>Output:</strong></p>

<pre><code class="language-no-highlight">1) Today's tasks
2) Add task
0) Exit
&gt; 1

Today:
Nothing to do!

1) Today's tasks
2) Add task
0) Exit
&gt; 2

Enter task
&gt;Prepare presentation
The task has been added!

1) Today's tasks
2) Add task
0) Exit
&gt; 1

Today:
1. Prepare presentation

1) Today's tasks
2) Add task
0) Exit
&gt; 0

Bye!
</code></pre>

## 3. Deadlines are scary
<h2>Description</h2>

<p>Everyday, we’re surrounded by thousands of small distractions, facts, and bits of odd information. When you’re on a deadline, you don’t have time for all this fluff. You need to focus on the task at hand, so you can’t afford to spend hours on Pinterest, chatting at the water cooler with your coworkers, or watching re-runs on TV. At this point in time, the deadline takes precedence.</p>

<p>So let's add the ability to set deadlines to our tasks. Python <code class="language-python">datetime</code> module will help us to work with dates.</p>

<p>Here are some methods that might help you:</p>

<pre><code class="language-python">from datetime import datetime, timedelta

datetime.today() # return current date and time.
datetime.today().date() # current date without time
datetime.today().time() # current time without date

datetime.strptime(date_string, format) # return a datetime corresponding to date_string, parsed according to format.
# Format example: '%Y-%m-%d' - '2020-04-24'

today = datetime.today()
today.day # the day of a current month.
today.strftime('%b') # the short name of the current month. I.e 'Apr'
today.weekday() # return the day of the week as an integer, where Monday is 0 and Sunday is 6.

yesterday = today - timedelta(days=1) # a timedelta object represents a duration, the difference between two dates or times.
day_after_tomorrow = today + timedelta(days=2)</code></pre>

<p>To select rows from the table with some condition, you can use <code class="language-python">filter()</code> method that accepts the condition by which to select rows:</p>

<pre><code class="language-python">from datetime import datetime

today = datetime.today()
rows = session.query(Table).filter(Table.date == today).all()</code></pre>

<p>In the code snippet above, we selected all rows from <code class="language-python">Table</code> where the date column equals today's date.</p>

<h2>Objectives</h2>

<p>Add the following items to your menu:</p>

<ul>
	<li><strong>Week's tasks</strong>: prints all tasks for 7 days from today.</li>
	<li><strong>All tasks</strong>: prints all tasks sorted by deadline.</li>
</ul>

<p>Now <strong>Add task</strong> item should ask for the deadline of the task. Users should input the deadline in this format: <strong>YYYY-MM-DD</strong>.</p>

<p>Also, <strong>Today's tasks </strong>item should print today's date.</p>

<p>See the format of the output in the example.</p>

<h2>Example</h2>

<p>The greater-than symbol followed by space (<code class="language-python">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Output:</strong></p>

<pre><code class="language-no-highlight">1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit
&gt; 1

Today 26 Apr:
Nothing to do!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit
&gt; 4

Enter task
&gt;Meet my friends
Enter deadline
&gt;2020-04-28
The task has been added!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit
&gt; 2

Sunday 26 Apr:
Nothing to do!

Monday 27 Apr:
Nothing to do!

Tuesday 28 Apr:
1. Meet my friends

Wednesday 29 Apr:
Nothing to do!

Thursday 30 Apr:
1. Math homework
2. Call my mom

Friday 1 May:
1. Order a new keyboard 

Saturday 2 May:
Nothing to do!
&gt;3

All tasks:
1. Meet my friends. 28 Apr
2. Math homework. 30 Apr
3. Call my mom. 30 Apr
4. Order a new keyboard. 1 May

1) Today's tasks
2) Week's tasks
3) All tasks
4) Add task
0) Exit
&gt; 0

Bye!</code></pre>

## 4. Bye, completed tasks
<h2>Description</h2>

<p>Planning is one thing, but when we need to knuckle down and put our plans into action, we tend to push our tasks back further and further until the last minute, or worse — past the established deadline. It happens to the best of us! </p>

<p>In this stage, let's implement the ability to see missed tasks and delete them.</p>

<p>To delete a row from a table, you need to use the <code class="language-python">delete()</code> method that accepts an object to delete. As you remember, each row is represented by a Python object:</p>

<pre><code class="language-python">from datetime import datetime

# delete all rows where date column equals today's date
session.query(Table).filter(Table.date == datetime.today()).delete()

# delete a specific row
rows = session.query(Table).filter(Table.date &lt; datetime.today()).all()
specific_row = rows[0] # in case rows is not empty
session.delete(specific_row)

# don't forget to commit changes
session.commit()</code></pre>

<p>To sort selected data, you can use <code class="language-python">order_by()</code> that accepts a column by which you need to sort data:</p>

<pre><code class="language-python"># select all rows ordered by the date column
session.query(Table).order_by(Table.date)

# select all rows where string_fields starts with 'L'. The result is ordered by date column
session.query(Table).filter(Table.string_field.startswith('L'))).order_by(Table.date)</code></pre>

<h2>Objectives</h2>

<p>Add the following items into your menu:</p>

<ul>
	<li><strong>Missed tasks</strong>: prints all tasks whose deadline was missed, that is, tasks whose deadline date is earlier than today's date.</li>
	<li><strong>Delete task</strong>: deletes the chosen task. Print 'Nothing to delete' if the tasks list is empty.</li>
</ul>

<p><strong>Missed tasks</strong> should print the tasks ordered by the deadline date.</p>

<p><strong>Delete task</strong> should print all the tasks sorted by the deadline date and ask to enter the number of the task to delete.</p>

<p>See in the example what your program should look like.</p>

<h2>Example</h2>

<p>The greater-than symbol followed by space (<code class="language-python">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<p><strong>Output:</strong></p>

<pre><code class="language-no-highlight">1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
&gt; 4

Missed tasks:
1. Learn the for-loop. 19 Apr

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
&gt; 6

Chose the number of the task you want to delete:
1. Learn the for-loop. 19 Apr
2. Learn the basics of SQL. 29 Apr
&gt; 1
The task has been deleted!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
&gt; 4

Missed tasks:
Nothing is missed!

1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit
&gt; 0

Bye!</code></pre>