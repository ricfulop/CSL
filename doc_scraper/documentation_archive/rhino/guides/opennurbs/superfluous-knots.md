---
url: https://developer.rhino3d.com/guides/opennurbs/superfluous-knots/
scraped_at: 2025-09-08T15:38:16.247566
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

[Superfluous
Knots](https://developer.rhino3d.com/guides/opennurbs/superfluous-knots/)

  * Question
  * Answer

[Guides](https://developer.rhino3d.com/en/guides/) / [openNURBS and rhino3dm
Guides](https://developer.rhino3d.com/en/guides/opennurbs/) /

Superfluous Knots

by [Dale Lear](https://discourse.mcneel.com/u/dalelear/) (Last updated:
Wednesday, December 5, 2018)

## Question

How is the representation of knot vector in openNURBS different from that in
OpenGL’s NURBS renderer? In openNURBS, the formula is:

$$m = n + p - 2 $$

where m is the number of knots in the knot vector; n is the number of control
points; p is the order of the curve.

While in OpenGL, the formula is:

$$m = n + p$$

So, in OpenGL, there are two additional knots required to draw a NURBS curve.

Could you explain how the two knot values are calculated? And, why openNURBS
adopted a representation different from most NURBS books?

## Answer

The knots are superfluous because they are not used in NURBS evaluation and
they make it appear the first and last spans are different from interior
spans.

If you grab a pencil and paper and work through the details you will
understand why dragging around and setting these two knot values is a waste of
time and adds needless complications to NURBS evaluation, NURBS degree
changing, NURBS knot insertion/deletion, NURBS span conversion to/from bezier,
NURBS periodic closure, NURBS curve fitting, etc., algorithms. If you look at
the openNURBS evaluation source code, you will see no knot juggling; it’s just
a simple computationally efficient calculation.

One reason some mathematical texts on NURBS, like Carl DeBoor’s b-splines,
have the extra knots is that it makes proving the theorems easier because it
means that the recursive b-spline basis function definition DeBoor uses is
well defined for degree zero b-splines. DeBoor’s use of the recursive
definition of the basis functions is elegant and having the extra knot values
along helps make them elegant.

There is no good reason for modern computer code or text books focused solely
on computer aided applications of NURBS to drag this kind of theoretical
baggage along. Having modern code drag these knot values around is akin to
having Excel store prime factors of integer cell entries and requiring Excel
add-in developers to compute the factorization. Prime factorization is
fundamental to understanding how integers work and it is interesting to people
that it interests, but it is not required if all you are trying to do is
add/subtract/multiply integers in spreadsheet cells.

Why the creators of the OpenGL specification, IGES NURBS specification, and
STEP NURBS specification decided to store two useless values in their knot
vectors is a mystery to us.

Rhino and openNURBS are not the only applications and toolkits that don’t
carry around the extra knots. The older versions of Alias and ACIS that we are
familiar with do not have the extra knots.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/opennurbs/superfluous-
knots/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/opennurbs/superfluous-
knots/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

