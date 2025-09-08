---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Documentation_GH_Link.htm
scraped_at: 2025-09-08T16:11:58.137685
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm
"Grasshopper.Documentation")

[GH_Link Class](../html/T_Grasshopper_Documentation_GH_Link.htm "GH_Link
Class")

[GH_Link
Properties](../html/Properties_T_Grasshopper_Documentation_GH_Link.htm
"GH_Link Properties")

[GH_Link Methods](../html/Methods_T_Grasshopper_Documentation_GH_Link.htm
"GH_Link Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Link Class  
  
---  
  
Represents a link to another location in the Help or some external address.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.DocumentationGH_Link  

**Namespace:** [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Link : IGH_Content
    
    
    Public Class GH_Link
    	Implements IGH_Content

The GH_Link type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Destination](P_Grasshopper_Documentation_GH_Link_Destination.htm)|  Gets the
link target.  
![Public property](../icons/pubproperty.gif)|
[IsSharedLink](P_Grasshopper_Documentation_GH_Link_IsSharedLink.htm)|  Gets
whether this link is a shared link. A shared link should not have text but it
should have a non-empty LinkId.  
![Public property](../icons/pubproperty.gif)|
[LinkId](P_Grasshopper_Documentation_GH_Link_LinkId.htm)|  Gets the link ID.
The link ID is only used for shared links.  
![Public property](../icons/pubproperty.gif)|
[Target](P_Grasshopper_Documentation_GH_Link_Target.htm)|  Gets the link type.  
![Public property](../icons/pubproperty.gif)|
[Text](P_Grasshopper_Documentation_GH_Link_Text.htm)|  Gets the list text.  
![Public property](../icons/pubproperty.gif)|
[Tooltip](P_Grasshopper_Documentation_GH_Link_Tooltip.htm)|  Gets the link
tooltip text.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateExternalLink(String,
String)](M_Grasshopper_Documentation_GH_Link_CreateExternalLink.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateExternalLink(String, String,
String)](M_Grasshopper_Documentation_GH_Link_CreateExternalLink_1.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateGlossaryLink(String)](M_Grasshopper_Documentation_GH_Link_CreateGlossaryLink.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateGlossaryLink(String,
String)](M_Grasshopper_Documentation_GH_Link_CreateGlossaryLink_1.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateSharedLink(String,
String)](M_Grasshopper_Documentation_GH_Link_CreateSharedLink.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateSharedLink(String, String,
String)](M_Grasshopper_Documentation_GH_Link_CreateSharedLink_1.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTopicLink(String,
String)](M_Grasshopper_Documentation_GH_Link_CreateTopicLink.htm)|  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[CreateTopicLink(String, String,
String)](M_Grasshopper_Documentation_GH_Link_CreateTopicLink_1.htm)|  
![Public method](../icons/pubmethod.gif)|
[ToString](M_Grasshopper_Documentation_GH_Link_ToString.htm)|  (Overrides
[ObjectToString](https://docs.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring).)  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

