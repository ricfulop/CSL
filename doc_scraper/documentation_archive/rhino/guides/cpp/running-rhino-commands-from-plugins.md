---
url: https://developer.rhino3d.com/guides/cpp/running-rhino-commands-from-plugins/
scraped_at: 2025-09-08T15:39:18.502274
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

[Running Rhino Commands from
Plugins](https://developer.rhino3d.com/guides/cpp/running-rhino-commands-from-
plugins/)

  * Overview
  * How To
  * Warning
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Running Rhino Commands from Plugins

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

One of the most common questions asked by new plugin developers is how to run,
or script, existing Rhino commands from a plugin command. Rhino doesn’t allow
plugin commands to run other commands except under very special circumstances.

Here’s the issue: If you have a command that is modifying the run-time
database, and you run another command, problems can happen.

To work around this, the Rhino C/C++ SDK provides a special kind of command
called a script command. You can create a script command as follows…

## How To

Derive your command class from CRhinoScriptCommand instead of CRhinoCommand.
In other words, instead of defining your command class like this:

    
    
    class CCommandTest : public CRhinoCommand
    

Define your command class like this:

    
    
    class CCommandTest : public CRhinoScriptCommand
    

Then, from within your command class’s `RunCommand()` member, you can call
`CRhinoApp::RunScript()` to script the running of a Rhino command. For
example:

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      RhinoApp().RunScript( L"_-Line 0,0,0 10,10,10", 0 );
      return CRhinoCommand::success;
    }
    

## Warning

This kind of command can be very dangerous. Please be sure you understand the
following:

  1. If you are not very familiar with how C++ references work, you should only call `CRhinoApp::RunScript()` from within a `CRhinoScriptCommand` derived command.
  2. If you are very familiar with C++ references, then please observe the following rules: 
     1. If you get a reference or pointer to any part of the Rhino run-time database, this reference or pointer will not be valid after you call `CRhinoApp::RunScript()`.
     2. If you get a reference or a pointer, then call `CRhinoApp::RunScript()`, and then use the reference, Rhino will probably crash.
     3. All pointers and references used by the command should be scoped such that they are only valid for the time between calls to `CRhinoApp::RunScript()`.

This is because `CRhinoApp::RunScript()` can change the dynamic arrays in the
run-time database. The result is that all pointers and references become
invalid. Be sure to scope your variables between `CRhinoApp::RunScript()`
calls.

**NOTE** : In a normal command, when the user enters a command beginning with
a !, the command exits. There is no documented way to get this behavior from
within a script command.

## Sample

Here’s good scoping practice when your command is a script command.

    
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      {
        section A
        ... do some stuff ...
      }
      RhinoApp().RunScript(...);
      {
        section B
        ... do some stuff ...
      }
      RhinoApp().RunScript(...);
      {
        section C
        ... do some stuff ...
      }
      RhinoApp().RunScript(...);
      {
        section D
        ... do some stuff ...
      }
      RhinoApp().RunScript(...);
      {
        section E
        ... do some stuff ...
      }
      return CRhinoCommand::success;
    }
    

Never allow references and pointers from one section to be used in another
section.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/running-
rhino-commands-from-plugins/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/running-
rhino-commands-from-plugins/index.md) [
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

