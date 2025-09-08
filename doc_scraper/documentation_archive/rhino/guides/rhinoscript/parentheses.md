---
url: https://developer.rhino3d.com/guides/rhinoscript/parentheses/
scraped_at: 2025-09-08T15:42:26.346437
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

[Parentheses
Error](https://developer.rhino3d.com/guides/rhinoscript/parentheses/)

  * Problem
  * Solution
  * Examples

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Parentheses Error

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
July 27, 2020)

## Problem

Every now and then, you may get the error message “Cannot use parentheses when
calling a Sub” when calling a function or method. This does not happen all the
time. For example, the following code appears to work:

    
    
    Result = MyFunc(MyArg)
    MySub(MyArg)
    

…but this code does not work:

    
    
    Result = MyOtherFunc(MyArg1, MyArg2)
    MyOtherSub(MyArg1, MyArg2)
    

## Solution

In VBScript, parentheses mean several different things:

Evaluate a subexpression before the rest of the expression. For example:

    
    
    Average = (First + Last) / 2
    

or…

Dereference the index of an array. For example:

    
    
    Item = MyArray(Index)
    

or…

Call a function or subroutine. For example:

    
    
    Limit = UBound(MyArray)
    

or…

Pass an argument which would normally be `ByRef` as `ByVal`. For example…

    
    
    'Arg1 is passed ByRef, Arg2 is passed ByVal.
    Result = MyFunction(Arg1, (Arg2))
    

And, there are additional rules that apply when calling a function or
subroutine…

An argument list for a function call with an assignment to the returned value
must be surrounded by parentheses. For example:

    
    
    Result = MyFunc(MyArg)
    

An argument list for a subroutine call, or a function call with no assignment,
that uses the `Call` keyword must be surrounded by parentheses. For example:

    
    
    Call MySub(MyArg)
    

If the above two rules do not apply, then the list must not be surrounded by
parentheses.

Finally, there is the `ByRef` rule: arguments are passed `ByRef` when
possible. But, if there are extra parentheses around a variable, then the
variable is passed `ByVal`, not `ByRef`.

From these rules, it should be clear why the statement `MySub(MyArg)` is legal
but `MyOtherSub(MyArg1, MyArg2)` is not. The first case appears to be a
subroutine call with parentheses around the argument list, but that would
violate the rules. Then why does this work? In fact, it is a subroutine call
with no parentheses around the argument list, but parentheses around the first
argument. This passes the argument by value. The second case is a clear
violation of rules, and there is no way to make it legal, so an error is
given.

## Examples

Here are some examples to what is legal and what is not in VBScript. Suppose
`X` and `Y` are variables, `Func1` is a one argument procedure, and `Func2` is
a two argument procedure.

To pass `X` `ByRef` and `Y` `ByRef`:

    
    
    Func1 X
    Call Func1(X)
    Z = Func1(X)
    Func2 X, Y
    Call Func2(X, Y)
    Z = Func2(X, Y)
    

To pass `X` `ByVal` and `Y` `ByRef`:

    
    
    Func1(X)
    Call Func1((X))
    Z = Func1((X))
    Func2 (X), Y
    Func2 ((X)), Y
    Call Func2((X), Y)
    Z = Func2((X), Y)
    

The following will give syntax errors:

    
    
    Call Func1 X
    Z = Func1 X
    Func2(X, Y)
    Call Func2 X, Y
    Z = Func2 X, Y
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/parentheses/index.md)
[
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/parentheses/index.md)
[ Admin](https://developer.rhino3d.com/admin)

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

