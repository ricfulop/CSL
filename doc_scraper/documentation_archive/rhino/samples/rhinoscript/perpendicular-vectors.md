---
url: https://developer.rhino3d.com/samples/rhinoscript/perpendicular-vectors/
scraped_at: 2025-09-08T15:50:27.268713
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

Perpendicular Vectors

__

Windows only

Demonstrates how to calculate a vector that is perpendicular to another vector
using RhinoScript.

VBScript

    
    
    ' Description:
    '   Returns a 3-D vector that is perpendicular to another 3-D vector.
    ' Parameters:
    '   v - the 3-D vector to evaluate.
    ' Returns:
    '   A perpendicular 3-D vector if successful, Null otherwise.
    ' Remarks:
    '   The result is not a unitized 3-D vector.
    '       
    
    Function GetPerpendicularVector( v )
    
      GetPerpendicularVector = Null
      If Not IsArray(v) Or UBound(v) <> 2 Then Exit Function
      If Rhino.IsVectorZero(v) Then Exit Function
    
      Dim i, j, k
      Dim a, b
      k = 2
      If Abs(v(1)) > Abs(v(0)) Then
        If Abs(v(2)) > Abs(v(1)) Then
          ' |v(2)| > |v(1)| > |v(0)|
          i = 2
          j = 1
          k = 0
          a = v(2)
          b = -v(1)
        ElseIf Abs(v(2)) >= Abs(v(0)) Then
          ' |v(1)| >= |v(2)| >= |v(0)|
          i = 1
          j = 2
          k = 0
          a = v(1)
          b = -v(2)
        Else
          ' |v(1)| > |v(0)| > |v(2)|
          i = 1
          j = 0
          k = 2
          a = v(1)
          b = -v(0)
        End If
      ElseIf Abs(v(2)) > Abs(v(0)) Then
        ' |v(2)| > |v(0)| >= |v(1)|
        i = 2
        j = 0
        k = 1
        a = v(2)
        b = -v(0)
       ElseIf Abs(v(2)) > Abs(v(1)) Then
        ' |v(0)| >= |v(2)| > |v(1)|
        i = 0
        j = 2
        k = 1
        a = v(0)
        b = -v(2)
      Else
        ' |v(0)| >= |v(1)| >= |v(2)|
        i = 0
        j = 1
        k = 2
        a = v(0)
        b = -v(1)
      End If
    
      Dim rc(2)
      rc(i) = b
      rc(j) = a
      rc(k) = 0.0
      GetPerpendicularVector = rc
    
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

