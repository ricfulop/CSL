---
url: https://developer.rhino3d.com/guides/rhinoscript/fibonacci-numbers/
scraped_at: 2025-09-08T15:42:45.394584
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

[Fibonacci
Numbers](https://developer.rhino3d.com/guides/rhinoscript/fibonacci-numbers/)

  * Overview
  * Recursion
  * Dynamic Iteration
  * Space Complexity Iteration
  * Binet’s Formula
  * Testing
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Fibonacci Numbers

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

By definition, [Fibonacci
numbers](http://en.wikipedia.org/wiki/Fibonacci_number) are a series of
numbers where the first two Fibonacci numbers are 0 and 1, and each remaining
number is the sum of the previous two.

The formula for calculating Fibonacci numbers is: $$F(n) = F(n-1) + F(n-2)$$

with seed values: $$F(0) = 0$$ and $$F(1) = 1$$

There are a number of methods that one can use to calculate these numbers.
Here are a few…

## Recursion

You can calculate Fibonacci numbers using a recursive function…

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Compute Fibonacci number using recursion
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function Fib_1(n)
      If (n < 2) Then
        Fib_1 = n
      Else
        Fib_1 = Fib_1(n-1) + Fib_1(n-2)
      End If
    End Function
    

…but, it is not always the fastest method.

## Dynamic Iteration

One of the reasons the recursive algorithm can be slow is we keep recomputing
the same subproblems over and over again. In this iterative approach, we solve
each subproblem once and then look up the solution later when we need it
instead of repeatedly recomputing it…

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Compute Fibonacci number using dynamic iteration
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function Fib_2(n)
      Dim f, i
      If (n < 2) Then
        Fib_2 = n
      Else
        ReDim f(n-1)
        f(0) = 1
        f(1) = 1
        For i = 2 To n - 1
          f(i) = f(i-1) + f(i-2)
        Next
        Fib_2 = f(n-1)
      End If
    End Function
    

## Space Complexity Iteration

It turns out that the dynamic iteration can be modified to use a much smaller
amount of space. Each step through the loop uses only the previous two values
of F(n), so instead of storing these values in an array, we can simply use two
variables. This requires some swapping around of values so that everything
stays in the appropriate places.

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Compute Fibonacci number using space complexity iteration
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function Fib_3(n)
      Dim a, b, c, i
      If (n < 2) Then
        Fib_3 = n
      Else  
        a = 1
        b = 1
        For i = 2 To n -1
          c = a + b
          a = b
          b = c
        Next           
        Fib_3 = b
      End If
    End Function
    

## Binet’s Formula

Binet’s Formula for calculating the nth Fibonacci number is fast because it
uses neither recursion nor iteration…

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Compute Fibonacci number using Binet's formula
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Function Fib_4(n)
       Fib_4 = Round(((Sqr(5) + 1) / 2) ^ n / Sqr(5))
    End Function
    

## Testing

You can use the following test code to benchmark the above functions:

    
    
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    ' Tests the Fibonacci functions
    '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Sub TestFibonacci
    
      Dim s, a, n, i, st, et
    
      a = Array("Recursion", "Dynamic", "Space", "Binet")
      s = Rhino.GetString("Fibonacci algorithm to use",,a)
      If IsNull(s) Then Exit Sub
    
      n = Rhino.GetInteger("Number of iterations", 20, 1, 100)
      If IsNull(n) Then Exit Sub
    
      Select Case s
        ' Iterative
        Case "Recursion"
          st = Timer
          For i = 0 To n - 1
            Rhino.Print Fib_1(i)
          Next
          et = Timer
        ' Recursive
        Case "Dynamic"
          st = Timer
          For i = 0 To n - 1
            Rhino.Print Fib_2(i)
          Next
          et = Timer
        ' Space
        Case "Space"
          st = Timer
          For i = 0 To n - 1
            Rhino.Print Fib_3(i)
          Next
          et = Timer
        'Binet  
        Case Else
          st = Timer
          For i = 0 To n - 1
            Rhino.Print Fib_4(i)
          Next
          et = Timer
      End Select
    
      Call Rhino.Print(s & " calculation completed in " & FormatNumber(et-st,3) & " seconds.")
    
    End Sub
    

## Related Topics

  * [Fibonacci Numbers on Wikipedia](http://en.wikipedia.org/wiki/Fibonacci_number)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/fibonacci-
numbers/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/fibonacci-
numbers/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

