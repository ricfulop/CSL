---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_Types_GH_String.htm
scraped_at: 2025-09-08T16:21:29.618264
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel.Types](../html/N_Grasshopper_Kernel_Types.htm
"Grasshopper.Kernel.Types")

[GH_String Class](../html/T_Grasshopper_Kernel_Types_GH_String.htm "GH_String
Class")

[GH_String Constructor
](../html/Overload_Grasshopper_Kernel_Types_GH_String__ctor.htm "GH_String
Constructor ")

[GH_String
Properties](../html/Properties_T_Grasshopper_Kernel_Types_GH_String.htm
"GH_String Properties")

[GH_String Methods](../html/Methods_T_Grasshopper_Kernel_Types_GH_String.htm
"GH_String Methods")

[GH_String Fields](../html/Fields_T_Grasshopper_Kernel_Types_GH_String.htm
"GH_String Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_String Class  
  
---  
  
Represents a literal string. GH_String re-implements the framework
System.String type.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
[Grasshopper.Kernel.TypesGH_Goo](T_Grasshopper_Kernel_Types_GH_Goo_1.htm)[String](https://docs.microsoft.com/dotnet/api/system.string)  
Grasshopper.Kernel.TypesGH_String  
[Grasshopper.Rhinoceros.AnnotationsAnnotationDateTimeFormat](T_Grasshopper_Rhinoceros_Annotations_AnnotationDateTimeFormat.htm)  

**Namespace:** [Grasshopper.Kernel.Types](N_Grasshopper_Kernel_Types.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_String : GH_Goo<string>
    
    
    Public Class GH_String
    	Inherits GH_Goo(Of String)

The GH_String type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[GH_String](M_Grasshopper_Kernel_Types_GH_String__ctor.htm)|  Blank
constructor  
![Public method](../icons/pubmethod.gif)|
[GH_String(GH_String)](M_Grasshopper_Kernel_Types_GH_String__ctor_1.htm)|
Initializes a new instance of the GH_String class  
![Public method](../icons/pubmethod.gif)|
[GH_String(String)](M_Grasshopper_Kernel_Types_GH_String__ctor_2.htm)|
Initializes a new instance of the GH_String class  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_Types_GH_String_IsValid.htm)|  Gets the
validity of this instance. String are valid if they are not null.  (Overrides
[GH_GooTIsValid](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValid.htm).)  
![Public property](../icons/pubproperty.gif)|
[IsValidWhyNot](P_Grasshopper_Kernel_Types_GH_String_IsValidWhyNot.htm)|  Gets
a string describing the state of "invalidness". If the instance _is_ valid,
then this property should return Nothing or String.Empty.  (Overrides
[GH_GooTIsValidWhyNot](P_Grasshopper_Kernel_Types_GH_Goo_1_IsValidWhyNot.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeDescription](P_Grasshopper_Kernel_Types_GH_String_TypeDescription.htm)|
(Overrides
[GH_GooTTypeDescription](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeDescription.htm).)  
![Public property](../icons/pubproperty.gif)|
[TypeName](P_Grasshopper_Kernel_Types_GH_String_TypeName.htm)|  (Overrides
[GH_GooTTypeName](P_Grasshopper_Kernel_Types_GH_Goo_1_TypeName.htm).)  
![Public property](../icons/pubproperty.gif)|
[Value](P_Grasshopper_Kernel_Types_GH_Goo_1_Value.htm)|  Gets or sets the
internal data.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[CastFrom](M_Grasshopper_Kernel_Types_GH_String_CastFrom.htm)|  (Overrides
[GH_GooTCastFrom(Object)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastFrom.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm)|  Attempt a
cast to type Q.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[CastToT(T)](M_Grasshopper_Kernel_Types_GH_String_CastTo__1.htm)|  (Overrides
[GH_GooTCastToQ(Q)](M_Grasshopper_Kernel_Types_GH_Goo_1_CastTo__1.htm).)  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_Types_GH_String_Duplicate.htm)|  (Overrides
[GH_GooTDuplicate](M_Grasshopper_Kernel_Types_GH_Goo_1_Duplicate.htm).)  
![Public method](../icons/pubmethod.gif)|
[DuplicateString](M_Grasshopper_Kernel_Types_GH_String_DuplicateString.htm)|  
![Public method](../icons/pubmethod.gif)|
[EmitProxy](M_Grasshopper_Kernel_Types_GH_String_EmitProxy.htm)|  (Overrides
[GH_GooTEmitProxy](M_Grasshopper_Kernel_Types_GH_Goo_1_EmitProxy.htm).)  
![Public method](../icons/pubmethod.gif)|
[Read](M_Grasshopper_Kernel_Types_GH_String_Read.htm)|  (Overrides
[GH_GooTRead(GH_IReader)](M_Grasshopper_Kernel_Types_GH_Goo_1_Read.htm).)  
![Public method](../icons/pubmethod.gif)|
[ScriptVariable](M_Grasshopper_Kernel_Types_GH_Goo_1_ScriptVariable.htm)|
This function will be called when the local IGH_Goo instance disappears into a
user Script. This would be an excellent place to cast your IGH_Goo type to a
simple data type.  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_Types_GH_String_ToString.htm)|  (Overrides
[GH_GooTToString](M_Grasshopper_Kernel_Types_GH_Goo_1_ToString.htm).)  
![Public method](../icons/pubmethod.gif)|
[Write](M_Grasshopper_Kernel_Types_GH_String_Write.htm)|  (Overrides
[GH_GooTWrite(GH_IWriter)](M_Grasshopper_Kernel_Types_GH_Goo_1_Write.htm).)  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_value](F_Grasshopper_Kernel_Types_GH_Goo_1_m_value.htm)|  (Inherited from
[GH_GooT](T_Grasshopper_Kernel_Types_GH_Goo_1.htm).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel.Types Namespace](N_Grasshopper_Kernel_Types.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

