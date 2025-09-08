---
url: https://developer.rhino3d.com/guides/rhinocommon/code-driven-file-io/
scraped_at: 2025-09-08T15:36:47.901837
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

[Code-Driven File IO](https://developer.rhino3d.com/guides/rhinocommon/code-
driven-file-io/)

  * How does it work?
  * Example: Write an AutoCAD dwg from Rhino
  * Headless Document Support
  * Example: Read a SketchUp file into Rhino
  * Using Grasshopper with Code Driven File.io
  * Other Use Cases

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Code-Driven File IO

[New in 8](https://developer.rhino3d.com/8/new)

by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/) (Last updated:
Wednesday, April 17, 2024)

Prior to Rhino 8, code-driven exporting was done by using the active document
and scripting the export command. This was both inefficient and painful to
write.

Rhino 8 introduces the abililty to read and write files of any format that
Rhino supports entirely through code. This includes support for options that
need to be applied to properly read or write different files.

## How does it work?

Import and export plug-ins are provided an optional dictionary at read and
write time. When the dictionary is present, instead of asking for user input,
the importers and exporters pay attention to keys and values in the dictionary
to make decisions on options for I/O. RhinoCommon provides classes for these
options that can be converted into a dictionary that the import and export
plug-ins can interpret. Look in the `Rhino.FileIO` namespace for format
specific option classes.

## Example: Write an AutoCAD dwg from Rhino

This example shows how to write the active `RhinoDoc` to an AutoCAD dwg with
options:

C# Python

    
    
    var doc = Rhino.RhinoDoc.ActiveDoc;
    if (doc != null)
    {
        // create/set options for exporting to DWG file
        var options = new Rhino.FileIO.FileDwgWriteOptions();
        options.UseLWPolylines = true;
        options.Version = Rhino.FileIO.FileDwgWriteOptions.AutocadVersion.Acad2000;
        // convert options into a dictionary
        var optionsDictionary = options.ToDictionary();
    
        var path = System.Environment.GetFolderPath(System.Environment.SpecialFolder.Desktop);
        path = System.IO.Path.Combine(path, "sample.dwg");
    
        // export to a file with our options dictionary
        bool success = doc.Export(path, optionsDictionary);
        if (success)
            System.Console.WriteLine("Successfully exported sample.dwg");
        else
            System.Console.WriteLine("Error while trying to export sample.dwg");
    }
    
    
    
    import scriptcontext
    import Rhino
    import os
    
    if scriptcontext.doc is not None:
        options = Rhino.FileIO.FileDwgWriteOptions()
        options.UseLWPolylines = True
        options.Version = Rhino.FileIO.FileDwgWriteOptions.AutocadVersion.Acad2000
        options_dictionary = options.ToDictionary()
    
        path = os.path.expanduser("~/Desktop/sample_py.dwg")
        success = scriptcontext.doc.Export(path, options_dictionary)
        if success:
            print("Successfully exported sample.dwg")
        else:
            print("Error while trying to export sample.dwg")
    

## Headless Document Support

Headless `RhinoDoc` instances can be used to further streamline the process.
Headless documents are `RhinoDoc` instances that never affect the Rhino user
interface. Their use can improve performance as none of the geometry in the
document needs to be displayed in Rhino. You can either create a headless
document from scratch and add geometry to it or import from a file using
options.

## Example: Read a SketchUp file into Rhino

This example shows how to read a SketchUp skp file and example the geometry
using a headless RhinoDoc:

C# Python

    
    
    // Create a headless doc and import SketchUp file into it
    var doc = Rhino.RhinoDoc.CreateHeadless(null);
    var options = new Rhino.FileIO.FileSkpReadOptions();
    options.ImportCurves = false;
    options.EmbedTexturesInModel = false;
    
    var path = System.Environment.GetFolderPath(System.Environment.SpecialFolder.Desktop);
    path = System.IO.Path.Combine(path, "test.skp");
    doc.Import(path, options.ToDictionary());
    
    // Analyze what was read into the doc
    System.Console.WriteLine($"{doc.Objects.Count} objects");
    foreach(var obj in doc.Objects)
    {
        var bbox = obj.Geometry.GetBoundingBox(true);
        System.Console.WriteLine($"Center is {bbox.Center}");
    }
    
    // done with the doc, free up the memory it is using
    doc.Dispose();
    
    
    
    import Rhino
    import os
    
    doc = Rhino.RhinoDoc.CreateHeadless(None)
    options = Rhino.FileIO.FileSkpReadOptions()
    options.ImportCurves = False
    options.EmbedTexturesInModel = False
    
    path = os.path.expanduser("~/Desktop/test.skp")
    doc.Import(path, options.ToDictionary())
    
    print(f"{doc.Objects.Count} objects")
    for obj in doc.Objects:
        bbox = obj.Geometry.GetBoundingBox(True)
        print(f"Center is {bbox.Center}")
    
    doc.Dispose()
    

## Using Grasshopper with Code Driven File.io

When using Grasshopper to read or write files, there are some differences then
the above examples. The main difference is Grasshopper is it own document.
When reading in a file, objects are then processed thru Grasshopper
independantly. And when writing out a file format, then a headless doc needs
to be created in the same component that writes the file. See the examples
below:

Reading in a file format can be done in new Rhino 8 components using the
Import File component:

![import_file_gh.png](import_file_gh.png)

[__](https://developer.rhino3d.com/guides/rhinocommon/code-driven-file-
io/ExportTo3MFV3.gh) [Download Example Grasshopper Definition for Exporting a
File](https://developer.rhino3d.com/guides/rhinocommon/code-driven-file-
io/ExportTo3MFV3.gh)

Here the file is imported and the objects can then be processed.

To write out any of the File formats from Rhino, create headless Doc and then
add objects to it. The example below writes a 3MF file using a Python 3
component. Set the script component `objects` input to `List Access` and
`GeometryBase` Input Hint:

    
    
    import System
    import Rhino
    
    doc = Rhino.RhinoDoc.CreateHeadless(None)
    
    if not objects is None:
        for o in objects:
            doc.Objects.Add(o)
    
    options = Rhino.FileIO.File3mfWriteOptions()
    options.Title = title
    options.Designer = Rhino.RhinoApp.LicenseUserName
    options.Metadata["Test"] = "Star"
    options.MoveOutputToPositiveXYZOctant = True;
    
    if not path is None:
        path = System.Environment.ExpandEnvironmentVariables(path)
        success = doc.Export(path, options.ToDictionary())
        print(success)
    doc.Dispose();
    

## Other Use Cases

  * Batch processing: a directory of files could be read into headless documents and exported to another format.
  * Grasshopper: Using headless documents in Grasshopper with all Rhino file formats supports allows for processing geometry from different files without forcing the main Rhino active doc to change.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/code-
driven-file-io/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/code-
driven-file-io/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

