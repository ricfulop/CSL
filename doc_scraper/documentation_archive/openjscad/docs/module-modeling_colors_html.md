---
url: https://openjscad.xyz/docs/module-modeling_colors.html#.rgbToHsv
scraped_at: 2025-09-08T16:29:23.152527
title: Untitled
---

All shapes (primitives or the results of operations) can be assigned a color
(RGBA). In all cases, the function returns the results, and never changes the
original shapes.

Source:

    

  * [modeling/src/colors/index.js](modeling_src_colors_index.js.html), [line 1](modeling_src_colors_index.js.html#line1)

##### Example

    
    
    const { colorize, hexToRgb } = require('@jscad/modeling').colors

### Members

#### (static, constant) cssColors :Array

Source:

    

  * [modeling/src/colors/cssColors.js](modeling_src_colors_cssColors.js.html), [line 8](modeling_src_colors_cssColors.js.html#line8)

See:

    

  * CSS color table from http://www.w3.org/TR/css3-color/

##### Properties:

Name | Type | Description  
---|---|---  
`black` |  Array |   
`silver` |  Array |   
`gray` |  Array |   
`white` |  Array |   
`maroon` |  Array |   
`red` |  Array |   
`purple` |  Array |   
`fuchsia` |  Array |   
`green` |  Array |   
`lime` |  Array |   
`olive` |  Array |   
`yellow` |  Array |   
`navy` |  Array |   
`blue` |  Array |   
`teal` |  Array |   
`aqua` |  Array |   
`aliceblue` |  Array |   
`antiquewhite` |  Array |   
`aquamarine` |  Array |   
`azure` |  Array |   
`beige` |  Array |   
`bisque` |  Array |   
`blanchedalmond` |  Array |   
`blueviolet` |  Array |   
`brown` |  Array |   
`burlywood` |  Array |   
`cadetblue` |  Array |   
`chartreuse` |  Array |   
`chocolate` |  Array |   
`coral` |  Array |   
`cornflowerblue` |  Array |   
`cornsilk` |  Array |   
`crimson` |  Array |   
`cyan` |  Array |   
`darkblue` |  Array |   
`darkcyan` |  Array |   
`darkgoldenrod` |  Array |   
`darkgray` |  Array |   
`darkgreen` |  Array |   
`darkgrey` |  Array |   
`darkkhaki` |  Array |   
`darkmagenta` |  Array |   
`darkolivegreen` |  Array |   
`darkorange` |  Array |   
`darkorchid` |  Array |   
`darkred` |  Array |   
`darksalmon` |  Array |   
`darkseagreen` |  Array |   
`darkslateblue` |  Array |   
`darkslategray` |  Array |   
`darkslategrey` |  Array |   
`darkturquoise` |  Array |   
`darkviolet` |  Array |   
`deeppink` |  Array |   
`deepskyblue` |  Array |   
`dimgray` |  Array |   
`dimgrey` |  Array |   
`dodgerblue` |  Array |   
`firebrick` |  Array |   
`floralwhite` |  Array |   
`forestgreen` |  Array |   
`gainsboro` |  Array |   
`ghostwhite` |  Array |   
`gold` |  Array |   
`goldenrod` |  Array |   
`greenyellow` |  Array |   
`grey` |  Array |   
`honeydew` |  Array |   
`hotpink` |  Array |   
`indianred` |  Array |   
`indigo` |  Array |   
`ivory` |  Array |   
`khaki` |  Array |   
`lavender` |  Array |   
`lavenderblush` |  Array |   
`lawngreen` |  Array |   
`lemonchiffon` |  Array |   
`lightblue` |  Array |   
`lightcoral` |  Array |   
`lightcyan` |  Array |   
`lightgoldenrodyellow` |  Array |   
`lightgray` |  Array |   
`lightgreen` |  Array |   
`lightgrey` |  Array |   
`lightpink` |  Array |   
`lightsalmon` |  Array |   
`lightseagreen` |  Array |   
`lightskyblue` |  Array |   
`lightslategray` |  Array |   
`lightslategrey` |  Array |   
`lightsteelblue` |  Array |   
`lightyellow` |  Array |   
`limegreen` |  Array |   
`linen` |  Array |   
`magenta` |  Array |   
`mediumaquamarine` |  Array |   
`mediumblue` |  Array |   
`mediumorchid` |  Array |   
`mediumpurple` |  Array |   
`mediumseagreen` |  Array |   
`mediumslateblue` |  Array |   
`mediumspringgreen` |  Array |   
`mediumturquoise` |  Array |   
`mediumvioletred` |  Array |   
`midnightblue` |  Array |   
`mintcream` |  Array |   
`mistyrose` |  Array |   
`moccasin` |  Array |   
`navajowhite` |  Array |   
`oldlace` |  Array |   
`olivedrab` |  Array |   
`orange` |  Array |   
`orangered` |  Array |   
`orchid` |  Array |   
`palegoldenrod` |  Array |   
`palegreen` |  Array |   
`paleturquoise` |  Array |   
`palevioletred` |  Array |   
`papayawhip` |  Array |   
`peachpuff` |  Array |   
`peru` |  Array |   
`pink` |  Array |   
`plum` |  Array |   
`powderblue` |  Array |   
`rosybrown` |  Array |   
`royalblue` |  Array |   
`saddlebrown` |  Array |   
`salmon` |  Array |   
`sandybrown` |  Array |   
`seagreen` |  Array |   
`seashell` |  Array |   
`sienna` |  Array |   
`skyblue` |  Array |   
`slateblue` |  Array |   
`slategray` |  Array |   
`slategrey` |  Array |   
`snow` |  Array |   
`springgreen` |  Array |   
`steelblue` |  Array |   
`tan` |  Array |   
`thistle` |  Array |   
`tomato` |  Array |   
`turquoise` |  Array |   
`violet` |  Array |   
`wheat` |  Array |   
`whitesmoke` |  Array |   
`yellowgreen` |  Array |   
  
##### Type:

  * Array

##### Example

    
    
    let newshape = colorize(cssColors.red, oldshape)

### Methods

#### (static) colorize(color, …objects) → {Object|Array}

Source:

    

  * [modeling/src/colors/colorize.js](modeling_src_colors_colorize.js.html), [line 45](modeling_src_colors_colorize.js.html#line45)

Assign the given color to the given objects.

##### Example

    
    
    let redSphere = colorize([1,0,0], sphere()) // red
    let greenCircle = colorize([0,1,0,0.8], circle()) // green transparent
    let blueArc = colorize([0,0,1], arc()) // blue
    let wildcylinder = colorize(colorNameToRgb('fuchsia'), cylinder()) // CSS color

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`color` |  Array |  | RGBA color values, where each value is between 0 and 1.0  
`objects` |  Object | Array |  <repeatable>  
| the objects of which to apply the given color  
  
##### Returns:

new object, or list of new objects with an additional attribute 'color'

Type

     Object | Array

#### (static) colorNameToRgb(s) → {Array}

Source:

    

  * [modeling/src/colors/colorNameToRgb.js](modeling_src_colors_colorNameToRgb.js.html), [line 12](modeling_src_colors_colorNameToRgb.js.html#line12)

Converts a CSS color name to RGB color.

##### Example

    
    
    let mysphere = colorize(colorNameToRgb('lightblue'), sphere())

##### Parameters:

Name | Type | Description  
---|---|---  
`s` |  String | the CSS color name  
  
##### Returns:

the RGB color, or undefined if not found

Type

     Array

#### (static) hexToRgb(notation) → {Array}

Source:

    

  * [modeling/src/colors/hexToRgb.js](modeling_src_colors_hexToRgb.js.html), [line 12](modeling_src_colors_hexToRgb.js.html#line12)

See:

    

  * <https://www.w3.org/TR/css-color-3/>

Converts CSS color notations (string of hex values) to RGB values.

##### Example

    
    
    let mysphere = colorize(hexToRgb('#000080'), sphere()) // navy blue

##### Parameters:

Name | Type | Description  
---|---|---  
`notation` |  String | color notation  
  
##### Returns:

RGB color values

Type

     Array

#### (static) hslToRgb(…values) → {Array}

Source:

    

  * [modeling/src/colors/hslToRgb.js](modeling_src_colors_hslToRgb.js.html), [line 16](modeling_src_colors_hslToRgb.js.html#line16)

See:

    

  * <http://en.wikipedia.org/wiki/HSL_color_space>

Converts HSL color values to RGB color values.

##### Example

    
    
    let mysphere = colorize(hslToRgb([0.9166666666666666, 1, 0.5]), sphere())

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`values` |  Number | Array |  <repeatable>  
| HSL or HSLA color values  
  
##### Returns:

RGB or RGBA color values

Type

     Array

#### (static) hsvToRgb(…values) → {Array}

Source:

    

  * [modeling/src/colors/hsvToRgb.js](modeling_src_colors_hsvToRgb.js.html), [line 14](modeling_src_colors_hsvToRgb.js.html#line14)

See:

    

  * <http://en.wikipedia.org/wiki/HSV_color_space.>

Converts HSV color values to RGB color values.

##### Example

    
    
    let mysphere = colorize(hsvToRgb([0.9166666666666666, 1, 1]), sphere())

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`values` |  Number | Array |  <repeatable>  
| HSV or HSVA color values  
  
##### Returns:

RGB or RGBA color values

Type

     Array

#### (static) hueToColorComponent(p, q, t) → {Number}

Source:

    

  * [modeling/src/colors/hueToColorComponent.js](modeling_src_colors_hueToColorComponent.js.html), [line 9](modeling_src_colors_hueToColorComponent.js.html#line9)

Convert hue values to a color component (ie one of r, g, b)

##### Parameters:

Name | Type | Description  
---|---|---  
`p` |  Number |   
`q` |  Number |   
`t` |  Number |   
  
##### Returns:

color component

Type

     Number

#### (static) rgbToHex(…values) → {String}

Source:

    

  * [modeling/src/colors/rgbToHex.js](modeling_src_colors_rgbToHex.js.html), [line 10](modeling_src_colors_rgbToHex.js.html#line10)

See:

    

  * <https://www.w3.org/TR/css-color-3/>

Convert the given RGB color values to CSS color notation (string)

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`values` |  Number | Array |  <repeatable>  
| RGB or RGBA color values  
  
##### Returns:

CSS color notation

Type

     String

#### (static) rgbToHsl(…values) → {Array}

Source:

    

  * [modeling/src/colors/rgbToHsl.js](modeling_src_colors_rgbToHsl.js.html), [line 12](modeling_src_colors_rgbToHsl.js.html#line12)

See:

    

  * <http://en.wikipedia.org/wiki/HSL_color_space.>
  * <http://axonflux.com/handy-rgb-to-hsl-and-rgb-to-hsv-color-model-c>

Converts an RGB color value to HSL.

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`values` |  Number | Array |  <repeatable>  
| RGB or RGBA color values  
  
##### Returns:

HSL or HSLA color values

Type

     Array

#### (static) rgbToHsv(…values) → {Array}

Source:

    

  * [modeling/src/colors/rgbToHsv.js](modeling_src_colors_rgbToHsv.js.html), [line 11](modeling_src_colors_rgbToHsv.js.html#line11)

See:

    

  * <http://en.wikipedia.org/wiki/HSV_color_space.>

Converts an RGB color value to HSV.

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`values` |  Number | Array |  <repeatable>  
| RGB or RGBA color values  
  
##### Returns:

HSV or HSVA color values

Type

     Array

