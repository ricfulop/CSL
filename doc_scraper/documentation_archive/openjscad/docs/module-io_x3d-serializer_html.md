---
url: https://openjscad.xyz/docs/module-io_x3d-serializer.html#.serialize
scraped_at: 2025-09-08T16:29:08.103970
title: Untitled
---

Serializer of JSCAD geometries to X3D source data (XML).

The serialization of the following geometries are possible.

  * serialization of 3D geometries (geom3) to X3D IndexedTriangleSet (a unique mesh containing coordinates)
  * serialization of 2D geometries (geom2) to X3D Polyline2D
  * serialization of 2D paths (path2) to X3D Polyline2D

Material (color) is added to X3D shapes when found on the geometry.

Source:

    

  * [io/x3d-serializer/src/index.js](io_x3d-serializer_src_index.js.html), [line 19](io_x3d-serializer_src_index.js.html#line19)

##### Example

    
    
    const { serializer, mimeType } = require('@jscad/x3d-serializer')

### Methods

#### (static) serialize(options, …objects) → {Array}

Source:

    

  * [io/x3d-serializer/src/index.js](io_x3d-serializer_src_index.js.html), [line 65](io_x3d-serializer_src_index.js.html#line65)

Serialize the give objects to X3D elements (XML).

##### Example

    
    
    const geometry = primitives.cube()
    const x3dData = serializer({unit: 'meter'}, geometry)

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`options` |  Object |  | options for serialization, REQUIRED

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`color` |  Array |  <optional>  
|  `[0,0,1,1]` | default color for objects  
`shininess` |  Number |  <optional>  
|  `8/256` | x3d shininess for specular highlights  
`smooth` |  Boolean |  <optional>  
|  `false` | use averaged vertex normals  
`decimals` |  Number |  <optional>  
|  `1000` | multiplier before rounding to limit precision  
`metadata` |  Boolean |  <optional>  
|  `true` | add metadata to 3MF contents, such at CreationDate  
`unit` |  String |  <optional>  
|  `'millimeter'` | unit of design; millimeter, inch, feet, meter or micrometer  
`statusCallback` |  function |  <optional>  
|  | call back function for progress ({ progress: 0-100 })  
`objects` |  Object | Array |  <repeatable>  
| objects to serialize as X3D  
  
##### Returns:

serialized contents, X3D format (XML)

Type

     Array

