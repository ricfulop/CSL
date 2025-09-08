---
url: https://developer.rhino3d.com/samples/cpp/split-brep-edges/
scraped_at: 2025-09-08T15:48:44.853600
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

Split Brep Edges

__

Windows only

Demonstrates how to split the edges of breps.

C/C++

    
    
    /*
    Description:
      Splits a brep edge into two edges.
    Parameters:
      brep       - [in/out] The brep to modify.
      edge_index - [in] The index of the edge to split.
      edge_t     - [in] The parameter on the edge to split at.
    Returns:
      True if successful, false otherwise.
    */
    static bool SplitBrepEdge( ON_Brep& brep, int edge_index, double edge_t )
    {
      bool rc = true;
      const ON_BrepEdge& edge = brep.m_E[edge_index];
    
      int trim_count = edge.TrimCount();
      ON_SimpleArray<double> trim_t( trim_count );
      trim_t.SetCount( trim_count );
    
      int i;
      for( i = 0; i < trim_count; i++ )
      {
        // Given a trim and parameter on the corresponding 3d edge,
        // get the corresponding parameter on the 2d trim curve.
        double t = 0.0;
        rc = brep.GetTrimParameter( edge.m_ti[i], edge_t, &t );
        if( rc )
          trim_t[i] = t;
        else
          break;
      }
    
      if( rc )
      {
        // Splits an edge into two edges.  The input edge
        // becomes the left portion and a new edge is created
        // for the right portion.
        rc = brep.SplitEdge( edge_index, edge_t, trim_t, -1 );
    
        // Delete any unreferenced objects from the brep arrays,
        // reindexes as needed, and shrinks arrays to minimum required size.
        brep.Compact();
    
        // Set the brep's vertex tolerances.
        brep.SetVertexTolerances( true );
      }
    
      return rc;
    }
    
    CRhinoCommand::result CCommandTest::RunCommand( const CRhinoCommandContext& context )
    {
      // Don't split kinky surfaces...
      CRhinoKeepKinkySurfaces keep_kinky_srfs;
    
      CRhinoGetObject go;
      go.SetCommandPrompt( L"Select edge to split" );
      go.SetGeometryFilter( CRhinoGetObject::curve_object );
      go.SetGeometryAttributeFilter( CRhinoGetObject::edge_curve );
      go.EnableReferenceObjectSelect( false );
      go.GetObjects( 1, 1 );
      if( go.CommandResult() != success )
        return go.CommandResult();
    
      const CRhinoObjRef objref = go.Object(0);
      const CRhinoObject* obj = objref.Object();
      const ON_BrepEdge* edge = objref.Edge();
      const ON_Brep* brep = objref.Brep();
      if( 0 == obj | 0 == edge | 0 == brep )
        return failure;
    
      CRhinoGetPoint gp;
      gp.SetCommandPrompt( L"Point to split edge" );
      gp.Constrain( *edge );
      gp.GetPoint();
      if( gp.CommandResult() != success )
        return gp.CommandResult();
    
      const ON_BrepTrim* trim = 0;
      double edge_t = 0;
      edge = gp.PointOnEdge( &edge_t, trim );
      if( edge )
      {
        ON_Brep newbrep( *brep );
        if( SplitBrepEdge(newbrep, edge->m_edge_index, edge_t) )
        {
          context.m_doc.ReplaceObject( CRhinoObjRef(obj), newbrep );
          context.m_doc.Redraw();
        }
      }
    
      return success;
    }
    

  

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

