---
url: https://developer.rhino3d.com/guides/cpp/rdk-linear-workflow-classes/
scraped_at: 2025-09-08T15:40:30.848465
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

[RDK Linear Workflow](https://developer.rhino3d.com/guides/cpp/rdk-linear-
workflow-classes/)

  * Introduction
  * The Document Linear Workflow

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

RDK Linear Workflow

__

Windows only

by [John Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated:
Wednesday, January 16, 2019)

### Introduction

Many consumer digital cameras output JPEG files which use the sRGB color
space. This color space incorporates gamma correction which makes it possible
to directly display the images on a computer monitor without even knowing that
gamma correction exists. This means that many available photographic textures
have already been gamma-corrected. Working with these images can give
unsatisfactory results when intermediate processing and rendering works in a
linear fashion. This problem can be avoided by using a _Linear Workflow_. This
means that the gamma correction is removed from the images before they are
used for rendering, and reapplied afterwards for display.

### The Document Linear Workflow

The _RDK Document Linear Workflow_ is a document-resident linear workflow
object which affects renderings and viewports. If you have a Rhino document,
you can read and write that document’s linear workflow settings through the
document’s
[IRhRdkLinearWorkflow](https://developer.rhino3d.com/api/cpp/class_i_rh_rdk_linear_workflow.html)
interface. Any changes you make will appear in the Rendering UI and will also
be stored in the 3dm file. Getting the linear workflow from a document always
returns a const reference. To write to the linear workflow, you must begin a
batch of write operations and afterwards end the batch. This is done using the
RDK’s standard BeginChange / EndChange system. The following is an example of
how to access and change the document linear workflow settings:

    
    
    static class CLinearWorkflowExampleCommand : public CRhinoTestCommand
    {
    protected:
    	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
    	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"LinearWorkflowExample"); }
    	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
    }
    theLinearWorkflowExampleCommand;
    
    CRhinoCommand::result CLinearWorkflowExampleCommand::RunCommand(const CRhinoCommandContext& context)
    {
    	auto* pDoc = context.Document();
    	if (nullptr == pDoc)
    		return failure;
    
    	const auto& lw = pDoc->LinearWorkflow();
    
    	RhinoApp().Print(L"LW gamma before: %.1f\n", lw.PreProcessGamma());
    
    	auto& write_lw = lw.BeginChange(RhRdkChangeContext::Program);
    	write_lw.SetPreProcessGamma(3.5f);
    	write_lw.EndChange();
    
    	RhinoApp().Print(L"LW gamma after: %.1f\n", lw.PreProcessGamma());
    
    	return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/rdk-
linear-workflow-classes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/rdk-
linear-workflow-classes/index.md) [
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

