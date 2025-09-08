---
url: https://wiki.freecad.org/Introduction_to_Python
title: Introduction to Python
scraped_at: 2025-09-08 16:41:17
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 The interpreter
  * 3 Variables
  * 4 Numbers
  * 5 Lists
  * 6 Indentation
  * 7 Functions
  * 8 Modules
  * 9 Starting with FreeCAD
  * 10 Notes

# Introduction to Python

  * [Page](/Introduction_to_Python "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Introduction_to_Python&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Introduction_to_Python)
  * [Edit](/index.php?title=Introduction_to_Python&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Introduction_to_Python&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Introduction_to_Python.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Introduction_to_Python&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Introduction_to_Python)
  * [Edit](/index.php?title=Introduction_to_Python&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Introduction_to_Python&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Introduction_to_Python&action=history)

General

  * [What links here](/Special:WhatLinksHere/Introduction_to_Python "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Introduction_to_Python "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Introduction_to_Python&oldid=1505083 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Introduction_to_Python&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Introduction_to_Python&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Introduction+to+Python&action=page&filter=&language=en)This is the approved
revision of this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Introduction+to+Python&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Introduction_to_Python/id "Introduction to Python \(1% translated\)")
  * [Deutsch](/Introduction_to_Python/de "Einführung in Python \(100% translated\)")
  * English
  * [Türkçe](/Introduction_to_Python/tr "Python'a Giriş \(10% translated\)")
  * [español](/Introduction_to_Python/es "Introducción a Python \(97% translated\)")
  * [français](/Introduction_to_Python/fr "Introduction à Python \(100% translated\)")
  * [italiano](/Introduction_to_Python/it "Introduzione a Python \(100% translated\)")
  * [polski](/Introduction_to_Python/pl "Wprowadzenie do środowiska Python \(100% translated\)")
  * [português](/Introduction_to_Python/pt "Introdução ao Python \(1% translated\)")
  * [português do Brasil](/Introduction_to_Python/pt-br "Introdução ao Python \(9% translated\)")
  * [română](/Introduction_to_Python/ro "Introducere în Python \(10% translated\)")
  * [svenska](/Introduction_to_Python/sv "Introduction to Python \(1% translated\)")
  * [čeština](/Introduction_to_Python/cs "Introduction to Python/cs \(0% translated\)")
  * [русский](/Introduction_to_Python/ru "Введение в Python \(16% translated\)")
  * [中文（中国大陆）](/Introduction_to_Python/zh-cn "Python简介 \(16% translated\)")
  * [日本語](/Introduction_to_Python/ja "Introduction to Python/Pythonの紹介 \(10% translated\)")
  * [한국어](/Introduction_to_Python/ko "파이썬 소개 \(11% translated\)")

![](/images/6/6f/Arrow-left.svg) [Scripts](/Scripts "Scripts")

