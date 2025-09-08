---
url: https://developer.rhino3d.com/guides/cpp/light-attenuation/
scraped_at: 2025-09-08T15:40:42.743773
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

[Light Attenuation](https://developer.rhino3d.com/guides/cpp/light-
attenuation/)

  * Problem
  * Solution
  * Types of Attenuation
    * Constant
    * Linear
    * Quadratic

[Guides](https://developer.rhino3d.com/en/guides/) / [C/C++
Guides](https://developer.rhino3d.com/en/guides/cpp/) /

Light Attenuation

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Problem

So you are interested in taking advantage `ON_Light::Attenuation` in your
render plugin, and you need to clarify how you can use it. Is the input vector
supposed to represent the distance over which you want the light to attenuate
to zero?

## Solution

Light attenuation determines how fast the light intensity decreases with
distance from objects.

The three coefficients to light attenuation are:

  1. Constant attenuation ( $$C$$)
  2. Linear attenuation ( $$L$$)
  3. Quadratic attenuation ( $$Q$$)

Thus, you could create the input vector as follows:

    
    
    ON_3dVector attenuation( C, L, Q );
    

**NOTE** : Rhino’s user interface only uses constant attenuation so that
adding a light reveals everything, no matter how far away the light source is
from any given piece of geometry.

## Types of Attenuation

### Constant

If you want constant attenuation, or:

$$1 \over C$$

then both $$L$$ and $$Q$$ must be $$0$$ and $$C > 0$$ (usually $$= 1.0$$).

### Linear

If you want linear attenuation:

$$1 \over C + dL$$

where $$d$$ = distance to light, then $$C$$ and $$L$$ vary and $$Q$$ must be
$$0$$.

### Quadratic

If you want quadratic attenuation:

$$1 \over C + dL + d^{2Q}$$

then all 3 coefficients can and should vary.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/cpp/light-
attenuation/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/cpp/light-
attenuation/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

