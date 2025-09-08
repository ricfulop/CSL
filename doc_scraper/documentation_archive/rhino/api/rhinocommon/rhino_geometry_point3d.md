---
url: https://developer.rhino3d.com/api/rhinocommon/rhino.geometry.point3d
scraped_at: 2025-09-08T16:06:50.590471
title: Untitled
---

[_home_](/api/rhinocommon/)

/

[Rhino.Geometry](/api/rhinocommon/rhino.geometry)

/

Point3d

# Point3d struct

Represents the three coordinates of a point in three-dimensional space, using
**double** -precision floating point values.

  
_Derived Classes:_

_Namespace:[Rhino.Geometry](/api/rhinocommon/rhino.geometry)_  
 _Point3d:[references](/api/rhinocommon/references/rhino.geometry.point3d)_

 _keyboard_arrow_down_

Constructors (5)

[**Point3d**(double x, double y, double z) Initializes a new point by defining
the X, Y and Z
coordinates.](/api/rhinocommon/rhino.geometry.point3d/point3d#\(double,double,double\))

* * *

[**Point3d**(Point3d point) Initializes a new point by copying coordinates
from another
point.](/api/rhinocommon/rhino.geometry.point3d/point3d#\(point3d\))

* * *

[**Point3d**(Point3f point) Initializes a new point by copying coordinates
from a single-precision
point.](/api/rhinocommon/rhino.geometry.point3d/point3d#\(point3f\))

* * *

[**Point3d**(Point4d point) Initializes a new point by copying coordinates
from a four-dimensional point. The first three coordinates are divided by the
last one. If the W (fourth) dimension of the input point is zero, then it will
be just
discarded.](/api/rhinocommon/rhino.geometry.point3d/point3d#\(point4d\))

* * *

[**Point3d**(Vector3d vector) Initializes a new point by copying coordinates
from the components of a
vector.](/api/rhinocommon/rhino.geometry.point3d/point3d#\(vector3d\))

* * *

_keyboard_arrow_down_

Properties (9)

[**IsValid** Each coordinate of the point must pass the
<b>RhinoMath.IsValidDouble</b>
test.](/api/rhinocommon/rhino.geometry.point3d/isvalid#)

* * *

[**Item** Gets or sets an indexed coordinate of this
point.](/api/rhinocommon/rhino.geometry.point3d/item#)

* * *

[**MaximumCoordinate** Gets the largest (both positive and negative) valid
coordinate in this point, or RhinoMath.UnsetValue if no coordinate is valid,
as an absolute
value.](/api/rhinocommon/rhino.geometry.point3d/maximumcoordinate#)

* * *

[**MinimumCoordinate** Gets the smallest (both positive and negative)
coordinate value in this
point.](/api/rhinocommon/rhino.geometry.point3d/minimumcoordinate#)

* * *

[**Origin** Gets the value of a point at location
0,0,0.](/api/rhinocommon/rhino.geometry.point3d/origin#)

* * *

[**Unset** Gets the value of a point at location
RhinoMath.UnsetValue,RhinoMath.UnsetValue,RhinoMath.UnsetValue.](/api/rhinocommon/rhino.geometry.point3d/unset#)

* * *

[**X** Gets or sets the X (first) coordinate of this
point.](/api/rhinocommon/rhino.geometry.point3d/x#)

* * *

[**Y** Gets or sets the Y (second) coordinate of this
point.](/api/rhinocommon/rhino.geometry.point3d/y#)

* * *

[**Z** Gets or sets the Z (third) coordinate of this
point.](/api/rhinocommon/rhino.geometry.point3d/z#)

* * *

_keyboard_arrow_down_

Methods (25)

[**Add**(Point3d point, Vector3d vector) Sums up a point and a vector, and
returns a new point.  
(Provided for languages that do not support operator overloading. You can use
the + operator
otherwise)](/api/rhinocommon/rhino.geometry.point3d/add#\(point3d,vector3d\))

* * *

[**Add**(Point3d point, Vector3f vector) Sums up a point and a vector, and
returns a new point.  
(Provided for languages that do not support operator overloading. You can use
the + operator
otherwise)](/api/rhinocommon/rhino.geometry.point3d/add#\(point3d,vector3f\))

* * *

[**Add**(Point3d point1, Point3d point2) Sums two <b>Point3d</b> instances.  
(Provided for languages that do not support operator overloading. You can use
the + operator
otherwise)](/api/rhinocommon/rhino.geometry.point3d/add#\(point3d,point3d\))

* * *

[**Add**(Vector3d vector, Point3d point) Sums up a point and a vector, and
returns a new point.  
(Provided for languages that do not support operator overloading. You can use
the + operator
otherwise)](/api/rhinocommon/rhino.geometry.point3d/add#\(vector3d,point3d\))

* * *

[**ArePointsCoplanar**(IEnumerable<Point3d> points,Double tolerance)
Determines whether a set of points is coplanar within a given
tolerance.](/api/rhinocommon/rhino.geometry.point3d/arepointscoplanar#\(ienumerable<point3d>,double\))

* * *

[**CompareTo**(Point3d other) Compares this <b>Point3d</b> with another
<b>Point3d</b> .  
Component evaluation priority is first X, then Y, then
Z.](/api/rhinocommon/rhino.geometry.point3d/compareto#\(point3d\))

* * *

[**CullDuplicates**(IEnumerable<Point3d> points,Double tolerance) Removes
duplicates in the supplied set of
points.](/api/rhinocommon/rhino.geometry.point3d/cullduplicates#\(ienumerable<point3d>,double\))

* * *

[**DistanceTo**(Point3d other) Computes the distance between two
points.](/api/rhinocommon/rhino.geometry.point3d/distanceto#\(point3d\))

* * *

[**DistanceToSquared**(Point3d other) Computes the square of the distance
between two points.  
This method is usually largely faster than
DistanceTo().](/api/rhinocommon/rhino.geometry.point3d/distancetosquared#\(point3d\))

* * *

[**Divide**(Point3d point,Double t) Divides a <b>Point3d</b> by a number.  
(Provided for languages that do not support operator overloading. You can use
the / operator
otherwise)](/api/rhinocommon/rhino.geometry.point3d/divide#\(point3d,double\))

* * *

[**EpsilonEquals**(Point3d other,Double epsilon) Check that all values in
other are within epsilon of the values in
this](/api/rhinocommon/rhino.geometry.point3d/epsilonequals#\(point3d,double\))

* * *

[**Equals**(Point3d point) Determines whether the specified <b>Point3d</b> has
the same values as the present
point.](/api/rhinocommon/rhino.geometry.point3d/equals#\(point3d\))

* * *

[**Equals**(Object obj) Determines whether the specified <b>object</b> is a
<b>Point3d</b> and has the same values as the present
point.](/api/rhinocommon/rhino.geometry.point3d/equals#\(object\))

* * *

[**FromPoint3f**(Point3f point) Converts a single-precision point in a double-
precision
point.](/api/rhinocommon/rhino.geometry.point3d/frompoint3f#\(point3f\))

* * *

[**GetHashCode**() Computes a hash code for the present
point.](/api/rhinocommon/rhino.geometry.point3d/gethashcode#\(\))

* * *

[**Interpolate**(Point3d pA, Point3d pB,Double t) Interpolate between two
points.](/api/rhinocommon/rhino.geometry.point3d/interpolate#\(point3d,point3d,double\))

* * *

[**Multiply**(Point3d point,Double t) Multiplies a <b>Point3d</b> by a number.  
(Provided for languages that do not support operator overloading. You can use
the * operator
otherwise)](/api/rhinocommon/rhino.geometry.point3d/multiply#\(point3d,double\))

* * *

[**Multiply**(Double t, Point3d point) Multiplies a <b>Point3d</b> by a
number.  
(Provided for languages that do not support operator overloading. You can use
the * operator
otherwise)](/api/rhinocommon/rhino.geometry.point3d/multiply#\(double,point3d\))

* * *

[**SortAndCullPointList**(IEnumerable<Point3d> points,Double minimumDistance)
Orders a set of points so they will be connected in a "reasonable polyline"
order.  
Also, removes points from the list if their common distance exceeds a
specified
threshold.](/api/rhinocommon/rhino.geometry.point3d/sortandcullpointlist#\(ienumerable<point3d>,double\))

* * *

[**Subtract**(Point3d point, Vector3d vector) Subtracts a vector from a point.  
(Provided for languages that do not support operator overloading. You can use
the - operator
otherwise)](/api/rhinocommon/rhino.geometry.point3d/subtract#\(point3d,vector3d\))

* * *

[**Subtract**(Point3d point1, Point3d point2) Subtracts a point from another
point.  
(Provided for languages that do not support operator overloading. You can use
the - operator
otherwise)](/api/rhinocommon/rhino.geometry.point3d/subtract#\(point3d,point3d\))

* * *

[**ToString**() Constructs the string representation for the current
point.](/api/rhinocommon/rhino.geometry.point3d/tostring#\(\))

* * *

[**ToString**(String format,IFormatProvider formatProvider)
](/api/rhinocommon/rhino.geometry.point3d/tostring#\(string,iformatprovider\))

* * *

[**Transform**(Transform xform) Transforms the present point in place. The
transformation matrix acts on the left of the point. i.e.,  
result =
transformation*point](/api/rhinocommon/rhino.geometry.point3d/transform#\(transform\))

* * *

[**TryParse**(String input, out Point3d result) Converts the string
representation of a point to the equivalent Point3d
structure.](/api/rhinocommon/rhino.geometry.point3d/tryparse#\(string,out\))

* * *

_keyboard_arrow_down_

Operators (16)

[**-** __ Subtracts a vector from a
point.](/api/rhinocommon/rhino.geometry.point3d/-#\(point3d,vector3d\))

* * *

[**-** __ Computes the additive inverse of all coordinates in the point, and
returns the new point.](/api/rhinocommon/rhino.geometry.point3d/-#\(point3d\))

* * *

[**-** __ Subtracts a point from another
point.](/api/rhinocommon/rhino.geometry.point3d/-#\(point3d,point3d\))

* * *

[**!=** __ Determines whether two Point3d have different
values.](/api/rhinocommon/rhino.geometry.point3d/!=#\(point3d,point3d\))

* * *

[***** __ Multiplies a <b>Point3d</b> by a
number.](/api/rhinocommon/rhino.geometry.point3d/*#\(double,point3d\))

* * *

[***** __ Multiplies a <b>Point3d</b> by a
number.](/api/rhinocommon/rhino.geometry.point3d/*#\(point3d,double\))

* * *

[**/** __ Divides a <b>Point3d</b> by a
number.](/api/rhinocommon/rhino.geometry.point3d//#\(point3d,double\))

* * *

[**+** __ Sums up a point and a vector, and returns a new
point.](/api/rhinocommon/rhino.geometry.point3d/+#\(point3d,vector3d\))

* * *

[**+** __ Sums up a point and a vector, and returns a new
point.](/api/rhinocommon/rhino.geometry.point3d/+#\(point3d,vector3f\))

* * *

[**+** __ Sums two <b>Point3d</b>
instances.](/api/rhinocommon/rhino.geometry.point3d/+#\(point3d,point3d\))

* * *

[**+** __ Sums up a point and a vector, and returns a new
point.](/api/rhinocommon/rhino.geometry.point3d/+#\(vector3d,point3d\))

* * *

[**<** __ Determines whether the first specified point comes before (has
inferior sorting value than) the second point.  
Coordinates evaluation priority is first X, then Y, then
Z.](/api/rhinocommon/rhino.geometry.point3d/<#\(point3d,point3d\))

* * *

[**< =** __ Determines whether the first specified point comes before (has
inferior sorting value than) the second point, or it is equal to it.  
Coordinates evaluation priority is first X, then Y, then
Z.](/api/rhinocommon/rhino.geometry.point3d/<=#\(point3d,point3d\))

* * *

[**==** __ Determines whether two Point3d have equal
values.](/api/rhinocommon/rhino.geometry.point3d/==#\(point3d,point3d\))

* * *

[**>** __ Determines whether the first specified point comes after (has
superior sorting value than) the second point.  
Coordinates evaluation priority is first X, then Y, then
Z.](/api/rhinocommon/rhino.geometry.point3d/>#\(point3d,point3d\))

* * *

[**> =** __ Determines whether the first specified point comes after (has
superior sorting value than) the second point, or it is equal to it.  
Coordinates evaluation priority is first X, then Y, then
Z.](/api/rhinocommon/rhino.geometry.point3d/>=#\(point3d,point3d\))

* * *

