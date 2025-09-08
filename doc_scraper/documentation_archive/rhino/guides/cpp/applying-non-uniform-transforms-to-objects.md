---
url: https://developer.rhino3d.com/guides/cpp/applying-non-uniform-transforms-to-objects/
scraped_at: 2025-09-08T15:38:44.362962
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

[Applying Non-Uniform Transformations to
Objects](https://developer.rhino3d.com/guides/cpp/applying-non-uniform-
transforms-to-objects/)

  * Discussion

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Applying Non-Uniform Transformations to Objects

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Discussion

Imagine you are trying to apply a non-uniform scale to a cylinder. If the same
scale operation is applied to another object type, it works as expected; but
not a cylinder. Why?

Not all `ON_Geometry` derived classes can be can be accurately modified with
“squishy” transformations like projections, shears, an non-uniform scaling.
For example, if you were to apply a non-uniform scale to a circle, which is
represented by an `ON_ArcCurve` curve, the resulting geometry is no longer a
circle.

Before transforming your object, you will want to first test to see if the the
transformation is a similarity transformation. This can be done by using
`ON_XForm::IsSimilarity()`. See _opennurbs_xform.h_ for more information.

If the transformation is not a similarity, then you should convert the
geometry into a form that can be accurately modified. This can be done by
using the `ON_Geometry::MakeDeformable()` override on the geometric object.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/applying-
non-uniform-transforms-to-objects/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/applying-
non-uniform-transforms-to-objects/index.md) [
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

