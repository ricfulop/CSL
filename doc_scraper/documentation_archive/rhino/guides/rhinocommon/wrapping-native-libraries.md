---
url: https://developer.rhino3d.com/guides/rhinocommon/wrapping-native-libraries/
scraped_at: 2025-09-08T15:36:48.770041
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

[Wrapping Native
Libraries](https://developer.rhino3d.com/guides/rhinocommon/wrapping-native-
libraries/)

  * Overview
    * Prerequisites
  * SampleLibrary
    * Windows
    * Mac
  * SampleNativeLibrary
    * Windows
    * Mac
  * Next Steps
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Wrapping Native Libraries

by [Dan Rigdon-Bel](https://discourse.mcneel.com/u/dan/) (Last updated:
Friday, September 3, 2021)

## Overview

We present a sample solution that uses Platform Invoke (PInvoke), which allows
.NET code to call functions that are implemented in a C/C++ DLL (Windows) or
dylib (macOS). It is important to understand that the main utility of this
advanced approach is in the ability to call the same C/C++ code on both
platforms from .NET.

First, we will build a simple C/C++ library that adds two numbers together.
After that, we will examine the wrapping .NET code required to call into our
library from a RhinoCommon plugin on both Windows and Mac.

### Prerequisites

This guide does not presume you are a C/C++ or .NET expert, but assumes you
have a functional working knowledge of both. This is an advanced guide; that
said, the intent of this guide is to illustrate basic considerations of
wrapping a C/C++ library and the logistical issues calling it from a
RhinoCommon plugin on both Windows and Mac.

