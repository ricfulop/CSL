---
url: https://developer.rhino3d.com/samples/rhinopython/current-model-info/
scraped_at: 2025-09-08T15:46:54.948691
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

Get Current Model Information

Demonstrates how to get current model information through Python.

Python

    
    
    # Displays information about the currently loaded Rhino document.
    import rhinoscriptsyntax as rs
    from System.IO import Path, File, FileInfo, FileAttributes
    
    # some helper functions for CurrentModelInfo
    def __FileAttributes(fullpath):
        "Returns a string describing a file's attributes."
        attr = File.GetAttributes(fullpath)
        if( attr == FileAttributes.Normal ):
            return "Normal"
        rc = ""
        if( attr & FileAttributes.Directory ): rc += "Directory "
        if( attr & FileAttributes.ReadOnly ): rc += "Read Only "
        if( attr & FileAttributes.Hidden ): rc += "Hidden "
        if( attr & FileAttributes.System ): rc += "System "
        if( attr & FileAttributes.Archive ): rc += "Archive "
        if( attr & FileAttributes.Compressed ): rc += "Compressed "
        return rc
    
    
    def __PrintFileInformation( fullpath ):
        "Displays a file's information."
        fi = FileInfo(fullpath)
        info  = "Full Path:  " + fullpath +"\n"
        info += "File Name:  " + Path.GetFileName(fullpath) + "\n"
        info += "File Attributes:  " + __FileAttributes(fullpath) + "\n"
        info += "Date Created:  " + File.GetCreationTime(fullpath).ToString() + "\n"
        info += "Last Date Accessed:  " + File.GetLastAccessTime(fullpath).ToString() + "\n"
        info += "Last Date Modified:  " + File.GetLastWriteTime(fullpath).ToString() + "\n"
        info += "File Size (Bytes):  " + fi.Length.ToString() + "\n"
        rs.MessageBox( info, 0, "Current Model Information" )
    
    
    def CurrentModelInfo():
        "Get the current document name and path"
        name = rs.DocumentName()
        path = rs.DocumentPath()
        fileexists = False
        if( path and name ):
            filespec = Path.Combine(path, name)
            fileexists = File.Exists(filespec)
        
        if fileexists:
            __PrintFileInformation(filespec)
        else:
            print "Current model not found. Make sure the model has been saved to disk."
    
    
    ##########################################################################
    # Check to see if this file is being executed as the "main" python
    # script instead of being used as a module by some other python script
    # This allows us to use the module which ever way we want.
    if( __name__ == "__main__" ):
      #call function defined above
      CurrentModelInfo()
    

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

