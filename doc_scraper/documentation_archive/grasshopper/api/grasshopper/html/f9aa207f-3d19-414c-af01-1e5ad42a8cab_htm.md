---
url: https://developer.rhino3d.com/api/grasshopper/html/f9aa207f-3d19-414c-af01-1e5ad42a8cab.htm
scraped_at: 2025-09-08T16:10:26.785774
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Examples](../html/d113a9f0-6e27-46df-8316-2079c44382ac.htm "Examples")

[Visual Basic .NET](../html/b883d0c0-4947-48bc-8e9e-492a6d6c2a06.htm "Visual
Basic .NET")

[Simple Component (VB)](../html/b883d0c0-4947-48bc-8e9e-492a6d6c2a06.htm
"Simple Component \(VB\)")

[Simple Mathematics (VB)](../html/2824c770-2673-49a3-8683-1a70bc0349cc.htm
"Simple Mathematics \(VB\)")

[Simple Geometry (VB)](../html/4306b177-1bf1-41bc-ac0e-2f6869d02365.htm
"Simple Geometry \(VB\)")

[Simple Data Types (VB)](../html/f9aa207f-3d19-414c-af01-1e5ad42a8cab.htm
"Simple Data Types \(VB\)")

[Simple Parameters (VB)](../html/0edd8dc9-32a7-40aa-b217-8e01e35e58bc.htm
"Simple Parameters \(VB\)")

[List Component (VB)](../html/4db493ec-0bb3-4b73-943a-fdff03863e1d.htm "List
Component \(VB\)")

[Extending the GUI (VB)](../html/99cd32c8-7c1f-4f9a-87ea-76b032de7f70.htm
"Extending the GUI \(VB\)")

[Custom Attributes (VB)](../html/ad6e93fe-e1c8-451e-a6d0-77cb8dd4516d.htm
"Custom Attributes \(VB\)")

[Custom Component Options
(VB)](../html/434018c0-6110-4478-bf2a-dcd099d8b8b2.htm "Custom Component
Options \(VB\)")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# Simple Data Types (VB)  
  
---  
  
  * Introduction
  * The IGH_Goo interface
  * The GH_Goo abstract class
  * An Example Type
    * Constructors
    * Formatters
    * Serialization
    * Casting

This article discusses how Grasshopper deals with data items and types. It's a
rather complicated topic as data is an integral part of the Grasshopper
process and GUI. Grasshopper needs to be able to (de)serialize data, display
data in tooltips, convert data to other types of data, prompt the user for
persistent data, draw geometry preview data in viewports and bake geometric
data. In this topic I'll only talk about non-geometric data, we'll get to
previews and baking in a later topic.

Practically all native data types in Grasshopper are based either on a .NET
Framework type or a RhinoCommon SDK type. For example System.Boolean,
System.String, Rhino.Geometry.Point3d and Rhino.Geometry.Brep to name but a
few. However the parameters in Grasshopper don't directly store Booleans,
String, Points and Breps as these types can't handle themselves in the
cauldron that is Grasshopper.

All data used in Grasshopper _must_ implement the
[IGH_Goo](T_Grasshopper_Kernel_Types_IGH_Goo.htm) interface. IGH_Goo defines
the bare minimum of methods and properties for any kind of data before it is
allowed to play ball.

![](../icons/SectionExpanded.png)The IGH_Goo interface

In this section I'll briefly discuss all the methods and properties that are
defined in IGH_Goo. What they're for, who uses them at what time, etc, etc.

Method| Purpose  
---|---  
VBCopy

    
    
    ReadOnly Property IsValid() As Boolean

|  Not all data types are valid all the time, and this property allows you to
teint the current instance of your data. When data is invalid it will often be
ignored by components.  
VBCopy

    
    
    ReadOnly Property TypeName() As String

|  This property must return a human-readable name for your data type.  
VBCopy

    
    
    ReadOnly Property TypeDescription() As String

|  This property must return a human-readable description of your data type.  
VBCopy

    
    
    Function Duplicate() As IGH_Goo

|  This function must return an exact duplicate of the data item. Data is
typically shared amongst multiple Grasshopper Parameters, so before data is
changed, it first needs to copy itself. When data only contains ValueTypes and
Primitives, making a copy of an instance is usually quite easy.  
VBCopy

    
    
    Function ToString() As String

|  This function is called whenever Grasshopper needs a human-readable version
of your data. It is this function that populates the data panel in parameter
tooltips. You don't need to create a String that is parsable, it only needs to
be somewhat informative.  
VBCopy

    
    
    Function EmitProxy() As IGH_GooProxy

|  Data proxies are used in the Data Collection Manager. You can ignore this
function (i.e. Return Nothing) without crippling your data type.  
VBCopy

    
    
    Function CastTo(Of T)(ByRef target As T) As Boolean

|  Data Casting is a core feature of Grasshopper data. It basically allows
data types defined in Grasshopper add-ons to become an integral part of
Grasshopper. Lets assume that we have a component that operates on data type
[A]. But instead of playing nice, we provide data of type [B]. Two conversion
(casting) attempts will be made in order to change [B] into [A]. If [B]
implements IGH_Goo, then it is asked if it knows how to convert itself into an
instance of [A]. Failing that, if [A] implements IGH_Goo, it is asked whether
or not it knows how to construct itself from an instance of [B].  The CastTo()
function is responsible for step 1. The CastTo() method is a generic method,
meaning the types on which it operates are not defined until the method is
actually called. This allows the function to operate 'intelligently' on data
types. It also unfortunately means you have to be 'intelligent' when
implementing this function.  
VBCopy

    
    
    Function CastFrom(ByVal source As Object) As Boolean

|  The CastFrom() method is responsible for step 2 of data casting. Some kind
of data is provided as a source object and if the local Type knows how to
'read' the source data it can perform the conversion.  
VBCopy

    
    
    Function ScriptVariable() As Object

|  When data is fed into a VB or C# script component, it is usually stripped
of IGH_Goo specific data and methods. The ScriptVariable() method allows a
data type to provide a stripped down version of itself for use in a Script
component.  
  
![](../icons/SectionExpanded.png)The GH_Goo abstract class

Although all data in Grasshopper must implement the IGH_Goo interface, it is
not necessary to actually write a type from scratch. It is good practice to
inherit from the abstract (MustInherit) class GH_Goo(Of T), as it takes care
of some of the basic functionality. GH_Goo is a generic type (that's what the
"(Of T)" bit means), where T is the actual type you're wrapping. GH_Goo(Of T)
has several MustOverride methods and properties which _must_ be implemented,
but a lot of the other methods are already implemented with basic (though
usually useless) functionality.

![](../icons/SectionExpanded.png)An Example Type

We'll now create a very simple Custom Type. This will introduce the basic
concept of custom type development, without dealing with any of the baking and
previewing logic yet. Our custom type will be a TriState flag, similar to
boolean values but with an extra state called "Unknown". We'll represent these
different states using integers:

Integer| TriState  
---|---  
Negative One| Unknown  
Zero| False  
Positive One| True  
  
We'll start with the general class layout, then drill down into each
individual function. Create a new public class called TriStateType and inherit
from GH_Goo(Of Integer). Be sure to import the Grasshopper Kernel and
Kernel.Types namespaces as we'll need them both:

VB

Copy

    
    
    Imports Grasshopper.Kernel
    Imports Grasshopper.Kernel.Types
    
    Namespace MyTypes
      Public Class TriStateType
        Inherits GH_Goo(Of Integer)
    
      End Class
    End Namespace

#### Constructors

Unless a constructor is defined, .NET classes always have a _default
constructor_ which initializes all the fields of the class to their default
values. This constructor does not require any inputs and when you develop
custom types it is a good idea to always provide a default constructor. If
there is no default constructor, then class instances cannot be created
automatically which thwarts certain algorithms in Grasshopper.

In addition to a default constructor I also find it useful to supply so called
_copy constructors_ which create a new instance of the Type class with a
preset value.

VB

Copy

    
    
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
local instance is provided by the GH_Goo(Of T) base class. GH_Goo(Of T)
defines a protected field of type T called m_value and also a public accessor
property called Value which gets or sets the m_value field.

In this particular case, it actually makes sense to override the default Value
property implementation, as the number of sensible values we can assign (-1, 0
and +1) is a subset of the total number values available through the integer
data type. It makes no sense to assign -62 for example. We _could_ of course
agree that all negative values indicate an "Unknown" state, but we should try
to restrict ourselves to only three integer values:

VB

Copy

    
    
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

#### Formatters

Formatting data is primarily a User Interface task. Both the data type and the
data state need to be presented in human-readable form every now and again.
This mostly involves readonly properties as looking at data does not change
its state:

VB

Copy

    
    
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

#### Serialization

Some data types can be stored as _persistent data_. Persistent data must be
able to serialize and deserialize itself from a Grasshopper file. Most simple
types support this feature (Booleans, Integers, Strings, Colours, Circles,
Planes etc.), most complex geometry types cannot be stored as persistent data
(Curves, Breps, Meshes). If possible, you should aim to provide robust
(de)serialization for your data:

VB

Copy

    
    
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

#### Casting

There are three casting methods on IGH_Goo; the CastFrom() and CastTo()
methods that facilitate conversions between different types of data and the
ScriptVariable() method which creates a safe instance of this data to be used
inside untrusted code (such as VB or C# Script components).

VB

Copy

    
    
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

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

