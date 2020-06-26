# Text Based Browser

![browser](https://media.giphy.com/media/l44Qqz6gO6JiVV3pu/giphy.gif)

### About this project

Sometimes you need to read online documentation or find something on the Internet from the command line or terminal. So, let's use Python to create a text-based browser! Of course, making a real, full-blown browser is a very difficult task. In this project, you'll create a very simple browser that will ignore JavaScript and CSS, won't have cookies, and will only process a limited set of tags.

### Run

Requirements:
- Python 3.7
- To run the tests: https://github.com/hyperskill/hs-test-python
- BeautyfulSoup
- Colorama

`python browser.py`

# Project
## 1. Address line
<h3 style="text-align: center;">Description</h3>

<p>Every browser accepts a string from the user and then shows a web page. A string from the user is a URL (Uniform Resource Locator) and looks somewhat like this: <a target="_blank" href="https://www.google.com" rel="noopener noreferrer nofollow">https://www.google.com</a>. After that, the browser has a lot of work. In a nutshell, this work can be described as finding a web page. The web page is located somewhere on the Internet and the browser has to retrieve it. Since the <code class="java">https://www.</code> part is always the same, it is often omitted and the correct shortened link looks like this: <a target="_blank" href="https://www.google.com" rel="noopener noreferrer nofollow">google.com</a>.</p>

<p>In our first stage, we'll try to imitate this behavior.</p>

<h3 style="text-align: center;">Objectives</h3>

<ol>
	<li>You should write a program that takes a string from the user (URL) and outputs a "hard-coded" website with news (just a header and some text below).<br>
	The websites are presented as two variables in source code, you can see them in the template. These are mock <a target="_blank" href="https://www.bloomberg.com" rel="noopener noreferrer nofollow">bloomberg.com</a> and <a target="_blank" href="https://www.nytimes.com" rel="noopener noreferrer nofollow">nytimes.com</a> sites. You just need to output them as a response to the corresponding input URL. </li>
	<li>
	<p>Also, you should add the possibility to quit the browser by typing <code class="java">exit</code>, because real browsers don’t finish their work when they output a single web page: they are ready to accept a new URL at any moment. You should realize this behavior, too. An endless loop can help you with that part.</p>
	</li>
</ol>

<h3 style="text-align: center;">Example</h3>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">&gt; bloomberg.com
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
of Apollo 11, and Neil Armstrong -- the first man to walk
on the moon. It was the height of the Cold War, and the charts
were filled with David Bowie's Space Oddity, and Creedence's
Bad Moon Rising. The world is a very different place than
it was 5 decades ago. But how has the space race changed since
the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
addressed Apple Inc. employees at the iPhone maker’s headquarters
Tuesday, a signal of the strong ties between the Silicon Valley giants.
&gt; exit
</code></pre>

## 2. Tabs
<h3 style="text-align: center;">Description</h3>

<p>Let's make our browser store web pages in a file and show them if the user types a shortened request (for example, wikipedia instead of <a target="_blank" href="https://www.wikipedia.org" rel="noopener noreferrer nofollow">wikipedia.org</a>). You can store each page as a separate file or find another way to do this. But your program should accept one command line argument which is a directory to store the files, and your web pages should be saved inside this directory.</p>

<h3 style="text-align: center;">Objectives</h3>

<p>At this stage, your program should: </p>

<ol>
	<li>Check if the user has entered a valid URL. It must contain at least one dot, for example, <code class="java">bloomberg.com</code>. If the URL is incorrect, the browser should output an error message (it should contain the word <code class="java">error</code>) and wait for another URL.</li>
	<li>Accept a command-line argument which is a directory for saved tabs. For example, if the argument is <code class="java">dir</code>, then you need to create a folder with the name <code class="java">dir</code> and save all web pages that the user downloads in this folder.</li>
	<li>Save this web page in a file. After that, the user needs to have a simple way to see the saved web page by typing "bloomberg". The rule is simple: you just need to remove the last dot and everything that comes after it. <code class="java">bloomberg.com</code> becomes <code class="java">bloomberg</code>, <code class="java">en.wikipedia.org</code> becomes <code class="java">en.wikipedia</code>.</li>
</ol>

<p>Check out a tutorial to learn how to <a target="_blank" href="https://www.techbeamers.com/read-write-file-in-python/" rel="noopener noreferrer nofollow">work with files</a> and <a target="_blank" href="https://thispointer.com/how-to-create-a-directory-in-python/" rel="noopener noreferrer nofollow">create folders</a> in Python.</p>

<h3 style="text-align: center;">Example</h3>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">&gt; python browser.py dir-for-files
&gt; bloomberg.com
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
of Apollo 11, and Neil Armstrong -- the first man to walk
on the moon. It was the height of the Cold War, and the charts
were filled with David Bowie's Space Oddity, and Creedence's
Bad Moon Rising. The world is a very different place than
it was 5 decades ago. But how has the space race changed since
the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
addressed Apple Inc. employees at the iPhone maker’s headquarters
Tuesday, a signal of the strong ties between the Silicon Valley giants.

&gt; bloomberg
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
of Apollo 11, and Neil Armstrong -- the first man to walk
on the moon. It was the height of the Cold War, and the charts
were filled with David Bowie's Space Oddity, and Creedence's
Bad Moon Rising. The world is a very different place than
it was 5 decades ago. But how has the space race changed since
the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
addressed Apple Inc. employees at the iPhone maker’s headquarters
Tuesday, a signal of the strong ties between the Silicon Valley giants.

&gt; nytimes
Error: Incorrect URL

&gt; exit
</code></pre>

## 3. Hotkeys
<h3 style="text-align: center;">Description</h3>

<p>Every browser has a “back” button. If the user presses this button, the browser shows the previous web page. This feature can be realized using a stack. You save the pages visited by the user: google, wikipedia, bloomberg, ..., but when the user types <code class="java">back</code>, you will see the pages in the reverse order: ..., bloomberg, wikipedia, google. </p>

<h3 style="text-align: center;">Objectives</h3>

<p>The result of this task is the same as in the previous task, but now the program has a new feature:</p>

<ol>
	<li>The program should show the previous page if the user types <code class="java">back</code>. You can implement a stack to do this.</li>
	<li>If there are no more pages in the browser history, just don’t output anything.</li>
</ol>

<h3 style="text-align: center;">Example</h3>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">&gt; python browser.py dir-for-files
&gt; bloomberg.com
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
of Apollo 11, and Neil Armstrong -- the first man to walk
on the moon. It was the height of the Cold War, and the charts
were filled with David Bowie's Space Oddity, and Creedence's
Bad Moon Rising. The world is a very different place than
it was 5 decades ago. But how has the space race changed since
the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
addressed Apple Inc. employees at the iPhone maker’s headquarters
Tuesday, a signal of the strong ties between the Silicon Valley giants.

&gt; nytimes.com
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow
and change shape, and that could be a boon to medicine
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
important female and minority scientists in less than two
years.

&gt; back
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
of Apollo 11, and Neil Armstrong -- the first man to walk
on the moon. It was the height of the Cold War, and the charts
were filled with David Bowie's Space Oddity, and Creedence's
Bad Moon Rising. The world is a very different place than
it was 5 decades ago. But how has the space race changed since
the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey
addressed Apple Inc. employees at the iPhone maker’s headquarters
Tuesday, a signal of the strong ties between the Silicon Valley giants.

&gt; exit
</code></pre>

## 4. Requesting
<h3 style="text-align: center;">Description</h3>

<p>Now we should get closer to the browser with the address bar. At this stage, you need to forget about your hard-coded variables with sites and show your user some real pages. Make the browser request the real input URL and show the result. </p>

<p>One of the simplest ways to do this is the Request library. It is already installed in your project, so you can use it. This library allows to get any web page via URL by one string. You can find this string in <a target="_blank" href="https://2.python-requests.org/en/master/user/quickstart/#response-content" rel="noopener noreferrer nofollow">Request documentation</a>, though it’s better to read the <a target="_blank" href="https://2.python-requests.org/en/master/user/quickstart" rel="noopener noreferrer nofollow">whole quick manual</a> to understand more.</p>

<p>Sometimes, it’s going to be a challenge. You might find that you suddenly don't have permission to visit certain websites. That’s because of the User-agent. It’s just a string that all browsers use to mark the request, and they all have different user-agents. Frankly, browsers add a lot of additional information to the requests. All this info can be set using the request library. For this task, it's optional, but feel free to experiment.</p>

<h3 style="text-align: center;">Objectives</h3>

<p>Add new features to the browser:</p>

<ol>
	<li>So, your program should read the URL from input as before, but now show the real web page using the Request library.</li>
	<li>Since the user can input the URL without <code class="java">https://</code> in the beginning, you need to append this string if it is not there.</li>
</ol>

<h3 style="text-align: center;">Example</h3>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">&gt; python browser.py dir-for-files
&gt; docs.python.org

&lt;!DOCTYPE html&gt;

&lt;html xmlns="http://www.w3.org/1999/xhtml"&gt;
  &lt;head&gt;
    &lt;meta charset="utf-8" /&gt;&lt;title&gt;3.7.4 Documentation&lt;/title&gt;
    &lt;link rel="stylesheet" target="_blank" href="_static/pydoctheme.css" type="text/css" /&gt;
    &lt;link rel="stylesheet" target="_blank" href="_static/pygments.css" type="text/css" /&gt;

    &lt;script type="text/javascript" id="documentation_options" data-url_root="./" src="_static/documentation_options.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="_static/jquery.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="_static/underscore.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="_static/doctools.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="_static/language_data.js"&gt;&lt;/script&gt;

    &lt;script type="text/javascript" src="_static/sidebar.js"&gt;&lt;/script&gt;

    &lt;link rel="search" type="application/opensearchdescription+xml"
          title="Search within Python 3.7.4 documentation"
          target="_blank" href="_static/opensearch.xml"/&gt;
    &lt;link rel="author" title="About these documents" target="_blank" href="about.html" /&gt;
    &lt;link rel="index" title="Index" target="_blank" href="genindex.html" /&gt;
    &lt;link rel="search" title="Search" target="_blank" href="search.html" /&gt;
    &lt;link rel="copyright" title="Copyright" target="_blank" href="copyright.html" /&gt;
    &lt;link rel="shortcut icon" type="image/png" target="_blank" href="_static/py.png" /&gt;
    &lt;link rel="canonical" target="_blank" href="https://docs.python.org/3/index.html" /&gt;

    &lt;script type="text/javascript" src="_static/copybutton.js"&gt;&lt;/script&gt;
    &lt;script type="text/javascript" src="_static/switchers.js"&gt;&lt;/script&gt;

   …  (More than 200 such terrifying strings)
&gt; exit

</code></pre>

## 5. Parsing
<h3 style="text-align: center;">Description</h3>

<p>Now it is important for us to bring the resulting "text" to a form that is understandable to the user.</p>

<p>If you don’t know what HTML is, here's a short explanation. When working on the previous task you could see a lot of <code class="java">&lt;div&gt;</code>, <code class="java">&lt;script&gt;</code> or <code class="java">&lt;p&gt;</code> “words” on the displayed web page. These are called <strong>tags</strong>. Browsers need tags to know how exactly to show the page. For example, there could be headers that look different from the rest of the text. Also, there could be links; they could be blue, and the cursor could look like a pointing finger when it's on the link. To let the browser know where the links are, where an image should be and so on, tags are used.</p>

<p>Tags are necessary for the browser but aren’t useful for users. Most tags are paired. For example: <code class="java">&lt;p&gt;Some text&lt;/p&gt;</code>, where <code class="java">&lt;p&gt;</code> is an opening tag and <code class="java">&lt;/p&gt;</code> is a closing tag. You need to show only “<code class="java">Some text</code>” without <code class="java">&lt;p&gt;</code> and <code class="java">&lt;/p&gt;</code> on a web page.</p>

<p>Each tag has its own purpose: <code class="java">&lt;p&gt;</code> for text, <code class="java">&lt;h1&gt; &lt;h3&gt; … &lt;h6&gt;</code> for headers, <code class="java">&lt;a&gt;</code> for links, <code class="java">&lt;ul&gt; &lt;ol&gt; &lt;li&gt;</code> for lists.</p>

<p> </p>

<h3 style="text-align: center;">Objectives</h3>

<p>At this stage, you need to cut all content outside of these tags and output what remains. No more <code class="java">&lt;div&gt;, &lt;script&gt;, &lt;p&gt;</code> and so on, just text! You need to show only the content of a limited list of tags (<code class="java">&lt;p&gt;</code>, headers, <code class="java">&lt;a&gt;</code> and <code class="java">&lt;ul&gt;</code>, <code class="java">&lt;ol&gt;</code>, <code class="java">&lt;li&gt;</code>) without the tags themselves.</p>

<p>Use <code class="java">beautifulsoup4</code> library for solving this, it is installed in your project already. Feel free to get curious and browse through some more information about <a target="_blank" href="https://www.dataquest.io/blog/web-scraping-tutorial-python/" rel="noopener noreferrer nofollow">parsing</a>!</p>

<h3 style="text-align: center;">Example</h3>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.</p>

<pre><code class="language-no-highlight">&gt; python browser.py dir-for-files
&gt; docs.python.org
index
modules
Python
Documentation
Python 3.7.4 documentation
Welcome! This is the documentation for Python 3.7.4.
Parts of the documentation:
What's new in Python 3.7? or all "What's new" documents since 2.0
Tutorial start here
Library Reference keep this under your pillow
Language Reference describes syntax and language elements
Python Setup and Usage how to use Python on different platforms
Python HOWTOs in-depth documents on specific topics
Installing Python Modules installing from the Python Package Index &amp; other sources
Distributing Python Modules publishing modules for installation by others
Extending and Embedding tutorial for C/C++ programmers
Python/C API reference for C/C++ programmers
FAQs frequently asked questions (with answers!)
Indices and tables:
Global Module Index quick access to all modules
General Index all functions, classes, terms
Glossary the most important terms explained
Search page search this documentation
Complete Table of Contents lists all sections and subsections
Meta information:
Reporting bugs
About the documentation
History and License of Python
Copyright
&gt; exit</code></pre>

## 6. Formatted output
<h3 style="text-align: center;">Description</h3>

<p>It’s not enough to just drop the tags. You should make your output “readable”. After all, we would like to have a user-friendly browser, right? At this stage, try to make your browser look more like a browser.</p>

<p>Almost every page contains links. Have you ever wondered why blue was chosen to highlight them?</p>

<p>One of the reasons lies in the physiology of the human eye. Red and green are detected by the same cells in the eye, and one of the most common forms of colorblindness is red-green colorblindness. It affects 7% of men and only 0.4% of women, that’s still one person in 25 overall. But almost no one has a blue deficiency. Accordingly, nearly everyone can see blue, or, more accurately, almost everyone can distinguish blue as a color different from others.</p>

<p>Also, blue is the darkest color that does not reduce the readability of the text.</p>

<h3 style="text-align: center;">Objectives</h3>

<p>Let all  links in your browser be blue! Pay attention to the <a target="_blank" href="https://pypi.org/project/colorama/" rel="noopener noreferrer nofollow">Colorama</a> library. This library is already installed in the project, so you can use it. With this library, you can easily solve this task just after reading the documentation!</p>

<h3 style="text-align: center;">Example</h3>

<p>The greater-than symbol followed by space (<code class="java">&gt; </code>) represents the user input. Notice that it's not the part of the input.<br>
<samp>&gt; https://docs.python.org <br>
<span style="color: #3366ff;">index</span><br>
<span style="color: #3366ff;">modules   </span>    <br>
Python       <br>
Documentation            <br>
Python 3.7.4 documentation<br>
Welcome! This is the documentation for Python 3.7.4.<br>
Parts of the documentation:<br>
<span style="color: #3366ff;">What's new in Python 3.7?</span> or <span style="color: #3366ff;">all "What's new" documents since 2.0</span><br>
<span style="color: #3366ff;">Tutorial </span>start here<br>
<span style="color: #3366ff;">Library Reference</span> keep this under your pillow<br>
<span style="color: #3366ff;">Language Reference</span> describes syntax and language elements<br>
<span style="color: #3366ff;">Python Setup and Usage</span> how to use Python on different platforms<br>
<span style="color: #3366ff;">Python HOWTOs</span> in-depth documents on specific topics<br>
<span style="color: #3366ff;">Installing Python Modules</span> installing from the Python Package Index &amp; other sources<br>
<span style="color: #3366ff;">Distributing Python Modules</span> publishing modules for installation by others<br>
<span style="color: #3366ff;">Extending and Embedding</span> tutorial for C/C++ programmers<br>
<span style="color: #3366ff;">Python/C API</span> reference for C/C++ programmers<br>
<span style="color: #3366ff;">FAQs</span> frequently asked questions (with answers!)<br>
Indices and tables:<br>
<span style="color: #3366ff;">Global Module Index</span> quick access to all modules<br>
<span style="color: #3366ff;">General Index</span> all functions, classes, terms<br>
<span style="color: #3366ff;">Glossary</span> the most important terms explained<br>
<span style="color: #3366ff;">Search page</span> search this documentation<br>
<span style="color: #3366ff;">Complete Table of Contents</span> lists all sections and subsections<br>
Meta information:<br>
<span style="color: #3366ff;">Reporting bugs<br>
About the documentation<br>
History and License of Python<br>
Copyright</span><br>
&gt; exit</samp></p>