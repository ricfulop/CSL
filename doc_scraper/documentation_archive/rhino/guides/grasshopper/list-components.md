---
url: https://developer.rhino3d.com/guides/grasshopper/list-components/
scraped_at: 2025-09-08T15:41:37.152559
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

[List Components](https://developer.rhino3d.com/guides/grasshopper/list-
components/)

  * Overview
  * List Parameters
  * Solving Routine
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) /

List Components

by [David Rutten](https://discourse.mcneel.com/u/davidrutten/) (Last updated:
Wednesday, December 5, 2018)

## Overview

So far the example components have all operated on individual data items. This
is known as One-In-One-Out. But what if you want to operate on more than one
item at a time; One-In-Many-Out, Many-In-One-Out or Many-In-Many-Out? This
requires that input or output parameters have a non-standard
[Grasshopper.Kernel.GH_ParamAccess](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ParamAccess.htm)
flag.

## List Parameters

Input and Output parameters that are part of Grasshopper components have an
access flag that affects how the component treats data stored in these
parameters. Take for example the Polyline component. It creates a single
polyline object from a _collection_ of corner-points. This is a Many-In-One-
Out kind of logic. The Divide component creates a whole bunch of division
points from a single curve. This is an example of One-In-Many-Out. The Cull
components remove certain items from lists, this is an example of Many-In-
Many-Out.

