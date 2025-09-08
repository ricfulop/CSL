---
url: https://developer.rhino3d.com/guides/cpp/crash-dump-analysis/
scraped_at: 2025-09-08T15:39:37.467528
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

[Crash Dump Analysis](https://developer.rhino3d.com/guides/cpp/crash-dump-
analysis/)

  * Overview
    * Configuration
    * Debugging Crashes
    * Try it!
    * Storing symbols
    * More

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Crash Dump Analysis

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

If Rhino crashes, two files are created on the user’s desktop:
_RhinoCrashDump.dmp_ and _RhinoCrashDump.3dm_. The _.3dm_ file is Rhino’s last
ditch effort to save the model. The _.dmp_ file can be used in Visual Studio
to find the place in the source code where a Rhino plugin crashed.

### Configuration

Before you can analyze crashes, you’ll need to set up Visual Studio to help
you get symbols.

  1. **Enable Symbol Servers**
     1. Open Visual Studio
     2. From the **Tools** menu, click **Options**
     3. Select **Debugging** > **General** and enable the following options: 
        * _Enable source server support_
        * _Print source server diagnostic messages to the Output window_
        * _Allow source server for partial trust assemblies (Managed only)_
        * _Always run untrusted source server commands without prompting_
     4. Select **Debugging** > **Symbols**
     5. In the _Symbol file (.pdb) locations_ box, add: 
        * <http://s3.symbols.rhino3d.com/symbols/dujour>
        * <https://msdl.microsoft.com/download/symbols>
     6. Optionally add these symbol servers if you need symbols for video driver related crashes: 
        * <https://driver-symbols.nvidia.com>
        * <https://download.amd.com/dir/bin_2018>
        * <https://download.amd.com/dir/bin>
        * <https://software.intel.com/sites/downloads/symbols>
     7. In the _Cache symbols in this directory_ folder, enter a folder where Visual Studio will cache symbols. Depending on the number of crashes you debug, this folder can get quite large.
     8. Under _Symbol search preferences:_ select **Search for all modules unless excluded** (Note that this will make debugging your project slow. To speed this up, select _Automatically choose what module symbols to search for_)

### Debugging Crashes

  1. Start Visual Studio
  2. From the **File** menu, click **Open**
  3. Browse to the **RhinoCrashDump.dmp** file in the extracted folder
  4. Click **Debug with Mixed**

### Try it!

Below is a sample C++ plugin that will crash Rhino. To test out crash dump
analysis:

  1. Download and build the [TestSdkCrash](https://developer.rhino3d.com/files/testsdkcrash.zip) plugin.
  2. Launch Rhino and load the plugin using the `PlugInManager` command.
  3. Run the `TestSdkCrash` command.
  4. While the _McNeel Error Reporting_ dialog is displayed, copy the _RhinoCrashDump.dmp_ from the desktop to some other location, and then click _Don’t Send_.
  5. Follow the steps above to analyze the crash dump.

### Storing symbols

In order to get the most out of your crashes, you need to save the symbols
(.pdb) and source code from each of the builds. You’ll also need to add source
information into your .pdb files before you store them in the symbol server.

### More

[Working with Debug Symbols and Source](https://learn.microsoft.com/en-
us/shows/visual-studio-2022-launch-event/tips-and-tricks-tips-for-working-
with-debug-symbols-and-source)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/crash-
dump-analysis/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/crash-
dump-analysis/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

