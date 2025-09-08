---
url: https://openjscad.xyz/docs/module-io_amf-serializer.html#.serialize
scraped_at: 2025-09-08T16:28:57.009742
title: Untitled
---

Serializer of JSCAD geometries to AMF source data (XML)

The serialization of the following geometries are possible.

  * serialization of 3D geometry (geom3) to AMF object (a unique mesh containing both vertices and volumes)

Colors are added to volumes when found on the 3D geometry. Colors are added to
triangles when found on individual polygons.

Source:

    

  * [io/amf-serializer/index.js](io_amf-serializer_index.js.html), [line 22](io_amf-serializer_index.js.html#line22)

##### Example

    
    
    const { serializer, mimeType } = require('@jscad/amf-serializer')

### Methods

#### (static) serialize(options, …objects) → {Array}

Source:

    

  * [io/amf-serializer/index.js](io_amf-serializer_index.js.html), [line 56](io_amf-serializer_index.js.html#line56)

Serialize the give objects (geometry) to AMF source data (XML).

##### Example

    
    
    const geometry = primitives.cube()
    const amfData = serializer({unit: 'meter'}, geometry)

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`options` |  Object |  | options for serialization

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`unit` |  String |  <optional>  
|  `'millimeter'` | unit of design; millimeter, inch, feet, meter or micrometer  
`statusCallback` |  function |  <optional>  
|  | call back function for progress ({ progress: 0-100 })  
`objects` |  Object |  <repeatable>  
| objects to serialize into AMF source data  
  
##### Returns:

serialized contents, AMF source data(XML)

Type

     Array

