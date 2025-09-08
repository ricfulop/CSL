---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-variables/
scraped_at: 2025-09-08T15:41:57.108329
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

[VBScript
Variables](https://developer.rhino3d.com/guides/rhinoscript/vbscript-
variables/)

  * Overview
  * Declaration
  * Naming Restrictions
  * Scope & Lifetime
  * Assigning Values
  * Scalar Variables & Arrays
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript Variables

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

A variable is a convenient placeholder that refers to a computer memory
location where you can store program information that may change during the
time your script is running. For example, you might create a variable called
ClickCount to store the number of times a user performs a certain operation.
Where the variable is stored in computer memory is unimportant. What is
important is that you only have to refer to a variable by name to see or
change its value. In VBScript, variables are always of one fundamental data
type: [Variant](https://developer.rhino3d.com/guides/rhinoscript/vbscript-
datatypes/).

## Declaration

You declare variables explicitly in your script using the `Dim` statement, the
`Public` statement, and the `Private` statement. For example:

    
    
    Dim AngleDegrees
    

You declare multiple variables by separating each variable name with a comma.
For example:

    
    
    Dim Top, Bottom, Left, Right
    

## Naming Restrictions

Variable names follow the standard rules for naming anything in VBScript. A
variable name:

  * Must begin with an alphabetic character.
  * Cannot contain an embedded period.
  * Must not exceed 255 characters.
  * Must be unique in the scope in which it is declared.

## Scope & Lifetime

A variable’s scope is determined by where you declare it. When you declare a
variable within a procedure, only code within that procedure can access or
change the value of that variable. It has local scope and is a procedure-level
variable. If you declare a variable outside a procedure, you make it
recognizable to all the procedures in your script. This is a script-level
variable, and it has script-level scope.

The lifetime of a variable depends on how long it exists. The lifetime of a
script-level variable extends from the time it is declared until the time the
script is finished running. At procedure level, a variable exists only as long
as you are in the procedure. When the procedure exits, the variable is
destroyed. Local variables are ideal as temporary storage space when a
procedure is executing. You can have local variables of the same name in
several different procedures because each is recognized only by the procedure
in which it is declared.

## Assigning Values

Values are assigned to variables creating an expression as follows: the
variable is on the left side of the expression and the value you want to
assign to the variable is on the right. For example:

    
    
    B = 200
    

## Scalar Variables & Arrays

Much of the time, you only want to assign a single value to a variable you
have declared. A variable containing a single value is a scalar variable.
Other times, it is convenient to assign more than one related value to a
single variable. Then you can create a variable that can contain a series of
values. This is called an array variable. Array variables and scalar variables
are declared in the same way, except that the declaration of an array variable
uses parentheses `( )` following the variable name. In the following example,
a single-dimension array containing 11 elements is declared:

    
    
    Dim A(10)
    

Although the number shown in the parentheses is 10, all arrays in VBScript are
zero-based, so this array actually contains 11 elements. In a zero-based
array, the number of array elements is always the number shown in parentheses
plus one. This kind of array is called a fixed-size array.

You assign data to each of the elements of the array using an index into the
array. Beginning at zero and ending at 10, data can be assigned to the
elements of an array as follows:

    
    
    A(0) = 256
    A(1) = 324
    A(2) = 100
    '. . .
    A(10) = 55
    

Similarly, the data can be retrieved from any element using an index into the
particular array element you want. For example:

    
    
    '. . .
    SomeVariable = A(8)
    '. . .
    

Arrays aren’t limited to a single dimension. You can have as many as 60
dimensions, although most people can’t comprehend more than three or four
dimensions. You can declare multiple dimensions by separating an array’s size
numbers in the parentheses with commas. In the following example, the MyTable
variable is a two-dimensional array consisting of 6 rows and 11 columns:

    
    
    Dim MyTable(5, 10)
    

In a two-dimensional array, the first number is always the number of rows; the
second number is the number of columns.

You can also declare an array whose size changes during the time your script
is running. This is called a dynamic array. The array is initially declared
within a procedure using either the `Dim` statement or using the `ReDim`
statement. However, for a dynamic array, no size or number of dimensions is
placed inside the parentheses. For example:

    
    
    Dim MyArray()
    ReDim AnotherArray()
    

To use a dynamic array, you must subsequently use `ReDim` to determine the
number of dimensions and the size of each dimension. In the following example,
`ReDim` sets the initial size of the dynamic array to 25. A subsequent `ReDim`
statement resizes the array to 30, but uses the `Preserve` keyword to preserve
the contents of the array as the resizing takes place.

    
    
    ReDim MyArray(25)
    ' . . .
    ReDim Preserve MyArray(30)
    

There is no limit to the number of times you can resize a dynamic array,
although if you make an array smaller, you lose the data in the eliminated
elements.

## Related topics

  * [VBScript Data Types](https://developer.rhino3d.com/guides/rhinoscript/vbscript-datatypes/)
  * [VBScript Procedures](https://developer.rhino3d.com/guides/rhinoscript/vbscript-procedures/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
variables/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
variables/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

