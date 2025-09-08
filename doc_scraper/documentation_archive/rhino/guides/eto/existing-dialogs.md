---
url: https://developer.rhino3d.com/guides/eto/existing-dialogs/
scraped_at: 2025-09-08T15:43:32.478771
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

Existing Dialogs

Using the already available dialogs available in Eto makes your application
more consistent with Rhino and the operating system your Plug-in is running
on. It also saves you time and effort.

## Message Box

[MessageBox](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_MessageBox.htm)
is a very simple and highly useful dialog for handling control flow and
allowing users to make informed decisions.

C# Python

    
    
    using Eto.Forms;
    
    var result = MessageBox.Show("Would you like to save before closing?",
                               MessageBoxButtons.YesNo,
                               MessageBoxType.Question,
                               MessageBoxDefaultButton.Yes);
    
    if (result != DialogResult.Yes)
    {
      MessageBox.Show("Model discarded successfully!", MessageBoxButtons.OK, MessageBoxType.Information);
    }
    else
    {
      MessageBox.Show("Model saved successfully before closing.", MessageBoxButtons.OK, MessageBoxType.Information);
    }
    
    
    
    import scriptcontext as sc
    
    import Eto.Forms as ef
    from Rhino.UI import RhinoEtoApp
    
    parent = RhinoEtoApp.MainWindowForDocument(sc.doc)
    
    result = ef.("Would you like to save before closing?",
                               MessageBoxButtons.YesNo,
                               MessageBoxType.Question,
                               MessageBoxDefaultButton.Yes)
    
    if result != DialogResult.Yes:
      ef.MessageBox.Show("Model discarded successfully!", MessageBoxButtons.OK, MessageBoxType.Information)
    
    else:
      ef.MessageBox.Show("Model saved successfully before closing.", MessageBoxButtons.OK, MessageBoxType.Information)
    

![Message Boxes](https://developer.rhino3d.com/images/eto/controls/message-
boxes.png)

## Color Picker

The Color Picker is a button that shows the
[ColorDialog](http://api.etoforms.picoe.ca/html/T_Eto_Forms_ColorDialog.htm).
The Color Dialog can also be used separately.

C# Python

    
    
    using Eto.Forms;
    
    var dialog = new Dialog()
    {
      Width = 80,
      Height = 80,
      Padding = 8,
      Content = new ColorPicker()
    };
    
    dialog.ShowModal();
    
    
    
    import Eto.Forms as ef
    import Eto.Drawing as ed
    
    dialog = ef.Dialog()
    dialog.Width = 80
    dialog.Height = 80
    dialog.Padding = ed.Padding(8)
    dialog.Content = ef.ColorPicker()
    
    dialog.ShowModal()
    

![Color Picker](https://developer.rhino3d.com/images/eto/controls/colour-
picker.png)

## File Dialogs

File dialogs make prompting users to choose new and existing files simple.

If you need to prompt for a folder, there is the
[SelectFolderDialog](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_SelectFolderDialog.htm)

__Your Data is Safe __

The below example **does not** save or open any files you choose. It only
shows dialogs that assist in getting file names.

C# Python

    
    
    using Eto.Forms;
    
    var parent = Rhino.UI.RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
    
    var openDialog = new OpenFileDialog()
    {
      Filters = {
          new FileFilter("Any", "*.*")
      },
      CurrentFilterIndex = 0,
      CheckFileExists = true,
      MultiSelect = true,
      Title = "Pick a file, any file"
    };
    
    var result = openDialog.ShowDialog(parent);
    if (result == DialogResult.Cancel)
    {
      MessageBox.Show("No File chosen!", MessageBoxType.Information);
      return;
    }
    
    var saveDialog = new SaveFileDialog()
    {
      Title = "Save your file",
      Directory = openDialog.Directory,
      FileName = openDialog.FileName
    };
    
    result = saveDialog.ShowDialog(parent);
    
    if (result == DialogResult.Cancel)
    {
      MessageBox.Show("File not saved!", MessageBoxType.Information);
      return;
    }
    
    
    
    import scriptcontext as sc
    
    import Eto.Forms as ef
    from Rhino.UI import RhinoEtoApp
    import Rhino
    
    parent = Rhino.UI.RhinoEtoApp.MainWindowForDocument(sc.doc);
    
    openDialog = ef.OpenFileDialog()
    openDialog.Filters.Add(ef.FileFilter("Any", "*.*"));
    openDialog.CurrentFilterIndex = 0
    openDialog.CheckFileExists = True
    openDialog.MultiSelect = True
    openDialog.Title = "Pick a file, any file"
    
    result = openDialog.ShowDialog(parent);
    if result == DialogResult.Cancel:
      ef.MessageBox.Show("No File chosen!", MessageBoxType.Warning)
    else:
      saveDialog = ef.SaveFileDialog()
      saveDialog.Title = "Save your file"
      saveDialog.Directory = openDialog.Directory
      saveDialog.FileName = openDialog.FileName
    
      result = saveDialog.ShowDialog(parent)
    
      if result == DialogResult.Cancel:
          ef.MessageBox.Show("File not saved!", MessageBoxType.Warning)
      else:
          ef.MessageBox.Show("File saved", MessageBoxType.Information)
    

![File Dialogs](https://developer.rhino3d.com/images/eto/controls/file-
dialogs.png)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/eto/existing-
dialogs/_index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/eto/existing-
dialogs/_index.md) [ Admin](https://developer.rhino3d.com/admin)

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

