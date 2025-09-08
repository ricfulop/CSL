---
url: https://developer.rhino3d.com/guides/eto/view-and-data/binding/
scraped_at: 2025-09-08T15:43:37.611942
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

[Binding](https://developer.rhino3d.com/guides/eto/view-and-data/binding/)

    * Check Box
    * Text Box
    * Drop Down
  * More Reading

Binding

An introduction to Bindings in Eto

__View Models __

This section is not for Python, python cannot use View Models and bindings in
the same way as C#.

# Introduction

Bindings pair properties in view models with UI Elements in the Eto Layout.
Let’s look at a very simple example.

    
    
    using Eto.Forms;
    using Eto.Drawing;
    
    using Rhino;
    using Rhino.UI;
    
    var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
    
    public class ViewModel
    {
      public string Name { get; set; }
    }
    
    var nameInput = new TextBox() { Width = 300 };
    nameInput.BindDataContext(t => t.Text, (ViewModel vm) => vm.Name);
    
    var viewModel = new ViewModel();
    var myDialog = new Dialog()
    {
      Padding = 12,
      Title = "What is your Name?",
      DataContext = viewModel,
      Content = nameInput
    };
    
    myDialog.ShowModal(parent);
    RhinoApp.WriteLine(viewModel.Name);
    

If we use the Script Editor to run this script, a dialog appears with a text
box. We can then enter text and hit close. You should see your inputted text
printed to the command line.

Let’s examine what happened.

  1. A ViewModel with a `Name` property was stored as the data context of a Dialog
  2. A TextBox’s `Text` property was “bound” to the ViewModel’s `Name` property in a binding that is stored in the Dialog
  3. When changing the `Text` property of the TextBox, the `Name` property in the ViewModel is updated with the value

# More Binding

Binding goes beyond BindDataContext, even if that might be enough for a
simpler UI.

Any binding in Eto can be created with
[`control.Bind<T>`](http://pages.picoe.ca/docs/api/html/Methods_T_Eto_Forms_IBindable.htm),
many controls will have binding methods or properties to simplify this. e.g

  * [`CheckBox.CheckedBinding`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_CheckBox_CheckedBinding.htm)
  * [`TextControl.TextBinding`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_TextControl_TextBinding.htm)
  * [`DropDown.ItemImageBinding`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_DropDown_ItemImageBinding.htm)

These create half the binding for you but aren’t strictly necessary.

These 3 snippets are functionally identical but achieve it through helper
methods and properties

    
    
    cb.Bind<bool>(nameof(CheckBox.Checked), DataContext, nameof(ViewModel.Checked));
    cb.BindDataContext(c => c.Checked, (ViewModel vm) => vm.Checked);
    cb.CheckedBinding.BindDataContext(nameof(ViewModel.Checked));
    

Lastly there are the
[BindableExtensions](http://pages.picoe.ca/docs/api/html/Methods_T_Eto_Forms_BindableExtensions.htm).

All bindings when created on an object are added to the
[`IBindable.Bindings`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_IBindable_Bindings.htm)
property that all Controls have.

# Examples

Why are some of the View Models below more complex than above? This page
conveniently side steps that for now, check out [this
page](https://developer.rhino3d.com/guides/eto/view-and-data/bindings-
explained/) to learn why.

### Check Box

    
    
    using Eto.Forms;
    using Eto.Drawing;
    
    using Rhino.UI;
     
    public class MyViewModel : ViewModel
    {
      private bool _checked { get; set; }
      public bool Checked
      {
        get => _checked;
        set
        {
          _checked = value;
          RaisePropertyChanged(nameof(Checked));
        }
      }
    }
    
    var checkBox = new CheckBox()
    {
        Text = "Check Please",
        Checked = true,
    };
    checkBox.BindDataContext(c => c.Checked, Binding.Property((MyViewModel vm) => vm.Checked).ToBool(true, false));
    // Also works
    // checkBox.CheckedBinding.BindDataContext(Binding.Property((MyViewModel vm) => vm.Checked).ToBool(true, false));
     
    var dialog = new Dialog()
    {
        Padding = 8,
        Content = checkBox,
        DataContext = new MyViewModel()
    };
     
    var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
    dialog.ShowModal(parent);
    

### Text Box

    
    
    using Eto.Forms;
    using Eto.Drawing;
    using Rhino.UI;
     
    public class MyViewModel : ViewModel
    {
      private string _text { get; set; }
      public string Text
      {
        get => _text;
        set
        {
          _text = value;
          RaisePropertyChanged(nameof(Text));
        }
      }
    }
     
    var textBox = new TextBox()
    {
        TextAlignment = TextAlignment.Center,
        Width = 200,
        PlaceholderText = "example@email.com"
    };
    textBox.BindDataContext(tb => tb.Text, (MyViewModel vm) => vm.Text);
     
    var dialog = new Dialog()
    {
        Padding = 8,
        Content = textBox
    };
     
    var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
    dialog.ShowModal(parent);
    

### Drop Down

    
    
    using System;
    using System.Collections.ObjectModel;
    
    using Eto.Forms;
    using Eto.Drawing;
    
    using Rhino.UI; 
    
    public class MyViewModel : ViewModel
    {
      private int _selectedIndex { get; set; }
      public int SelectedIndex
      {
        get => _selectedIndex;
        set
        {
          _selectedIndex = value;
          RaisePropertyChanged(nameof(SelectedIndex));
        }
      }
    
      public ObservableCollection<string> Choices { get; set; } = new () {
        "Point", "Curve", "Brep",
      };
    }
     
    var dropDown = new DropDown();
    dropDown.BindDataContext(dd => dd.DataStore, (MyViewModel vm) => vm.Choices);
    dropDown.BindDataContext(dd => dd.SelectedIndex, (MyViewModel vm) => vm.SelectedIndex);
     
    var dialog = new Dialog()
    {
        Padding = 8,
        Content = dropDown,
        DataContext = new MyViewModel(),
    };
     
    var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
    dialog.ShowModal(parent);
    

## More Reading

  * [Eto Wiki Binding](https://github.com/picoe/Eto/wiki/Data-Binding)
  * [Complex Bindings](https://developer.rhino3d.com/guides/eto/view-and-data/complex-bindings/)
  * [Bindings Deep Dive ](https://developer.rhino3d.com/guides/eto/view-and-data/bindings-explained/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/eto/view-
and-data/binding/_index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/eto/view-
and-data/binding/_index.md) [ Admin](https://developer.rhino3d.com/admin)

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

