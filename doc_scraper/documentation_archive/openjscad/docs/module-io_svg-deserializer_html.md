---
url: https://openjscad.xyz/docs/module-io_svg-deserializer.html#.deserialize
scraped_at: 2025-09-08T16:28:59.020171
title: Untitled
---

Deserializer of SVG source data to JSCAD geometries.

Source:

    

  * [io/svg-deserializer/src/index.js](io_svg-deserializer_src_index.js.html), [line 26](io_svg-deserializer_src_index.js.html#line26)

See:

    

  * [README](https://github.com/jscad/OpenJSCAD.org/blob/master/packages/io/svg-deserializer/README.md) for supported conversion of SVG elements.

##### Example

    
    
    const { deserializer, extension } = require('@jscad/svg-deserializer')

### Methods

#### (static) deserialize(options, input) → {Array|String}

Source:

    

  * [io/svg-deserializer/src/index.js](io_svg-deserializer_src_index.js.html), [line 50](io_svg-deserializer_src_index.js.html#line50)

See:

    

  * [SVG Specification](https://www.w3.org/TR/SVG/intro.html)

Deserialize the given SVG source into either a script or an array of
geometries

##### Parameters:

Name | Type | Description  
---|---|---  
`options` |  Object | options used during deserializing, REQUIRED

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`addMetadata` |  boolean |  <optional>  
|  `true` | toggle injection of metadata at the start of the script  
`filename` |  string |  <optional>  
|  `'svg'` | filename of original SVG source  
`output` |  string |  <optional>  
|  `'script'` | either 'script' or 'geometry' to set desired output  
`pxPmm` |  float |  <optional>  
|  | custom pixels per mm unit  
`segments` |  integer |  <optional>  
|  | number of segments for rounded shapes  
`target` |  string |  <optional>  
|  | target 2D geometry; 'geom2' or 'path2'  
`version` |  string |  <optional>  
|  `'0.0.0'` | version number to add to the metadata  
`pathSelfClosed` |  string |  <optional>  
|  `'error'` | [error||trim||split] if path self-closes with one of commands without stop command right after  
`input` |  string | SVG source data  
  
##### Returns:

either an array of objects (geometry) or a string (script)

Type

     Array | String