Most components treat their inputs and outputs as parameters that provide
individual instances of data, rather than related collections of data. This is
indicated by all parameters having an
[GH_ParamAccess.item](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ParamAccess.htm)
access flag. You can however assign different access flags to parameters.
Preferably this flag should be assigned only once, namely in the
[RegisterInputParams](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_RegisterInputParams.htm)
or
[RegisterOutputParams](https://developer.rhino3d.com/api/grasshopper/html/M_Grasshopper_Kernel_GH_Component_RegisterOutputParams.htm)
method overrides. It is legal to modify an access flag as long as a solution
is not currently in progress, but it is not recommended.

In this guide, we’ll be writing a component that removes (culls) the bottom-
most N objects in a collection of geometric shapes. As inputs we’ll need a
collection of geometry and an integer indicating how many objects the user
wants to remove, and as output we’ll provide the same collection of geometry,
but with the bottom-most objects missing. This is therefore a Many-In-Many-Out
case.

The Component code (without the `RegisterInputParams`, `RegisterOutputParams`
and `SolveInstance` methods) may look like this:

C# VB.NET

    
    
    public class Component_CullByElevation : GH_Component
    {
      public Component_CullByElevation()
        : base("Cull Elevation", "CullZ", "Cull objects by relative elevation", "Sets", "Sequence")
      { }
    
      public override Kernel.GH_Exposure Exposure
      {
        get { return GH_Exposure.primary | GH_Exposure.obscure; }
      }
      public override System.Guid ComponentGuid
      {
        get { return new Guid("{A8FF9CBA-0837-4cd6-9198-0D17325D3F8F}"); }
      }
    
      //...additional component code will go here..
    }
    
    
    
    Public Class Component_CullByElevation
      Inherits GH_Component
    
      Public Sub New()
        MyBase.New("Cull Elevation", "CullZ", "Cull objects by relative elevation", "Sets", "Sequence")
      End Sub
    
      Protected Overrides ReadOnly Property Icon() As System.Drawing.Bitmap
        Get
          Return My.Resources.TheIconNameForThisComponent
        End Get
      End Property
      Public Overrides ReadOnly Property Exposure() As Kernel.GH_Exposure
        Get
          Return GH_Exposure.primary Or GH_Exposure.obscure
        End Get
      End Property
      Public Overrides ReadOnly Property ComponentGuid() As System.Guid
        Get
          Return New Guid("{A8FF9CBA-0837-4cd6-9198-0D17325D3F8F}")
        End Get
      End Property
    
      '...further example code will come here...
    
    End Class
    

We’ll need to register the parameters as well, and we’ll use the overloaded
methods to immediately assign the correct parameter access flags…

C# VB.NET

    
    
    protected override void RegisterInputParams(Kernel.GH_Component.GH_InputParamManager pManager)
    {
      pManager.AddGeometryParameter("Geometry", "G", "Geometry to cull", GH_ParamAccess.list);
      pManager.AddIntegerParameter("Count", "C", "Number of objects to cull", GH_ParamAccess.item, 1);
    }
    protected override void RegisterOutputParams(Kernel.GH_Component.GH_OutputParamManager pManager)
    {
      pManager.AddGeometryParameter("Geometry", "G", "Culled geometry", GH_ParamAccess.list);
    }
    
    
    
    Protected Overrides Sub RegisterInputParams(ByVal pManager As Kernel.GH_Component.GH_InputParamManager)
      'list access is non-standard, so we need to specifically assign it.
      pManager.AddGeometryParameter("Geometry", "G", "Geometry to cull", GH_ParamAccess.list)
      pManager.AddIntegerParameter("Count", "C", "Number of objects to cull", GH_ParamAccess.item, 1)
    End Sub
    Protected Overrides Sub RegisterOutputParams(ByVal pManager As Kernel.GH_Component.GH_OutputParamManager)
      'Again, we need to specify list access as that is not default.
      pManager.AddGeometryParameter("Geometry", "G", "Culled geometry", GH_ParamAccess.list)
    End Sub
    

Input parameters rigorously enforce their access. You are only allowed to
retrieve individual items from inputs that have the
[GH_ParamAccess.item](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ParamAccess.htm)
flag set. Lists can only be retrieved when the access is set to
`GH_ParamAccess.list` and data trees can only be gotten from a
`GH_ParamAccess.tree` parameter. Failure to do so will result in an error
message at runtime. Output parameter are more flexible, but this is only
because output access was added only in Grasshopper 0.9.0001 and strict
enforcement would result in SDK breakage with previous versions.

## Solving Routine

The `SolveInstance` implementation is basically identical to previous
examples, the only difference is the way the component interacts with the
parameters…

C# VB.NET

    
    
    protected override void SolveInstance(Kernel.IGH_DataAccess DA)
    {
      //Declare a new List(Of T) to hold your data.
      //This list must exist and should probably be empty.
      List<IGH_GeometricGoo> geometry = new List<IGH_GeometricGoo>();
      Int32 count = 0;
    
      //Retrieve the whole list using Da.GetDataList().
      if ((!DA.GetDataList(0, geometry)))
        return;
      if ((!DA.GetData(1, count)))
        return;
    
      //Validate inputs.
      if ((count < 0))
      {
        AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Count must be a positive integer");
        return;
      }
    
      //The number of objects to cull is larger than or
      //equal to the total number of objects. I.e. cull them all.
      if ((geometry.Count <= count))
        return;
    
      //Iteratively remove the lowest object from the list.
      for (Int32 N = 1; N <= count; N++)
      {
        double lowestElevation = double.MaxValue;
        Int32 lowestIndex = -1;
    
        //Iterate over all remaining geometry and find the lowest one.
        for (Int32 i = 0; i <= geometry.Count - 1; i++)
        {
          if ((geometry[i] == null))
            continue;
          BoundingBox bbox = geometry[i].Boundingbox;
          if ((!bbox.IsValid))
            continue;
    
          double localElevation = bbox.Min.Z;
          if ((localElevation < lowestElevation))
          {
            lowestElevation = localElevation;
            lowestIndex = i;
          }
        }
    
        //Delete the lowest object.
        geometry.RemoveAt(lowestIndex);
      }
    
      //Assign the remaining geometry
      //(even if it is only a single item!)
      //using the DA.SetDataList() method.
      DA.SetDataList(0, geometry);
    }
    
    
    
    Protected Overrides Sub SolveInstance(ByVal DA As Kernel.IGH_DataAccess)
      'Declare a new List(Of T) to hold your data.
      'This list cannot be a null reference.
      Dim geometry As New List(Of IGH_GeometricGoo)
      Dim count As Int32 = 0
    
      'Retrieve the whole list using DA.GetDataList().
      If (Not DA.GetDataList(0, geometry)) Then Return
      If (Not DA.GetData(1, count)) Then Return
    
      'Validate inputs.
      If (count < 0) Then
        AddRuntimeMessage(GH_RuntimeMessageLevel.Error, "Count must be a positive integer")
        Return
      End If
    
      'The number of objects to cull is larger than or
      'equal to the total number of objects. I.e. cull them all.
      If (geometry.Count <= count) Then Return
    
      'Iteratively remove the lowest object from the list.
      For N As Int32 = 1 To count
        Dim lowestElevation As Double = Double.MaxValue
        Dim lowestIndex As Int32 = -1
    
        'Iterate over all remaining geometry and find the lowest one.
        For i As Int32 = 0 To geometry.Count - 1
          If (geometry(i) Is Nothing) Then Continue For
          Dim bbox As BoundingBox = geometry(i).Boundingbox
          If (Not bbox.IsValid) Then Continue For
    
          Dim localElevation As Double = bbox.Min.Z
          If (localElevation < lowestElevation) Then
            lowestElevation = localElevation
            lowestIndex = i
          End If
        Next
    
        'Delete the lowest object.
        If (lowestIndex >= 0) Then geometry.RemoveAt(lowestIndex)
      Next
    
      'Assign the remaining geometry using the DA.SetDataList() method.
      DA.SetDataList(0, geometry)
    End Sub
    

## Related Topics

  * [What is a Grasshopper Component?](https://developer.rhino3d.com/guides/grasshopper/what-is-a-grasshopper-component/)
  * [Your First Component](https://developer.rhino3d.com/guides/grasshopper/your-first-component-windows/)
  * [Simple Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)
  * [Simple Mathematics Component](https://developer.rhino3d.com/guides/grasshopper/simple-mathematics-component/)
  * [Simple Geometry Component](https://developer.rhino3d.com/guides/grasshopper/simple-geometry-component/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/list-
components/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/list-
components/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

