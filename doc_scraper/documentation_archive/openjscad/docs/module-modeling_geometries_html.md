---
url: https://openjscad.xyz/docs/module-modeling_geometries.html
scraped_at: 2025-09-08T16:29:54.254142
title: Untitled
---

Geometries are objects that represent the contents of primitives or the
results of operations. Note: Geometries are considered immutable, so never
change the contents directly.

Source:

    

  * [modeling/src/geometries/index.js](modeling_src_geometries_index.js.html), [line 1](modeling_src_geometries_index.js.html#line1)

See:

    

  * [geom2](global.html#geom2) \- 2D geometry consisting of sides
  * [geom3](global.html#geom3) \- 3D geometry consisting of polygons
  * [path2](global.html#path2) \- 2D geometry consisting of ordered points
  * [poly2](global.html#poly2) \- 2D polygon consisting of ordered vertices
  * [poly3](global.html#poly3) \- 3D polygon consisting of ordered vertices

##### Example

    
    
    const { geom2, geom3, path2, poly2, poly3 } = require('@jscad/modeling').geometries

