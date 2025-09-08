---
url: https://developer.rhino3d.com/guides/rhinoscript/converting-to-grayscale/
scraped_at: 2025-09-08T15:42:38.352295
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

[Converting to
Grayscale](https://developer.rhino3d.com/guides/rhinoscript/converting-to-
grayscale/)

  * Overview
  * Example

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) /

Converting to Grayscale

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Overview

To convert any color to a grayscale representation of its luminance, first one
must obtain the values of its red, green, and blue (RGB) primaries in linear
intensity encoding, by gamma expansion. Then, add together 30% of the red
value, 59% of the green value, and 11% of the blue value. The resultant number
is the desired linear luminance value; it typically needs to be gamma
compressed to get back to a conventional grayscale representation.

## Example

The following example demonstrates the above algorithm…

    
    
    Option Explicit
    
    Sub ConvertLayersToGrayscale()
    
      ' Declare local variables
      Dim arrLayers, strLayer, lngColor
      Dim nGray, nRed, nGreen, nBlue
    
      ' Turn off screen redrawing (for performance)
      Call Rhino.EnableRedraw(False)
    
      ' Get all of the layers in the document
      arrLayers = Rhino.LayerNames
    
      ' Process each layer one-by-one
      For Each strLayer In arrLayers
    
        ' Get the layer's color
        lngColor = Rhino.LayerColor(strLayer)
    
        ' Get the color's red-green-blue components
        nRed = Rhino.ColorRedValue(lngColor)
        nGreen = Rhino.ColorGreenValue(lngColor)
        nBlue = Rhino.ColorBlueValue(lngColor)
    
        ' Calculate the grayscale based on the NTSC color gamut
        nGray = CByte(nRed * 0.30) + CByte(nGreen * 0.59) + CByte(nBlue * 0.11)
    
        ' Modify the layer's color
        Call Rhino.LayerColor(strlayer, RGB(nGray, nGray, nGray))
    
      Next
    
      ' Turn on screen redrawing
      Call Rhino.EnableRedraw(True)
    
    End Sub
    

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/converting-
to-grayscale/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/converting-
to-grayscale/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

