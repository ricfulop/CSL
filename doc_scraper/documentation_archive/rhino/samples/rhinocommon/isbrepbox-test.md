---
url: https://developer.rhino3d.com/samples/rhinocommon/isbrepbox-test/
scraped_at: 2025-09-08T15:46:20.849640
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

IsBrepBox Test

Demonstrates how to determine whether a given Brep is a box.

C# VB.NET Python

    
    
    partial class Examples
    {
      private static bool IsBrepBox(Rhino.Geometry.Brep brep)
      {
        const double zero_tolerance = 1.0e-6; // or whatever
        bool rc = brep.IsSolid;
        if( rc )
          rc = brep.Faces.Count == 6;
    
        var N = new Rhino.Geometry.Vector3d[6];
        for (int i = 0; rc && i < 6; i++)
        {
          Rhino.Geometry.Plane plane;
          rc = brep.Faces[i].TryGetPlane(out plane, zero_tolerance);
          if( rc )
          {
            N[i] = plane.ZAxis;
            N[i].Unitize();
          }
        }
    
        for (int i = 0; rc && i < 6; i++)
        {
          int count = 0;
          for (int j = 0; rc && j < 6; j++)
          {
            double dot = Math.Abs(N[i] * N[j]);
            if (dot <= zero_tolerance)
              continue;
            if (Math.Abs(dot - 1.0) <= zero_tolerance)
              count++;
            else
              rc = false;
          }
    
          if (rc)
          {
            if (2 != count)
              rc = false;
          }
        }
        return rc;
      }
    
      public static Rhino.Commands.Result IsBrepBox(Rhino.RhinoDoc doc)
      {
        Rhino.DocObjects.ObjRef obj_ref;
        var rc = Rhino.Input.RhinoGet.GetOneObject("Select Brep", true, Rhino.DocObjects.ObjectType.Brep, out obj_ref);
        if (rc == Rhino.Commands.Result.Success)
        {
          var brep = obj_ref.Brep();
          if (brep != null)
          {
            Rhino.RhinoApp.WriteLine(IsBrepBox(brep) ? "Yes it is a box" : "No it is not a box");
          }
        }
        return rc;
      }
    }
    
    
    
    Partial Friend Class Examples
      Private Shared Function IsBrepBox(ByVal brep As Rhino.Geometry.Brep) As Boolean
    	Const zero_tolerance As Double = 1.0e-6 ' or whatever
    	Dim rc As Boolean = brep.IsSolid
    	If rc Then
    	  rc = brep.Faces.Count = 6
    	End If
    
    	Dim N = New Rhino.Geometry.Vector3d(5){}
    	Dim i As Integer = 0
    	Do While rc AndAlso i < 6
    	  Dim plane As Rhino.Geometry.Plane = Nothing
    	  rc = brep.Faces(i).TryGetPlane(plane, zero_tolerance)
    	  If rc Then
    		N(i) = plane.ZAxis
    		N(i).Unitize()
    	  End If
    		i += 1
    	Loop
    
    	i = 0
    	Do While rc AndAlso i < 6
    	  Dim count As Integer = 0
    	  Dim j As Integer = 0
    	  Do While rc AndAlso j < 6
    		Dim dot As Double = Math.Abs(N(i) * N(j))
    		If dot <= zero_tolerance Then
    		  j += 1
    		  Continue Do
    		End If
    		If Math.Abs(dot - 1.0) <= zero_tolerance Then
    		  count += 1
    		Else
    		  rc = False
    		End If
    		  j += 1
    	  Loop
    
    	  If rc Then
    		If 2 <> count Then
    		  rc = False
    		End If
    	  End If
    		i += 1
    	Loop
    	Return rc
      End Function
    
      Public Shared Function IsBrepBox(ByVal doc As Rhino.RhinoDoc) As Rhino.Commands.Result
    	Dim obj_ref As Rhino.DocObjects.ObjRef = Nothing
    	Dim rc = Rhino.Input.RhinoGet.GetOneObject("Select Brep", True, Rhino.DocObjects.ObjectType.Brep, obj_ref)
    	If rc Is Rhino.Commands.Result.Success Then
    	  Dim brep = obj_ref.Brep()
    	  If brep IsNot Nothing Then
    		Rhino.RhinoApp.WriteLine(If(IsBrepBox(brep), "Yes it is a box", "No it is not a box"))
    	  End If
    	End If
    	Return rc
      End Function
    End Class
    
    
    
    import Rhino
    
    def IsBrepBox(brep):
        zero_tolerance = 1.0e-6 #or whatever
        rc = brep.IsSolid
        if rc: rc = brep.Faces.Count == 6
    
        N = []
        for i in range(6):
            if not rc: break
            rc, plane = brep.Faces[i].TryGetPlane(zero_tolerance)
            if rc:
                v = plane.ZAxis
                v.Unitize()
                N.append(v)
    
        for i in range(6):
            count = 0
            for j in range(6):
                if not rc: break
                dot = abs(N[i] * N[j])
                if dot<=zero_tolerance: continue
                if abs(dot-1.0)<=zero_tolerance:
                    count += 1
                else:
                    rc = False
    
        if rc:
            if 2!=count: rc = False
        return rc
    
    
    if __name__=="__main__":
        rc, objref = Rhino.Input.RhinoGet.GetOneObject("Select Brep", True, Rhino.DocObjects.ObjectType.Brep)
        if rc==Rhino.Commands.Result.Success:
            brep = objref.Brep()
            if brep:
                if IsBrepBox(brep): print "Yes it is a box"
                else: print "No it is not a box"
    

  

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

