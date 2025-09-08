---
url: https://developer.rhino3d.com/guides/rhinocommon/creating-a-skin/
scraped_at: 2025-09-08T15:36:45.866568
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

[Creating a Skin
(Windows)](https://developer.rhino3d.com/guides/rhinocommon/creating-a-skin/)

  * Overview
  * Create the Skin DLL
  * Skin Class
  * Installation
  * Testing

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Creating a Skin (Windows)

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Tuesday,
April 13, 2021)

## Overview

Rhino allows developers to customize most of Rhino’s interface so that the
application appears to be their own. We call this a custom _Skin_. With a
custom Skin, you can change the application icon, splash screen, the
application name etc.

Creating a custom Skin for Rhino involves creating a custom skin assembly:

_skin name.rhs_ This is a regular .NET Assembly (_.DLL_) that implements the
skin’s icon, splash screen, application name, etc. In this guide, we will
refer this to the Skin DLL. See a full list of methods and properties on the
[Skin class
documentation](https://developer.rhino3d.com/api/RhinoCommon/html/T_Rhino_Runtime_Skin.htm).

## Create the Skin DLL

To create the Skin DLL:

  1. Launch _Visual Studio_ and add a new Class Library project to your solution.
  2. In the new Class Library project, add a reference to _RhinoCommon.dll_ , which is found in Rhino’s _System_ folder. Note: make sure, after adding the reference, to set the properties of the reference to _Copy Local = False_.
  3. Create a new class that inherits from `Rhino.Runtime.Skin`.
  4. Add a post build event to the project to rename the assembly from _.dll_ to _.rhs_ :

    
    
    Copy "$(TargetPath)" "$(TargetDir)$(ProjectName).rhs"
    Erase "$(TargetPath)"
    

## Skin Class

The skin class can override basic properties, like the `ApplicationName`:

C# VB.NET

    
    
    namespace MySkin
    {
      public class MyHippoSkin : Rhino.Runtime.Skin
      {
        protected override string ApplicationName
        {
          get
          {
            return "Hippopotamus";
          }
        }
      }
      // You can override more methods and properties here
    }
    
    
    
    Namespace MySkin
        Public Class MyHippoSkin
            Inherits Rhino.Runtime.Skin
            Protected Overrides ReadOnly Property ApplicationName() As String
                Get
                    Return "Hippopotamus"
                End Get
            End Property
        End Class
        ' You can override more methods and properties here
    End Namespace
    

## Installation

#### WARNING

Modifying the registry incorrectly can have negative consequences on your
system's stability and even damage the system.

To install your custom Skin, use _REGEDIT.EXE_ to add a scheme key to your
registry with a path to your Skin DLL. For example:

**Item** |  |  | **Value**  
---|---|---|---  
Subkey |  |  | HKEY_LOCAL_MACHINE\SOFTWARE\McNeel\Rhinoceros\MajorVersion.0\Scheme: MySkin  
Entry name |  |  | SkinDLLPath  
Type |  |  | REG_SZ  
Data value |  |  | C:\Src\MySkin\Bin\Release\MySkin.rhs  
  
Where `MajorVersion` is the major version of Rhino (e.g. 6, 7, 8).

## Testing

You can now test your custom Skin by creating shortcut to your Rhino
executable with `/scheme="<scheme name from the previous step>"` as command
line argument. For example:

_C:\Program Files\Rhino 8\System\Rhino.exe" /scheme=MySkin_

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/creating-
a-skin/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/creating-
a-skin/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

