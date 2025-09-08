---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-looping/
scraped_at: 2025-09-08T15:42:01.287812
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

[VBScript Looping](https://developer.rhino3d.com/guides/rhinoscript/vbscript-
looping/)

  * Overview
  * Do Loops
  * Do While
  * Do Until
  * Exiting a Do Loop
  * For…Next
  * For Each…Next
  * Continue
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript Looping

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Looping allows you to run a group of statements repeatedly. Some loops repeat
statements until a condition is _False_ ; others repeat statements until a
condition is _True_. There are also loops that repeat statements a specific
number of times.

The following looping statements are available in VBScript:

  * `Do...Loop` \- Loops while or until a condition is True.
  * `While...Wend` \- Loops while a condition is True.
  * `For...Next` \- Uses a counter to run statements a specified number of times.
  * `For Each...Next` \- Repeats a group of statements for each item in a collection or each element of an array.

## Do Loops

You can use `Do...Loop` statements to run a block of statements an indefinite
number of times. The statements are repeated either while a condition is
_True_ or until a condition becomes _True_.

## Do While

Use the `While` keyword to check a condition in a `Do...Loop` statement. You
can check the condition before you enter the loop (as shown in the following
`ChkFirstWhile` example), or you can check it after the loop has run at least
once (as shown in the `ChkLastWhile` example). In the `ChkFirstWhile`
procedure, if myNum is set to 9 instead of 20, the statements inside the loop
will never run. In the `ChkLastWhile` procedure, the statements inside the
loop run only once because the condition is already _False_.

    
    
     Sub ChkFirstWhile()
       Dim counter, myNum
       counter = 0
       myNum = 20
       Do While myNum > 10
         myNum = myNum - 1
         counter = counter + 1
       Loop
       MsgBox "The loop made " & counter & " repetitions."
     End Sub
    
     Sub ChkLastWhile()
       Dim counter, myNum
       counter = 0
       myNum = 9
       Do
         myNum = myNum - 1
         counter = counter + 1
       Loop While myNum > 10
       MsgBox "The loop made " & counter & " repetitions."
     End Sub
    

## Do Until

There are two ways to use the `Until` keyword to check a condition in a
`Do...Loop` statement. You can check the condition before you enter the loop
(as shown in the following `ChkFirstUntil` example), or you can check it after
the loop has run at least once (as shown in the `ChkLastUntil` example). As
long as the condition is _False_ , the looping occurs.

    
    
     Sub ChkFirstUntil()
       Dim counter, myNum
       counter = 0
       myNum = 20
       Do Until myNum = 10
         myNum = myNum - 1
         counter = counter + 1
       Loop
       MsgBox "The loop made " & counter & " repetitions."
     End Sub
    
     Sub ChkLastUntil()
       Dim counter, myNum
       counter = 0
       myNum = 1
       Do
         myNum = myNum + 1
         counter = counter + 1
       Loop Until myNum = 10
       MsgBox "The loop made " & counter & " repetitions."
     End Sub
    

## Exiting a Do Loop

You can exit a `Do...Loop` by using the `Exit Do` statement. Because you
usually want to exit only in certain situations, such as to avoid an endless
loop, you should use the `Exit Do` statement in the True statement block of an
`If...Then...Else` statement. If the condition is _False_ , the loop runs as
usual.

In the following example, myNum is assigned a value that creates an endless
loop. The `If...Then...Else` statement checks for this condition, preventing
the endless repetition.

    
    
     Sub ExitExample()
       Dim counter, myNum
       counter = 0
       myNum = 9
       Do Until myNum = 10
          myNum = myNum - 1
          counter = counter + 1
          If myNum < 10 Then Exit Do
       Loop
       MsgBox "The loop made " & counter & " repetitions."
     End Sub
    Using While...Wend
    

The `While...Wend` statement is provided in VBScript for those who are
familiar with its usage. However, because of the lack of flexibility in
`While...Wend`, it is recommended that you use `Do...Loop` instead.

## For…Next

You can use `For...Next` statements to run a block of statements a specific
number of times. For loops, use a counter variable whose value increases or
decreases with each repetition of the loop.

The following example causes a procedure called `MyProc` to execute 50 times.
The `For` statement specifies the counter variable `x` and its start and end
values. The `Next` statement increments the counter variable by 1.

    
    
     Sub DoMyProc50Times()
       Dim x
       For x = 1 To 50
         MyProc
       Next
     End Sub
    

Using the `Step` keyword, you can increase or decrease the counter variable by
the value you specify. In the following example, the counter variable `j` is
incremented by 2 each time the loop repeats. When the loop is finished, the
total is the sum of 2, 4, 6, 8, and 10.

    
    
     Sub TwosTotal()
       Dim j, total
       For j = 2 To 10 Step 2
         total = total + j
       Next
       MsgBox "The total is " & total
     End Sub
    

To decrease the counter variable, use a negative `Step` value. You must
specify an end value that is less than the start value. In the following
example, the counter variable `myNum` is decreased by 2 each time the loop
repeats. When the loop is finished, total is the sum of 16, 14, 12, 10, 8, 6,
4, and 2.

    
    
     Sub NewTotal()
       Dim myNum, total
       For myNum = 16 To 2 Step -2
         total = total + myNum
       Next
       MsgBox "The total is " & total
     End Sub
    

You can exit any `For...Next` statement before the counter reaches its end
value by using the `Exit For` statement. Because you usually want to exit only
in certain situations, such as when an error occurs, you should use the `Exit
For` statement in the _True_ statement block of an `If...Then...Else`
statement. If the condition is _False_ , the loop runs as usual.

## For Each…Next

A `For Each...Next` loop is similar to a `For...Next` loop. Instead of
repeating the statements a specified number of times, a `For Each...Next` loop
repeats a group of statements for each item in a collection of objects or for
each element of an array. This is especially helpful if you don’t know how
many elements are in a collection.

In the following RhinoScript code example, the contents of a document’s layer
table is printed to the command line.

    
    
     Sub PrintLayerNames
       Dim l, n   'Create variables
       n = Rhino.LayerNames
       For Each l In n
         Rhino.Print l
       Next
     End Sub
    

## Continue

Both C++ and C# have a continue statement that, when used with a For loop,
skips the remaining statements of that iteration and moves on to next
iteration. There is no continue or continue-like statement in VBScript. But
using a `Do While` loop inside of a `For Each` statement, you can achieve the
same functionality. For example:

    
    
    For i = 0 To 10
      Do
        If i = 4 Then Exit Do
        Rhino.Print i
      Loop While False
    Next
    

Here is another example…

    
    
    Sub TestContinue
    
      Dim arrTests, arrTest
    
      arrTests = Array( _
            Array(1) _
          , Array(1,2,3 ) _
          , Array(1,2) _
          , Array(1) _
          , Array(1,2,3) _
          )
    
      For Each arrTest In arrTests
         Call Rhino.Print("Process: {" & Join(arrTest, ", ") & "}")
         Do While True ' Continue trick
           Call Rhino.Print(" Process: " & arrTest(0))
           If 0 = UBound(arrTest) Then Exit Do ' Continue
           Call Rhino.Print(" Process: " & arrTest(1))
           If 1 = UBound(arrTest) Then Exit Do ' Continue
           Call Rhino.Print(" Process: " & arrTest(2))
           Exit Do
         Loop
      Next
    
    End Sub
    

## Related Topics

  * [What are VBScript and RhinoScript?](https://developer.rhino3d.com/guides/rhinoscript/what-are-vbscript-rhinoscript/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
looping/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
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

