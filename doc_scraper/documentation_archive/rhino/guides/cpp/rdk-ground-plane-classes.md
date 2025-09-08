---
url: https://developer.rhino3d.com/guides/cpp/rdk-ground-plane-classes/
scraped_at: 2025-09-08T15:40:29.797359
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

[RDK Ground Plane](https://developer.rhino3d.com/guides/cpp/rdk-ground-plane-
classes/)

  * Introduction
  * The Document Ground Plane

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

RDK Ground Plane

__

Windows only

by [John Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated:
Wednesday, January 16, 2019)

### Introduction

When rendering real-world scenes, it is very often the case that the rendering
will include a large area of ground or flooring. This could be modeled by
using a plane, but this is inconvenient because the ground tends to stretch as
far as the eye can see. To circumvent this problem, the RDK provides a set of
_ground plane_ services to make it easier to add a ground or floor to your
scene. A ground plane has an _altitude_ , which is usually the same as its
position along the z-axis. It can also have a material assigned to it, which
will appear in renderings and in the viewport, much as materials assigned to
objects do. If the _auto-altitude_ option is enabled, the ground plane will
adjust itself to sit below the objects in the scene.

![Road](https://developer.rhino3d.com/images/rdk-ground-plane-road.jpg)
Interstate 15, Nevada, USA ~ Photo by John Croudy.

### The Document Ground Plane

The _RDK Document Ground Plane_ is a document-resident ground plane which
affects viewports and renderings. If you have a Rhino document, you can read
and write that document’s ground plane through the document’s
[IRhRdkGroundPlane](https://developer.rhino3d.com/api/cpp/class_i_rh_rdk_ground_plane.html)
interface. Any changes you make will appear in the main ground plane UI and
will also be stored in the 3dm file. Getting the ground plane from a document
always returns a const reference. To write to the ground plane, you must begin
a batch of write operations and afterwards end the batch. This is done using
the RDK’s standard BeginChange / EndChange system. The following is an example
of how to access and change the document ground plane:

    
    
    static class CGroundPlaneExampleCommand: public CRhinoTestCommand
    {
    protected:
    	virtual UUID CommandUUID() override { static const UUID uuid = { your_uuid_here } }; return uuid; }
    	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"MyGroundPlaneCmd"); }
    	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
    }
    theGroundPlaneExampleCommand;
    
    CRhinoCommand::result CGroundPlaneExampleCommand::RunCommand(const CRhinoCommandContext& context)
    {
    	auto* pDoc = context.Document();
    	if (nullptr == pDoc)
    		return failure;
    
    	// Get the document ground plane.
    	const auto& gp = pDoc->GroundPlane();
    
    	RhinoApp().Print(L"Ground plane altitude before: %.1f\n", gp.Altitude());
    
    	// Begin a change bracket on the ground plane.
    	auto& write_gp = gp.BeginChange(RhRdkChangeContext::Program);
    
    	// Set the ground plane's altitude manually.
    	write_gp.SetAutoAltitude(false);
    	write_gp.SetAltitude(10.0);
    
    	// Create a new custom material.
    	ON_Material mat;
    	mat.SetDiffuse(ON_Color(185, 14, 14));
    	auto* pMaterial = ::RhRdkNewBasicMaterial(mat, pDoc);
    	if (nullptr != pMaterial)
    	{
    		auto& write_contents = pDoc->Contents().BeginChange(RhRdkChangeContext::Program);
    		write_contents.Attach(*pMaterial);
    		write_contents.EndChange();
    
    		write_gp.SetOn(true);
    		write_gp.SetShadowOnly(false);
    		write_gp.SetMaterialInstanceId(pMaterial->InstanceId());
    	}
    
    	// End the ground plane change bracket.
    	write_gp.EndChange();
    
    	RhinoApp().Print(L"Ground plane altitude after: %.1f\n", gp.Altitude());
    
    	return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/rdk-
ground-plane-classes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/rdk-
ground-plane-classes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

