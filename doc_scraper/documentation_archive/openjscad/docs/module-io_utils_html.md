---
url: https://openjscad.xyz/docs/module-io_utils.html#.makeBlob
scraped_at: 2025-09-08T16:29:04.035989
title: Untitled
---

Utility functions of various sorts in support of IO packages.

Source:

    

  * [io/io-utils/index.js](io_io-utils_index.js.html), [line 1](io_io-utils_index.js.html#line1)

##### Example

    
    
    const { BinaryReader } = require('@jscad/io-utils')

### Methods

#### (static) convertToBlob(input) → {[Blob](Blob.html)}

Source:

    

  * [io/io-utils/convertToBlob.js](io_io-utils_convertToBlob.js.html), [line 16](io_io-utils_convertToBlob.js.html#line16)

Convert the given input into a BLOB of data for export.

##### Example

    
    
    const blob1 = convertToBlob({ data: ['test'], mimeType: 'text/plain' })
    const blob2 = convertToBlob({ data: [Int32Array.from('12345').buffer], mimeType: 'application/mine' })

##### Parameters:

Name | Type | Description  
---|---|---  
`input` |  Object | input object to convert

###### Properties

| Name | Type | Description  
---|---|---  
`data` |  Array | array of data to be inserted into the blob, either String or ArrayBuffer  
`mimeType` |  String | mime type of the data to be inserted  
  
##### Returns:

a new Blob

Type

     [Blob](Blob.html)

#### (static) makeBlob() → {function}

Source:

    

  * [io/io-utils/makeBlob.js](io_io-utils_makeBlob.js.html), [line 11](io_io-utils_makeBlob.js.html#line11)

Make a constructor for Blob objects.

##### Example

    
    
    const Blob = makeBlob()
    const ablob = new Blob(data, { type: mimeType })

##### Returns:

constructor of Blob objects

Type

     function

