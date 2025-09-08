---
url: https://developer.rhino3d.com/guides/cpp/rdk-decal-classes/
scraped_at: 2025-09-08T15:40:26.813406
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

[RDK Decals](https://developer.rhino3d.com/guides/cpp/rdk-decal-classes/)

  * IRhRdkDecal
  * CRhRdkObjectDataAccess

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

RDK Decals

__

Windows only

by [John Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated:
Wednesday, January 16, 2019)

### IRhRdkDecal

_IRhRdkDecal_ is an abstract decal interface. It provides access to all the
properties of a Decal.

### CRhRdkObjectDataAccess

_CRhRdkObjectDataAccess_ is a wrapper around an object or layer which makes it
easy to get RDK-specific information from that object or layer. When the
wrapped object is a Rhino object, it can be used for accessing the object’s
decals using the following methods:

  * `AddDecal()` Adds a new decal to the object.
  * `RemoveDecal()` Remove a particular decal from the object.
  * `RemoveAllDecals()` Removes all decals from the object.
  * `NewDecalIterator()` Obtains an iterator for accessing the object’s decals.

A particularly important property of decals is the _decal CRC_. This value
identifies a decal by its state. Multiple decals which would be exactly the
same would have the same CRC and are culled from the system. If you store this
value with the intention of using it to find the decal again later, you must
update your stored value whenever the decal state changes.

The following is an example of how to access decals already on an object. It
uses NewDecalIterator() to get IRhRdkDecal and lists decal information on
every object in the document. To keep the example short it does not list
_every_ piece of information available from IRhRdkDecal but should be enough
to get you started:

    
    
    using OI = CRhinoObjectIterator;
    
    int objCount = 1;
    
    CRhinoObjectIterator it(*pDoc, OI::undeleted_objects, OI::active_and_reference_objects);
    const auto* pObject = it.First();
    while (nullptr != pObject)
    {
    	CRhRdkObjectDataAccess da(pObject);
    
    	auto* pDI = da.NewDecalIterator();
    	if (nullptr != pDI)
    	{
    		const auto* pDecal = pDI->NextDecal();
    		while (nullptr != pDecal)
    		{
    			const auto m = pDecal->Mapping();
    
    			const wchar_t* wszMapping = L"";
    			switch (m)
    			{
    			case IRhRdkDecal::mapUV:          wszMapping = L"UV";          break;
    			case IRhRdkDecal::mapPlanar:      wszMapping = L"Planar";      break;
    			case IRhRdkDecal::mapCylindrical: wszMapping = L"Cylindrical"; break;
    			case IRhRdkDecal::mapSpherical:   wszMapping = L"Spherical";   break;
    			}
    
    			const auto pt = pDecal->Origin();
    			RhinoApp().Print(L"Object %u: Decal %08X, mapping: %s, origin: (%.1f, %.1f, %.1f)",
    			                 objCount, pDecal->CRC(), wszMapping, pt.x, pt.y, pt.z);
    
    			if ((IRhRdkDecal::mapSpherical == m) || (IRhRdkDecal::mapCylindrical == m))
    			{
    				RhinoApp().Print(L", Radius: %.1f", pDecal->Radius());
    
    				if (IRhRdkDecal::mapCylindrical == m)
    				{
    					RhinoApp().Print(L", Height: %.1f", pDecal->Height());
    				}
    			}
    
    			RhinoApp().Print(L"\n");
    
    			pDecal = pDI->NextDecal();
    		}
    
    		delete pDI;
    	}
    
    	pObject = it.Next();
    
    	objCount++;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/rdk-
decal-classes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/rdk-
decal-classes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