We will be analyzing a sample solution called
_[SampleNativeLibrary](https://github.com/dalefugier/SampleNativeLibrary)_.
Please clone or download this repository. _SampleNativeLibrary_ builds against
the RhinoWIP (on Windows) and Rhino 5 for Mac (on macOS). (On Windows, it is
possible to use Rhino 6, but you will have to change the RhinoCommon
references).

It is presumed you already have _all_ the necessary tools installed and are
ready to go. If you are not there yet, see both [Installing Tools
(Windows)](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-
windows/) and [Installing Tools
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/installing-tools-
mac/). It is also helpful to have read and understood [Your First Plugin
(Windows)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-
windows/) and [Your First Plugin
(Mac)](https://developer.rhino3d.com/guides/rhinocommon/your-first-plugin-
mac/).

#### WARNING

Other methods to create a .NET binding to a C# library exist. A notorious one
is based on the compilation of the C++ library with the C++/CLI compiler. To
keep things compatible with the Apple macOS, and because the IJW (it just
works) technology sometimes does not, we suggest the use of PInvoke.

## SampleLibrary

Let’s begin by taking a look at an absurdly simple C/C++ “library” -
SampleLibrary - that does one thing: add two numbers together. We’ll start on
Windows, but it really doesn’t matter if you start on a macOS, nearly
everything that follows applies on each platform…

### Windows

  1. Open _SampleNativeLibrary.sln_ in _Visual Studio_.

  2. In the Solution Explorer, you will notice there are three projects…two C# (.csproj) projects and one C++ project. Expand the _SampleLibrary_ C++ project… ![SampleNativeLibrary](https://developer.rhino3d.com/images/wrapping-native-libraries-02.png)

  3. The _SampleLibrary_ (.vcxproj) is just a boilerplate C++ project (created using the regular Shared MFC C++ project wizard) that was created by Visual Studio. _There is nothing fancy going on here at all; much of the code is not even relevant to this guide_.

  4. Open the _SampleLibrary.cpp_ file and take a look. Nearly all of the code in this file is auto-generated boilerplate. The only important section to pay attention to is:
         
         SAMPLELIBRARY_C_FUNCTION
          double Add(int a, double b)
          {
            return a + b;
          }  
         

…even if you are not a C/C++ programmer, this C function should be clear to
you. `Add` takes a native `int` and a native `double`, and returns the sum of
the inputs as a native `double`. Take note of the `SAMPLELIBRARY_C_FUNCTION`
decoration above the implementation…we will talk about that in a moment.

  5. In the _Header Files_ filter, find and open the _SampleLibraryInclude.h_ header file. The first thing to note is that there are two well `#defined` sections to this header: one that relates to Windows (`#if defined (_WIN32)`) and one that relates to Mac (`#if defined(__APPLE__)`). The code in these #defines are basically telling the linker to export functions in a specific way. The reason they are different on each platform is that Dynamic Link Libraries (DLLs) are implemented differently in Windows and macOS - each platform has a unique way of telling the linker what to do with the library. How this works is not really important at this juncture, just know that these MACROs tell the linker to export the functions. More importantly…

  6. Take a look at the function declaration at the bottom of the file:
         
         SAMPLELIBRARY_C_FUNCTION
          double Add(int a, double b);
         

…is decorated with the same `SAMPLELIBRARY_C_FUNCTION`.

  7. This is the decoration that tells the linker to make the function available to outside callers. By decorating with this macro, the linker adds information to the DLL that makes these functions public. Without this decoration, these functions would not be available outside the the assembly (.dll or .dylib). By providing this decoration, we are doing the .NET equivalent of making them “public”.

  8. Do a “sanity check” and _Build_ SampleLibrary to make sure that all your tools are working as expected. SampleLibrary should build without errors as the native _SampleLibrary.dll_ in the project _/bin_ folder. Ok, now that we know roughly what is in the native SampleLibrary on Windows, let’s take a look at it on macOS…

### Mac

  1. Launch _Xcode_ and open _SampleLibrary.xcodeproj_. (Unlike Visual Studio on Windows, on macOS, we cannot do all of our development in a single IDE, but we have to build our native C/C++ _SampleLibrary_ using the native Apple Tools - Xcode and xcodebuild).
  2. In the _Project Navigator_ , notice that this project is referencing the _exact same source code_ as its Windows counterpart… ![SampleLibrary on macOS](https://developer.rhino3d.com/images/wrapping-native-libraries-03.png)
  3. Instead of building a .dll, on macOS we are building _libSampleLibrary.dylib_ which - despite the extension - amounts to exactly the same thing as a dll. For all intents and purposes, SampleLibrary does exactly the same thing on macOS that it does on Windows and the source is the same.
  4. _Build_ SampleLibrary using Xcode to make sure that it builds successfully.
  5. _Quit_ Xcode. On macOS, we are actually going to use command line `xcodebuild` from Visual Studio for Mac to build our native library, but we’ll talk about that below.

Now that we have examined the simple native SampleLibrary, let’s turn our
attention to the .NET portion of our wrapping code…

## SampleNativeLibrary

SampleNativeLibrary is the .NET project that calls into the SampleLibrary. On
each platform, we are using the exact same wrapping source code, just using
cloned .csproj projects on each platform.

Let’s take a look at SampleNativeLibrary on Windows using Visual Studio first…

### Windows

  1. If you have not done so already, open the _SampleNativeLibrary.sln_ in _Visual Studio_.

  2. If you have not done so already, build _SampleLibrary_. Verify that _SampleLibrary.dll_ is present in your _/bin_ folder.

  3. Now, let’s turn our attention to the _SampleRhino.Win_ project. Make sure that _SampleRhino.Win_ is set as the Startup Project and expand it so you can see the source files… ![SampleRhino on Windows](https://developer.rhino3d.com/images/wrapping-native-libraries-04.png)

  4. Before we do anything, let’s build and test the plugin. Build _SampleRhino.Win_.

  5. Load the _SampleRhino.rhp_ in Rhino and run the _SampleRhinoCommand_. You will be prompted to enter two numbers. Once you have done that you should see the result in a dialog box… ![SampleRhino plugin test](https://developer.rhino3d.com/images/wrapping-native-libraries-05.png)

  6. The “additional” calculation for this command was all performed in the native C/C++ SampleLibrary.dll. Return to _Visual Studio_. Let’s take a look at how the `Add` function is being called.

  7. Open _SampleRhinoCommand.cs_ and find the `RunCommand` method. After prompting the user to enter two numbers, we see the following code
         
         var result = RhinoMath.UnsetValue;
          try
          {
            result = UnsafeNativeMethods.Add(first, second);
          }
          catch (Exception ex)
          {
            RhinoApp.WriteLine(ex.Message);        
            return Result.Failure;
          }
         

  8. The `Add(first, second)` method is being called on the `UnsafeNativeMethods` class. Open _UnsafeNativeMethods.cs_. Let’s go through this class line-by-line.

  9. The necessary functionality to use PInvoke is contained in the `System.Runtime.InteropServices` namespace, specifically the `DllImport` function.

  10. _UnsafeNativeMethods.cs_ contains the class:
         
         internal static class Import
          {
            public const string lib = "SampleLibrary.dll";
          }
         

…which declares a `lib` string member. On Windows, it is necessary to
explicitly state the name of the native dll being called (on macOS, a
_.dll.config_ file is used to point to a .dylib - see below).

  11. The `UnsafeNativeMethods` class itself contains a single function…
         
         internal static extern double Add(int a, double b);
         

…does this look familiar?

  12. The `Add` function is decorated with an [Attribute](https://msdn.microsoft.com/en-us/library/z0w1kczw.aspx):
         
         [DllImport(Import.lib, CallingConvention = CallingConvention.Cdecl)]
         

…this important bit of metadata tells the runtime to look in the native
library and call the associated function with a specific language (C) calling
convention when the `Add` method is called from .NET. _This is the point at
which the link between the managed .NET code and the unmanaged C/C++ code is
established._

  13. Since we are bridging the world of managed and unmanaged code, _we need to be very careful about the types of variables we are using_. To illustrate this point, let’s change the code and see what happens…

  14. In _UnsafeNativeMethods_ change the function declaration of `Add` to accept `double`s (instead of `int`s) as the first argument…
         
         internal static extern double Add(double a, double b);
         

  15. _Build_ the plugin. No errors or warnings, right? Now run the plugin and test the _SampleRhinoCommand_ with this change. Try adding 2 + 2. What happens? _2 + 2 no longer equals 4_. That’s bad (hopefully, Rhino did not crash). The compiler did not detect the error we introduced. Change the type of argument `a` back to an `int`, rather than a `double` and save the file.

  16. _You must ensure that the function in .NET exactly matches the function declaration in the header file made in the unmanaged code_ (in this case, in _SampleLibraryInclude.h_). Managing these correspondences is challenging with all but the most trivial libraries. In [Using methodgen](https://developer.rhino3d.com/guides/rhinocommon/using-methodgen/), we will discuss a way of generating these function signatures using a utility program we wrote to maintain RhinoCommon. Before we do that, let’s turn our attention to…

### Mac

  1. If you have not done so already, open the _SampleNativeLibrary.sln_ in _Visual Studio for Mac_.

  2. The native _SampleLibrary_ project cannot be built from Visual Studio for Mac. As mentioned above, Visual Studio for Mac is a .NET only IDE; it cannot build C/C++ projects like Visual Studio. (We will work around this limitation in a moment).

  3. First, let’s turn our attention to the _SampleRhino.Mac_ project. Make sure that _SampleRhino.Mac_ is set as the Startup Project and expand it so you can see the source files… ![SampleRhino on Mac](https://developer.rhino3d.com/images/wrapping-native-libraries-06.png)

  4. Just as with _SampleLibrary_ , _SampleRhino_ is exactly the same source on both platform: the platform-specific _.csproj_ files are referencing exactly the same _.cs_ files.

  5. _Build_ , run, and test _SampleRhinoCommand_ in Rhino for Mac. Everything should work as expected. No surprises here…all the code is the same (if you skipped the [Windows section above](https://developer.rhino3d.com/guides/rhinocommon/wrapping-native-libraries/#windows-1), read it now; all of it applies on macOS).

  6. There is one critical difference between how the Windows and macOS wrapping works and it has little to do with code. As we saw above, _UnsafeNativeMethods.cs_ contains the class:
         
         internal static class Import
          {
            public const string lib = "SampleLibrary.dll";
          }
         

…which declares a `lib` string member. On Windows, it was necessary to
explicitly state the name of the native dll being called. On macOS, this works
a little differently. In order to understand what is different, let’s look at
how _SampleLibrary.dll_ gets built on macOS…

  7. In the [SampleLibrary (Mac) section above](https://developer.rhino3d.com/guides/rhinocommon/wrapping-native-libraries/#mac), we built SampleLibrary using Xcode. We mentioned in passing that we could build this using `xcodebuild` command line from Visual Studio for Mac. Let’s take a look.

  8. In the _Solution Explorer_ , _double-click_ the name of the _SampleRhino.Mac_ project to bring up the _Project Options_ dialog. Navigate to the _Build_ > _Custom Commands_ section… ![SampleRhino.Mac Project Options](https://developer.rhino3d.com/images/wrapping-native-libraries-07.png)

  9. There are 5 _Custom Commands_ :

     1. _Before Build_ : This before build steps runs a python script called _build_native.py_ that uses `xcodebuild` to build the _SampleLibrary.xcodeproj_ , which builds _libSampleLibrary.dylib_.

     2. _After Build 1_ : This after build step copies the _SampleLibrary.dll.config_ file from the _/SampleLibrary_ folder to the target folder. _SampleLibrary.dll.config_ creates a mapping between calls to _SampleLibrary.dll_ and _libSampleLibrary.dylib_ …
            
            <configuration>
                <dllmap dll=“SampleLibrary.dll” target="libSampleLibrary.dylib" />
             </configuration>
            

On macOS, both the _.dll.config_ file and the _.dylib_ must be in the same
folder as the calling .NET dll.

     3. _After Build 2_ : This after build step copies _libSampleLibrary.dylib_ to the same folder as the calling .NET dll.

     4. _After Clean 1_ : This after build step deletes the _libSampleLibrary.dylib_ when a clean is performed.

     5. _After Clean 1_ : This after build step deletes the _SampleLibrary.dll.config_ when a clean is performed.

  10. When you _Build_ and run _SampleRhino.Mac_ you can watch the build steps in the _output_ (right) side of the _Errors_ panel. You may notice that _build_native.py_ will only build _libSampleLibrary.dylib_ if it does not find a previous version. You can overwrite this with the `-o --overwrite` command argument if you want to build the native library every time you build the .NET wrapping dll.

## Next Steps

You have seen how a basic C/C++ library can be wrapped and called from .NET in
a Rhino Plugin. You have also seen what can go wrong when a native method’s
export declaration is out-of-sync with its .NET counterpart. _Now what?_

Check out the [Using
methodgen](https://developer.rhino3d.com/guides/rhinocommon/using-methodgen/)
guide for instructions on programmatically generating UnsafeNativeMethods
export declarations.

## Related topics

  * [Microsoft Platform Invoke Tutorial on MSDN](https://msdn.microsoft.com/en-us/library/aa288468%28VS.71%29.aspx)
  * [Interop with Native Libraries on mono-project.org](http://www.mono-project.com/docs/advanced/pinvoke/)
  * [Attributes on MSDN](https://msdn.microsoft.com/en-us/library/z0w1kczw.aspx)
  * [Moose sample on GitHub](https://github.com/dalefugier/Moose)
  * [Using methodgen](https://developer.rhino3d.com/guides/rhinocommon/using-methodgen/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/wrapping-
native-libraries/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/wrapping-
native-libraries/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

