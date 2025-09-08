---
url: https://developer.rhino3d.com/guides/grasshopper/custom-component-options/
scraped_at: 2025-09-08T15:41:41.160890
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

[Custom Component
Options](https://developer.rhino3d.com/guides/grasshopper/custom-component-
options/)

  * Overview
  * Example Component
  * Class Level Variables
  * (De)serialization of Custom Data
  * Context Menu Changes
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) /

Custom Component Options

by [David Rutten](https://discourse.mcneel.com/u/davidrutten/) (Last updated:
Wednesday, December 5, 2018)

It skips over some portions of Component design which have already been
handled in previous guides, so do not read this guide before familiarizing
yourself with the [Simple
Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)
guide.

## Overview

The component we’ll create in this article will sort a list of numbers and
have the custom option to convert those numbers to absolute values prior to
sorting. However, rather than providing this option as a boolean input
parameter, we’ll allow people to set it via the Component context menu. We’ll
need to do four special things to achieve this, to wit:

  * Declare a class level variable/property.
  * Provide access to the variable from within the Component menu.
  * Include the variable in (de)serialization.
  * Record undo events when changing the value.

## Example Component

Before you start with this guide, create a new class that derives from
[GH_Component](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_Component.htm),
as outlined in the [Simple
Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)
guide.

This component will require one input parameter and one output parameter, both
of type Number with list access:

C# VB.NET

    
    
    ...
      protected override void RegisterInputParams(Kernel.GH_Component.GH_InputParamManager pManager)
      {
        pManager.AddNumberParameter("Values", "V", "Values to sort", GH_ParamAccess.list);
      }
      protected override void RegisterOutputParams(Kernel.GH_Component.GH_OutputParamManager pManager)
      {
        pManager.AddNumberParameter("Values", "V", "Sorted values", GH_ParamAccess.list);
      }
    ...
    
    
    
    ...
    Protected Overrides Sub RegisterInputParams(ByVal pManager As GH_Component.GH_InputParamManager)
      pManager.AddNumberParameter("Values", "V", "Values to sort", GH_ParamAccess.list)
    End Sub
    Protected Overrides Sub RegisterOutputParams(ByVal pManager As Kernel.GH_Component.GH_OutputParamManager)
      pManager.AddNumberParameter("Values", "V", "Sorted values", GH_ParamAccess.list)
    End Sub
    ...
    

Assuming for now we’ll have a local property called `Absolute()` which gets a
single boolean, we can also already write the `SolveInstance()` method:

C# VB.NET

    
    
    ...
      protected override void SolveInstance(Kernel.IGH_DataAccess DA)
      {
        List<double> values = new List<double>();
        if ((!DA.GetDataList(0, values)))
          return;
        if ((values.Count == 0))
          return;
    
        // Don't worry about where the Absolute property comes from, we'll get to it soon.
        if ((Absolute))
        {
          for (Int32 i = 0; i < values.Count; i++)
          {
            values(i) = Math.Abs(values(i));
          }
        }
    
        values.Sort();
        DA.SetDataList(0, values);
      }
    ...
    
    
    
    ...
    Protected Overrides Sub SolveInstance(ByVal DA As Kernel.IGH_DataAccess)
      Dim values As New List(Of Double)
      If (Not DA.GetDataList(0, values)) Then Return
      If (values.Count = 0) Then Return
    
      'Don't worry about where the Absolute property comes from, we'll get to it soon.
      If (Absolute) Then
        For i As Int32 = 0 To values.Count - 1
          values(i) = Math.Abs(values(i))
        Next
      End If
    
      values.Sort()
      DA.SetDataList(0, values)
    End Sub
    ...
    

## Class Level Variables

The “Absolute” option for this component applies to the entire object, but not
to other instances of this component. Since it needs to survive (i.e. retain
its value) for as long as the component lives, it has to be declared as a
class level variable:

C# VB.NET

    
    
    ...
    private bool m_absolute = false;
    public bool Absolute
    {
      get { return m_absolute; }
      set
      {
        m_absolute = value;
        if ((m_absolute))
        {
          Message = "Absolute";
        }
        else
        {
          Message = "Standard";
        }
      }
    }
    ...
    
    
    
    ...
    Private m_absolute As Boolean = False
    Public Property Absolute() As Boolean
      Get
        Return m_absolute
      End Get
      Set(ByVal value As Boolean)
        m_absolute = value
        If (m_absolute) Then
          Message = "Absolute"
        Else
          Message = "Standard"
        End If
      End Set
    End Property
    ...
    

