---
url: https://developer.rhino3d.com/guides/cpp/rdk-safe-frame-classes/
scraped_at: 2025-09-08T15:40:34.822849
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

[RDK Safe Frame](https://developer.rhino3d.com/guides/cpp/rdk-safe-frame-
classes/)

  * Introduction
  * The Document Safe Frame

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

RDK Safe Frame

__

Windows only

by [John Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated:
Wednesday, January 16, 2019)

### Introduction

A _Safe Frame_ is a guide to help ensure that the most important elements of a
scene will appear inside a certain region of the rendered image. The name
comes from movie and TV production where a camera operator sees one or more
rectangles in the camera’s viewfinder which shows limits inside which an actor
or prop is guaranteed to be visible on all viewer’s screens.

![SafeFrame](https://developer.rhino3d.com/images/rdk-safeframe.jpg)

### The Document Safe Frame

The _RDK Document Safe Frame_ is a document-resident safe frame which can be
displayed in viewports. If you have a Rhino document, you can read and write
that document’s safe frame through the document’s
[IRhRdkSafeFrame](https://developer.rhino3d.com/api/cpp/class_i_rh_rdk_safe_frame.html)
interface. Any changes you make will appear in the Safe Frame UI and will also
be stored in the 3dm file. Getting the safe frame from a document always
returns a const reference. To write to the safe frame, you must begin a batch
of write operations and afterwards end the batch. This is done using the RDK’s
standard BeginChange / EndChange system. The following is an example of how to
access and change the document safe frame:

    
    
    static class CSafeFrameExampleCommand : public CRhinoTestCommand
    {
    protected:
    	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
    	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"MySafeFrameCmd"); }
    	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
    }
    theSafeFrameExampleCommand;
    
    CRhinoCommand::result CSafeFrameExampleCommand::RunCommand(const CRhinoCommandContext& context)
    {
    	auto* pDoc = context.Document();
    	if (nullptr == pDoc)
    		return failure;
    
    	const auto& sf = pDoc->SafeFrame();
    
    	RhinoApp().Print(L"Safe frame before: %s\n", sf.On() ? L"on" : L"off");
    
    	auto& write_sf = sf.BeginChange(RhRdkChangeContext::Program);
    	write_sf.SetOn(false);
    	write_sf.EndChange();
    
    	RhinoApp().Print(L"Safe frame after: %s\n", sf.On() ? L"on" : L"off");
    
    	return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/rdk-
safe-frame-classes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/rdk-
safe-frame-classes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

