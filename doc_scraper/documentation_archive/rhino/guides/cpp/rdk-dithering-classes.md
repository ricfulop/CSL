---
url: https://developer.rhino3d.com/guides/cpp/rdk-dithering-classes/
scraped_at: 2025-09-08T15:40:27.689467
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

[RDK Dithering](https://developer.rhino3d.com/guides/cpp/rdk-dithering-
classes/)

  * Introduction
  * The Document Dithering Settings

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

RDK Dithering

__

Windows only

by [John Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated:
Wednesday, January 16, 2019)

### Introduction

Image _dithering_ is a process in which some form of noise is added to an
image in order to reduce color banding and other artifacts. This is commonly
used when a display device is unable to display the full range of colors. The
image below shows an extreme example. A photo was converted to use only two
colors. On the left, no dithering was used and a lot of detail has been lost.
On the right, Floyd-Steinberg dithering was used and the amount of detail is
much improved. Although modern displays don’t usually require any dithering,
there are cases where it can make a subtle difference to the final quality of
an image. For this reason, the RDK provides two kinds of dithering, _Simple
Noise_ and _Floyd Steinberg_.

![Dithering](https://developer.rhino3d.com/images/rdk-dithering.png) Photo by
John Croudy.

### The Document Dithering Settings

The _RDK Document Dithering settings_ is a document-resident dithering object
which affects renderings. If you have a Rhino document, you can read and write
that document’s dithering settings through the document’s
[IRhRdkDithering](https://developer.rhino3d.com/api/cpp/class_i_rh_rdk_dithering.html)
interface. Any changes you make will appear in the Dithering and Color
Adjustment section of the Rendering panel and will also be stored in the 3dm
file. Getting the dithering settings from a document always returns a const
reference. To write to the settings, you must begin a batch of write
operations and afterwards end the batch. This is done using the RDK’s standard
BeginChange / EndChange system. The following is an example of how to access
and change the document dithering settings:

    
    
    static class CDitheringExampleCommand : public CRhinoTestCommand
    {
    protected:
    	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
    	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"DitheringExample"); }
    	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
    }
    theDitheringExampleCommand;
    
    using DM = IRhRdkDithering::Methods;
    
    static const wchar_t* StringFromDitheringMethod(DM dm)
    {
    	switch (dm)
    	{
    	case DM::FloydSteinberg: return L"Floyd-Steinberg"; break;
    	case DM::SimpleNoise:    return L"Simple noise"; break;
    	}
    
    	return L"None";
    }
    
    CRhinoCommand::result CDitheringExampleCommand::RunCommand(const CRhinoCommandContext& context)
    {
    	auto* pDoc = context.Document();
    	if (nullptr == pDoc)
    		return failure;
    
    	const auto& dither = pDoc->Dithering();
    
    	RhinoApp().Print(L"Dithering before: %s\n", StringFromDitheringMethod(dither.Method()));
    
    	auto& write_dither = dither.BeginChange(RhRdkChangeContext::Program);
    	write_dither.SetMethod(DM::FloydSteinberg);
    	write_dither.EndChange();
    
    	RhinoApp().Print(L"Dithering after: %s\n", StringFromDitheringMethod(dither.Method()));
    
    	return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/rdk-
dithering-classes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/rdk-
dithering-classes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

