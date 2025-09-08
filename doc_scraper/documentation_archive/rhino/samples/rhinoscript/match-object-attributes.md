---
url: https://developer.rhino3d.com/samples/rhinoscript/match-object-attributes/
scraped_at: 2025-09-08T15:50:23.248510
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

Match Object Attributes

__

Windows only

Demonstrates a custom object attribute matching function in RhinoScript.

VBScript

    
    
    ' Description:
    '   Matches, or copies, the attributes of a source object to a
    '   target object or an array of target objects. If the source
    '   object is not specified, the attributes of the target object(s)
    '   will be reset to Rhino's default object attributes.
    ' Parameters:
    '   arrTargets - An array of strings identifying the target objects.
    '   strSource  - The identifier of the source object. If the source
    '                object is not specified, the attributes of the target
    '                object(s) will be reset to Rhino's default object
    '                attributes.
    '   intMode    - The group mode flag, where:
    '                  intMode = -1, remove all groups from targets
    '                  intMode =  0, do not copy source groups to targets
    '                  intMode =  1, copy source groups to targets
    '
    Function MatchObjectAttributesEx(arrTargets, strSource, intMode)
    
      Dim strTarget, arrGroups, strGroup
    
      If intMode < -1 Then
        intMode = -1
      ElseIf intMode > 1 Then
        intMode = 1
      End If
    
      For Each strTarget In arrTargets
    
        If intMode = 0 Then
          arrGroups = Rhino.ObjectGroups(strTarget)
        Else
          arrGroups = Null
        End If
    
        Call Rhino.MatchObjectAttributes(strTarget, strSource)
    
        If intMode = -1 Or intMode = 0 Then
          Call Rhino.RemoveObjectFromAllGroups(strTarget)
        End If
    
        If intMode = 0 And Not IsNull(arrGroups) Then
          For Each strGroup In arrGroups
          	Call Rhino.AddObjectToGroup(strTarget, strGroup)
          Next
        End If
    
      Next
    
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

