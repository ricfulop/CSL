---
url: https://developer.rhino3d.com/samples/rhinoscript/evaluate-curve-torsion/
scraped_at: 2025-09-08T15:49:13.854662
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

Evaluate Curve Torsion

__

Windows only

Demonstrates how to evaluate the torsion of a curve in RhinoScript.

VBScript

    
    
    '''
    ''' Description
    '''   Evaluate the torsion of a curve.
    ''' Parameters
    '''   crv - a string that identifies the curve to evaluate
    '''   t   - a parameter of the curve within its domain
    ''' Returns
    '''   The torsion if successful.
    '''   Null if the torsion is undefined at the parameter.
    '''
    Function EvaluateTorsion(crv, t)
    
      ' Local variables
      Dim data, d1xd2, numer, denom
    
      ' Default return value
      EvaluateTorsion = Null
    
      ' Calculate the torsion
      data = Rhino.CurveEvaluate(crv, t, 3)
      If IsArray(data) And UBound(data) = 3 Then
        d1xd2 = Rhino.VectorCrossProduct(data(1), data(2))
        numer = Rhino.VectorDotProduct(d1xd2, data(3))
        denom = Rhino.VectorDotProduct(d1xd2, d1xd2)
        If denom > 0 Then
          EvaluateTorsion = numer / denom
        End If
      End If
    
    End Function
    

  

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

