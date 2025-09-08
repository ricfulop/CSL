---
url: https://developer.rhino3d.com/guides/rhinopython/python-procedures/
scraped_at: 2025-09-08T15:37:18.011596
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

[Python Procedures](https://developer.rhino3d.com/guides/rhinopython/python-
procedures/)

  * Overview
  * Import Modules
  * Common Modules
  * User-Defined Procedures
  * Getting Data In and Out
  * Assigning a Function to a Variable
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Python Procedures

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

In Python a function is a named block of code that can perform a reusable
action. This allows Python code to be broken down into functional, reusable
blocks of code.

There are many modules available for Python. These modules contain a great
number of pre-defined procedures that can be very useful. There are libraries
that help with Date, Time, Math, etc.

## Import Modules

You can use any Python file as a module by using the import statement. Once
imported all the procedures in the import are available. The standard syntax
for importing is:

    
    
    import rhinoscriptsyntax
    

To import more the one module, use commas to separate module names:

    
    
    import rhinoscriptsyntax, time, math
    

To access procedures in imported modules, prefix the function with the
imported model name, separated by a period (.):

    
    
    import time
    
    print (time.strftime("%H:%M:%S")) #strftime is a proccedure in the time module.
    

The `import` statement can also be used to change the reference name of the
incoming module. Use this function to make module names shorter to use and
easier to read in the code. A very common example of this is how we normally
will shorted the `rhinoscriptsyntax` module to `rs` for convenience:

    
    
    import rhinoscriptsyntax as rs
    
    rs.AddPoint (1, 2, 3) # The Rhinoscriptsyntax module is accessed throught 'rs' abreviation.
    

It is also possible to import only a portion of a module. In the following
case, only certain namespaces are imported from the larger `Syste.IO` module:

    
    
    from System.IO import Path, File, FileInfo, FileAttributes
    

The imported modules above are referenced by using `Path`, `File`, `FileInfo`,
`FileAttributes` as namespaces.

## Common Modules

There are many modules available for Python. Some of the most useful to Rhino
Python are:

  * Rhinoceros modules 
    * rhinoscriptsyntax - The basic rhino library of procedures
    * rhino -
  * String Services 
    * string — Common string operations
    * StringIO — Read and write strings as files
    * fpformat — Floating point conversions
  * Date and Time 
    * datetime — Basic date and time types
    * time — Time access and conversions
  * Numeric and Mathematical Modules 
    * math — Mathematical functions
    * fractions — Rational numbers
    * random — Generate pseudo-random numbers
  * File and Directory Access 
    * System.IO — Common pathname manipulations
    * tempfile — Generate temporary files and directories
    * csv — CSV File Reading and Writing

A complete list of predefined modules in Python, see the [Python Standard
Library modules](https://docs.python.org/2/library/)

## User-Defined Procedures

A `Function` is a series of Python statements begins by a `def`, followed by
the function name and enclosed in parenthesis. A Function may or may not
return a value. A Function procedure can take arguments (constants, variables,
or expressions that are passed by a calling procedure). If a Function
procedure has no arguments, its `def` statement should include an empty set of
parentheses `()`. Parameters can also be defined within the parenthesis. The
parenthesis are followed by a colon (:) to end the first line.

The end of the function is marked by the loss of whitespace in the next line
of the code (ending the code block). It is common practice to use a `return`
statement followed by the argument to return a value. You may also finish a
function with a return statement and a simple colon (;).

In the following example, the Celsius `def` calculates degrees Celsius from
degrees Fahrenheit. When the def is called from the `ConvertTemp` def
procedure, a variable containing the argument value is passed to the def. The
result of the calculation is returned to the calling procedure and displayed
in a message box.

    
    
    def Celsius(fDegrees):
        _Celsius = (fDegrees - 32) * 5 / 9
        return _Celsius;
    
    # Use this code to call the Celsius function
    temp = raw_input("Please enter the temperature in degrees F.", 1)
    MsgBox "The temperature is " & Celsius(temp) & " degrees C."
    

## Getting Data In and Out

Each piece of data is passed into your procedures using an argument. Arguments
serve as placeholders for the data you want to pass into your procedure. You
can name your arguments any valid variable name. When you create a procedure
parentheses must be included after the name of the procedure. Any arguments
are placed inside these parentheses, separated by spaces. For example, in the
following example, `fDegrees` is a placeholder for the value being passed into
the Celsius function for conversion.

    
    
    Function Celsius(fDegrees)
        _Celsius = (fDegrees - 32) * 5 / 9
        return _Celsius;
    

To call a procedure from another procedure, type the name of the procedure
along with values for any required arguments, each separated by a space.

The function will returns a single value based on its final `return`
statement. A return statement with a variable name, followed by a semicolon
(;) returns the reference to that variable. A return statement with simply a
semicolon (;) returns nothing. The return statement is not required to end a
procedure.

## Assigning a Function to a Variable

Python allows a variable to contain a function.

## Related Topics

  * [What are Python and RhinoScriptSyntax?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Additional information on Functions in Python](https://www.tutorialspoint.com/python/python_functions.htm)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
procedures/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
procedures/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

