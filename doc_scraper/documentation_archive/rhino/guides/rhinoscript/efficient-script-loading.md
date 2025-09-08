---
url: https://developer.rhino3d.com/guides/rhinoscript/efficient-script-loading/
scraped_at: 2025-09-08T15:42:43.265326
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

[Efficient Script
Loading](https://developer.rhino3d.com/guides/rhinoscript/efficient-script-
loading/)

  * LoadScript and RunScript
  * Considerations
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Efficient Script Loading

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## LoadScript and RunScript

When running a script from a toolbar button, is it better to use the
_LoadScript_ command or _RunScript_ command? Which is better for Rhino,
resource wise?

The **LoadScript** command:

  1. Opens the script file, reads the contents of the file into a buffer, and then closes the file.
  2. Loads the buffer, read in from the script file, it into the scripting engine. The script engine, then, attempts to parse the script.
  3. If the script was parsed successfully, it is run, or executed.

The **RunScript** command:

  1. Runs the script, skipping steps 1. and 2. listed above.

## Considerations

Using _LoadScript_ to load the same script file over and over and over again
is somewhat inefficient and certainly unnecessary, as you are simply replacing
the same script, over and over again, that is already resident in the script
engine. The only time you need reload a script is if the script has changed,
or if the script engine was reset.

One technique you can use to be more efficient, when loading scripts, is to
have them load at startup. You can specify the scripts to load at startup by
selecting **Tool** > **Option** > **RhinoScript**. Then, you can just use the
_RunScript_ to execute your pre-loaded scripts.

Another technique you can use it to load your scripts on demand. For example,
say you have a _Hello.rvb_ script file with a single function defined as such:

    
    
    Sub Hello
      Call MsgBox("Hello Rhino!")
    End Sub
    

From a toolbar button, you could use the following macro to load it on demand
and then run it:

    
    
    _-NoEcho _-RunScript (
    If Not Rhino.IsProcedure("Hello") Then
      Call Rhino.Command("_-LoadScript Hello.rvb", 0)
    End If
    Call Hello
    

The code above checks for the existence of a user-defined procedure (e.g.
subroutine or function) named `"Hello"`. If the procedure is not found, then
script file, were the procedure is stored, is loaded by running the
_LoadScript_ command. Finally, the specified procedure is called.

To ensure this technique works, make sure to included the path to Hello.rvb is
included in Rhino’s file search path by selecting **Tools** > **Options** >
**Files**.

## Related Topics

  * [Script Demand Loading](https://developer.rhino3d.com/guides/rhinoscript/script-demand-load/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/efficient-
script-loading/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/efficient-
script-loading/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

