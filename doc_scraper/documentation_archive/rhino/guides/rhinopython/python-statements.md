---
url: https://developer.rhino3d.com/guides/rhinopython/python-statements/
scraped_at: 2025-09-08T15:37:16.878961
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

[Python Basic Syntax](https://developer.rhino3d.com/guides/rhinopython/python-
statements/)

  * Overview
  * End of Statements

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Python Basic Syntax

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Many scripting and programming languages, such as JScript, C#, and C++, make
no attempt to match the code that is run with the actual physical lines typed
into the text editor. This is because they not recognize the end of a line of
code until it sees the termination character (in these cases, the semicolon).
Thus, the actual physical lines of type taken up by the code are irrelevant.

Unlike other languages, Python does not use an end of line character. Most of
the time a simple `Enter` will do. Yet, Python is very particular about
indentation, spaces and lines in certain cases. This document is to help
understand Python formatting.

It is important to understand how Python interprets:

  2. End of Statement
  3. Names and Capitalization
  4. Comments
  5. Block Structures
  6. Tabs and Spaces

For the official very detailed documentation on Python Syntax, see the [Style
Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## End of Statements

To end a statement in Python, you do not have to type in a semicolon or other
special character; you simply press `Enter`. For example, this code will
generate a syntax error:

    
    
    message
    =
    'Hello World!'
    

This will not:

    
    
    message = 'Hello World!'
    

In general, the lack of a required statement termination character simplifies
script writing in Python. There is, however, one complication: To enhance
readability, it is recommended that you limit the length of any single line of
code to 79 characters. What happens, then, if you have a line of code that
contains 100 characters?

Although it might seem like the obvious solution, you cannot split a statement
into multiple lines simply by entering a carriage return. For example, the
following code snippet returns a run-time error in Python because a statement
was split by using `Enter`.

    
    
      message= 'This message will generate an error because
      it was split by using the enter button on your
      keyboard'
    

You cannot split a statement into multiple lines in Python by pressing
`Enter`. Instead, use the backslash (`\`) to indicate that a statement is
continued on the next line. In the revised version of the script, a blank
space and an underscore indicate that the statement that was started on line 1
is continued on line 2. To make it more apparent that line 2 is a continuation
of line 1, line 2 is also indented four spaces. (This was done for the sake of
readability, but you do not have to indent continued lines. )

    
    
    message\
    =\
    'This \
    back slash \
    acts \
    like \
    enter'
    print\
    message
    
    
    
    message\
    =\
    '''triple
    quotes
    will
    span
    multiple lines
    without
    errors'''
    print\
    message
    

Line continuation is automatic when the split comes while a statement is
inside parenthesis ( ( ), brackets ( [ ) or braces ( { ). This is convenient,
but can also lead to errors if there is no closing Parenthesis, bracket or
brace. Python would interpret the rest of the script as one statement in that
case.

Python uses single quotes (’) double quotes (") and triple quotes (""") to
denote literal strings. Only the triple quoted strings (""") also will
automatically continue across the end of line statement.

Sometimes, more than one statement may be put on a single line. In Python a
semicolon (;) can be used to separate multiple statements on the same line.
For instance three statements can be written:

    
    
    y = 3; x = 5; print(x+y)
    

To the Python interpreter, this would be the same set of statements:

    
    
    y = 3
    x = 5
    print(x+y)
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
statements/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
statements/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

