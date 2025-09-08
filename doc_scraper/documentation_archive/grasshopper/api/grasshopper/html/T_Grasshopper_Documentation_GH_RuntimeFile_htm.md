---
url: https://developer.rhino3d.com/api/grasshopper/html/T_Grasshopper_Documentation_GH_RuntimeFile.htm
scraped_at: 2025-09-08T16:12:02.157102
title: Untitled
---

Grasshopper API

[Grasshopper API](../html/723c01da-9986-4db2-8f53-6f3a7494df75.htm
"Grasshopper API")

[Grasshopper.Documentation](../html/N_Grasshopper_Documentation.htm
"Grasshopper.Documentation")

[GH_RuntimeFile Class](../html/T_Grasshopper_Documentation_GH_RuntimeFile.htm
"GH_RuntimeFile Class")

[GH_RuntimeFile
Properties](../html/Properties_T_Grasshopper_Documentation_GH_RuntimeFile.htm
"GH_RuntimeFile Properties")

[GH_RuntimeFile
Methods](../html/Methods_T_Grasshopper_Documentation_GH_RuntimeFile.htm
"GH_RuntimeFile Methods")

[GH_RuntimeFile
Fields](../html/Fields_T_Grasshopper_Documentation_GH_RuntimeFile.htm
"GH_RuntimeFile Fields")

![Click or drag to resize](../icons/TocOpen.gif)![Click or drag to
resize](../icons/TocClose.gif)

# GH_RuntimeFile Class  
  
---  
  
Runtime representation of a Grasshopper help file. A GH_RuntimeFile is nothing
more than a collection of keywords with associated content. This class does
not interpret a file or check its validity, it merely figures out the
different content section based on "Keyword:" entries.

![](../icons/SectionExpanded.png)Inheritance Hierarchy

[SystemObject](https://docs.microsoft.com/dotnet/api/system.object)  
Grasshopper.DocumentationGH_RuntimeFile  

**Namespace:** [Grasshopper.Documentation](N_Grasshopper_Documentation.htm)  
**Assembly:** Grasshopper (in Grasshopper.dll)

![](../icons/SectionExpanded.png)Syntax

C#

VB

Copy

    
    
    public class GH_RuntimeFile
    
    
    Public Class GH_RuntimeFile

The GH_RuntimeFile type exposes the following members.

![](../icons/SectionExpanded.png)Properties

| Name| Description  
---|---|---  
![Public property](../icons/pubproperty.gif)|
[Content](P_Grasshopper_Documentation_GH_RuntimeFile_Content.htm)|  Gets the
data associated with a certain key. For every time the key appears in the
file, an array of content strings will be returned.  
![Public property](../icons/pubproperty.gif)|
[Keys](P_Grasshopper_Documentation_GH_RuntimeFile_Keys.htm)|  Gets a list of
all the keys present in the File.  
![Public property](../icons/pubproperty.gif)|
[Path](P_Grasshopper_Documentation_GH_RuntimeFile_Path.htm)|  Gets the path of
this help file.  
![Public property](../icons/pubproperty.gif)![Static
member](../icons/static.gif)|
[Tags](P_Grasshopper_Documentation_GH_RuntimeFile_Tags.htm)|  Gets a
collection of all the pre-defined keywords. Use IsKeyword(string) if you want
to know whether a string equals a keyword. It's both faster and more reliable
than comparing against this collection.  
Top

![](../icons/SectionExpanded.png)Methods

| Name| Description  
---|---|---  
![Public method](../icons/pubmethod.gif)|
[ContainsKey](M_Grasshopper_Documentation_GH_RuntimeFile_ContainsKey.htm)|
Test whether a certain key is present in the File.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsTag](M_Grasshopper_Documentation_GH_RuntimeFile_IsTag.htm)|  Tests whether
a string is a predefined Grasshopper Help keyword.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[IsTagLine](M_Grasshopper_Documentation_GH_RuntimeFile_IsTagLine.htm)|  Tests
whether a line of text starts with a Grasshopper Help keyword.  
![Public method](../icons/pubmethod.gif)![Static member](../icons/static.gif)|
[ParseFile](M_Grasshopper_Documentation_GH_RuntimeFile_ParseFile.htm)|  Parse
a file and return the runtime representation of said file.  
Top

![](../icons/SectionExpanded.png)Fields

| Name| Description  
---|---|---  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagAuthor](F_Grasshopper_Documentation_GH_RuntimeFile_TagAuthor.htm)|  String
tag used to identify Author fields in documentation source files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagAutoLink](F_Grasshopper_Documentation_GH_RuntimeFile_TagAutoLink.htm)|
String tag used to signal whether automatic linking to a topic is allowed.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagBeginner](F_Grasshopper_Documentation_GH_RuntimeFile_TagBeginner.htm)|
String tag used t o identify Beginner Level Help Content in documentation
source files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagCategory](F_Grasshopper_Documentation_GH_RuntimeFile_TagCategory.htm)|
String tag used to identify Category fields in documentation source files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagComponent](F_Grasshopper_Documentation_GH_RuntimeFile_TagComponent.htm)|
String tag used to identify Component IDs in documentation source files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagContact](F_Grasshopper_Documentation_GH_RuntimeFile_TagContact.htm)|
String tag used to identify Author contact details in documentation source
files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagDescription](F_Grasshopper_Documentation_GH_RuntimeFile_TagDescription.htm)|
String tag used t o identify Description fields in glossary source files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagErranyms](F_Grasshopper_Documentation_GH_RuntimeFile_TagErranyms.htm)|
String tag used to identify Do Not Confuse collections in documentation source
files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagExpert](F_Grasshopper_Documentation_GH_RuntimeFile_TagExpert.htm)|  String
tag used t o identify Expert Level Help Content in documentation source files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagInclude](F_Grasshopper_Documentation_GH_RuntimeFile_TagInclude.htm)|
String tag used to signal whether inclusion of a topic is allowed.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagIntermediate](F_Grasshopper_Documentation_GH_RuntimeFile_TagIntermediate.htm)|
String tag used t o identify Intermediate Level Help Content in documentation
source files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagKeywords](F_Grasshopper_Documentation_GH_RuntimeFile_TagKeywords.htm)|
String tag used to identify Keyword collections in documentation source files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagPronunciation](F_Grasshopper_Documentation_GH_RuntimeFile_TagPronunciation.htm)|
String tag used to identify Pronunciaion Guide fields (IPA) in glossary source
files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagRhinoCommand](F_Grasshopper_Documentation_GH_RuntimeFile_TagRhinoCommand.htm)|
String tag used to identify Similar Rhino Commands in documentation source
files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagSeeAlso](F_Grasshopper_Documentation_GH_RuntimeFile_TagSeeAlso.htm)|
String tag used to identify See Also collections in documentation source
files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagSynonyms](F_Grasshopper_Documentation_GH_RuntimeFile_TagSynonyms.htm)|
String tag used to identify Synonym collections in glossary source files.  
![Public field](../icons/pubfield.gif)![Static member](../icons/static.gif)|
[TagTitle](F_Grasshopper_Documentation_GH_RuntimeFile_TagTitle.htm)|  String
tag used to identify title fields in documentation source files.  
Top

![](../icons/SectionExpanded.png)See Also

#### Reference

[Grasshopper.Documentation Namespace](N_Grasshopper_Documentation.htm)

Grasshopper for Rhino 8.22.25217.12450 (2025-08-05)  
Copyright © 2009-2025 Robert McNeel & Associates

[Report wishes and bugs at
discourse.mcneel.com](https://discourse.mcneel.com/c/grasshopper)

