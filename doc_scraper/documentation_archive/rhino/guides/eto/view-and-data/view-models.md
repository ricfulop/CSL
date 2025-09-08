---
url: https://developer.rhino3d.com/guides/eto/view-and-data/view-models/
scraped_at: 2025-09-08T15:43:36.481892
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

[View Models](https://developer.rhino3d.com/guides/eto/view-and-data/view-
models/)

  * What is a View Model?
  * Why are View Models needed?
  * More Reading

View Models

An introduction to View Models

## What is a View Model?

View Models contain the data and logic that accompanies our UI, separating
view logic and model logic keeps our UIs more organised and promotes better
coding.

## Why are View Models needed?

The simplest reason is to keep different things in different places.

#### Examples of View Model data and logic

Notice how none of the properties or methods relate to the UI and focus
entirely on Data and back end.

    
    
    // Data
    internal ObservableCollection<User> Users { get; }
    
    // Methods
    internal void LoadSettings();
    internal void ResetSettings();
    internal void AddUser(User user);
    

#### Examples of view data and logic

Notice that the properties and methods are very much view specific only
relating to the UI.

    
    
    // Data
    private bool IsButtonVisible { get; }
    private static float BorderThickness { get; }
    public Color BackgroundColour { get; }
    
    // Methods
    internal void RedrawView();
    internal void CloseView();
    

## More Reading

  * [Binding Data](https://developer.rhino3d.com/guides/eto/view-and-data/binding/)
  * [Complex Bindings](https://developer.rhino3d.com/guides/eto/view-and-data/complex-bindings/)
  * [Bindings Deep Dive ](https://developer.rhino3d.com/guides/eto/view-and-data/bindings-explained/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/eto/view-
and-data/view-models/_index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/eto/view-
and-data/view-models/_index.md) [ Admin](https://developer.rhino3d.com/admin)

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

