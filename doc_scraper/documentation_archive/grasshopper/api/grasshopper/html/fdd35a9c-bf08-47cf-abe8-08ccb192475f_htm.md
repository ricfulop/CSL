---
url: https://developer.rhino3d.com/api/grasshopper/html/fdd35a9c-bf08-47cf-abe8-08ccb192475f.htm#SolveInstance
scraped_at: 2025-09-08T16:25:35.593794
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Examples](../html/d113a9f0-6e27-46df-8316-2079c44382ac.htm "Examples")

[C#](../html/730f0792-7bfb-4310-a416-239e8c315645.htm "C#")

[Simple Component (C#)](../html/730f0792-7bfb-4310-a416-239e8c315645.htm
"Simple Component \(C#\)")

[Simple Mathematics (C#)](../html/fdd35a9c-bf08-47cf-abe8-08ccb192475f.htm
"Simple Mathematics \(C#\)")

[Simple Geometry (C#)](../html/5764fa15-29d1-4e37-8496-2478d3cf28dc.htm
"Simple Geometry \(C#\)")

[Simple Data Types (C#)](../html/d823ee90-ea94-4a8a-a972-df5d006a8d9f.htm
"Simple Data Types \(C#\)")

[Simple Parameters (C#)](../html/fbfe5e40-ba8d-4e53-97c6-27572e049835.htm
"Simple Parameters \(C#\)")

[List Component (C#)](../html/020a5098-963f-4da8-bf65-650993c73bcb.htm "List
Component \(C#\)")

[Extending the GUI (C#)](../html/a367a8b3-a8b6-4d92-ad15-00b5aa60fd48.htm
"Extending the GUI \(C#\)")

[Custom Attributes (C#)](../html/8a7974ab-7b2b-4f48-84d0-6e81b184e6b0.htm
"Custom Attributes \(C#\)")

[Custom Component Options
(C#)](../html/5f6a9f31-8838-40e6-ad37-a407be8f2c15.htm "Custom Component
Options \(C#\)")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Simple Mathematics (C#)  
  
---  
  
  * Introduction
  * Input parameters
  * Output parameters
  * SolveInstance

This article contains a brief example of a component that deals with some
simple mathematics and multiple input and output parameters. We'll discuss
parameter order, legacy support for changing component layouts and default
values for input parameters. We will not be dealing with any of the basics of
component development. You should have read the [My First
Component](730f0792-7bfb-4310-a416-239e8c315645.htm) topic before starting
this one.

For this component we'll bundle the Sine(), Cosine() and Tangent()
trigonometry functions while allowing inputs to be specified in either Radians
or Degrees. We'll need to define two input parameter (one of which will have a
default value) and three output parameters.

Before you start with this topic, create a new class that derives from
Grasshopper.Kernel.GH_Component, as outlined in the [My First
Component](730f0792-7bfb-4310-a416-239e8c315645.htm) topic.

![](../icons/SectionExpanded.png)Input parameters

This component will require two input parameters, one of which has a default
value. We'll need to register these parameters inside the
RegisterInputParams() method:

C#

Copy

    
    
    ...
    protected override void RegisterInputParams(GH_Component.GH_InputParamManager pManager)
    {
      pManager.AddNumberParameter("Angle", "A", "The angle to measure", GH_ParamAccess.item);
      pManager.AddBooleanParameter("Radians", "R", "Work in Radians", GH_ParamAccess.item, true); // The default value is 'true'
    }
    ...

The first parameter is of type Double meaning it accepts floating point
values. It only has a name, abbreviation, description and access level
defined. The second parameter is of type bool and it will accept true and
false values. The pManager object allows us to specify a single default value
for many parameter types.

The order in which we register the parameters is also the order in which
they'll appear on the component. We should not change the order (or the types,
or the number) of the parameters once the component has been released to the
world. Every Grasshopper file that was saved with one of our components will
expect to be deserialized by the exact same component layout. If you add an
additional parameter to an component and someone tries to open a file which
was saved while an older version of that component, it will fail to
deserialize as the data in the file no longer matches the new layout. An
exception will be thrown and Grasshopper will short circuit that particular
instance. The entire component and all connections to it will be missing when
the file is eventually displayed to the user.

If you _must_ change the parameter layout of a component, you should create a
completely new GH_Component class with a different ComponentGuid, while
maintaining the old component type for legacy file purposes. You can hide
xomponents from the Grasshopper GUI by overriding the
[Exposure](P_Grasshopper_Kernel_IGH_DocumentObject_Exposure.htm) property of
the GH_Component class and changing the return value to GH_Exposure.hidden:

C#

Copy

    
    
    public override Grasshopper.Kernel.GH_Exposure Exposure 
    {
      get { return GH_Exposure.hidden; }
    }

![](../icons/SectionExpanded.png)Output parameters

Our component will also need three output parameters. Output parameters differ
from input parameters in that they have much fewer options. Users cannot add
expressions to them, there are no default values, they don't support
persistent data. Outputs are always cleared when the component expires, and
they are slowly filled out from within the SolveInstance() routine.

C#

Copy

    
    
    ...
    protected override void RegisterOutputParams(GH_Component.GH_OutputParamManager pManager)
    {
      pManager.AddNumberParameter("Sin", "sin", "The sine of the Angle.", GH_ParamAccess.item);
      pManager.AddNumberParameter("Cos", "cos", "The cosine of the Angle.", GH_ParamAccess.item);
      pManager.AddNumberParameter("Tan", "tan", "The tangent of the Angle.", GH_ParamAccess.item);
    }
    ...

![](../icons/SectionExpanded.png)SolveInstance

The SolveInstance() implementation for this component is hardly any more
complicated than it was for [My First
Component](730f0792-7bfb-4310-a416-239e8c315645.htm). The only difference is
that we now have more than one parameter on each side.

C#

Copy

    
    
    ...
    protected override void SolveInstance(IGH_DataAccess DA)
    {
      // Declare variables to contain all inputs.
      // We can assign some initial values that are either sensible or indicative.
      double angle = double.NaN;
      bool radians = false;
    
      // Use the DA object to retrieve the data inside the input parameters.
      // If the retrieval fails (for example if there is no data) we need to abort.
      if (!DA.GetData(0, ref angle)) { return; }
      if (!DA.GetData(1, ref radians)) { return; }
    
      // If the angle value is not a valid number, we should abort.
      if (!Rhino.RhinoMath.IsValidDouble(angle)) { return; }
    
      // If the user wants to work in degrees rather than radians, 
      // we assume that angle is defined in degrees. 
      // We need to convert it into Radians again.
      if (!radians)
      {
        angle = Rhino.RhinoMath.ToRadians(angle);
      }
    
      // Now we are ready to assign the outputs via the DA object.
      // Since the Sin(), Cos() and Tan() never fail, we might as well 
      // combine them with the assignment.
      DA.SetData(0, Math.Sin(angle));
      DA.SetData(1, Math.Cos(angle));
      DA.SetData(2, Math.Tan(angle));
    }
    ...

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

