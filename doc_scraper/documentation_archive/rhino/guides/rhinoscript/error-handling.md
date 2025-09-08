---
url: https://developer.rhino3d.com/guides/rhinoscript/error-handling/
scraped_at: 2025-09-08T15:42:44.396850
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

[Error Handling](https://developer.rhino3d.com/guides/rhinoscript/error-
handling/)

  * Overview
  * Discussion

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Error Handling

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

There are two statements that affect error handling in VBScript:

    
    
    On Error Resume Next
    On Error Goto 0
    

The meaning of the first statement is this: if you get an error, ignore it and
resume execution on the next statement. As we’ll see, there are some
subtleties.

The second statement simply turns off “Resume Next” mode if it is on. The odd
syntax is because Visual Basic has an error handling mode which VBScript does
not – VB can branch to a labeled or numbered statement.

## Discussion

The subtlety in the “Resume Next” mode is best illustrated with an example…

    
    
    Const InvalidCall = 5
    Rhino.Print "Global code start"
    Blah1
    Rhino.Print "Global code end"
    
    Sub Blah1()
      On Error Resume Next
      Rhino.Print "Blah1 Start"
      Blah2
      Rhino.Print "Blah1 End"
    End Sub
    Sub Blah2()
      Rhino.Print "Blah2 Start"       
      Err.Raise InvalidCall
      Rhino.Print "Blah2 End"
    End Sub
    

This prints out:

    
    
    Global code start
    Blah1 Start
    Blah2 Start
    Blah1 End
    Global code end
    

When the error ocurred, Blah1 had already turned “Resume Next” mode on. The
next statement after the error raise is Print “Blah2 End” but that statement
was never executed. This is because the error mode is on a per-procedure
basis, not a global basis.

Also, remember that the `Next` in “Resume Next” mode is the next statement.
Consider these two scripts:

    
    
    On Error Resume Next
    Temp = CInt(Foo.Bar(123))
    Blah Temp
    Rhino.Print "Done"
    
    On Error Resume Next
    Blah CInt(Foo.Bar(123))
    Rhino.Print "Done"
    

They do not have the same semantics. If `Foo.Bar` raises an error, then the
first script passes `Empty` to `Blah`. The second one never calls `Blah` at
all if an error is raised, because it resumes to the next statement.

You can get into similar trouble with other constructs. For example, these do
have the same semantics:

    
    
    On Error Resume Next
    If Blah Then
      Rhino.Print "Hello"
    End If
    Rhino.Print "Goodbye"
    
    On Error Resume Next
    If Blah Then Rhino.Print "Hello"
    Rhino.Print "Goodbye"
    

If `Blah` raises an error then it resumes on the `Rhino.Print "Hello"` in
either case.

You can also get into trouble with loops:

    
    
    On Error Resume Next
    
    For index = 1 to Blah
      Rhino.Print TypeName(index)
    Next
    Rhino.Print "Goodbye"
    

If Blah raises an error, this resumes into the loop, not after the loop. This
prints out:

    
    
    Empty
    Goodbye
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/error-
handling/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/error-
handling/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

