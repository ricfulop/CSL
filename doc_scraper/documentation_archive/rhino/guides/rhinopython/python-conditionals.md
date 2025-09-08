---
url: https://developer.rhino3d.com/guides/rhinopython/python-conditionals/
scraped_at: 2025-09-08T15:37:21.063599
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

[Python Conditionals](https://developer.rhino3d.com/guides/rhinopython/python-
conditionals/)

  * Overview
    * if
    * if..else
    * if..elif..elif..else
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Python Conditionals

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

You can control the flow of your script with conditional statements and
looping statements. Using conditional statements, you can write Python code
that makes decisions and repeats actions. The following conditional statements
are available in Python:

  * `if` statement
  * `if`…`else` statement
  * `if`…`elif`…`elif`…`else` nested statement

The `if`… statement is used to evaluate whether a condition is True or False
and, depending on the result, to specify one or more statements to run.
Usually the condition is an expression that uses a comparison operator to
compare one value or variable with another. For information about comparison
operators, see the [Python
Operators](https://developer.rhino3d.com/guides/rhinopython/python-operators/)
guide. `if`… and `if...elif` statements can be nested to as many levels as you
need.

Python programming language assumes any non-zero and non-null values as TRUE,
and if it is either zero or null, then it is assumed as FALSE value.

### if

To run only one statement when a condition is True, use the single-line syntax
for the `if`… statement. The following example shows the single-line syntax.

    
    
    var1 = 350
    if var1 == 350 : print ("The value of the variable is 350")
    

To run more than one line of code, you must use the multiple-line (or block)
syntax. The first line ends in a colon (:). As with all Python block syntax,
the whitespaces to the left of the lines must be the same throughout the
block. As an example:

    
    
    var1 = 350
    if var1 == 350 :
        print ("The value of the variable is 350")
        var2 = 450
        print ("The value of variable 2 is 450")
    

### if..else

You can use an `if`…`else` statement to define two blocks of executable
statements: one block to run if the condition is True, the other block to run
if the condition is False…

    
    
    var1 = 350
    if var1 == 0 :
        MyLayerColor = 'vbRed'
        MyObjectColor = 'vbBlue'
    else :
        MyLayerColor = 'vbGreen'
        MyObjectColor = 'vbBlack'
    print (MyLayerColor)
    

### if..elif..elif..else

A variation on the `if`…`else` statement allows you to choose from several
alternatives. Adding `elif` clauses expands the functionality of the
`if`…`else` statement so you can control program flow based on multiple
different possibilities. For example:

    
    
    var1 = 0
    if var1 == 0 :
        print ("This is the first " + str(var1))
    elif var1 == 1 :
        print ("This is the second " + str(var1))
    elif var1 == 2 :
        print ("This is the third " + str(var1))
    else :
        print ("Value out of range!")
    

You can add as many `elif` clauses as you need to provide alternative choices.
Thie `elif` statement takes the place of the `Select Case` statement in other
languages.

For more information on nesting if..elif..else statements see [Python nested
if statements on
TutorialsPoint](https://www.tutorialspoint.com/python/nested_if_statements_in_python.htm)

## Related Topics

  * [What are Python and RhinoScriptSyntax?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Python Operators](https://developer.rhino3d.com/guides/rhinopython/python-operators/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
conditionals/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
conditionals/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

