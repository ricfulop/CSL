---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_Goo_1.htm
scraped_at: 2025-09-08T16:20:43.413485
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_Goo(T) Class](../html/T_Grasshopper_Kernel_Types_GH_Goo_1.htm "GH_Goo\(T\)
Class")

[GH_Goo(T) Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_Goo_1__ctor.htm "GH_Goo\(T\)
Constructor ")

[GH_Goo(T)
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_Goo_1.htm
"GH_Goo\(T\) Properties")

[GH_Goo(T) Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_Goo_1.htm
"GH_Goo\(T\) Methods")

[GH_Goo(T) Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_Goo_1.htm
"GH_Goo\(T\) Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_GooT Class  
  
---  
  
Base class for IGH_Goo implementation. Takes care of some default behaviour.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_GooT  
More...

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_Goo<T> : IGH_Goo
    
    
    
    Public MustInherit Class GH_Goo(Of T)
    	Implements IGH_Goo

#### Type Parameters

T

    

The GH_GooT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_GooT](M_Grasshopper_Kernel_Types_GH_Goo_1__ctor.htm)|  Blank constructor,
m_value will be set to default (null for reference types, zeroes for value
types)  
![Protected method](../icons/protmethod.gif)|
[GH_GooT(T)](M_Grasshopper_Kernel_Types_GH_Goo_1__ctor_2.htm)|  Data
constructor, m_value will be set to internal_data.  
![Protected method](../icons/protmethod.gif)|
[GH_GooT(GH_GooT)](M_Grasshopper_Kernel_Types_GH_Goo_1__ctor_1.htm)|  Copy
constructor, copies the data from another GH_Goo(Of T) instance. Reference
types will not be duplicated.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm)|  Gets a value
indicating whether or not the current value is valid.  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm)|
Gets a description of the type of the implementation.  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm)|  Gets the name
of the type of the implementation.  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm)|  Gets or sets the
internal data.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm)|  Attempt a cast
from generic data.  
![Public method](../icons/pubmethod.gif)|
[CastToQ](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a cast
to type Q.  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm)|  Make a
complete duplicate of this instance. No shallow copies.  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm)|  Create a new
proxy for this instance. Return Null if this class does not support proxies.  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm)|  Default behaviour is to
return True.  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disappears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm)|  Creates a
string description of the current instance value.  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm)|  Default behaviour is
to return True.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm)|  
Top

![](../icons/SectionExpanded.png)Remarks

Feel free to implement IGH_Goo directly though.

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.Kernel.TypesGH_GooT  
[Grasshopper.Kernel.TypesGH_Boolean](T_Grasshopper_Kernel_Types_GH_Boolean.htm)  
[Grasshopper.Kernel.TypesGH_Colour](T_Grasshopper_Kernel_Types_GH_Colour.htm)  
[Grasshopper.Kernel.TypesGH_ComplexNumber](T_Grasshopper_Kernel_Types_GH_ComplexNumber.htm)  
[Grasshopper.Kernel.TypesGH_Culture](T_Grasshopper_Kernel_Types_GH_Culture.htm)  
[Grasshopper.Kernel.TypesGH_GeometricGooT](T_Grasshopper_Kernel_Types_GH_GeometricGoo_1.htm)  
[Grasshopper.Kernel.TypesGH_Guid](T_Grasshopper_Kernel_Types_GH_Guid.htm)  
[Grasshopper.Kernel.TypesGH_Integer](T_Grasshopper_Kernel_Types_GH_Integer.htm)  
[Grasshopper.Kernel.TypesGH_Interval](T_Grasshopper_Kernel_Types_GH_Interval.htm)  
[Grasshopper.Kernel.TypesGH_Interval2D](T_Grasshopper_Kernel_Types_GH_Interval2D.htm)  
[Grasshopper.Kernel.TypesGH_Material](T_Grasshopper_Kernel_Types_GH_Material.htm)  
[Grasshopper.Kernel.TypesGH_Matrix](T_Grasshopper_Kernel_Types_GH_Matrix.htm)  
[Grasshopper.Kernel.TypesGH_MeshFace](T_Grasshopper_Kernel_Types_GH_MeshFace.htm)  
[Grasshopper.Kernel.TypesGH_MeshingParameters](T_Grasshopper_Kernel_Types_GH_MeshingParameters.htm)  
[Grasshopper.Kernel.TypesGH_Number](T_Grasshopper_Kernel_Types_GH_Number.htm)  
[Grasshopper.Kernel.TypesGH_ObjectWrapper](T_Grasshopper_Kernel_Types_GH_ObjectWrapper.htm)  
[Grasshopper.Kernel.TypesGH_String](T_Grasshopper_Kernel_Types_GH_String.htm)  
[Grasshopper.Kernel.TypesGH_StructurePath](T_Grasshopper_Kernel_Types_GH_StructurePath.htm)  
[Grasshopper.Kernel.TypesGH_Time](T_Grasshopper_Kernel_Types_GH_Time.htm)  
[Grasshopper.Kernel.TypesGH_Transform](T_Grasshopper_Kernel_Types_GH_Transform.htm)  
[Grasshopper.Kernel.TypesGH_Vector](T_Grasshopper_Kernel_Types_GH_Vector.htm)  
[Grasshopper.Rhinoceros.DisplayDisplayColorGradient](T_Grasshopper_Rhinoceros_Display_DisplayColorGradient.htm)  
[Grasshopper.Rhinoceros.DisplayDisplayColorStop](T_Grasshopper_Rhinoceros_Display_DisplayColorStop.htm)  
[Grasshopper.RhinocerosModelFont](T_Grasshopper_Rhinoceros_ModelFont.htm)  

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

