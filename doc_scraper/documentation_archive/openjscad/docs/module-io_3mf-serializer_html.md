---
url: https://openjscad.xyz/docs/module-io_3mf-serializer.html#~serialize
scraped_at: 2025-09-08T16:28:52.984186
title: Untitled
---

Serializer of JSCAD geometries to 3D manufacturing format (XML)

The serialization of the following geometries are possible.

  * serialization of 3D geometry (geom3) to 3MF object (a unique mesh containing both vertices and triangles)

Colors are added to base materials when found on the 3D geometry, i.e.
attribute color. Names are added to meshs when found on the 3D geometry, i.e.
attribute name.

Source:

    

  * [io/3mf-serializer/src/index.js](io_3mf-serializer_src_index.js.html), [line 19](io_3mf-serializer_src_index.js.html#line19)

##### Example

    
    
    const { serializer, mimeType } = require('@jscad/3mf-serializer')

### Methods

#### (inner) serialize(optionsopt, …objects) → {Array}

Source:

    

  * [io/3mf-serializer/src/index.js](io_3mf-serializer_src_index.js.html), [line 58](io_3mf-serializer_src_index.js.html#line58)

See:

    

  * <https://3mf.io/specification/>

Serialize the give objects to 3MF contents (XML) or 3MF packaging (OPC).

##### Example

    
    
    const geometry = primitives.cube()
    const package = serializer({unit: 'meter'}, geometry) // 3MF package, ZIP format

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`options` |  Object |  <optional>  
| options for serialization

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`unit` |  String |  <optional>  
|  `'millimeter'` | unit of design; millimeter, inch, feet, meter or micrometer  
`metadata` |  Boolean |  <optional>  
|  `true` | add metadata to 3MF contents, such at CreationDate  
`defaultcolor` |  Array |  <optional>  
|  `[0,0,0,1]` | default color for objects  
`compress` |  Boolean |  <optional>  
|  `true` | package and compress the contents  
`objects` |  Object | Array |  <repeatable>  
| objects to serialize into 3D manufacturing format  
  
##### Returns:

serialized contents, 3MF contents (XML) or 3MF packaging (ZIP)

Type

     Array

