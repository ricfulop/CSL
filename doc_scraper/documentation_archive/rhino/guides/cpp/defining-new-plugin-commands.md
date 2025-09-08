---
url: https://developer.rhino3d.com/guides/cpp/defining-new-plugin-commands/
scraped_at: 2025-09-08T15:38:31.217495
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

[Defining New Plugin
Commands](https://developer.rhino3d.com/guides/cpp/defining-new-plugin-
commands/)

  * Overview
  * Rhino 8
  * Rhino 7
  * Sample

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Defining New Plugin Commands

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Monday,
October 7, 2024)

## Overview

Rhino plugins can contain any number of commands. Commands are created by
deriving a new class from `CRhinoCommand`. See _rhinoSdkCommand.h_ for details
on the `CRhinoCommand` class.

Command classes must return a unique _GUID_. If you try to use a _GUID_ that
is already in use, then your command will not work. Use the _GUIDGEN.EXE_
utility, that comes with Visual Studio, to create unique _GUIDs_.

Command classes must return a unique command name. If you try to use a command
name that is already in use, then your command will not work.

Only ONE instance of a command class can be created. This is why you should
put the definition of your command classes in _.cpp_ files.

## Rhino 8

The **[Rhino Visual Studio
Extension](https://github.com/mcneel/RhinoVisualStudioExtensions/releases)** ,
for the Rhino 8 C/C++ SDK, includes a template that lets you quickly add new
commands to your plugin project.

To add a new Rhino command to your plugin project, right-click on the _Source
Files_ folder, in _Visual Studio’s Solution Explorer_ , and click _Add > New
Item…_. From the _Add New Item_ dialog, select _Empty Command for Rhino 3D
(C++)_ , specify the name of the command, and click _Add_.

![Add New Item](https://developer.rhino3d.com/images/defining-new-plugin-
commands-cpp.png)

## Rhino 7

The _Rhino Command Generator_ wizard, included with the Rhino 7 C/C++ SDK, is
a standalone application that will generate new skeleton
`CRhinoCommand`-derived class. The generated source code is copied to the
Windows clipboard so you can easily paste it into your source files.

To use this tool in Visual Studio:

  1. Launch Visual Studio.
  2. Navigate to _Tools_ > _External Tools…_.
  3. Use the _Add_ button to add the _RhinoCommandGenerator.exe_ file to the list. The file can be found in the following location: _C:\Program Files\Rhino 7.0 SDK\Wizards\Command_

![Rhino Command Generator](https://developer.rhino3d.com/images/your-first-
plugin-windows-cpp-08.png)

Once the tool is installed, you can create a new command by selecting _Tools_
> _Rhino Command_. If you add the command declaration to a new _.cpp_ file, be
sure to `#include "stdafx.h"` at the top.

## Sample

The following sample code demonstrates a simple command class that essentially
does nothing:

    
    
    // Do NOT put the definition of class CCommandTest in a header
    // file. There is only ONE instance of a CCommandTest class
    // and that instance is the static theTestCommand that appears
    // immediately below the class definition.
    
    class CCommandTest : public CRhinoCommand
    {
    public:
      // The one and only instance of CCommandTest is created below.
      // No copy constructor or operator= is required.
      // Values of member variables persist for the duration of the application.
    
      // CCommandTest::CCommandTest()
      // is called exactly once when static theTestCommand is created.
      CCommandTest() = default;
    
      // CCommandTest::~CCommandTest()
      // is called exactly once when static theTestCommand is destroyed.
      // The destructor should not make any calls to the Rhino SDK. 
      // If your command has persistent settings, then override 
      // CRhinoCommand::SaveProfile and CRhinoCommand::LoadProfile.
      ~CCommandTest() = default;
    
      // Returns a unique UUID for this command.
      // If you try to use an id that is already being used, then
      // your command will not work. Use GUIDGEN.EXE to make unique UUID.
      UUID CommandUUID() override
      {
        // {F502C783-C0CE-4118-8869-EFB0CB34CCCB}
        static const GUID TestCommand_UUID =
        { 0xF502C783, 0xC0CE, 0x4118, { 0x88, 0x69, 0xEF, 0xB0, 0xCB, 0x34, 0xCC, 0xCB } };
        return TestCommand_UUID;
      }
    
      // Returns the English command name.
      // If you want to provide a localized command name, then override 
      // CRhinoCommand::LocalCommandName.
      const wchar_t* EnglishCommandName() override { return L"Test"; }
    
      // Rhino calls RunCommand to run the command.
      CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
    };
    
    // The one and only CCommandTest object
    // Do NOT create any other instance of a CCommandTest class.
    static class CCommandTest theTestCommand;
    
    CRhinoCommand::result CCommandTest::RunCommand(const CRhinoCommandContext& context)
    {
      // CCommandTest::RunCommand() is called when the user
      // runs the "Test".
    
      // TODO: Add command code here.
    
      // Rhino command that display a dialog box interface should also support
      // a command-line, or scriptable interface.
    
      ON_wString str;
      str.Format(L"The \"%s\" command is under construction.\n", EnglishCommandName());
      if (context.IsInteractive())
        RhinoMessageBox(str, TestPlugIn().PlugInName(), MB_OK);
      else
        RhinoApp().Print(str);
    
      // TODO: Return one of the following values:
      //   CRhinoCommand::success:  The command worked.
      //   CRhinoCommand::failure:  The command failed because of invalid input, inability
      //                            to compute the desired result, or some other reason.
      //   CRhinoCommand::cancel:   The user interactively canceled the command 
      //                            (by pressing ESCAPE, clicking a CANCEL button, etc.)
      //                            in a Get operation, dialog, time consuming computation, etc.
    
      return CRhinoCommand::success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/defining-
new-plugin-commands/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/defining-
new-plugin-commands/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