The `m_absolute` field is a private field (only accessible from within this
component) and it is exposed publicly via the `Absolute()` method, which
allows both getting and setting. Furthermore, whenever the `m_absolute` field
is set, the `Absolute()` method ensures that the correct message is assigned.
The
[Message](https://developer.rhino3d.com/api/grasshopper/html/P_Grasshopper_Kernel_GH_Component_Message.htm)
field on `GH_Component` allows you to set a string which will be displayed
underneath the component on the canvas. This is to signal to users that
there’s an option they can change which is not directly accessible via the
input parameters. Note that the message is not set _until_ the `Absolute()`
property is accessed, so you should specifically place a call to `Absolute =
False` (or `True`) in the constructor.

It is of course possible to add any number of custom fields to a component,
but you can only attach a single message, if you have more than one field you
want to make the user aware of, you’ll need to get creative.

## (De)serialization of Custom Data

When you add options or states to your component which need to be “sticky,”
you’ll also need to (de)serialize them correctly. (De)serialization is used
when saving and opening files, when copying and pasting objects and during
undo/redo actions. In this particular case, we only need to add a single
boolean to the standard file archive. Serialization in Grasshopper happens
using the _GH_IO.dll_ methods and types, not via standard framework mechanisms
such as the `SerializableAttribute`.

Override the
[Write](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_Write.htm)
and
[Read](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_Read.htm)
methods on `GH_Component` and be sure to always call the base implementation.

C# VB.NET

    
    
    ...
    public override bool Write(GH_IO.Serialization.GH_IWriter writer)
    {
      // First add our own field.
      writer.SetBoolean("Absolute", Absolute);
      // Then call the base class implementation.
      return base.Write(writer);
    }
    public override bool Read(GH_IO.Serialization.GH_IReader reader)
    {
      // First read our own field.
      Absolute = reader.GetBoolean("Absolute");
      // Then call the base class implementation.
      return base.Read(reader);
    }
    ...
    
    
    
    ...
    Public Overrides Function Write(ByVal writer As GH_IO.Serialization.GH_IWriter) As Boolean
      'First add our own field.
      writer.SetBoolean("Absolute", Absolute)
      'Then call the base class implementation.
      Return MyBase.Write(writer)
    End Function
    Public Overrides Function Read(ByVal reader As GH_IO.Serialization.GH_IReader) As Boolean
      'First read our own field.
      Absolute = reader.GetBoolean("Absolute")
      'Then call the base class implementation.
      Return MyBase.Read(reader)
    End Function
    ...
    

## Context Menu Changes

We’ll also need to add an additional menu item to the component context menu,
then handle the click event for that item. Adding items to a context menu is
best done via the
[AppendAdditionalComponentMenuItems](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_AppendAdditionalComponentMenuItems.htm)
method. It allows you to insert any number of item in between the Bake and the
Help items. The easiest way to add menu items is to use the Shared methods on
[GH_DocumentObject](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_DocumentObject.htm)
such as
[Menu_AppendItem](https://developer.rhino3d.com/api/grasshopper/html/Overload_Grasshopper_Kernel_GH_DocumentObject_Menu_AppendItem.htm)
or one of the overloads. In this case we also want to assign a tooltip text to
the item which cannot be done from inside `Menu_AppendItem()`.

C# VB.NET

    
    
    ...
    protected override void AppendAdditionalComponentMenuItems(System.Windows.Forms.ToolStripDropDown menu)
    {
      // Append the item to the menu, making sure it's always enabled and checked if Absolute is True.
      ToolStripMenuItem item = Menu_AppendItem(menu, "Absolute", Menu_AbsoluteClicked, true, Absolute);
      // Specifically assign a tooltip text to the menu item.
      item.ToolTipText = "When checked, values are made absolute prior to sorting.";
    }
    ...
    
    
    
    ...
    Protected Overrides Sub AppendAdditionalComponentMenuItems(ByVal menu As System.Windows.Forms.ToolStripDropDown)
      'Append the item to the menu, making sure it's always enabled and checked if Absolute is True.
      Dim item As ToolStripMenuItem = Menu_AppendItem(menu, "Absolute", AddressOf Menu_AbsoluteClicked, True, Absolute)
      'Specifically assign a tooltip text to the menu item.
      item.ToolTipText = "When checked, values are made absolute prior to sorting."
    End Sub
    ...
    

When this menu item is clicked, the delegate assigned inside the
`Menu_AppendItem()` method will be invoked. It is here that we must handle a
click event. There are usually three steps involved in handling clicks; Record
the current state as an undo event, change the state, trigger a new solution:

C# VB.NET

    
    
    private void Menu_AbsoluteClicked(object sender, EventArgs e)
    {
      RecordUndoEvent("Absolute");
      Absolute = !Absolute;
      ExpireSolution(true);
    }
    ...
    
    
    
    ...
    Private Sub Menu_AbsoluteClicked(ByVal sender As Object, ByVal e As EventArgs)
      RecordUndoEvent("Absolute")
      Absolute = Not Absolute
      ExpireSolution(True)
    End Sub
    ...
    

Since our `Write()` and `Read()` methods handle the (de)serialization of the
`Absolute` field, we can use the default
[RecordUndoEvent](https://developer.rhino3d.com/api/grasshopper/html/Overload_Grasshopper_Kernel_GH_DocumentObject_RecordUndoEvent.htm)
method. It is possible to define your own undo records, but that is a topic
for another guide.

## Related Topics

  * [Simple Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/custom-
component-options/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/custom-
component-options/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

