---
url: https://developer.rhino3d.com/guides/grasshopper/simple-data-types/
scraped_at: 2025-09-08T15:41:29.004384
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

[Simple Data Types](https://developer.rhino3d.com/guides/grasshopper/simple-
data-types/)

  * Overview
  * Prerequisites
  * The IGH_Goo interface
    * IsValid
    * TypeName
    * TypeDescription
    * Duplicate
    * ToString
    * EmitProxy
    * CastTo
    * CastFrom
    * ScriptVariable
  * The GH_Goo abstract class
  * An Example Type
    * Constructors
    * Formatters
    * Serialization
    * Casting
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) /

Simple Data Types

by [David Rutten](https://discourse.mcneel.com/u/davidrutten/) (Last updated:
Wednesday, December 5, 2018)

## Overview

It’s a rather complicated topic as data is an integral part of the Grasshopper
process and GUI. Grasshopper needs to be able to (de)serialize data, display
data in tooltips, convert data to other types of data, prompt the user for
persistent data, draw geometry preview data in viewports and bake geometric
data. In this topic I’ll only talk about non-geometric data, we’ll get to
previews and baking in a later topic.

Practically all native data types in Grasshopper are based either on a .NET
Framework type or a RhinoCommon type. For example `System.Boolean`,
`System.String`, `Rhino.Geometry.Point3d` and `Rhino.Geometry.Brep` to name
but a few. However, the parameters in Grasshopper don’t directly store
Booleans, String, Points and Breps as these types can’t handle themselves in
the cauldron that is Grasshopper.

## Prerequisites

We will not be dealing with any of the basics of component development in this
guide. Please start with the [Your First
Component](https://developer.rhino3d.com/guides/grasshopper/your-first-
component-windows/) guide and the [Simple
Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)
guide before starting this one.

Before you start, create a new class that derives from
`Grasshopper.Kernel.GH_Component`, as outlined in the [Simple
Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)
guide.

## The IGH_Goo interface

In this section I’ll briefly discuss all the methods and properties that are
defined in IGH_Goo. What they’re for, who uses them at what time, etc, etc.

All data used in Grasshopper must implement the
[IGH_Goo](https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_IGH_Goo.htm)
interface. `IGH_Goo` defines the bare minimum of methods and properties for
any kind of data before it is allowed to play ball.

### IsValid

C# VB.NET

    
    
    bool IsValid { get{} }
    
    
    
    ReadOnly Property IsValid() As Boolean
    

Not all data types are valid all the time, and this property allows you to
test the current instance of your data. When data is invalid it will often be
ignored by components.

### TypeName

C# VB.NET

    
    
    string TypeName { get{} }
    
    
    
    ReadOnly Property TypeName() As String
    

This property must return a human-readable name for your data type.

### TypeDescription

C# VB.NET

    
    
    string TypeDescription { get{} }
    
    
    
    ReadOnly Property TypeDescription() As String
    

This property must return a human-readable description of your data type.

### Duplicate

C# VB.NET

    
    
    IGH_Goo Duplicate()
    
    
    
    Function Duplicate() As IGH_Goo
    

This function must return an exact duplicate of the data item. Data is
typically shared amongst multiple Grasshopper parameters, so before data is
changed, it first needs to copy itself. When data only contains ValueTypes and
Primitives, making a copy of an instance is usually quite easy.

### ToString

C# VB.NET

    
    
    string ToString()
    
    
    
    Function ToString() As String
    

This function is called whenever Grasshopper needs a human-readable version of
your data. It is this function that populates the data panel in parameter
tooltips. You don’t need to create a String that is parsable, it only needs to
be somewhat informative.

### EmitProxy

C# VB.NET

    
    
    IGH_GooProxy EmitProxy()
    
    
    
    Function EmitProxy() As IGH_GooProxy
    

Data proxies are used in the Data Collection Manager. You can ignore this
function (i.e. Return Nothing) without crippling your data type.

### CastTo

C# VB.NET

    
    
    bool CastTo<T>(out T target)
    
    
    
    Function CastTo(Of T)(ByRef target As T) As Boolean
    

Data Casting is a core feature of Grasshopper data. It basically allows data
types defined in Grasshopper add-ons to become an integral part of
Grasshopper. Lets assume that we have a Component that operates on data type
[A]. But instead of playing nice, we provide data of type [B]. Two conversion
(casting) attempts will be made in order to change [B] into [A]. If [B]
implements IGH_Goo, then it is asked if it knows how to convert itself into an
instance of [A]. Failing that, if [A] implements `IGH_Goo`, it is asked
whether or not it knows how to construct itself from an instance of [B].

