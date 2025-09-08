---
url: https://developer.rhino3d.com/guides/scripting/editor-editing/#autocomplete-in-function-help
scraped_at: 2025-09-08T16:04:25.812615
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

[Script Editing
Features](https://developer.rhino3d.com/guides/scripting/editor-editing/)

  * Tabs or Spaces?
  * Indentation Guides
  * Minimap
  * Line Numbers
  * Diagnostics (Linting)
  * Autocompletion
    * Word-based Autocomplete
    * Autocomplete in Function Help

[Guides](https://developer.rhino3d.com/en/guides/) / [Scripting
Guides](https://developer.rhino3d.com/en/guides/scripting/) /

Script Editing Features

[New in 8](https://developer.rhino3d.com/8/new)

by [Ehsan Iran-Nejad](https://discourse.mcneel.com/u/eirannejad/) (Last
updated: Wednesday, December 11, 2024)

Script Editor has a few editing features that can be changed or toggled for
each specific language. These settings are toggled/set using two different
methods:

  * **Edit > Toggle** menu items: Affect the current session and are forgotten when Rhino restarts.

  * **Editor Options** Dialog: Are persistent and are stored in editor configuration file to disk.

Depending on the type of feature, there might be a _Toggle_ menu item or a
setting in _Editor Options_ , or _both_. Some features are language-specific
and can be set independently by scripting language.

## Tabs or Spaces?

Choose **Edit > Toggle White Spaces** to toggle visibilty of white spaces (Tab
or Space) in your scripts. See **Show White Spaces** in [Editing
Options](https://developer.rhino3d.com/guides/scripting/editor-
configs/#editing-options). This option is _Off_ by default:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
tabsspaces.png)

**Edit > Convert Indentation to Tabs/Spaces** commands can be used to convert
between Space and Tab indentations. When changing your scripts to [SDK-
Mode](https://developer.rhino3d.com/guides/scripting/scripting-gh-python/#sdk-
mode) in Grasshopper, the indentation is detected and used in modified script:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
tabsspaces-gh.png)

## Indentation Guides

Indentation guides are vertical lines drawn at different indentation levels to
help visually identifying scopes and blocks. See **Show Indentation Guides**
in [Editing Options](https://developer.rhino3d.com/guides/scripting/editor-
configs/#editing-options). This option is _On_ by default:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
indentGuides.png)

## Minimap

Choose **Edit > Toggle Minimap** to toggle visibilty of minimap. It is
effectively a thicker vertical scrollbar that shows a tiny preview of your
script. You can scroll up and down the script using minimap. See **Show
Minimap** in [Editing
Options](https://developer.rhino3d.com/guides/scripting/editor-
configs/#editing-options). This option is _Off_ by default:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
minimap.png)

## Line Numbers

Pretty clear what they are! Choose **Edit > Toggle Line Numbers** to toggle
their visibility:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
lineNumbers.png)

## Diagnostics (Linting)

As you are typing your script, the editor is continiously checking for syntax
errors using the static analyzers provided by the language. These messages are
categorized as **Errors** , **Warnings** , or **Info** and show up in the
_Problems_ panel at the bottom of the editor. The script text area also shows
squiggly lines where these errors are located. You can click on each item in
_Problems_ panel to navigate the cursor to where the problem is:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
diags.png)

When there are messages in the _Problems_ panel, its tab shows an icon with a
count of messages listed in the panel:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
diags-problemsTab.png)

By default, the _Problems_ panel only shows error messages. You can use the
filter toggles on the panel to see other message types as well:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
diags-problemsFilter.png)

See **Diagnostics (Linting)** in [Language Support
Options](https://developer.rhino3d.com/guides/scripting/editor-
configs/#language-support-options) to turn diagnostics off for a specific
language. This option is _On_ by default.

## Autocompletion

Script editor has completion support for all languages. There are a few kinds
of autocompletion:

  * **Word Completion:** usually triggers when typing space or `.` and provides completion for methods, properties, function calls, etc:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
autocomplete-word.png)

  * **Signature Completion** usually triggers when opening a `(` and provides function help and parameter list, as well as tracking and highlighting arguments as you type:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
autocomplete-signature.png)

  * **Snippet Completion** usually triggers when typing space after a keyword and provides templates for common language constructs like `if` statements or `foreach` loops. It is _Off_ by default. Choose **Edit > Toggle Snippet in Autocomplete** to toggle snippets on.

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
autocomplete-snippet.png)

### Word-based Autocomplete

Editor can collect words already used in the script to help with autocomplete.
However as it does not have a full understanding of the context and meaning of
these collected words, this type of autocompletion is not always useful. This
option is _Off_ by default. Choose **Edit > Toggle Word-based Autocomplete**
to turn it on. See **Autocompletion** in [Language Support
Options](https://developer.rhino3d.com/guides/scripting/editor-
configs/#language-support-options) to toggle this option on for a specific
language:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
autocomplete-wordBased.png)

### Autocomplete in Function Help

Usually when typing up arguments to a function, we would like to keep the
_Signature Completion_ open so it can track the arguments being typed and help
with each argument type or expected values. For this reason, autocompletion is
momentarily stopped to keep the _Signature Completion_ popup open:

![](https://developer.rhino3d.com/guides/scripting/editor-editing/editor-
autocomplete-insignature.png)

To change this behaviour - for example to get the autocompletion for `os.` in
example above - choose **Edit > Toggle Autocomplete in Function Help**. See
**Autocompletion** in [Language Support
Options](https://developer.rhino3d.com/guides/scripting/editor-
configs/#language-support-options) to toggle this option for a specific
language.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/scripting/editor-
editing/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/scripting/editor-
editing/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

