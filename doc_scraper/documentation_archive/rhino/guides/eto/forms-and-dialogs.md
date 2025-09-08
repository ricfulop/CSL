---
url: https://developer.rhino3d.com/guides/eto/forms-and-dialogs/
scraped_at: 2025-09-08T15:43:31.458322
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

Forms and Dialogs

An introduction to Forms and Dialogs

## What’s the difference?

Dialogs are modal, Forms are non-modal. Which just means that when you show a
dialog, the program blocks further input until the dialog is closed. A form
however allows for input to continue. Let’s look at a simple example.

C# Python

    
    
    using Eto.Forms;
     
    var form = new Form()
    {
      Width = 100,
      Height = 100
    };
    form.Show();
     
    var dialog = new Dialog()
    {
      Width = 100,
      Height = 100
    };
    dialog.ShowModal(); // <-- Code execution stops here
    
    
    
    import Eto.Forms as ef
    
    form = ef.Form()
    form.Width = 100
    form.Height = 100
    form.Show()
    
    dialog = ef.Dialog()
    dialog.Width = 100
    dialog.Height = 100
    dialog.ShowModal() # <-- Code execution stops here
    

If you paste this into your script editor and run, the Form will show, and
then the dialog, however code written after the dialog will not be run until
the dialog is closed. It is important to choose a Form or Dialog correctly. It
can however be changed easily later on without too much extra effort.

## Forms

Forms are best used when you want to present information or controls to the
user that mix input between the form and the parent window, i.e Rhino. If you
want users to be able to run commands and interact with Rhino, a form is the
most flexible choice.

For example, a form would be best suited to a help window that the user might
consult whilst using Rhino, or a window of custom visibility modes.

## Dialogs

Dialogs are best used when you need to force the user to make a decision
before continuing. For example, choosing a file to open, or alerting the user
that an error has occurred.

[Dialog](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_Dialog.htm) is
available in two flavours, `Dialog`, and `Dialog<T>`. `Dialog<T>` returns a
result on closing which is very useful for obtaining a users choice, such as
Ok, Cancel or even a filename.

## Semi-Model Dialogs

Dialogs can also be run as semi-modal, meaning, code execution is blocked, but
the user can still input information to the command line and interact with
Rhino.

C# Python

    
    
    using Eto.Forms;
    
    using Rhino.UI;
    
    var dialog = new Dialog() { 
      Width = 100,
      Height = 100
    };
    var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
    
    // DefaultButton and AbortButton is required for SemiModal
    dialog.DefaultButton = new Button();
    dialog.AbortButton = new Button();
    
    dialog.ShowSemiModal(__rhino_doc__, parent); // <-- Code execution stops here
    
    
    
    import scriptcontext as sc
     
    from Rhino.UI import RhinoEtoApp, EtoExtensions
    import Eto.Forms as ef
     
    parent = RhinoEtoApp.MainWindowForDocument(sc.doc)
     
    dialog = ef.Dialog()
    dialog.Width = 100
    dialog.Height = 100
    
    # DefaultButton and AbortButton is required for SemiModal
    dialog.DefaultButton = ef.Button()
    dialog.AbortButton = ef.Button()
     
    EtoExtensions.ShowSemiModal(dialog, sc.doc, parent) # <-- Code execution stops here
    

## Modal Summary

Type | Stops Code Execution | Prevents input outside the window  
---|---|---  
**Form** | ❌ | ❌  
**Dialog** | ✔️ | ✔️  
**Dialog (SemiModal)** | ✔️ | ❌  
  
Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/eto/forms-
and-dialogs/_index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/eto/forms-
and-dialogs/_index.md) [ Admin](https://developer.rhino3d.com/admin)

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

