---
url: https://developer.rhino3d.com/guides/cpp/adjusting-clipping-planes-from-conduits/
scraped_at: 2025-09-08T15:39:33.578809
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

[Adjusting Clipping Planes from
Conduits](https://developer.rhino3d.com/guides/cpp/adjusting-clipping-planes-
from-conduits/)

  * Overview
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Adjusting Clipping Planes from Conduits

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

You may reason that it is necessary to change Rhino’s Z-Buffer range because
when you draw using the `CRhinoDisplayConduit` class, as objects that are far
from Rhino’s objects are being clipped. However, the Z-Buffer range has
nothing to do with whether or not objects get culled, or clipped, from the
viewing frustum. This behavior has to do with Rhino’s near and far clipping
planes. Rhino’s clipping planes are adjusted dynamically in order to maximize
the precision within the Z-Buffer. Additionally, Rhino does this by placing
the near plane as close to the closest visible object in the frustum, and the
far plane as far as the furthest visible object in the frustum.

If you are adding or drawing objects that Rhino does not know about - that are
not in the drawing database - then they will not be included in those
calculations. Thus, you must also implement the `SC_CALCBOUNDINGBOX` channel
inside your conduit and add to the overall scene bounding box. This will make
Rhino adjust its clipping planes to include your objects. For example…

## Example

    
    
    class CTestDisplayConduit : public CRhinoDisplayConduit
    {
    public:
      CTestDisplayConduit();
    
      bool ExecConduit(
        CRhinoDisplayPipeline& dp,
        UINT nChannel,
        bool& bTerminate
        );
    
      // TODO: add other methods and members here
    };
    
    CTestDisplayConduit::CTestDisplayConduit()
    : CRhinoDisplayConduit(CSupportChannels::SC_PREDRAWOBJECTS|CSupportChannels::SC_CALCBOUNDINGBOX)
    {
      // TODO: initialize members here
    }
    
    bool CTestDisplayConduit::ExecConduit(
        CRhinoDisplayPipeline& dp,
        UINT nChannel,
        bool& bTerminate
        )
    {
      switch( nChannel )
      {
        case CSupportChannels::SC_CALCBOUNDINGBOX:
        {
          m_pChannelAttrs->m_BoundingBox.Union( /*YOUR_OBJECTS_BOUNDING_BOXES*/ );
          break;
        }
        case CSupportChannels::SC_PREDRAWOBJECTS:
        {
          // TODO: add drawing code here
          break;
        }
      }
      return true;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/adjusting-
clipping-planes-from-conduits/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/adjusting-
clipping-planes-from-conduits/index.md) [
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

