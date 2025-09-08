---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-conditionals/
scraped_at: 2025-09-08T15:41:59.207919
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
Conditionals](https://developer.rhino3d.com/guides/rhinoscript/vbscript-
conditionals/)

  * Overview
  * If Then Else
    * If True
    * Some True Some False
    * Several Alternatives
  * Select Case
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript Conditionals

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

You can control the flow of your script with conditional statements and
looping statements. Using conditional statements, you can write VBScript code
that makes decisions and repeats actions. The following conditional statements
are available in VBScript:

  * `If`…`Then`…`Else` statement
  * `Select Case` statement

## If Then Else

The `If`…`Then`…`Else` statement is used to evaluate whether a condition is
True or False and, depending on the result, to specify one or more statements
to run. Usually the condition is an expression that uses a comparison operator
to compare one value or variable with another. For information about
comparison operators, see the [VBScript
Operators](https://developer.rhino3d.com/guides/rhinoscript/vbscript-
operators/) guide. `If`…`Then`…`Else` statements can be nested to as many
levels as you need.

### If True

To run only one statement when a condition is True, use the single-line syntax
for the `If`…`Then`…`Else` statement. The following example shows the single-
line syntax. Notice that this example omits the `Else` keyword…

    
    
    Sub FixDate()
      Dim myDate
      myDate = #11/17/2008#
      If myDate < Now Then myDate = Now
    End Sub
    

To run more than one line of code, you must use the multiple-line (or block)
syntax. This syntax includes the `End If` statement, as shown in the following
example:

    
    
    Sub AlertUser(value)
      If value = 0 Then
        MyLayerColor = vbRed
        MyObjectColor = vbBlue
      End If
    End Sub
    

### Some True Some False

You can use an `If`…`Then`…`Else` statement to define two blocks of executable
statements: one block to run if the condition is True, the other block to run
if the condition is False…

    
    
    Sub AlertUser(value)
      If value = 0 Then
        MyLayerColor = vbRed
        MyObjectColor = vbBlue
      Else
        MyLayerColor = vbGreen
        MyObjectColor = vbBlack
      End If
    End Sub
    

### Several Alternatives

A variation on the `If`…`Then`…`Else` statement allows you to choose from
several alternatives. Adding `ElseIf` clauses expands the functionality of the
`If`…`Then`…`Else` statement so you can control program flow based on
different possibilities. For example:

    
    
    Sub ReportValue(value)
      If value = 0 Then
        MsgBox value
      ElseIf value = 1 Then
        MsgBox value
      ElseIf value = 2 then
        Msgbox value
      Else
        Msgbox "Value out of range!"
      End If
    End Sub
    

You can add as many `ElseIf` clauses as you need to provide alternative
choices. Extensive use of the `ElseIf` clauses often becomes cumbersome. A
better way to choose between several alternatives is the `Select Case`
statement.

## Select Case

The `Select Case` structure provides an alternative to `If`…`Then`…`Else` for
selectively executing one block of statements from among multiple blocks of
statements. A `Select Case` statement provides capability similar to the
`If`…`Then`…`Else` statement, but it makes code more efficient and readable.

A `Select Case` structure works with a single test expression that is
evaluated once, at the top of the structure. The result of the expression is
then compared with the values for each `Case` in the structure. If there is a
match, the block of statements associated with that `Case` is executed, as in
the following example…

    
    
    Select Case MyVar
      Case "red"     MyColor = vbRed
      Case "green"   MyColor = vbGreen
      Case "blue"    MyColor = vbBlue
      Case Else      MsgBox "Pick another color."
    End Select
    

Notice that the `Select Case` structure evaluates an expression once at the
top of the structure. In contrast, the `If`…`Then`…`Else` structure can
evaluate a different expression for each `ElseIf` statement. You can replace
an `If`…`Then`…`Else` structure with a `Select Case` structure only if each
`ElseIf` statement evaluates the same expression.

## Related Topics

  * [What are VBScript and RhinoScript?](https://developer.rhino3d.com/guides/rhinoscript/what-are-vbscript-rhinoscript/)
  * [VBScript Operators](https://developer.rhino3d.com/guides/rhinoscript/vbscript-operators/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
conditionals/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
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

