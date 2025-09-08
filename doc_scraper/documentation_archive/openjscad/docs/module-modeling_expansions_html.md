---
url: https://openjscad.xyz/docs/module-modeling_expansions.html#.offset
scraped_at: 2025-09-08T16:29:33.220748
title: Untitled
---

All shapes (primitives or the results of operations) can be expanded (or
contracted.) In all cases, the function returns the results, and never changes
the original shapes.

Source:

    

  * [modeling/src/operations/expansions/index.js](modeling_src_operations_expansions_index.js.html), [line 1](modeling_src_operations_expansions_index.js.html#line1)

##### Example

    
    
    const { expand, offset } = require('@jscad/modeling').expansions

### Methods

#### (static) expand(options, …objects) → {Object|Array}

Source:

    

  * [modeling/src/operations/expansions/expand.js](modeling_src_operations_expansions_expand.js.html), [line 29](modeling_src_operations_expansions_expand.js.html#line29)

Expand the given geometry using the given options. Both internal and external
space is expanded for 2D and 3D shapes.

Note: Contract is expand using a negative delta.

##### Example

    
    
    let newarc = expand({delta: 5, corners: 'edge'}, arc({}))
    let newsquare = expand({delta: 5, corners: 'chamfer'}, square({size: 30}))
    let newcuboid = expand({delta: 2, corners: 'round'}, cuboid({size: [20, 25, 5]}))

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`options` |  Object |  | options for expand

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`delta` |  Number |  <optional>  
|  `1` | delta (+/-) of expansion  
`corners` |  String |  <optional>  
|  `'edge'` | type of corner to create after expanding; edge, chamfer, round  
`segments` |  Integer |  <optional>  
|  `16` | number of segments when creating round corners  
`objects` |  Objects |  <repeatable>  
| the geometries to expand  
  
##### Returns:

new geometry, or list of new geometries

Type

     Object | Array

#### (static) offset(options, …objects) → {Object|Array}

Source:

    

  * [modeling/src/operations/expansions/offset.js](modeling_src_operations_expansions_offset.js.html), [line 23](modeling_src_operations_expansions_offset.js.html#line23)

Create offset geometry from the given geometry using the given options.
Offsets from internal and external space are created.

##### Example

    
    
    let small = offset({ delta: -4, corners: 'chamfer' }, square({size: 40})) // contract

##### Parameters:

Name | Type | Attributes | Description  
---|---|---|---  
`options` |  Object |  | options for offset

###### Properties

| Name | Type | Attributes | Default | Description  
---|---|---|---|---  
`delta` |  Float |  <optional>  
|  `1` | delta of offset (+ to exterior, - from interior)  
`corners` |  String |  <optional>  
|  `'edge'` | type of corner to create after offseting; edge, chamfer, round  
`segments` |  Integer |  <optional>  
|  `16` | number of segments when creating round corners  
`objects` |  Object |  <repeatable>  
| the geometries to offset  
  
##### Returns:

new geometry, or list of new geometries

Type

     Object | Array

