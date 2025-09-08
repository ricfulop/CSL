---
url: https://developer.rhino3d.com/guides/cpp/rdk-task-classes/
scraped_at: 2025-09-08T15:40:37.901066
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

[RDK Tasks](https://developer.rhino3d.com/guides/cpp/rdk-task-classes/)

  * Introduction
  * Registering custom tasks

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

RDK Tasks

__

Windows only

by [John Croudy](https://discourse.mcneel.com/u/johnc/) (Last updated: Monday,
February 4, 2019)

### Introduction

![Task](https://developer.rhino3d.com/images/rdk-tasks.png) An RDK _task_
encapsulates the functionality of any operation the user can perform by
clicking a menu item or pressing a key in a Render Content Editor. For
example, when the user right-clicks in the preview area of such an editor, a
context menu is displayed with commands such as ‘Assign to Objects’ and
‘Delete’. All of these menu items are implemented by tasks, derived from
[CRhRdkTask](https://developer.rhino3d.com/api/cpp/class_c_rh_rdk_task.html).
To make it easy for plug-in developers to add their own tasks to these menus,
the RDK provides the class
[CRhRdkCustomTask](https://developer.rhino3d.com/api/cpp/class_c_rh_rdk_custom_task.html).
The developer only has to implement a subclass of this and then register the
subclass with the RDK. An example of how to do this is shown below. Tasks use
an interface called
[IRhRdkTaskOrigin](https://developer.rhino3d.com/api/cpp/class_i_rh_rdk_task_origin.html)
which represents the place in the UI where the user clicked to invoke the
menu. Among other things, this interface allows the task to get the contents
that are currently selected in the UI. These are the contents that the user
wants to perform an operation on.

### Registering custom tasks

To register a custom task, you first need to derive a class from
CRhRdkCustomTask. You provide a menu _string_ that is displayed to the user, a
menu _order_ which tells the RDK where on the menu to put the item, and one
(or optionally two) _icons_. You also implement an Update() method and an
Execute() method.

    
    
    class CExampleCustomTask : public CRhRdkCustomTask
    {
    public:
    	virtual UUID Id(void) const override { static const UUID uuid = your_uuid_here; return uuid; }
    	virtual UUID PlugInId(void) const final override { return your_plug_in_uuid_here; }
    	virtual bool IsEnabled(const IRhRdkTaskOrigin& origin) const override { return true; }
    	virtual const wchar_t* MenuString(const IRhRdkTaskOrigin&, CRhRdkContent::Kinds)
    	                                 const override { return L"Example Custom Task"; }
    	virtual bool IconOut(CRhRdkContent::Kinds kind, int w, int h, OUT CRhinoDib& dib)
    	                     const override { return false; }
    	virtual bool IconIn(CRhRdkContent::Kinds kind, int w, int h, OUT CRhinoDib& dib) const override;
    	virtual void Update(IRhRdkTaskUpdate& tu) const override;
    	virtual Result Execute(const IRhRdkTaskOrigin&) const override;
    	virtual int MenuOrder(const IRhRdkTaskOrigin& origin) const override;
    };
    
    int  CExampleCustomTask::MenuOrder(const IRhRdkTaskOrigin& origin) const
    {
    	// This value should be below 100 to make your task appear
    	// before all the RDK's tasks, and above 10,000 to make it
    	// appear below all the RDK's tasks. After that, simply use
    	// numbers in the order you want the tasks to appear.
    	return 10;
    }
    
    bool CExampleCustomTask::IconIn(CRhRdkContent::Kinds kind, int width, int height, OUT CRhinoDib& dib) const
    {
    	// Depending on the 'kind' you might want to use different icons.
    	// Use the supplied 'width' and 'height' to load an icon by
    	// whatever means your platform allows, and set the icon into
    	// the supplied 'dib'. The following just uses a simple check mark.
    	return ::RhRdkGetMenuIcon(RhRdkMenuIcons::Check, ON_2iSize(width, height), dib);
    }
    
    void CExampleCustomTask::Update(IRhRdkTaskUpdate& tu) const override
    {
    	// This is called when the user opens the menu. Here you can set if the
    	// item is enabled or disabled, and if the item is checked or checked
    	// like a radio button. Note that there is also an IsEnabled() method
    	// on the task. Update() is only called if IsEnabled() returns true.
    	// Generally it is best to have IsEnabled() return true and implement
    	// Update() for finer control.
    	tu.SetIsChecked(...);
    	// or
    	tu.SetRadio(...);
    
    	tu.SetIsEnabled(...);
    }
    
    CRhRdkTask::Result CExampleCustomTask::Execute(const IRhRdkTaskOrigin& origin) const
    {
    	// This is called when the user chooses the menu item associated with this task.
    	CRhRdkContentArray aContent;
    	origin.GetSelection(aContent);
    	for (int i = 0; i < aContent.Count(); i++)
    	{
    		const auto sName = aContent[i]->InstanceName();
    		RhinoApp().Print(L"Selected: %s\n", static_cast<const wchar_t*>(sName));
    	}
    
    	return Result::Success;
    }
    

Finally, in your override of `CRhRdkPlugIn::RegisterExtensions()`, you need to
register your custom task as an RDK extension:

    
    
    void CMyRdkPlugIn::RegisterExtensions(void) const
    {
    	...
    	AddExtension(new CExampleCustomTask);
    	...
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/rdk-
task-classes/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/rdk-
task-classes/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

