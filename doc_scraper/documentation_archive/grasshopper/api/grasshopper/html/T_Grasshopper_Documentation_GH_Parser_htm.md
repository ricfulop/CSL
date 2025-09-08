---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Documentation_GH_Parser.htm
scraped_at: 2025-09-08T16:12:01.161570
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm
"Grasshopper.Documentation")

[GH_Parser Class](../html/T_Grasshopper_Documentation_GH_Parser.htm "GH_Parser
Class")

[GH_Parser
Properties](../html/Properties_T_Grasshopper_Documentation_GH_Parser.htm
"GH_Parser Properties")

[GH_Parser Methods](../html/Methods_T_Grasshopper_Documentation_GH_Parser.htm
"GH_Parser Methods")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_Parser Class  
  
---  
  
Provides parsing methods for the Grasshopper Markdown flavour.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.DocumentationGH_Parser  

**Namespace:** [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_Parser
    
    
    Public Class GH_Parser

The GH_Parser type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Whitespace](P_Grasshopper_Documentation_GH_Parser_Whitespace.htm)|  Gets an
array of characters that are considered to be whitespace. At the moment, this
array contains the space char and the tab char, it does not contain feeds or
breaks.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsChapterHeaderLine](M_Grasshopper_Documentation_GH_Parser_IsChapterHeaderLine.htm)|
Test whether a line represents a chapter header underline. Chapter header
underlines contain at least 4 consecutive equals symbols preceded or followed
by any amount of white space.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsCommentLine](M_Grasshopper_Documentation_GH_Parser_IsCommentLine.htm)|
Test whether a line is a comment. Commented lines begin with double slashes
(//) and are ignored during parsing.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsLinkLine(String)](M_Grasshopper_Documentation_GH_Parser_IsLinkLine.htm)|
Test whether a line represents a referenced link target. Note; this is a quick
check. The link might still be invalid, use the IsLinkLine overload to include
validity checks.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsLinkLine(String, String, String,
String)](M_Grasshopper_Documentation_GH_Parser_IsLinkLine_1.htm)|  Test
whether a line represents a referenced link target.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsListLine](M_Grasshopper_Documentation_GH_Parser_IsListLine.htm)|  Test
whether a line contains a list item.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsParagraphHeaderLine](M_Grasshopper_Documentation_GH_Parser_IsParagraphHeaderLine.htm)|
Test whether a line represents a paragraph header underline. Paragraph header
underlines contain at least 4 consecutive dashes preceded or followed by any
amount of white space.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsQuoteLine](M_Grasshopper_Documentation_GH_Parser_IsQuoteLine.htm)|  Test
whether a line is a block quote line. Block quotes start with a larger than
symbol.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[StringToFragment](M_Grasshopper_Documentation_GH_Parser_StringToFragment.htm)|
Parse a block of text and return it as an interpreted IGH_Fragment.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

