---
url: https://developer.rhino3d.com/guides/rhinocommon/run-rhino-command-from-plugin/
scraped_at: 2025-09-08T15:36:42.110151
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

[Run a Rhino command from a
Plugin](https://developer.rhino3d.com/guides/rhinocommon/run-rhino-command-
from-plugin/)

  * The Problem
  * The Solution
  * Warnings

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Run a Rhino command from a Plugin

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
August 2, 2021)

## The Problem

One of the most common questions asked by new plugin developers is how to run,
or script, existing Rhino commands from a plugin command. Rhino doesn’t allow
plugin commands to run other commands except under very special circumstances.

Here’s the problem: If you have a command that is modifying the Rhino
document, and you run another command, problems can happen.

To work around this, the RhinoCommon provides a special kind of command called
a script command. You can create a script command as follows…

## The Solution

When defining your command class, make sure to add the `ScriptRunner` command
style attribute. In other words, instead of defining your command classes like
this:

C# VB.NET

    
    
    public class TestCommand : Rhino.Commands.Command
    
    
    
    Public Class TestCommand
      Inherits Rhino.Commands.Command
    

Define your command classes like this:

C# VB.NET

    
    
    [Rhino.Commands.CommandStyle(Rhino.Commands.Style.ScriptRunner)]
    public class TestCommand : Rhino.Commands.Command
    
    
    
    <Rhino.Commands.CommandStyle(Rhino.Commands.Style.ScriptRunner)>
    Public Class TestCommand
      Inherits Rhino.Commands.Command
    

Then, from within your command class’s `RunCommand()` method, you can call
`RhinoApp.RunScript()` to script the running of a Rhino command. For example…

C# VB.NET

    
    
    protected override Rhino.Commands.Result RunCommand(Rhino.RhinoDoc doc, Rhino.Commands.RunMode mode)
    {
      Rhino.RhinoApp.RunScript("_-Line 0,0,0 10,10,10", false);
      return Rhino.Commands.Result.Success;
    }
    
    
    
    Protected Overrides Function RunCommand(ByVal doc As Rhino.RhinoDoc, ByVal mode As Rhino.Commands.RunMode) As Rhino.Commands.Result
      Rhino.RhinoApp.RunScript("_-Line 0,0,0 10,10,10", False)
      Return Rhino.Commands.Result.Success
    End Function
    

## Warnings

This kind of command can be very dangerous. Please be sure you understand the
following:

  1. If you are not very familiar with how references work, you should only call `Rhino.RhinoApp.RunScript()` from within a `RhinoScriptCommand` derived command.
  2. If you are very familiar with references, then please observe the following rules: 
     1. If you get a reference or pointer to any part of the Rhino run-time database, this reference or pointer will not be valid after you call `Rhino.RhinoApp.RunScript()`.
     2. If you get a reference or a pointer, then call `Rhino.RhinoApp.RunScript()`, and then use the reference, Rhino will probably crash.
     3. All pointers and references used by the command should be scoped such that they are only valid for the time between calls to `Rhino.RhinoApp.RunScript()`.

This is because `Rhino.RhinoApp.RunScript()` can change the dynamic arrays in
the run-time database. The result is that all pointers and references become
invalid. Be sure to scope your variables between `Rhino.RhinoApp.RunScript()`
calls.

Never allow references and pointers from one section to be used in another
section.

In a normal command, when the user enters a command beginning with a !, the
command exits. There is no documented way to get this behavior from within a
script command.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/run-
rhino-command-from-plugin/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/run-
rhino-command-from-plugin/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

