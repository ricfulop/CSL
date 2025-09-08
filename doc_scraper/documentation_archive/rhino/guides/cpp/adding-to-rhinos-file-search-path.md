---
url: https://developer.rhino3d.com/guides/cpp/adding-to-rhinos-file-search-path/
scraped_at: 2025-09-08T15:39:32.550042
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

[Adding to Rhino's File Search
Path](https://developer.rhino3d.com/guides/cpp/adding-to-rhinos-file-search-
path/)

  * Problem
  * Solution
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Adding to Rhino's File Search Path

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

You would like to add a file path to Rhino’s file search path without having
to script the Options command.

## Solution

Rhino’s file search path is held by Rhino’s `CRhinoDirectoryManager` object.
You can get the one and only `CRhinoDirectoryManager` singleton as follows:

    
    
    CRhinoDirectoryManager& dm = RhinoApp().RhinoDirectoryManager();
    

## Example

The following utility function demonstrates how to add (insert append or
insert) to Rhino’s file search path:

    
    
    int RhAddSearchPath( const wchar_t* pszFolder, int index = -1 )
    {
      int rc = -1;
      if( 0 == pszFolder || 0 == pszFolder[0] )
        return -1;
    
      int rc = -1;
      if( CRhinoFileUtilities::DirExists(pszFolder) )
      {
        CRhinoDirectoryManager& dm = RhinoApp().RhinoDirectoryManager();
        const int path_count = dm.SearchPathCount();
        for( int i = 0; i < path_count; i++ )
        {
          if( 0 == on_wcsicmp(pszFolder, dm.SearchPath(i)) )
          {
            rc = i;
            break;
          }
        }
    
        if( rc == -1 )
        {
          index = RHINO_CLAMP( index, -1, path_count );
          if( index == -1 )
            rc = dm.AppendSearchPath( pszFolder );
          else if( dm.InsertSearchPath(index, pszFolder) )
            rc = index;
        }
      }
      return rc;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/adding-
to-rhinos-file-search-path/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/adding-
to-rhinos-file-search-path/index.md) [
Admin](https://developer.rhino3d.com/admin)

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

