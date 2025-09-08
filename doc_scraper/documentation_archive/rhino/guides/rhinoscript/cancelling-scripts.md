---
url: https://developer.rhino3d.com/guides/rhinoscript/cancelling-scripts/
scraped_at: 2025-09-08T15:42:35.347943
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

[Cancelling
Scripts](https://developer.rhino3d.com/guides/rhinoscript/cancelling-scripts/)

  * Overview
  * Sleep
  * OnCancelScript

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Cancelling Scripts

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

When running a RhinoScript, it often occurs that a user wants to interrupt a
running RhinoScript by pressing `ESC`. This most frequently happens when
running a script with a tight loop or a recursive function. In order to cancel
the script, we want to allow the user to press `ESC`, rather than having to
stop Rhino using Task Manager and restart everything. There are two topics to
cover: Sleep and OnCancelScript.

## Sleep

If you have a tight loop that does not call back into Rhino, then it is
possible for `ESC` key processing to be either very slow or not happen at all.
This is because the tight loop does not allow Rhino to process the messages,
such as keystrokes, sent to it by Windows.

To work around this situation, you will want to call back into Rhino inside of
your tight loop. Using RhinoScript’s **Sleep** function is a good way to do
this without slowing down your code…

    
    
    Sub TightLoopEscapeTest
       For i = 0 To 100000
         '
         ' Do tight loop processing here...
         '
         ' Allow Rhino to "pump" it's message queue
         Call Rhino.Sleep(0)
       Next
     End Sub
    

If your loop is relatively fast, you may want to postpone the Sleep call or
else it will slow down your script significantly…

    
    
    Sub TightLoopEscapeTest
      For i = 0 To 100000
        '
        ' Do tight loop processing here...
        '
        ' Allow Rhino to "pump" it's message queue
        If ((i Mod 25) = 0) Then Call Rhino.Sleep(0)
      Next
    End Sub
    

…which will call the Sleep method only once every 25 iterations.

## OnCancelScript

The default behavior when cancelling a script is to halt the script’s
execution and print a “Script cancelled” message to Rhino’s command line.
There are often times when you might want to know when your script is
cancelled. For example, lets say you have a script that does the following
steps in this order:

  1. Modifies some Rhino parameters…
  2. Performs an operation and…
  3. Resets the modified parameters.

If your script is cancelled in operation (2), then Rhino can be left in a
state unfamiliar to the user.

It is possible for your script to be notified when it has been cancelled. This
is done through a special, user-defined subroutine named `OnCancelScript`.

When a script is running and the `ESC` key is pressed, RhinoScript searches
for loaded, user-defined subroutine named `OnCancelScript`. If this subroutine
is detected, RhinoScript will automatically run this procedure instead of just
printing the “Script cancelled” message.

In the above script scenario, the user-defined `OnCancelScript` subroutine
could reset the parameters (3) that were modified when the script started (1).

The following is a simple example that demonstrates the `OnCancelScript`
procedure…

    
    
    Sub TightLoopEscapeTest
    
      For i = 0 to 100000
    
        Call Rhino.Print(i)
    
        Call Rhino.Sleep(0)
    
      Next
    
    End Sub
    
    ' User-defined cancel script handler
    
    Sub OnCancelScript
    
      ' Do script cancelling operations here...
    
      Call MsgBox("Script Cancelled!", vbOkOnly + vbExclamation, "RhinoScript")
    
    End Sub
    

**NOTE** : your user-defined `OnCancelScript` subroutine must not have any
arguments. If you define your `OnCancelScript` subroutine as one that requires
one or more arguments, then RhinoScript will not execute it when `ESC` is
pressed.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/cancelling-
scripts/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/cancelling-
scripts/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

