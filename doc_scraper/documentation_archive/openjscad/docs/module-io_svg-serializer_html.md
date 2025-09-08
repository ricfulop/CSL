---
url: https://openjscad.xyz/docs/module-io_svg-serializer.html#.serialize
scraped_at: 2025-09-08T16:29:01.026652
title: Untitled
---

Serializer of JSCAD geometries to SVG source (XML).

The serialization of the following geometries are possible.

  * serialization of 2D geometry (geom2) to SVG path (a continous path containing the outlines of the geometry)
  * serialization of 2D geometry (path2) to SVG path

Colors are added to SVG shapes when found on the geometry. Special attributes
(id and class) are added to SVG shapes when found on the geometry.

Source:

    

  * [io/svg-serializer/index.js](io_svg-serializer_index.js.html), [line 19](io_svg-serializer_index.js.html#line19)

##### Example

    
    
    const { serializer, mimeType } = require('@jscad/svg-serializer')

### Methods

#### (static) serialize(options, …objects) → {Array}

Source:

    

  * [io/svg-serializer/index.js](io_svg-serializer_index.js.html), [line 55](io_svg-serializer_index.js.html#line55)

See:

    

  * <https://www.w3.org/TR/SVG/Overview.html>

Serialize the give objects to SVG code (XML).

##### Example

    
    
    const geometry = primitives.square()
    const svgData = serializer({unit: 'mm'}, geometry)

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`options` |  Object |  | options for serialization, REQUIRED

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`unit` |  String |  <optional>  
|  `'mm'` | unit of design; em, ex, px, in, cm, mm, pt, pc  
`statusCallback` |  function |  <optional>  
|  | call back function for progress ({ progress: 0-100 })  
`objects` |  Object | Array |  <repeatable>  
| objects to serialize as SVG  
  
##### Returns:

serialized contents, SVG code (XML string)

Type

     Array

