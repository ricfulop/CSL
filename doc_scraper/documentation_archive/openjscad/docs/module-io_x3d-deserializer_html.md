---
url: https://openjscad.xyz/docs/module-io_x3d-deserializer.html#.deserialize
scraped_at: 2025-09-08T16:29:06.056753
title: Untitled
---

Deserializer of X3D source data (XML) to JSCAD geometries.

Source:

    

  * [io/x3d-deserializer/src/index.js](io_x3d-deserializer_src_index.js.html), [line 16](io_x3d-deserializer_src_index.js.html#line16)

See:

    

  * [README](https://github.com/jscad/OpenJSCAD.org/blob/master/packages/io/x3d-deserializer/README.md) for supported conversion of X3D entities.

##### Example

    
    
    const { deserializer, extension } = require('@jscad/x3d-deserializer')

### Methods

#### (static) deserialize(optionsopt, input) → {Array|String}

Source:

    

  * [io/x3d-deserializer/src/index.js](io_x3d-deserializer_src_index.js.html), [line 43](io_x3d-deserializer_src_index.js.html#line43)

See:

    

  * [X3D File Format](https://www.web3d.org/documents/specifications/19776-1/V3.3/index.html)
  * README for supported conversions.

Deserialize the given X3D source (XML Encoding) into either a script or an
array of geometry

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`options` |  Object |  <optional>  
| options used during deserializing

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`filename` |  String |  <optional>  
|  `'x3d'` | filename of original X3D source  
`output` |  String |  <optional>  
|  `'script'` | either 'script' or 'geometry' to set desired output  
`version` |  String |  <optional>  
|  | version added to the script metadata, default is package version  
`addMetadata` |  Boolean |  <optional>  
|  `true` | toggle injection of metadata at the start of the script  
`input` |  String |  | X3D source data (XML)  
  
##### Returns:

either an array of objects (geometry) or a string (script)

Type

     Array | String

