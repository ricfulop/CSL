---
url: https://openjscad.xyz/docs/module-io_amf-deserializer.html#.deserialize
scraped_at: 2025-09-08T16:28:55.001921
title: Untitled
---

Deserializer of AMF source data (XML) to JSCAD geometries.

Source:

    

  * [io/amf-deserializer/src/index.js](io_amf-deserializer_src_index.js.html), [line 17](io_amf-deserializer_src_index.js.html#line17)

See:

    

  * [README](https://github.com/jscad/OpenJSCAD.org/blob/master/packages/io/amf-deserializer/README.md) for supported conversion of AMF objects.

##### Example

    
    
    const { deserializer, extension } = require('@jscad/amf-serializer')

### Methods

#### (static) deserialize(options, input) → {Array|String}

Source:

    

  * [io/amf-deserializer/src/index.js](io_amf-deserializer_src_index.js.html), [line 44](io_amf-deserializer_src_index.js.html#line44)

See:

    

  * [AMF File Format](https://en.wikipedia.org/wiki/Additive_manufacturing_file_format)
  * README for supported conversions

Deserialize the given AMF source (XML) into either a script or an array of
geometry

##### Parameters:

Name | Type | Description  
---|---|---  
`options` |  Object | options used during deserializing

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`filename` |  String |  <optional>  
|  `'amf'` | filename of original AMF source  
`output` |  String |  <optional>  
|  `'script'` | either 'script' or 'geometry' to set desired output  
`version` |  String |  <optional>  
|  | version added to the script metadata, default is package version  
`addMetadata` |  Boolean |  <optional>  
|  `true` | toggle injection of metadata at the start of the script  
`input` |  String | AMF source data (XML)  
  
##### Returns:

either an array of objects (geometry) or a string (script)

Type

     Array | String

