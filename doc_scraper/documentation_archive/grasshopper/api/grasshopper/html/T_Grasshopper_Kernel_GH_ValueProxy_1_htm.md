---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Kernel_GH_ValueProxy_1.htm
scraped_at: 2025-09-08T16:18:10.758068
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Kernel](../html/N_Grasshopper_Kernel.htm "Grasshopper.Kernel")

[GH_ValueProxy(T) Class](../html/T_Grasshopper_Kernel_GH_ValueProxy_1.htm
"GH_ValueProxy\(T\) Class")

[GH_ValueProxy(T) Constructor
](../html/M_Grasshopper_Kernel_GH_ValueProxy_1__ctor.htm "GH_ValueProxy\(T\)
Constructor ")

[GH_ValueProxy(T)
Properties](../html/Properties_T_Grasshopper_Kernel_GH_ValueProxy_1.htm
"GH_ValueProxy\(T\) Properties")

[GH_ValueProxy(T)
Methods](../html/Methods_T_Grasshopper_Kernel_GH_ValueProxy_1.htm
"GH_ValueProxy\(T\) Methods")

[GH_ValueProxy(T)
Fields](../html/Fields_T_Grasshopper_Kernel_GH_ValueProxy_1.htm
"GH_ValueProxy\(T\) Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_ValueProxyT Class  
  
---  
  
Represents the abstract base implementation of the IGH_ValueProxy interface.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.KernelGH_ValueProxyT  

**Namespace:** [Grasshopper.Kernel](N_Grasshopper_Kernel.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public abstract class GH_ValueProxy<T> : IGH_ValueProxy
    
    
    
    Public MustInherit Class GH_ValueProxy(Of T)
    	Implements IGH_ValueProxy

#### Type Parameters

T

    The type of this implementation

The GH_ValueProxyT type exposes the following members.

![](../icons/SectionExpanded.png)Constructors

| Name| Description  
---|---|---  
![Protected method](../icons/protmethod.gif)|
[GH_ValueProxyT](M_Grasshopper_Kernel_GH_ValueProxy_1__ctor.htm)|  Default
constructor for the base class. All derived classes must call this
constructor.  
Top

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[IsValid](P_Grasshopper_Kernel_GH_ValueProxy_1_IsValid.htm)|  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[Duplicate](M_Grasshopper_Kernel_GH_ValueProxy_1_Duplicate.htm)|  
![Public method](../icons/pubmethod.gif)|
[Duplicate_T](M_Grasshopper_Kernel_GH_ValueProxy_1_Duplicate_T.htm)|  
![Public method](../icons/pubmethod.gif)|
[FromString](M_Grasshopper_Kernel_GH_ValueProxy_1_FromString.htm)|  Performs
the String->Value parsing. The default implementation always returns False.  
![Public method](../icons/pubmethod.gif)|
[MutateString](M_Grasshopper_Kernel_GH_ValueProxy_1_MutateString.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Kernel_GH_ValueProxy_1_ToString.htm)|  Performs a
default ToString operation on the local value. If the value is Nothing, an
empty String is returned.  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Protected field](../icons/protfield.gif)|
[m_IsStringProxy](F_Grasshopper_Kernel_GH_ValueProxy_1_m_IsStringProxy.htm)|  
![Protected field](../icons/protfield.gif)|
[m_Name](F_Grasshopper_Kernel_GH_ValueProxy_1_m_Name.htm)|  
![Protected field](../icons/protfield.gif)|
[m_UserString](F_Grasshopper_Kernel_GH_ValueProxy_1_m_UserString.htm)|  
![Protected field](../icons/protfield.gif)|
[m_Valid](F_Grasshopper_Kernel_GH_ValueProxy_1_m_Valid.htm)|  
![Protected field](../icons/protfield.gif)|
[m_Value](F_Grasshopper_Kernel_GH_ValueProxy_1_m_Value.htm)|  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Kernel Namespace](N_Grasshopper_Kernel.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

