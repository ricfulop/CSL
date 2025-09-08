---
url: https://developer.rhino3d.com/guides/rhinoscript/vbscript-statements/
scraped_at: 2025-09-08T15:41:54.046489
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
Statements](https://developer.rhino3d.com/guides/rhinoscript/vbscript-
statements/)

  * Overview
  * Details

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

VBScript Statements

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Many scripting and programming languages, such as JScript, C#, and C++, make
no attempt to match the code that is run with the actual physical lines typed
into the text editor. This is because they not recognize the end of a line of
code until it sees the termination character (in these cases, the semicolon).
Thus, the actual physical lines of type taken up by the code are irrelevant.

By contrast, VBScript uses the carriage return instead of a special line
termination character. To end a statement in VBScript, you do not have to type
in a semicolon or other special character; you simply press `Enter`. For
example, this code will generate a syntax error:

    
    
    Set
    objFSO
    =
    CreateObject("Scripting.FileSystemObject")
    

This will not:

    
    
    	Set objFSO = CreateObject("Scripting.FileSystemObject")
    

## Details

In general, the lack of a required statement termination character simplifies
script writing in VBScript. There is, however, one complication: To enhance
readability, it is recommended that you limit the length of any single line of
code to 80 characters. What happens, then, if you have a line of code that
contains 100 characters?

Although it might seem like the obvious solution, you cannot split a statement
into multiple lines simply by entering a carriage return. For example, the
following code snippet returns a run-time error in VBScript because a
statement was split by using `Enter`.

    
    
      strMessageToDisplay = strUserFirstName & " " & strUserMiddleInitial & " " & strUserLastName
      Rhino.Print strMessageToDisplay
    

You cannot split a statement into multiple lines in VBScript by pressing
`Enter` because VBScript sees a carriage return as marking the end of a
statement. In the preceding example, VBScript interprets the first line as the
first statement in the script. Next, it interprets the second line as the
second statement in the script, and the error occurs because strUserLastName
is not a valid VBScript statement.

Instead, use the underscore (`_`) to indicate that a statement is continued on
the next line. In the revised version of the script, a blank space and an
underscore indicate that the statement that was started on line 1 is continued
on line 2. To make it more apparent that line 2 is a continuation of line 1,
line 2 is also indented four spaces. (This was done for the sake of
readability, but you do not have to indent continued lines.)

    
    
      strMessageToDisplay = strUserFirstName & " " & strUserMiddleInitial & " " _ & strUserLastName
      Rhino.Print strMessageToDisplay
    

Line continuation is more complex when you try to split a statement inside a
set of quotation marks. For example, suppose you split this statement using a
blank space and an underscore:

    
    
      strMessage = "If you ask me anything I don't know, _ I'm not going to answer."
      Rhino.Print strMessage
    

If you run this script, you will encounter a run-time error because the line
continuation character has been placed inside a set of quotation marks (and is
therefore considered part of the string). To split this statement:

  1. Close the first line with quotation marks, and then insert the blank space and the underscore.
  2. Use an ampersand at the beginning of the second line. This indicates that line two is a continuation of the interrupted string in line 1.
  3. Add quotation marks before continuing the statement.

These quotation marks indicate that this line should be included as part of
the quoted string started on the previous line. Without the quotation marks,
the script engine would interpret the continued line as a VBScript statement.
Because this is not a valid VBScript statement, an error would occur.

The revised statement looks like this:

    
    
      strMessage = "If you ask me anything I don't know, " _ & " I'm not going to answer."
      Rhino.Print strMessage
    

When splitting statements in this fashion, be careful to insert spaces in the
proper location.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/vbscript-
statements/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/vbscript-
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