The `CastTo()` function is responsible for step 1. The `CastTo()` method is a
generic method, meaning the types on which it operates are not defined until
the method is actually called. This allows the function to operate
“intelligently” on data types. It also unfortunately means you have to be
“intelligent” when implementing this function.

See the [Grasshopper Data
Types](https://developer.rhino3d.com/guides/grasshopper/grasshopper-data-
types/) guide for more information on conversion.

### CastFrom

C# VB.NET

    
    
    bool CastFrom(object source)
    
    
    
    Function CastFrom(ByVal source As Object) As Boolean
    

The `CastFrom()` function is responsible for step 2 of data casting. Some kind
of data is provided as a source object and if the local Type knows how to
“read” the source data it can perform the conversion.

See the [Grasshopper Data
Types](https://developer.rhino3d.com/guides/grasshopper/grasshopper-data-
types/) guide for more information on conversion.

### ScriptVariable

C# VB.NET

    
    
    object ScriptVariable()
    
    
    
    Function ScriptVariable() As Object
    

When data is fed into a VB or C# script component, it is usually stripped of
`IGH_Goo` specific data and methods. The `ScriptVariable()` method allows a
data type to provide a stripped down version of itself for use in a Script
component.

## The GH_Goo abstract class

Although all data in Grasshopper must implement the `IGH_Goo` interface, it is
not necessary to actually write a type from scratch. It is good practice to
inherit from the abstract class `GH_Goo<T>`, as it takes care of some of the
basic functionality. `GH_Goo` is a generic type (that’s what the “`<T>`” bit
means), where `T` is the actual type you’re wrapping. `GH_Goo<T>` has several
abstract methods and properties which _must_ be implemented, but a lot of the
other methods are already implemented with basic (though usually useless)
functionality.

## An Example Type

We’ll now create a very simple custom type. This will introduce the basic
concept of custom type development, without dealing with any of the baking and
previewing logic yet. Our custom type will be a TriState flag, similar to
boolean values but with an extra state called “Unknown”. We’ll represent these
different states using integers:

  * Negative One `-1` = Unknown
  * Zero `0` = False
  * One `1` = True

We’ll start with the general class layout, then drill down into each
individual function. Create a new public class called `TriStateType` and
inherit from `GH_Goo<Integer>`. Be sure to import the Grasshopper `Kernel` and
`Kernel.Types` namespaces as we’ll need them both:

C# VB.NET

    
    
    using Grasshopper.Kernel;
    using Grasshopper.Kernel.Types;
    
    namespace MyTypes
    {
      public class TriStateType : GH_Goo<int>
      {
    
      }
    }
    
    
    
    Imports Grasshopper.Kernel
    Imports Grasshopper.Kernel.Types
    
    Namespace MyTypes
      Public Class TriStateType
        Inherits GH_Goo(Of Integer)
    
      End Class
    End Namespace
    

### Constructors

Unless a constructor is defined, .NET classes always have a default
constructor which initializes all the fields of the class to their default
values. This constructor does not require any inputs and when you develop
custom types it is a good idea to always provide a default constructor. If
there is no default constructor, then class instances cannot be created
automatically which thwarts certain algorithms in Grasshopper.

In addition to a default constructor I also find it useful to supply so called
copy constructors which create a new instance of the type class with a preset
value.

C# VB.NET

    
    
    // Default Constructor, sets the state to Unknown.
    public TriStateType()
    {
      this.Value = -1;
    }
    
    // Constructor with initial value
    public TriStateType(int tristateValue)
    {
      this.Value = tristateValue;
    }
    
    // Copy Constructor
    public TriStateType(TriStateType tristateSource)
    {
      this.Value = tristateSource.Value;
    }
    
    // Duplication method (technically not a constructor)
    public override IGH_Goo Duplicate()
    {
      return new TriStateType(this);
    }
    
    
    
    '' Default Constructor, sets the state to Unknown.
    Public Sub New()
      Me.Value = -1
    End Sub
    
    '' Constructor with initial value
    Public Sub New(ByVal tristateValue As Integer)
      Me.Value = tristateValue
    End Sub
    
    '' Copy Constructor
    Public Sub New(ByVal tristateSource As TriStateType)
      Value = tristateSource.Value
    End Sub
    
    '' Duplication method (technically not a constructor)
    Public Overrides Function Duplicate() As Kernel.Types.IGH_Goo
      Return New TriStateType(Me)
    End Function
    

Incidentally, the Value property which we are using to assign integers to our
local instance is provided by the `GH_Goo<T>` base class. `GH_Goo<T>` defines
a protected field of type `T` called `m_value` and also a public accessor
property called `Value` which gets or sets the `m_value` field.

