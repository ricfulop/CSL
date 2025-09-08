---
url: https://developer.rhino3d.com/guides/cpp/rdk-skylight-classes/
scraped_at: 2025-09-08T15:40:35.841990
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

[RDK Skylight](https://developer.rhino3d.com/guides/cpp/rdk-skylight-classes/)

  * Introduction
  * The Document Skylight

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

RDK Skylight

__

Windows only

by [John Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated:
Wednesday, January 16, 2019)

### Introduction

The _skylight_ is a feature that allows a scene to be rendered realistically,
as if the objects in the scene were in a real environment under a real sky.
When the skylight is used, the objects in the scene are lit not only by the
scene’s lights (or the sun), but also by the environment. The image below
shows a comparison of a scene rendered with the skylight disabled (left) and
enabled (right). Notice the subtly different coloring and the softer more
diffuse shadows in the sky-lit image. The disadvantage of the skylight is that
it is very CPU-intensive and renderings are much slower when it is enabled.

![Road](https://developer.rhino3d.com/images/rdk-skylight.jpg)

### The Document Skylight

The _RDK Document Skylight_ is a document-resident skylight which affects
viewports and renderings. If you have a Rhino document, you can read and write
that document’s skylight through the document’s
[IRhRdkSkylight](https://developer.rhino3d.com/api/cpp/class_i_rh_rdk_skylight.html)
interface. Any changes you make will appear in the Lighting section of the
Rendering panel and will also be stored in the 3dm file. Getting the skylight
from a document always returns a const reference. To write to the skylight,
you must begin a batch of write operations and afterwards end the batch. This
is done using the RDK’s standard BeginChange / EndChange system. The following
is an example of how to access and change the document skylight:

    
    
    static class CSkylightExampleCommand : public CRhinoTestCommand
    {
    protected:
    	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
    	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"MySkylightCmd"); }
    	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
    }
    theSkylightExampleCommand;
    
    CRhinoCommand::result CSkylightExampleCommand::RunCommand(const CRhinoCommandContext& context)
    {
    	auto* pDoc = context.Document();
    	if (nullptr == pDoc)
    		return failure;
    
    	const auto& sl = pDoc->Skylight();
    
    	RhinoApp().Print(L"Skylight before: %s\n", sl.On() ? L"on" : L"off");
    
    	auto& write_sl = sl.BeginChange(RhRdkChangeContext::Program);
    	write_sl.SetOn(false);
    	write_sl.EndChange();
    
    	RhinoApp().Print(L"Skylight after: %s\n", sl.On() ? L"on" : L"off");
    
    	return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/rdk-
skylight-classes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/rdk-
skylight-classes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

