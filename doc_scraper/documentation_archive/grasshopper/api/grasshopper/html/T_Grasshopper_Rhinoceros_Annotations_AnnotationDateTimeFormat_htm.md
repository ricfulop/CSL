---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat.htm
scraped_at: 2025-09-08T16:22:51.958140
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Rhinoceros.Annotations](../html/N_Grasshopper_Rhinoceros_Annotations.htm
"Grasshopper.Rhinoceros.Annotations")

[AnnotationDateTimeFormat
Class](../html/T_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat.htm
"AnnotationDateTimeFormat Class")

[AnnotationDateTimeFormat Constructor
](../html/Overload_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat__ctor.htm
"AnnotationDateTimeFormat Constructor ")

[AnnotationDateTimeFormat
Properties](../html/Properties_T_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat.htm
"AnnotationDateTimeFormat Properties")

[AnnotationDateTimeFormat
Methods](../html/Methods_T_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat.htm
"AnnotationDateTimeFormat Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# AnnotationDateTimeFormat Class  
  
---  
  
Represents a Date Time format.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)[String](https://docs.microsoft.com/dotnet/api/system.string)  
[Grasshopper.Kernel.TypesGH_String](T_Grasshopper_Kernel_Types_GH_String.htm)  
Grasshopper.Rhinoceros.AnnotationsAnnotationDateTimeFormat  

**Namespace:**
[Grasshopper.Rhinoceros.Annotations](N_Grasshopper_Rhinoceros_Annotations.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public sealed class AnnotationDateTimeFormat : GH_String, 
    	IEquatable<AnnotationDateTimeFormat>
    
    
    Public NotInheritable Class AnnotationDateTimeFormat
    	Inherits GH_String
    	Implements IEquatable(Of AnnotationDateTimeFormat)

The AnnotationDateTimeFormat type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[AnnotationDateTimeFormat](M_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat__ctor.htm)|
Initializes a new instance of the AnnotationDateTimeFormat class  
![Public method](../icons/pubmethod.gif)|
[AnnotationDateTimeFormat(GH_String)](M_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat__ctor_1.htm)|
Initializes a new instance of the AnnotationDateTimeFormat class  
![Public method](../icons/pubmethod.gif)|
[AnnotationDateTimeFormat(String)](M_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat__ctor_2.htm)|
Initializes a new instance of the AnnotationDateTimeFormat class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[DisplayName](P_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat_DisplayName.htm)|  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_String_IsValid.htm)|  Gets the
validity of this instance. String are valid if they are not null.  (Inherited
from [GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_String_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  (Inherited from
[GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_String_TypeDescription.htm)|
(Inherited from [GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_String_TypeName.htm)|  (Inherited
from [GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm)|  Gets or sets the
internal data.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat_CastFrom.htm)|
(Overrides
[GH_StringCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_String_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_String_CastTo__1.htm)|  (Inherited
from [GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat_Duplicate.htm)|
(Overrides
[GH_StringDuplicate](M_Grasshopper_Kernel_Types_GH_String_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateString](M_Grasshopper_Kernel_Types_GH_String_DuplicateString.htm)|
(Inherited from [GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_String_EmitProxy.htm)|  (Inherited
from [GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
![Public method](../icons/pubmethod.gif)|
[Equals(AnnotationDateTimeFormat)](M_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat_Equals.htm)|  
![Public method](../icons/pubmethod.gif)|
[Equals(Object)](M_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat_Equals_1.htm)|
(Overrides
[ObjectEquals(Object)](https://docs.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)).)  
![Public method](../icons/pubmethod.gif)|
[GetHashCode](M_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat_GetHashCode.htm)|
(Overrides
[ObjectGetHashCode](https://docs.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_String_Read.htm)|  (Inherited from
[GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disappears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_String_ToString.htm)|  (Inherited
from [GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_String_Write.htm)|  (Inherited from
[GH_String](T_Grasshopper_Kernel_Types_GH_String.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Rhinoceros.Annotations
Namespace](N_Grasshopper_Rhinoceros_Annotations.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

