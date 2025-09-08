---
url: https://developer.rhino3d.com/guides/cpp/rdk-contents-classes/
scraped_at: 2025-09-08T15:40:28.785931
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

[RDK Document Contents](https://developer.rhino3d.com/guides/cpp/rdk-contents-
classes/)

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

RDK Document Contents

__

Windows only

by [John Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated:
Tuesday, August 11, 2020)

The _RDK Document Contents_ is an object that enables the plug-in developer to
perform certain operations on document-resident [Render
Contents](https://developer.rhino3d.com/guides/cpp/rdk-render-content/) (AKA
‘Contents’). It is particularly useful for attaching contents to a document
and finding contents by their instance ids. If you have a Rhino document, you
can read and modify that document’s contents through the document’s
[IRhRdkContents](https://developer.rhino3d.com/api/cpp/class_i_rh_rdk_contents.html)
interface. Any changes you make will appear in the relevant editor and will
also be stored in the 3dm file. Getting the contents from a document always
returns a const reference. To write to the contents, you must begin a batch of
write operations and afterwards end the batch. This is done using the RDK’s
standard BeginChange / EndChange system. The following is an example of how to
access the document contents:

    
    
    static class CTestContents : public CRhinoTestCommand
    {
    protected:
    	virtual UUID CommandUUID() override { static const UUID uuid = your_uuid_here; return uuid; }
    	virtual const wchar_t* EnglishCommandName() override { return RHSTR_LIT(L"ContentsExample"); }
    	virtual CRhinoCommand::result RunCommand(const CRhinoCommandContext& context) override;
    }
    theContentsExampleCommand;
    
    CRhinoCommand::result CTestContents::RunCommand(const CRhinoCommandContext& context)
    {
    	auto* pDoc = context.Document();
    	if (nullptr == pDoc)
    		return failure;
    
    	const auto& contents = pDoc->Contents();
    
    	// Create a new basic material.
    	ON_Material mat;
    	auto* pMaterial = ::RhRdkNewBasicMaterial(mat, pDoc);
    	if (nullptr == pMaterial)
    		return failure;
    
    	// Attach it to the document.
    	auto& write_contents = contents.BeginChange(RhRdkChangeContext::Program);
    	write_contents.Attach(*pMaterial);
    	write_contents.EndChange();
    
    	// Find the material in the document.
    	const auto* pFound = contents.Find(pMaterial->InstanceId());
    
    	ASSERT((nullptr != pFound) && (pFound->InstanceId() == pMaterial->InstanceId()));
    
    	return success;
    }
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/rdk-
contents-classes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/rdk-
contents-classes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

