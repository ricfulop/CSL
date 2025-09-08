---
url: https://docs.blender.org/api/current/bpy.ops.surface.html
scraped_at: 2025-09-08T14:18:52.694517
title: Surface Operators¶
---

# Surface Operators¶

bpy.ops.surface.primitive_nurbs_surface_circle_add(_*_ , _radius =1.0_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Nurbs surface Circle

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.surface.primitive_nurbs_surface_curve_add(_*_ , _radius =1.0_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Nurbs surface Curve

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.surface.primitive_nurbs_surface_cylinder_add(_*_ , _radius =1.0_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Nurbs surface Cylinder

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.surface.primitive_nurbs_surface_sphere_add(_*_ , _radius =1.0_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Nurbs surface Sphere

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.surface.primitive_nurbs_surface_surface_add(_*_ , _radius =1.0_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Nurbs surface Patch

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

bpy.ops.surface.primitive_nurbs_surface_torus_add(_*_ , _radius =1.0_,
_enter_editmode =False_, _align =WORLD_, _location =(0.0, 0.0, 0.0)_,
_rotation =(0.0, 0.0, 0.0)_, _scale =(0.0, 0.0, 0.0)_)¶

    

Construct a Nurbs surface Torus

Parameters:

    

  * **radius** (_float in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Radius

  * **enter_editmode** (_boolean_ _,__(__optional_ _)_) – Enter Edit Mode, Enter edit mode when adding this object

  * **align** (enum in [`WORLD`, `VIEW`, `CURSOR`], (optional)) – 

Align, The alignment of the new object

    * `WORLD` World – Align the new object to the world.

    * `VIEW` View – Align the new object to the view.

    * `CURSOR` 3D Cursor – Use the 3D cursor orientation for the new object.

  * **location** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Location, Location for the newly added object

  * **rotation** ([`mathutils.Euler`](mathutils.html#mathutils.Euler "mathutils.Euler") rotation of 3 items in [-inf, inf], (optional)) – Rotation, Rotation for the newly added object

  * **scale** ([`mathutils.Vector`](mathutils.html#mathutils.Vector "mathutils.Vector") of 3 items in [-inf, inf], (optional)) – Scale, Scale for the newly added object

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