In this particular case, it actually makes sense to override the default
`Value` property implementation, as the number of sensible values we can
assign (-1, 0 and +1) is a subset of the total number values available through
the Integer data type. It makes no sense to assign -62 for example. We _could_
of course agree that all negative values indicate an “Unknown” state, but we
should try to restrict ourselves to only three integer values:

C# VB.NET

    
    
    // Override the Value property to strip non-sensical states.
    public override int Value
    {
      get { return base.Value; }
      set
      {
        if (value < -1) { value = -1; }
        if (value > +1) { value = +1; }
        base.Value = value;
      }
    }
    
    
    
    '' Override the Value property to strip non-sensical states.
    Public Overrides Property Value() As Integer
      Get
        Return MyBase.Value
      End Get
      Set(ByVal value As Integer)
        If (value < -1) Then value = -1
        If (value > +1) Then value = +1
        MyBase.Value = value
      End Set
    End Property
    

### Formatters

Formatting data is primarily a User Interface task. Both the data type and the
data state need to be presented in human-readable form every now and again.
This mostly involves readonly properties as looking at data does not change
its state:

C# VB.NET

    
    
    // TriState instances are always valid
    public override bool IsValid
    {
      get { return true; }
    }
    
    // Return a string with the name of this Type.
    public override string TypeName
    {
      get { return "TriState"; }
    }
    
    // Return a string describing what this Type is about.
    public override string TypeDescription
    {
      get { return "A TriState Value (True, False or Unknown)"; }
    }
    
    // Return a string representation of the state (value) of this instance.
    public override string ToString()
    {
      if (this.Value == 0) { return "False"; }
      if (this.Value > 0) { return "True"; }
      return "Unknown";
    }
    
    
    
    '' TriState instances are always valid
    Public Overrides ReadOnly Property IsValid() As Boolean
      Get
        Return True
      End Get
    End Property
    
    '' Return a string with the name of this Type.
    Public Overrides ReadOnly Property TypeName() As String
      Get
        Return "TriState"
      End Get
    End Property
    
    '' Return a string describing what this Type is about.
    Public Overrides ReadOnly Property TypeDescription() As String
      Get
        Return "A TriState Value (True, False or Unknown)"
      End Get
    End Property
    
    '' Return a string representation of the state (value) of this instance.
    Public Overrides Function ToString() As String
      If (Value = 0) Then Return "False"
      If (Value > 0) Then Return "True"
      Return "Unknown"
    End Function
    

### Serialization

Some data types can be stored as _persistent data_. Persistent data must be
able to serialize and deserialize itself from a Grasshopper file. Most simple
types support this feature (Booleans, Integers, Strings, Colours, Circles,
Planes etc.), most complex geometry types cannot be stored as persistent data
(Curves, Breps, Meshes). If possible, you should aim to provide robust
(de)serialization for your data:

C# VB.NET

    
    
    // Serialize this instance to a Grasshopper writer object.
    public override bool Write(GH_IO.Serialization.GH_IWriter writer)
    {
      writer.SetInt32("tri", this.Value);
      return true;
    }
    
    // Deserialize this instance from a Grasshopper reader object.
    public override bool Read(GH_IO.Serialization.GH_IReader reader)
    {
      this.Value = reader.GetInt32("tri");
      return true;
    }
    
    
    
    '' Serialize this instance to a Grasshopper writer object.
    Public Overrides Function Write(ByVal writer As GH_IO.Serialization.GH_IWriter) As Boolean
      writer.SetInt32("tri", Value)
      Return True
    End Function
    
    '' Deserialize this instance from a Grasshopper reader object.
    Public Overrides Function Read(ByVal reader As GH_IO.Serialization.GH_IReader) As Boolean
      Value = reader.GetInt32("tri")
      Return True
    End Function
    

### Casting

