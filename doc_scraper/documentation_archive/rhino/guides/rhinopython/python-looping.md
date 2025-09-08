---
url: https://developer.rhino3d.com/guides/rhinopython/python-looping/
scraped_at: 2025-09-08T15:37:22.024063
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[Python Looping](https://developer.rhino3d.com/guides/rhinopython/python-
looping/)

  * Overview
  * For Loop
  * While Loop
  * Nested Loops
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Python Looping

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Looping allows you to run a group of statements repeatedly. Some loops repeat
statements until a condition is _False_ ; others repeat statements until a
condition is _True_. There are also loops that repeat statements a specific
number of times.

The following looping statements are available in Python:

  * `for` \- Uses a counter or loops through a each item in a list a specified number of times.
  * `while` \- Loops while a condition is True.
  * Nested loops - Repeats a group of statements for each item in a collection or each element of an array.

Loop statements use a very specific syntax. Unlike other languages, Python
does not use an end statement for its loop syntax. The initial Loop statement
is followed by a colon `:` symbol. Then the next line will be indented by 4
spaces. It is these spaces to the left of the line that is key.

    
    
    for c in range(0, 3):
       This is the the loop
       This is a second line and the last line of the for loop
    This line is not part of the loop. It is the first line in the rest of the script.
    .....
    

Each subsequent lone in the loop also needs to be indented by 4 or more
spaces. If a line is not indented it is considered outside the loop and will
also terminate any additional lines considered in the loop. A common mistake
is remove the spaces and therefore prematurely end the loop.

## For Loop

You can use _for_ statements to run a block of statements a specific number of
times.

Using Python to loop through each item in any type of list based structure is
very easy.

For loops, use a counter variable whose value increases or decreases with each
repetition of the loop.

The following example causes a procedure to execute 4 times. The _for_
statement specifies the counter variable `x` and its start and end values.
Python will automatically increments the counter (x) variable by 1 after
coming to end of the execution block.

    
    
    for x in range(0, 3):
        print ("We're on loop " + str(x))
    

Python can use any iterable method as a the for loop counter. In the case
above we are using `range()`. Other iterable objects can be lists or a string.
You can also create you own iterable objects if needed.

Sometimes it is required to increase or decrease the counter variable by the
value you specify. In the following example, the counter variable `j` is
incremented by 2 each time the loop repeats. When the loop is finished, the
total is the sum of 0, 2, 4, 6 and 8.

    
    
    for j in range(0, 10, 2):
        print ("We're on loop " + str(j))
    

To decrease the counter variable, use a negative `range` value. You must
specify an end value that is less than the start value. In the following
example, the counter variable `j` is decreased by 2 each time the loop
repeats. When the loop is finished, total is the sum of 10, 8, 6, 4, and 2.

    
    
     for j in range(10, 0, -2):
        print ("We're on loop " + str(j))
    

You can exit any _for_ statement before the counter reaches its end value by
using the `break` statement. Because you usually want to exit only in certain
situations, such as when an error occurs, you could also use the `if`
statement in the _True_ statement block. If the condition is _False_ , the
loop runs as usual.

More information on the `for` loop can be found at the [Python.org For Loops
article](https://wiki.python.org/moin/ForLoop).

## While Loop

Use the `while` loop to check a condition before each execution of the loop.

    
    
    var1 = 2
    while var1 < 32:
        var1 = var1 * 2
        print var1
    print ("Exited while loop.")
    

_while_ loops are not used as much as _for_ loops. But _while_ loops are used
often in in cases the following way, polling for specific input or a loop that
will execute forever until a condition is met:

    
    
    while True:
        n = raw_input("Please enter 'hello':")
        if n.strip() == 'hello':
            break
    

As you can see, this compacts the whole thing into a piece of code managed
entirely by the while loop. Having True as a condition ensures that the code
runs until it’s broken by n.strip() equaling ‘hello’.

More information on the `while` loop can be found at the [Python.org While
Loop article](https://wiki.python.org/moin/WhileLoop).

## Nested Loops

Python allows for loops to be nested inside one another. Any type of loop can
be nested within any other type of loop.

    
    
    for x in range(0, 100):
       if x % 2 == 0:
          print (str(x) + " is an even number.")
    

## Related Topics

  * [What are VBScript and RhinoScript?](https://developer.rhino3d.com/guides/rhinoscript/what-are-vbscript-rhinoscript/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
looping/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
looping/index.md) [ Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