[Python scripting tutorial](/Python_scripting_tutorial "Python scripting
tutorial") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

This is a short tutorial for those new to
[Python](https://en.wikipedia.org/wiki/Python_%28programming_language%29).
Python is an open-source, multiplatform [programming
language](https://en.wikipedia.org/wiki/Programming_language). It has several
features that make it different from other programming languages, and very
accessible to new users:

  * It has been designed to be to readable by human beings, making it relatively easy to learn and understand.
  * It is interpreted, this means that programs do not need to be compiled before they can be executed. Python code can be executed immediately, even line by line if you wish.
  * It can be embedded in other programs as a scripting language. FreeCAD has an embedded Python interpreter. You can write Python code to manipulate parts of FreeCAD. This is very powerful, it means you can build your very own tools.
  * It is extensible, you can easily plug new modules into your Python installation and extend its functionality. For example, there are modules that allow Python to read and write images, to communicate with Twitter, to schedule tasks to be performed by your operating system, etc.

The following is a very basic introduction, and by no means a complete
tutorial. But hopefully it will provide a good starting point for further
exploration into FreeCAD and its mechanisms. We strongly encourage you to
enter the code snippets below into a Python interpreter.

## The interpreter

Usually when writing computer programs, you open a text editor or your special
programming environment (which is basically a text editor with some additional
tools), write your program, then compile and execute. Often one or more errors
were made during entry, so your program won't work. You may even get an error
message telling you what went wrong. Then you go back to your text editor,
correct the mistakes, run again, repeating until your program works as
intended.

In Python that whole process can be done transparently inside the Python
interpreter. The interpreter is a Python window with a command prompt, where
you can simply type Python code. If you have installed Python on your computer
(download it from the [Python website](https://www.python.org/) if you are on
Windows or Mac, install it from your package repository if you are on
GNU/Linux), you will have a Python interpreter in your start menu. But, as
already mentioned, FreeCAD also has a built-in Python interpreter: the [Python
console](/Python_console "Python console").

[![](/images/0/0b/FreeCAD_Python_console.png)](/index.php?title=File:FreeCAD_Python_console.png&filetimestamp=20190921064541&)

The FreeCAD Python console

If you don't see it, click on **View → Panels → Python console**. The Python
console can be resized and also undocked.

The interpreter shows the Python version, then a `>>>` symbol which is the
command prompt. Writing code in the interpreter is simple: one line is one
instruction. When you press Enter, your line of code will be executed (after
being instantly and invisibly compiled). For example, try writing this:

    
    
    print("hello")
    

`print()` is a Python command that, obviously, prints something on the screen.
When you press Enter, the operation is executed, and the message `"hello"` is
printed. If you make an error, for example let's write:

    
    
    print(hello)
    

Python will immediately tell you so. In this case Python doesn't know what
`hello` is. The `" "` characters specify that the content is a string,
programming jargon for a piece of text. Without these the `print()` command
doesn't recognize `hello`. By pressing the up arrow you can go back to the
last line of code and correct it.

The Python interpreter also has a built-in help system. Let's say we don't
understand what went wrong with `print(hello)` and we want specific
information about the command:

    
    
    help(print)
    

You'll get a long and complete description of everything the `print()` command
can do.

Now that you understand the Python interpreter, we can continue with the more
serious stuff.

Top

## Variables

Very often in programming you need to store a value under a name. That's where
variables come in. For example, type this:

    
    
    a = "hello"
    print(a)
    

You probably understand what happened here, we saved the string `"hello"`
under the name `a`. Now that `a` is known we can use it anywhere, for example
in the `print()` command. We can use any name we want, we just need to follow
some simple rules, such as not using spaces or punctuation and not using
Python keywords. For example, we can write:

    
    
    hello = "my own version of hello"
    print(hello)
    

Now `hello` is not an undefined any more. Variables can be modified at any
time, that's why they are called variables, their content can vary. For
example:

    
    
    myVariable = "hello"
    print(myVariable)
    myVariable = "good bye"
    print(myVariable)
    

We changed the value of `myVariable`. We can also copy variables:

    
    
    var1 = "hello"
    var2 = var1
    print(var2)
    

It is advisable to give meaningful names to your variables. After a while you
won't remember what your variable named `a` represents. But if you named it,
for example, `myWelcomeMessage` you'll easily remember its purpose. Plus your
code is a step closer to being self-documenting.

Case is very important, `myVariable` is not the same as `myvariable`. If you
were to enter `print(myvariable)` it would come back with an error as not
defined.

Top

## Numbers

Of course Python programs can deal with all kinds of data, not just text
strings. One thing is important, Python must know what kind of data it is
dealing with. We saw in our print hello example, that the `print()` command
recognized our `"hello"` string. By using `" "` characters, we specified that
what follows is a text string.

We can always check the data type of a variable with the `type()` command:

    
    
    myVar = "hello"
    type(myVar)
    

It will tell us the content of `myVar` is a `'str'`, which is short for
string. We also have other basic data types such as integer and float numbers:

    
    
    firstNumber = 10
    secondNumber = 20
    print(firstNumber + secondNumber)
    type(firstNumber)
    

Python knows that 10 and 20 are integer numbers, so they are stored as
`'int'`, and Python can do with them everything it can do with integers. Look
at the results of this:

    
    
    firstNumber = "10"
    secondNumber = "20"
    print(firstNumber + secondNumber)
    

Here we forced Python to consider that our two variables are not numbers but
pieces of text. Python can add two pieces of text together, although in that
case, of course, it won't perform any arithmetic. But we were talking about
integer numbers. There are also float numbers. The difference is float numbers
can have a decimal part and integer numbers do not:

    
    
    var1 = 13
    var2 = 15.65
    print("var1 is of type ", type(var1))
    print("var2 is of type ", type(var2))
    

Integers and floats can be mixed together without problems:

    
    
    total = var1 + var2
    print(total)
    print(type(total))
    

Because `var2` is a float Python automatically decides that the result must
also be a float. But there are cases where Python does not knows what type to
use. For example:

    
    
    varA = "hello 123"
    varB = 456
    print(varA + varB)
    

This results in an error, `varA` is a string and `varB` is an integer, and
Python doesn't know what to do. However, we can force Python to convert
between types:

    
    
    varA = "hello"
    varB = 123
    print(varA + str(varB))
    

Now that both variables are strings the operation works. Note that we
"stringified" `varB` at the time of printing, but we didn't change `varB`
itself. If we wanted to turn `varB` permanently into a string, we would need
to do this:

    
    
    varB = str(varB)
    

We can also use `int()` and `float()` to convert to integer and float if we
want:

    
    
    varA = "123"
    print(int(varA))
    print(float(varA))
    

You must have noticed that we have used the `print()` command in several ways.
We printed variables, sums, several things separated by commas, and even the
result of another Python command. Maybe you also saw that these two commands:

    
    
    type(varA)
    print(type(varA))
    

have the same result. This is because we are in the interpreter, and
everything is automatically printed. When we write more complex programs that
run outside the interpreter, they won't print automatically, so we'll need to
use the `print()` command. With that in mind let's stop using it here. From
now on we will simply write:

    
    
    myVar = "hello friends"
    myVar
    

Top

## Lists

Another useful data type is a list. A list is a collection of other data. To
define a list we use `[ ]`:

    
    
    myList = [1, 2, 3]
    type(myList)
    myOtherList = ["Bart", "Frank", "Bob"]
    myMixedList = ["hello", 345, 34.567]
    

As you can see a list can contain any type of data. You can do many things
with a list. For example, count its items:

    
    
    len(myOtherList)
    

Or retrieve one item:

    
    
    myName = myOtherList[0]
    myFriendsName = myOtherList[1]
    

While the `len()` command returns the total number of items in a list, the
first item in a list is always at position `0`, so in our `myOtherList`
`"Bob"` will be at position `2`. We can do much more with lists such as
sorting items and removing or adding items.

Interestingly a text string is very similar to a list of characters in Python.
Try doing this:

    
    
    myvar = "hello"
    len(myvar)
    myvar[2]
    

Usually what you can do with lists can also be done with strings. In fact both
lists and strings are sequences.

Apart from strings, integers, floats and lists, there are more built-in data
types, such as dictionaries, and you can even create your own data types with
classes.

Top

## Indentation

One important use of lists is the ability to "browse" through them and do
something with each item. For example look at this:

    
    
    alldaltons = ["Joe", "William", "Jack", "Averell"]
    for dalton in alldaltons:
        print(dalton + " Dalton")
    

We iterated (programming jargon) through our list with the `for in` command
and did something with each of the items. Note the special syntax: the `for`
command terminates with `:` indicating the following will be a block of one of
more commands. In the interpreter, immediately after you enter the command
line ending with `:`, the command prompt will change to `...` which means
Python knows that there is more to come.

How will Python know how many of the next lines will need to be executed
inside the `for in` operation? For that, Python relies on indentation. The
next lines must begin with a blank space, or several blank spaces, or a tab,
or several tabs. And as long as the indentation stays the same the lines will
be considered part of the `for in` block. If you begin one line with 2 spaces
and the next one with 4, there will be an error. When you have finished, just
write another line without indentation, or press Enter to come back from the
`for in` block

Indentation also aids in program readability. If you use large indentations
(for example use tabs instead of spaces) when you write a big program, you'll
have a clear view of what is executed inside what. We'll see that other
commands use indented blocks of code as well.

The `for in` command can be used for many things that must be done more than
once. It can, for example, be combined with the `range()` command:

    
    
    serie = range(1, 11)
    total = 0
    print("sum")
    for number in serie:
        print(number)
        total = total + number
    print("----")
    print(total)
    

If you have been running the code examples in an interpreter by copy-pasting,
you will find the previous block of text will throw an error. Instead, copy to
the end of the indented block, i.e. the end of the line `total = total +
number` and then paste in the interpreter. In the interpreter press Enter
until the three dot prompt disappears and the code runs. Then copy the final
two lines followed by another Enter. The final answer should appear.

If you type into the interpreter `help(range)` you will see:

    
    
    range(...)
        range(stop) -> list of integers
        range(start, stop[, step]) -> list of integers
    

Here the square brackets denote an optional parameter. However all are
expected to be integers. Below we will force the step parameter to be an
integer using `int()`:

    
    
    number = 1000
    for i in range(0, 180 * number, int(0.5 * number)):
        print(float(i) / number)
    

Another `range()` example:

    
    
    alldaltons = ["Joe", "William", "Jack", "Averell"]
    for n in range(4):
        print(alldaltons[n], " is Dalton number ", n)
    

The `range()` command also has that strange particularity that it begins with
`0` (if you don't specify the starting number) and that its last number will
be one less than the ending number you specify. That is, of course, so it
works well with other Python commands. For example:

    
    
    alldaltons = ["Joe", "William", "Jack", "Averell"]
    total = len(alldaltons)
    for n in range(total):
        print(alldaltons[n])
    

Another interesting use of indented blocks is with the `if` command. This
command executes a code block only if a certain condition is met, for example:

    
    
    alldaltons = ["Joe", "William", "Jack", "Averell"]
    if "Joe" in alldaltons:
        print("We found that Dalton!!!")
    

Of course this will always print the sentence, but try replacing the second
line with:

    
    
    if "Lucky" in alldaltons:
    

Then nothing is printed. We can also specify an `else` statement:

    
    
    alldaltons = ["Joe", "William", "Jack", "Averell"]
    if "Lucky" in alldaltons:
        print("We found that Dalton!!!")
    else:
        print("Such Dalton doesn't exist!")
    

Top

## Functions

There are very few [standard Python
commands](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)
and we already know several of them. But you can create your own commands. In
fact, most of the additional modules that you can plug into your Python
installation do just that, they add commands that you can use. A custom
command in Python is called a function and is made like this:

    
    
    def printsqm(myValue):
        print(str(myValue) + " square meters")
    
    printsqm(45)
    

The `def()` command defines a new function, you give it a name, and inside the
parenthesis you define the arguments that the function will use. Arguments are
data that will be passed to the function. For example, look at the `len()`
command. If you just write `len()`, Python will tell you it needs an argument.
Which is obvious: you want to know the length of something. If you write
`len(myList)` then `myList` is the argument that you pass to the `len()`
function. And the `len()` function is defined in such a way that it knows what
to do with this argument. We have done the same thing with our `printsqm`
function.

The `myValue` name can be anything, and it will only be used inside the
function. It is just a name you give to the argument so you can do something
with it. By defining arguments you also to tell the function how many to
expect. For example, if you do this:

    
    
    printsqm(45, 34)
    

there will be an error. Our function was programmed to receive just one
argument, but it received two, `45` and `34`. Let's try another example:

    
    
    def sum(val1, val2):
        total = val1 + val2
        return total
    
    myTotal = sum(45, 34)
    

Here we made a function that receives two arguments, sums them, and returns
that value. Returning something is very useful, because we can do something
with the result, such as store it in the `myTotal` variable.

Top

## Modules

Now that you have a good idea of how Python works, you will need to know one
more thing: How to work with files and modules.

Until now, we have written Python instructions line by line in the
interpreter. This method is obviously not suitable for larger programs.
Normally the code for Python programs is stored in files with the .py
extension. Which are just plain text files and any text editor (Linux gedit,
emacs, vi or even Windows Notepad) can be used to create and edit them.

There are several of ways to execute a Python program. In Windows, simply
right-click your file, open it with Python, and execute it. But you can also
execute it from the Python interpreter itself. For this, the interpreter must
know where your program is. In FreeCAD the easiest way is to place your
program in a folder that FreeCAD's Python interpreter knows by default, such
as FreeCAD's user Mod folder:

  * On Linux it is usually /home/<username>/.local/share/FreeCAD/Mod/ (0.20 and above) or /home/<username>/.FreeCAD/Mod/ (0.19 and below).
  * On Windows it is %APPDATA%\FreeCAD\Mod\, which is usually C:\Users\<username>\Appdata\Roaming\FreeCAD\Mod\.
  * On macOS it is usually /Users/<username>/Library/Application Support/FreeCAD/Mod/.

Let's add a subfolder there called scripts and then write a file like this:

    
    
    def sum(a,b):
        return a + b
    
    print("myTest.py succesfully loaded")
    

Save the file as myTest.py in the scripts folder, and in the interpreter
window write:

    
    
    import myTest
    

without the .py extension. This will execute the contents of the file, line by
line, just as if we had written it in the interpreter. The sum function will
be created, and the message will be printed. Files containing functions, like
ours, are called modules.

When we write a `sum()` function in the interpreter, we execute it like this:

    
    
    sum(14, 45)
    

But when we import a module containing a `sum()` function the syntax is a bit
different:

    
    
    myTest.sum(14, 45)
    

That is, the module is imported as a "container", and all its functions are
inside that container. This is very useful, because we can import a lot of
modules, and keep everything well organized. Basically when you see
`something.somethingElse`, with a dot in between, then this means
`somethingElse` is inside `something`.

We can also import our sum() function directly into the main interpreter
space:

    
    
    from myTest import *
    sum(12, 54)
    

Almost all modules do that: they define functions, new data types and classes
that you can use in the interpreter or in your own Python modules, because
nothing prevents you from importing other modules inside your module!

How do we know what modules we have, what functions are inside and how to use
them (that is, what kind of arguments they need)? We have already seen that
Python has a `help()` function. Doing:

    
    
    help("modules")
    

will give us a list of all available modules. We can import any of them and
browse their content with the `dir()` command:

    
    
    import math
    dir(math)
    

We'll see all the functions contained in the `math` module, as well as strange
stuff named `__doc__`, `__file__`, `__name__`. Every function in a well made
module has a `__doc__` that explains how to use it. For example, we see that
there is a `sin()` function inside the math module. Want to know how to use
it?

    
    
    print(math.sin.__doc__)
    

It may not be evident, but on either side of `doc` are two underscore
characters.

And finally one last tip: When working on new or existing code, it is better
to not use the FreeCAD macro file extension, .FCMacro, but instead use the
standard .py extension. This is because Python doesn't recognize the .FCMacro
extension. If you use .py your code can be easily loaded with `import`, as we
have already seen, and also reloaded with `importlib.reload()`:

    
    
    import importlib
    importlib.reload(myTest)
    

There is however an alternative:

    
    
    exec(open("C:/PathToMyMacro/myMacro.FCMacro").read())
    

Top

## Starting with FreeCAD

Hopefully you now have a good idea of how Python works, and you can start
exploring what FreeCAD has to offer. FreeCAD's Python functions are all well
organized in different modules. Some of them are already loaded (imported)
when you start FreeCAD. Just try:

    
    
    dir()
    

Top

## Notes

  * FreeCAD was originally designed to work with Python 2. Since Python 2 reached the end of its life in 2020, future development of FreeCAD will be done exclusively with Python 3, and backwards compatibility will not be supported.
  * Much more information about Python can be found in the [official Python tutorial](https://docs.python.org/3/tutorial/index.html) and the [official Python reference](https://docs.python.org/3/reference/).

Top

![](/images/6/6f/Arrow-left.svg) [Scripts](/Scripts "Scripts")

[Python scripting tutorial](/Python_scripting_tutorial "Python scripting
tutorial") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), Introduction to Python, [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects "Scripted objects"), [Viewproviders](/Viewprovider "Viewprovider") ([Custom icon in tree view](/Custom_icon_in_tree_view "Custom icon in tree view"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/Scenegraph "Scenegraph"), [Pivy](/Pivy "Pivy")
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

