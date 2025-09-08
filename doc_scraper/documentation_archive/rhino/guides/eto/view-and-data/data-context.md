---
url: https://developer.rhino3d.com/guides/eto/view-and-data/data-context/
scraped_at: 2025-09-08T15:43:35.479309
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

[Data Context](https://developer.rhino3d.com/guides/eto/view-and-data/data-
context/)

  * An Overview
  * The relationship between DataContext and DataStore
  * Trickle Down
  * Related topics

Data Context

An introduction to the Eto Data Context

## An Overview

All `Eto.Forms.Control` objects have the
[`DataContext`](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_BindableWidget_DataContext.htm)
property. DataContext lets us choose a data object for our View to bind to,
this will likely be a ViewModel, or a data object class. But it could even be
as simple as an integer (although this would be unusual). If a View does not
have or need bindings, it will likely not need a DataContext object. The
DataContext should not be used for arbitrary data storage, use
[Tag](http://pages.picoe.ca/docs/api/html/P_Eto_Forms_Control_Tag.htm) for
this.

## The relationship between DataContext and DataStore

Some Controls have a `DataStore` property, a good example is the
[GridView](http://pages.picoe.ca/docs/api/html/T_Eto_Forms_GridView.htm). The
DataStore is _similar_ to the DataContext, but should be used differently. The
DataStore will always be an enumerable, such as a list, array, or better yet,
an [`ObservableCollection<T>`](https://learn.microsoft.com/en-
us/dotnet/api/system.collections.objectmodel.observablecollection-1?view=net-7.0).

## Trickle Down

A very useful feature to be aware of is the trickle-down effect of
DataContext. Any Control, (including Forms and Dialogs) that has a DataContext
will set the DataContext of every child control meaning that this can be
accessed anywhere in your UI Tree. If a child control overrides its
DataContext with a new DataContext then a new lineage of this DataContext is
created.

C# Python

    
    
    using Eto.Forms;
    
    using Rhino.UI;
    
    class MyMainViewModel {}
    class MyNewViewModel {}
    
    var dialog = new Dialog()
    {
      DataContext = new MyMainViewModel(), // <-- Start of Main View Model
      Content = new TableLayout()
      {
        Rows = {
          new TableRow( // <-- TableRow has a DataContext of MyMainViewModel
            new StackLayout() // <-- StackLayout has a DataContext of MyNewViewModel
            {
              DataContext = new MyNewViewModel(), // <-- Start of New View Model
              Items = {
                new Drawable(), // <-- Drawable has a DataContext of MyNewViewModel
                new Button()    // <-- Button has a DataContext of MyNewViewModel
              }
            }
          ),
          new TableRow(    // <-- TableRow has a DataContext of MyMainViewModel
            new Button(), 
            new Button(), // <-- Buttons all have a DataContext of MyMainViewModel
            new Button()
          ),
        }
      }
    };
    
    var parent = RhinoEtoApp.MainWindowForDocument(__rhino_doc__);
    dialog.ShowModal(parent);
    
    
    
    import scriptcontext as sc
     
    import Rhino
    from Rhino.UI import RhinoEtoApp, EtoExtensions
    import Eto.Forms as ef
    import Eto.Drawing as ed
     
    parent = RhinoEtoApp.MainWindowForDocument(sc.doc)
    
    class MyMainViewModel():
      pass
    
    class MyNewViewModel():
      pass
    
    stack_layout = ef.StackLayout()
    stack_layout.DataContext = ef.MyNewViewModel()
    
    # Drawable has a DataContext of MyNewViewModel
    stack_layout.Items.Add(ef.StackLayoutItem(ef.Drawable()))
    
    # Button has a DataContext of MyNewViewModel
    stack_layout.Items.Add(ef.StackLayoutItem(ef.Button()))
    
    table_layout = ef.TableLayout()
    table_layout.Rows.Add(ef.TableRow(ef.TableCell(stack_layout)))
    
    # Buttons and TableRow all have a DataContext of MyMainViewModel
    table_layout.Rows.Add(ef.TableRow(ef.TableCell(ef.Button()), ef.TableCell(ef.Button()), ef.TableCell(ef.Button())))
    
    dialog = ef.Dialog()
    dialog.DataContext = ef.MyMainViewModel()
    dialog.Content = table_layout
    
    dialog.ShowModal(parent)
    

## Related topics

  * [Binding Data with a ViewModel](https://developer.rhino3d.com/guides/eto/view-and-data/binding/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/eto/view-
and-data/data-context/_index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/eto/view-
and-data/data-context/_index.md) [ Admin](https://developer.rhino3d.com/admin)

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