There are three casting methods on `IGH_Goo`; the `CastFrom()` and `CastTo()`
methods that facilitate conversions between different types of data and the
`ScriptVariable()` method which creates a safe instance of this data to be
used inside untrusted code (such as VB or C# Script components).

C# VB.NET

    
    
    // Return the Integer we use to represent the TriState flag.
    public override object ScriptVariable()
    {
      return this.Value;
    }
    
    // This function is called when Grasshopper needs to convert this
    // instance of TriStateType into some other type Q.
    public override bool CastTo<Q>(ref Q target)
    {
      //First, see if Q is similar to the Integer primitive.
      if (typeof(Q).IsAssignableFrom(typeof(int)))
      {
        object ptr = this.Value;
        target = (Q)ptr;
        return true;
      }
    
      //Then, see if Q is similar to the GH_Integer type.
      if (typeof(Q).IsAssignableFrom(typeof(GH_Integer)))
      {
        object ptr = new GH_Integer(this.Value);
        target = (Q)ptr;
        return true;
      }
    
      //We could choose to also handle casts to Boolean, GH_Boolean,
      //Double and GH_Number, but this is left as an exercise for the reader.
      return false;
    }
    
    // This function is called when Grasshopper needs to convert other data
    // into TriStateType.
    public override bool CastFrom(object source)
    {
      //Abort immediately on bogus data.
      if (source == null) { return false; }
    
      //Use the Grasshopper Integer converter. By specifying GH_Conversion.Both
      //we will get both exact and fuzzy results. You should always try to use the
      //methods available through GH_Convert as they are extensive and consistent.
      int val;
      if (GH_Convert.ToInt32(source, out val, GH_Conversion.Both))
      {
        this.Value = val;
        return true;
      }
    
      //If the integer conversion failed, we can still try to parse Strings.
      //If possible, you should ensure that your data type can 'deserialize' itself
      //from the output of the ToString() method.
      string str = null;
      if (GH_Convert.ToString(source, out str, GH_Conversion.Both))
      {
        switch (str.ToUpperInvariant())
        {
          case "FALSE":
          case "F":
          case "NO":
          case "N":
            this.Value = 0;
            return true;
    
          case "TRUE":
          case "T":
          case "YES":
          case "Y":
            this.Value = +1;
            return true;
    
          case "UNKNOWN":
          case "UNSET":
          case "MAYBE":
          case "DUNNO":
          case "?":
            this.Value = -1;
            return true;
        }
      }
    
      //We've exhausted the possible conversions, it seems that source
      //cannot be converted into a TriStateType after all.
      return false;
    }
    
    
    
    '' Return the Integer we use to represent the TriState flag.
    Public Overrides Function ScriptVariable() As Object
      Return Value
    End Function
    
    '' This function is called when Grasshopper needs to convert this
    '' instance of TriStateType into some other type Q.
    Public Overrides Function CastTo(Of Q)(ByRef target As Q) As Boolean
      'First, see if Q is similar to the Integer primitive.
      If (GetType(Q).IsAssignableFrom(GetType(Integer))) Then
        Dim ptr As Object = Value
        target = DirectCast(ptr, Q)
        Return True
      End If
    
      'Then, see if Q is similar to the GH_Integer type.
      If (GetType(Q).IsAssignableFrom(GetType(GH_Integer))) Then
        Dim int As Object = New GH_Integer(Value)
        target = DirectCast(int, Q)
        Return True
      End If
    
      'We could choose to also handle casts to Boolean, GH_Boolean,
      'Double and GH_Number, but this is left as an exercise for the reader.
      Return False
    End Function
    
    '' This function is called when Grasshopper needs to convert other data
    '' into TriStateType.
    Public Overrides Function CastFrom(ByVal source As Object) As Boolean
      'Abort immediately on bogus data.
      If (source Is Nothing) Then Return False
    
      'Use the Grasshopper Integer converter. By specifying GH_Conversion.Both
      'we will get both exact and fuzzy results. You should always try to use the
      'methods available through GH_Convert as they are extensive and consistent.
      Dim int As Integer
      If (GH_Convert.ToInt32(source, int, GH_Conversion.Both)) Then
        Value = int
        Return True
      End If
    
      'If the integer conversion failed, we can still try to parse Strings.
      'If possible, you should ensure that your data type can 'deserialize' itself
      'from the output of the ToString() method.
      Dim str As String = Nothing
      If (GH_Convert.ToString(source, str, GH_Conversion.Both)) Then
        Select Case str.ToUpperInvariant()
          Case "FALSE", "F", "NO", "N"
            Value = 0
            Return True
          Case "TRUE", "T", "YES", "Y"
            Value = +1
            Return True
          Case "UNKNOWN", "UNSET", "MAYBE", "DUNNO", "?"
            Value = -1
            Return True
        End Select
      End If
    
      'We've exhausted the possible conversions, it seems that source
      'cannot be converted into a TriStateType after all.
      Return False
    End Function
    

## Related Topics

  * [Grasshopper Data Types](https://developer.rhino3d.com/guides/grasshopper/grasshopper-data-types/)
  * [Simple Component](https://developer.rhino3d.com/guides/grasshopper/simple-component/)
  * [Simple Parameters](https://developer.rhino3d.com/guides/grasshopper/simple-parameters/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/simple-
data-types/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/simple-
data-types/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

