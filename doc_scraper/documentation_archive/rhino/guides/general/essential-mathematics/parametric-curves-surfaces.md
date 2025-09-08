---
url: https://developer.rhino3d.com/guides/general/essential-mathematics/parametric-curves-surfaces/#solution
scraped_at: 2025-09-08T16:00:15.179313
title: Untitled
---

[RhinoDeveloper®](/)

[design, model, present, analyze, realize...](/)

[![Rhino Logo](https://developer.rhino3d.com/images/rhinodevlogo.png)](/)

__

[Guides](https://developer.rhino3d.com/guides)
[Samples](https://developer.rhino3d.com/samples)
[API](https://developer.rhino3d.com/api)
[Videos](https://developer.rhino3d.com/videos)
[Community](https://discourse.mcneel.com/c/rhino-developer) [my account
](https://www.rhino3d.com/my-account/ "Manage your account, licenses, and
teams")

[3 Parametric Curves and
Surfaces](https://developer.rhino3d.com/guides/general/essential-
mathematics/parametric-curves-surfaces/)

  * 3.1 Parametric curves
    * Curve parameter
    * Curve domain or interval
    * Curve evaluation
    * Tangent vector to a curve
    * Cubic polynomial curves
    * Evaluating cubic Bézier curves
  * 3.2 NURBS curves
    * Degree
    * Control points
    * Weights of control points
    * Knots
    * Knots are parameter values
    * Knot multiplicity
    * Fully-multiple knots
    * Uniform knots
    * Non uniform knots
    * Evaluation rule
    * Characteristics of NURBS curves
    * Clamped vs. periodic NURBS curves
    * Weights
    * Evaluating NURBS curves
  * 3.3 Curve geometric continuity
  * 3.4 Curve curvature
  * 3.5 Parametric surfaces
    * Surface parameters
    * Surface domain
    * Surface evaluation
    * Tangent plane of a surface
  * 3.6 Surface geometric continuity
  * 3.7 Surface curvature
    * Principal curvatures
    * Gaussian curvature
    * Mean curvature
  * 3.8 NURBS surfaces
    * Characteristics of NURBS surfaces
    * Singularity in NURBS surfaces
    * Trimmed NURBS surfaces
  * 3.9 Polysurfaces
  * 3.10 Tutorials
    * 3.10.1 Continuity between curves
    * 3.10.2 Surfaces with singularity
  * Download Sample Files
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [General
Guides](https://developer.rhino3d.com/en/guides/general/) / [Essential
Mathematics for Computational
Design](https://developer.rhino3d.com/en/guides/general/essential-
mathematics/) /

3 Parametric Curves and Surfaces

by [Rajaa Issa](https://discourse.mcneel.com/u/rajaa/) (Last updated:
Wednesday, August 14, 2019)

Suppose you travel every weekday from your house to your work. You leave at
8:00 in the morning and arrive at 9:00. At each point in time between 8:00 and
9:00, you would be at some location along the way. If you plot your location
every minute during your trip, you can define the path between home and work
by connecting the 60 points you plotted. Assuming you travel the exact same
speed every day, at 8:00 you would be at home (start location), at 9:00 you
would be at work (end location) and at 8:40 you would at the exact same
location on the path as the 40th plot point. Congratulations, you have just
defined your first parametric curve! You have used _time_ as a _parameter_ to
define your path, and hence you can call your path curve a _parametric curve_.
The time interval you spend from start to end (8 to 9) is called the curve
_domain_ or _interval_.

![https://developer.rhino3d.com/images/math-
image106.png](https://developer.rhino3d.com/images/math-image106.png)

In general, we can describe the $$x$$, $$y$$, and $$z$$ location of a
parametric curve in terms of some parameter $$t$$ as follows:  
$$x = x(t)$$  
$$y = y(t)$$  
$$z = z(t)$$  
Where:  
$$t$$ is a range of real numbers

We saw earlier that the parametric equation of a line in terms of parameter
$$t$$ is defined as:

$$x = x’ + t * a$$  
$$y = y’ + t * b$$  
$$z = z’ + t * c$$

Where:

$$x$$, $$y$$, and $$z$$ are functions of t where t represents a range of real
numbers. $$x’$$, $$y’$$, and $$z’$$ are the coordinates of a point on the line
segment. $$a$$, $$b$$, and $$c$$ define the slope of the line, such that the
vector $$\mathbf{\vec v} <a, b, c>$$ is parallel to the line.

![https://developer.rhino3d.com/images/math-
image108.png](https://developer.rhino3d.com/images/math-image108.png)

We can therefore write the parametric equation of a line segment using a $$t$$
parameter that ranges between two real number values $$t0$$, $$t1$$ and a unit
vector $$\mathbf{\vec v}$$ that is in the direction of the line as follows:

$$P = P’ + t * \mathbf{\vec v}​$$

Another example is a circle. The parametric equation of the circle on the xy-
plane with a center at the origin (0,0) and an angle parameter $$t$$ ranging
between $$0$$ and $$2π$$ radians is:

![https://developer.rhino3d.com/images/math-
image110.png](https://developer.rhino3d.com/images/math-image110.png)

$$x = r \dot cos(t)$$  
$$y = r \dot sin(t)$$

We can derive the general equation of a circle for the parametric one as
follows:

$$ x/r = cos(t)$$  
$$y/r = sin(t)$$

And since:

$$cos(t)^2 + sin(t)^2 = 1$$ (Pythagorean identity)

Then:

$$(x/r)^2 + (y/r)^2 = 1$$ , or  
$$x^2 + y^2 = r^2$$

## 3.1 Parametric curves

### Curve parameter

A parameter on a curve represents the address of a point on that curve. As
mentioned before, you can think of a parametric curve as a path traveled
between two points in a certain amount of time, traveling at a fixed or
variable speed. If traveling takes $$T$$ amount of time, then the parameter t
represents a time within $$T$$ that translates to a location (point) on the
curve.

If you have a straight path (line segment) between the two points $$A$$ and
$$B$$, and $$\mathbf{\vec v}$$ were a vector from $$A$$ to $$B$$ (
$$\mathbf{\vec v} = B - A$$), then you can use the parametric line equation to
find all points $$M$$ between $$A$$ and $$B$$ as follows:

$$M = A + t*(B-A)$$

Where:

$$t$$ is a value between 0 and 1.

The range of t values, 0 to 1 in this case, is referred to as the curve domain
or interval. If t was a value outside the domain (less that 0 or more than 1),
then the resulting point $$M$$ will be outside the linear curve
$$\overline{AB}$$.

![](https://developer.rhino3d.com/images/math-image112.png) Figure (25):
Parametric linear curve in 3-D space and parameter interval.

The same principle applies for any parametric curve. Any point on the curve
can be calculated using the parameter t within the interval or domain of
values that define the limits of the curve. The start parameter of the domain
is usually referred to as $$t0$$ and the end of the domain as $$t1$$.

![](https://developer.rhino3d.com/images/math-image94.png) Figure (26): Curve
in 3-D space (1). Curve domain (2).

### Curve domain or interval

A curve _domain_ or _interval_ is defined as the range of parameters that
evaluate into a point within that curve. The domain is usually described with
two real numbers defining the domain limits expressed in the form (min to
max)or (min, max). The domain limits can be any two values that may or may not
be related to the actual length of the curve. In an increasing domain, the
domain min parameter evaluates to the start point of the curve and the domain
max evaluates to the end point ofthe curve.

![](https://developer.rhino3d.com/images/math-image95.png) Figure (27): Curve
domain or interval can be between any two numbers.

Changing a curve domain is referred to as the process of reparameterizing the
curve. For example, it is very common to change the domain to be (0 to 1).
Reparameterizing a curve does not affect the shape of the 3-D curve. It is
like changing the travel time on a path by running instead of walking, which
does not change the shape of the path.

![](https://developer.rhino3d.com/images/math-image96.png) Figure (28):
Normalized curve domain to be 0 to 1.

An increasing domain means that the minimum value of the domain points to the
start of the curve. Domains are typically increasing, but not always.

### Curve evaluation

We learned that a curve interval is the range of all parameter values that
evaluate to points within the 3-D curve. There is, however, no guarantee that
evaluating at the middle of the domain, for example, will give a point that is
in the middle of the curve, as shown in Figure (29).

We can think of uniform parameterization of a curve as traveling a path with
constant speed. A degree-1 line between two points is one example where equal
intervals or parameters translate into equal intervals of arc length on the
line. This is a special case where equal intervals of parameters evaluate to
equal intervals on the 3-D curve.

![](https://developer.rhino3d.com/images/math-image79.png) Figure (29): Equal
parameter intervals in a degree-1 line evaluate to equal curve lengths.

It is, however, more likely that the speed decreases or increases along the
path. For example, if it takes 30 minutes to travel a road, it is unlikely
that you will be exactly half way through at minute 15. Figure (30) shows a
typical case where equal parameter intervals evaluate to variable length on
the 3-D curve.

![](https://developer.rhino3d.com/images/math-image81.png) Figure (30): Equal
parameter intervals do not usually translate into equal distances on a curve.

You may need to evaluate points on a 3-D curve that are at a defined
percentage of the curve length. For example, you might need to divide the
curve into equal lengths. Typically, 3-D modelers provide tools to evaluate
curves relative to arc length.

### Tangent vector to a curve

A tangent to a curve at any parameter (or point on a curve) is the vector that
touches the curve at that point, but does not cross over. The slope of the
tangent vector equals the slope of the curve at the same point. The following
example evaluates the tangent to a curve at two different parameters.

![](https://developer.rhino3d.com/images/math-image83.png) Figure (31):
Tangents to a curve.

### Cubic polynomial curves

Hermite and Bézier curves are two examples of cubic polynomial curves that are
determined by four parameters. A Hermite curve is determined by two end points
and two tangent vectors at these points, while a Bézier curve is defined by
four points. While they differ mathematically, they share similar
characteristics and limitations.

![](https://developer.rhino3d.com/images/math-image85.png) Figure (32): Cubic
polynomial curves. The Bézier curve (left) is defined by four points. The
Hermite curve (right) is defined by two points and two tangents..

In most cases, curves are made out of multiple segments. This requires making
what is called a _piecewise_ cubic curve. Here is an illustration of a
piecewise Bézier curve that uses 7 storage points to create a two-segment
cubic curve. Note that although the final curve is joined, it does not look
smooth or continuous.

![](https://developer.rhino3d.com/images/math-image87.png) Figure (33): Two
Bezier spans share one point.

Although Hermite curves use the same number of parameters as Bézier curves
(four parameters to define one curve), they offer the additional information
of the tangent curve that can also be shared with the next piece to create a
smoother looking curve with less total storage, as shown in the following.

![](https://developer.rhino3d.com/images/math-image88.png) Figure (34): Two
Hermite spans share one point and a tangent.

The non-uniform rational B-spline (NURBS) is a powerful curve representation
that maintains even smoother and more continuous curves. Segments share more
control points to achieve even smoother curves with less storage.

![](https://developer.rhino3d.com/images/math-image90.png) Figure (35): Two
degree-3 NURBS spans share three control points.

NURBS curves and surfaces are the main mathematical representation used by
Rhino to represent geometry. NURBS curve characteristics and components will
be covered with some detail later in this chapter.

### Evaluating cubic Bézier curves

Named after its inventor, Paul de Casteljau, the de Casteljau algorithm
evaluates Bézier curves using a recursive method. The algorithm steps can be
summarized as follows:

**Input:**

Four points $$A$$, $$B$$, $$C$$, $$D$$ define a curve $$t$$, is any parameter
within curve domain

**Output:**

![https://developer.rhino3d.com/images/math-
image72.png](https://developer.rhino3d.com/images/math-image72.png)

Point $$R$$ on curve that is at parameter $$t$$.

**Solution:**

  1. Find point $$M$$ at $$t$$ parameter on line $$\overline{AB}$$.   
2.Find point $$N$$ at $$t$$ parameter on line $$\overline{BC}$$.  
3.Find point $$O$$ at $$t$$ parameter on line $$\overline{CD}$$.  
4.Find point $$P$$ at $$t$$ parameter on line $$\overline{MN}$$.  
5.Find point $$Q$$ at $$t$$ parameter on line $$\overline{NO}$$.  
6.Find point $$R$$ at $$t$$ parameter on line $$\overline{PQ}$$.

## 3.2 NURBS curves

NURBS is an accurate mathematical representation of curves that is highly
intuitive to edit. It is easy to represent free-form curves using NURBS and
the control structure makes it easy and predictable to edit.

![](https://developer.rhino3d.com/images/math-image74.png) Figure (36): Non-
uniform rational B-splines and their control structure.

There are many books and references for those of you interested in an in-depth
reading about NURBS. A basic understanding of NURBS is however necessary to
help use a NURBS modeler more effectively. There are four main attributes
define the NURBS curve: degree, control points, knots, and evaluation rules.

  1. [Wikipedia: De Boor’s algorithm](http://en.wikipedia.org/wiki/De_Boor%27s_algorithm)
  2. [Michigan Tech, Department of Computer Science, De Boor’s algorithm](http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/de-Boor.html)

### Degree

Curve degree is a whole positive number. Rhino allows working with any degree
curve starting with 1. Degrees 1, 2, 3, and 5 are the most useful but the
degrees 4 and those above 5 are not used much in the real world. Following are
a few examples of curves and their degree:

**Lines** and **polylines** are degree-1 NURBS curves. | ![](https://developer.rhino3d.com/images/math-image75.png)  
---|---  
**Circles** and **ellipses** are examples of degree-2 NURBS curves.  | ![](https://developer.rhino3d.com/images/math-image77.png)  
Free-form **curves** are usually represented as  
degree-3 or 5 NURBS curves.  |  ![](https://developer.rhino3d.com/images/math-image128.png)  
  
### Control points

The control points of a NURBS curve is a list of at least (degree+1) points.
The most intuitive way to change the shape of a NURBS curve is through moving
its control points.

The number of control points that affect each span in a NURBS curve is defined
by the degree of the curve. For example, each span in a degree-1 curve is
affected only by the two end control points. In a degree-2 curve, three
control points affect each span and so on.

Control points of degree-1 curves go through all curve control points. In a degree-1 NURBS curve, two (degree+1) control points define each span. Using five control points, the curve has four spans.  | ![](https://developer.rhino3d.com/images/math-image130.png)  
---|---  
Circles and ellipses are examples of degree two curves. In a degree-2 NURBS curve, three (degree+1) control points define each span. Using five control points, the curve has three spans. | ![](https://developer.rhino3d.com/images/math-image132.png)  
Control points of degree‑3 curves do not usually touch the curve, except at the end points in open curves. In a degree‑3 NURBS curve, four (degree+1) control points define each span. Using five control points, the curve has two spans  |  ![](https://developer.rhino3d.com/images/math-image134.png)  
  
### Weights of control points

Each control point has an associated number called _weight_. With a few
exceptions, weights are positive numbers. When all control points have the
same weight, usually 1, the curve is called non-rational. Intuitively, you can
think of weights as the amount of gravity each control point has. The higher
the relative weight a control point has, the closer the curve is pulled
towards that control point.

It is worth noting that it is best to avoid changing curve weights. Changing
weights rarely gives desired result while it introduces a lot of calculation
challenges in operations such as intersections. The only good reason for using
rational curves is to represent curves that cannot otherwise be drawn, such as
circles and ellipses.

![](https://developer.rhino3d.com/images/math-image135.png) Figure (37): The
effect of varying weights of control points on the result curve. The left
curve is non-rational with uniform control point weights. The circle on the
right is a rational curve with corner control points having weights less than
1.

### Knots

Each NURBS curve has a list of numbers associated with it called a _list of
knots_ (sometimes referred to as _knot vector_). Knots are a little harder to
understand and set. While using a 3-D modeler, you will not need to manually
set the knots for each curve you create; a few things will be useful to learn
about knots.

### Knots are parameter values

Knots are a non-decreasing list of parameter values that lie within the curve
domain. In Rhino, there is degree-1 more knots than control points. That is
the number of knots equals the number of control points plus curve degree
minus 1:

|knots| = |CVs| + Degree - 1

Usually, for non-periodic curves, the first degree many knots are equal to the
domain minimum, and the last degree many knots are equal to the domain
maximum.

For example, the knots of an open degree-3 NURBS curve with 7 control points
and a domain between 0 and 4 may look like <0, 0, 0, 1, 2, 3, 4, 4, 4>.

![](https://developer.rhino3d.com/images/figure-38a.png) Figure (38): There
are degree minus 1 more knots than control points. If the number of control
points=7, and curve degree=3, then number of knots is 9. Knots values are
parameters that evaluate to points on the 3D curve.

Scaling a knot list does not affect the 3D curve. If you change the domain of
the curve in the above example from “0 to 4” to “0 to 1”, knot list get
scaled, but the 3D curve does not change.

![](https://developer.rhino3d.com/images/math-image-figure38A.png) Figure
(39): Scaling the knot list does not change the 3D curve.

We call a knot with value appearing only once as simple knot. Interior knots
are typically simple as in the two examples above.

### Knot multiplicity

The multiplicity of a knot is the number of times it is listed in the list of
knots. The multiplicity of a knot cannot be more than the degree of the curve.
Knot multiplicity is used to control continuity at the corresponding curve
point.

### Fully-multiple knots

A fully multiple knot has multiplicity equal to the curve degree. At a fully
multiple knot there is a corresponding control point, and the curve goes
through this point.

For example, clamped or open curves have knots with full multiplicity at the
ends of the curve. This is why the end control points coincide with the curve
end points. Interior fully multiple knots allow a kink in the curve at the
corresponding point.

For example, the following two curves are both degree-3, and have the same
number and location of control points. However they have different knots and
their shape is also different. Fully multiplicity forces the curve through the
associated control point.

Here are two curves that have the same degree, and same number and location of
control points, and yet have different knots vector that results in different
curve shape:

Degree = 3  
Number of control points = 7  
knots = <0,0,0,1,2,3,4,4,4> = 9 knots  
Domain (0 to 4) | ![](https://developer.rhino3d.com/images/math-image151.png)  
---|---  
Degree = 3  
Number of control points = 7  
knots = <0,0,0,1,1,1,4,4,4> = 9 knots  
Domain (0 to 4)  
**Note:** A fully multiple knot in the middle creates a kink and the curve is forced to go through the associated control point. | ![](https://developer.rhino3d.com/images/math-image154.png)  
  
### Uniform knots

A uniform list of knots satisfies the following condition.

Knots start with a fully-multiple knot, are followed by simple knots, and
terminate with a fully-multiple knot. The values are increasing and equally
spaced. This is typical of clamped or open curves. Periodic curves work
differently as we will see later.

![](https://developer.rhino3d.com/images/math-image-figure41.png) Figure (40):
Uniform knot list means that spacing between knots is constant, with the
exception of clamped curves where they can have full multiplicity knots at
start and end, and still be considered uniform. The left curve is periodic
(closed without kink), and the right is clamped (open).

### Non uniform knots

NURBS curves are allowed to have non-uniform spacing between knots. This can
help control the curvature along the curve to create more smooth curves. Take
the following example interpolating through points using non-uniform knots
list in the left, and uniform in the right. In general, if a NURBS curve
spacing of knots is proportional to the spacing between control points, then
the curve is smoother.

![](https://developer.rhino3d.com/images/figure-38b.png) Figure (41): Non-
uniform knot list can help produce smoother curves. The curve on the left
interpolate through points with non-uniform knots, and produces smoother
curvature. The curve on the right interpolate through the same points but
forces a uniform spacing of knots, resulting curve is not as smooth.

An example of a curve that is both non-uniform and rational is a NURBS circle.
The following is a degree 2 curve with 9 control points and 10 knots. Domain
is 0-4, and the spacing alternate between 0 and 1. knots =
<0,0,1,1,2,2,3,3,4,4> — (full multiplicity in the interior knots) spacing
between knots = [0,1,0,1,0,1,0,1,0] — (non-uniform)

![](https://developer.rhino3d.com/images/math-image-figure43.png) Figure (42):
A NURBS approximation of a circle is rational and non-uniform NURBS.

### Evaluation rule

The evaluation rule uses a mathematical formula that takes a number within the
curve domain and assigns a point. The formula takes into account the degree,
control points, and knots.

Using this formula, specialized curve functions can take a curve parameter and
produce the corresponding point on that curve. A parameter is a number that
lies within the curve domain. Domains are usually increasing and consist of
two numbers: the minimum domain parameter $$t(0)$$ that evaluates to the start
point of the curve and the maximum $$t(1)$$ that evaluates to the end point of
the curve.

![](https://developer.rhino3d.com/images/math-image153.png) Figure (43):
Evaluate parameters to points on curve.

### Characteristics of NURBS curves

In order tocreate a NURBS curve, you will need to provide the
followinginformation:

  * Dimension, typically 3
  * Degree, (sometimes use the _order_ ,which is equal to degree+1)
  * Control points (list of points)
  * Weight of the control point (listof numbers)
  * Knots (list of numbers)

When you create a curve, you need to at least define the degree and locations
of the control points. The rest of the information necessary to construct
NURBS curves can be generated automatically. Selecting an end point to
coincide with the start point would typically create a periodic smooth closed
curve. The following table shows examples of open and closed curves:

Degree-1 open curve.  
The curve goes through all control points. | ![](https://developer.rhino3d.com/images/math-image148.png)  
---|---  
Degree-3 open curve.  
Both curve ends coincide with end control points. | ![](https://developer.rhino3d.com/images/math-image147.png)  
Degree-3 closed periodic curve.  
The curve seam does not go through a control point. | ![](https://developer.rhino3d.com/images/math-image150.png)  
Moving control points of a periodic curve does not affect curve smoothness. | ![](https://developer.rhino3d.com/images/math-image149.png)  
Kinks are created when the curve is forced through some control points. | ![](https://developer.rhino3d.com/images/math-image146.png)  
Moving the control points of a non-periodic curve does not guarantee smooth continuity of the curve, but enables more control over the outcome. | ![](https://developer.rhino3d.com/images/math-image145.png)  
  
### Clamped vs. periodic NURBS curves

The end points of closed clamped curves coincide with end control points.
Periodic curves are smooth closed curves. The best way to understand the
differences between the two is through comparing control points and knots.

The following is an example of an open, clamped non-rational NURBS curve. This
curve has four control points, uniform knots with full-multiplicity at the
start and end knots and the weights of all control points equal to 1.

![](https://developer.rhino3d.com/images/math-image118.png) Figure (44):
Analyze degree-3 open non-rational NURBS curve.

The following circular curve is an example of a degree-3 closed periodic NURBS
curve. It is also non-rational because all weights are equal. Note that
periodic curves require more control points with few overlapping. Also the
knots are simple.

![](https://developer.rhino3d.com/images/math-image119.png) Figure (45):
Analyze degree-3 closed (periodic) NURBS curve.

Notice that the periodic curve turned the four input points into seven control
points (degree+4), while the clamped curve used only the four control points.
The knots of the periodic curve uses only simple knots, while the clamped
curve start and end knots have full multiplicity forcing the curve to go
through the start and end control points.

If we set the degree of the previous examples to 2 instead of 3, the knots
become smaller, and the number of control points of periodic curves changes.

![](https://developer.rhino3d.com/images/math-image120.png) Figure (46):
Analyze degree-2 open NURBS curve.
![](https://developer.rhino3d.com/images/math-image121.png) Figure (47):
Analyze degree-2 closed (periodic) NURBS curve.

### Weights

Weights of control points in a uniform NURBS curve are set to 1, but this
number can vary in rational NURBS curves. The following example shows the
effect of varying the weights of control points.

![](https://developer.rhino3d.com/images/math-image122.png) Figure (48):
Analyze weights in open NURBS curve.
![](https://developer.rhino3d.com/images/math-image115.png) Figure (49):
Analyze weights in closed NURBS curve.

### Evaluating NURBS curves

![https://developer.rhino3d.com/images/math-
image114.png](https://developer.rhino3d.com/images/math-image114.png)

Named after its inventor, Carl de Boor, the de Boor’s algorithmi is a
generalization of the de Casteljau algorithm for Bézier curves. It is
numerically stable and is widely used to evaluate points on NURBS curves in
3-D applications. The following is an example for evaluating a point on a
degree-3 NURBS curve using de Boor’s algorithm.

**Input:**  
Seven control points $$P0$$ to $$P6$$  
Knots:  
$$u_0 = 0.0$$  
$$u_1 = 0.0$$  
$$u_2 = 0.0$$  
$$u_3= 0.25$$  
$$u_4 = 0.5$$  
$$u_5 = 0.75$$  
$$u_6 = 1.0$$  
$$u_7 = 1.0$$  
$$u_8 = 1.0$$

**Output:**

Point on curve that is at $$u=0.4$$

**Solution:**

1\. Calculate coefficients for the first iteration:  
$$A_c = ((u – u_1)/(u_{1+3} – u_1) = 0.8$$  
$$B_c = (u – u_2)/(u_{2+3} – u_2) = 0.53$$  
$$C_c = (u – u_3)/(u_{3+3} – u_3) = 0.2$$

2\. Calculate points using coefficient data:  
$$A = 0.2P_1 + 0.8P_2$$  
$$B = 0.47 P_2 + 0.53 P_3$$  
$$C = 0.8 P_3 + 0.2 P_4$$

3\. Calculate coefficients for the second iteration:  
$$D_c = (u – u_2) / (u_{2+3-1} – u_2) = 0.8$$  
$$E_c = (u – u_3) / (u_{3+3-1} – u_3) = 0.3$$

4\. Calculate points using coefficient data:  
$$D = 0.2A+ 0.8B$$  
$$E = 0.7B + 0.3C$$

5\. Calculate the last coefficient:  
$$Fc = (u – u_3)/ (u_{3+3-2} – u_3) = 0.6$$

Find the point on curve at $$u=0.4$$ parameter:

$$F= 0.4D + 0.6E$$

## 3.3 Curve geometric continuity

Continuity is an important concept in 3‑D modeling. Continuity is important
for achieving visual smoothness and for obtaining smooth light and airflow.
The following table shows various continuities and their definitions:

| **G0** | (Position continuous) | Two curve segments joined together |  
| **G1** | (Tangent continuous) | Direction of tangent at joint point is the same for both curve segments. |  
| **G2** | ( Curvature Continuous) | Curvatures as well as tangents agree for both curve segments at the common endpoint. |  
| **GN** |……. | The curves agree to higher order |

![](https://developer.rhino3d.com/images/math-image138.png) Figure (50):
Examining curve continuity with curvature graph analysis.

## 3.4 Curve curvature

Curvature is a widely used concept in modeling 3‑D curves and surfaces.
Curvature is defined as the change in inclination of a tangent to a curve over
unit length of arc. For a circle or sphere, it is the reciprocal of the radius
and it is constant across the full domain.

At any point on a curve in the plane, the line best approximating the curve
that passes through this point is the tangent line. We can also find the best
approximating circle that passes through this point and is tangent to the
curve. The reciprocal of the radius of this circle is the curvature of the
curve at this point.

![](https://developer.rhino3d.com/images/math-image188.png) Figure (51):
Examining curve curvature at different points.

The best approximating circle can lie either to the left or to the right of
the curve. If we care about this, we establish a convention, such as giving
the curvature positive sign if the circle lies to the left and negative sign
if the circle lies to the right of the curve. This is known as signed
curvature. Curvature values of joined curves indicate continuity between these
curves.

## 3.5 Parametric surfaces

### Surface parameters

A parametric surface is a function of two independent parameters (usually
denoted $$u$$, $$v$$) over some two-dimensional domain. Take for example a
plane. If we have a point $$P$$ on the plane and two nonparallel vectors on
the plane, $$\vec a$$ and $$\vec b$$, then we can define a parametric equation
of the plane in terms of the two parameters $$u$$ and $$v$$ as follows:

$$P = P’ + u * \mathbf{\vec a} + v * \mathbf{\vec b}$$

Where:

$$P’$$: is a known point on the plane  
$$\mathbf{\vec a}$$: is the first vector on the plane  
$$\mathbf{\vec b}$$: is the first vector on the plane  
$$u$$: is the first parameter  
$$v$$: is the first parameter

![](https://developer.rhino3d.com/images/math-image189.png) Figure (52): The
parameter rectangle of a plane.

Another example is the sphere. The Cartesian equation of a sphere centered at
the origin with radius $$R$$ is

$$x^2 + y^2 + z^2 = R^2$$

That means for each point, there are three variables ( $$x$$, $$y$$, $$z$$),
which is not useful to use for a parametric representation that requires only
two variables. However, in the spherical coordinate system, each point is
found using the three values:

$$r$$: radial distance between the point and the origin  
$$θ$$: the angle from the x-axis in the xy-plane  
$$ø$$: the angle from the z-axis and the point

![](https://developer.rhino3d.com/images/math-image127.png) Figure (53):
Spherical coordinate system.

A conversion of points from spherical to Cartesian coordinate can be obtained
as follows:

$$x = r * sin(ø) * cos(θ)$$  
$$y = r * sin(ø) * sin(θ)$$  
$$z = r * cos (ø)$$

Where:

$$r$$ is distance from origin $$≥ 0$$  
$$θ$$ is running from $$0$$ to $$2π$$  
$$ø$$ is running from $$0$$ to $$π$$

Since $$r$$ is constant in a sphere surface, we are left with only two
variables, and hence we can use the above to create a parametric
representation of a sphere surface:

$$u = θ$$  
$$v = ø$$

So that:

$$x = r * sin(v) * cos(u)$$  
$$y = r * sin(v) * sin(u)$$  
$$z = r * cos(v)$$

Where ( $$u$$, $$v$$) is within the domain ( $$2 π$$, $$π$$)

![](https://developer.rhino3d.com/images/math-image191.png) Figure (54): The
parameter rectangle of a sphere.

The parametric surface follows the general form:  
$$x = x(u,v)$$  
$$y = y(u,v)$$  
$$z = z(u,v)$$

Where:

$$u$$ and $$v$$ are the two parameters within the surface domain or region.

### Surface domain

A surface domain is defined as therange of ( $$u,v$$) parameters that evaluate
into a 3 D point on thatsurface. The domain in each dimension ( $$u$$ or
$$v$$) is usually describedas two real numbers ( $$u_{min}$$ to $$u_{max}$$)
and ( $$v_{min}$$ to $$v_{max}$$)

Changing a surface domain is referredto as _reparameterizing_ the surface. An
increasingdomain means that the minimum value of the domain points to
theminimum point of the surface. Domains are typically increasing, butnot
always.

![](https://developer.rhino3d.com/images/math-image192.png) Figure (55): NURBS
surface in 3-D modeling space (left). The surface parameter rectangle with
domain spanning from u0 to u1 in the first direction and v0 to v1 in the
second direction (right).

### Surface evaluation

Evaluating a surface at a parameter that is within the surface domain results
in a point that is on the surface. Keep in mind that the middle of the domain
( $$u_{mid}$$, $$v_{mid}$$) might not necessarily evaluate to the middle point
of the 3-D surface. Also, evaluating $$u-$$ and $$v-$$ values that are outside
the surface domain will not give a useful result.

![](https://developer.rhino3d.com/images/math-image193.png) Figure (56):
Surface evaluation.

### Tangent plane of a surface

The tangent plane to a surface at a given point is the plane that touches the
surface at that point. The z-direction of the tangent plane represents the
normal direction of the surface at that point.

![](https://developer.rhino3d.com/images/math-image194.png) Figure (57):
Tangent and normal vectors to a surface.

## 3.6 Surface geometric continuity

Many models cannot be constructed from one surface patch. Continuity between
joined surface patches is important for visual smoothness, light reflection,
and airflow. The following table shows various continuities and their
definitions:

| **G0** | (Position continuous) | Two surfaces joined together. |  
| **G1** | (Tangent continuous) | The corresponding tangents of the two surfaces along their joint edge are parallel in both u‑ and v‑directions. |  
| **G2** | ( Curvature Continuous) | Curvatures as well as tangents agree for both surfaces at the common edge. |  
| **GN** |……. | The surfaces agree to higher order. |

![](https://developer.rhino3d.com/images/math-image126.png) Figure (58):
Examining surface continuity with zebra analysis.

## 3.7 Surface curvature

For surfaces, normal curvature is one generalization of curvature to surfaces.
Given a point on the surface and a direction lying in the tangent plane of the
surface at that point, the normal section curvature is computed by
intersecting the surface with the plane spanned by the point, the normal to
the surface at that point, and the direction. The normal section curvature is
the signed curvature of this curve at the point of interest.

If we look at all directions in the tangent plane to the surface at our point,
and we compute the normal curvature in all these directions, there will be a
maximum value and a minimum value.

![](https://developer.rhino3d.com/images/math-image125.png) Figure (59):
Normal curvatures.

### Principal curvatures

The principal curvatures of a surface at a point are the minimum and maximum
of the normal curvatures at that point. They measure the maximum and minimum
bend amount of the surface at that point. The principal curvatures are used to
compute the Gaussian and mean curvatures of the surface.

For example, in a cylindrical surface, there is no bend along the linear
direction (curvature equals zero) while the maximum bend is when intersecting
with a plane parallel to the end faces (curvature equals 1/radius). Those two
extremes make the principle curvatures of that surface.

![](https://developer.rhino3d.com/images/math-image86.png) Figure (60):
Principle curvatures at a surface point are the minimum and maximum curvatures
at that point.

### Gaussian curvature

The Gaussian curvature of a surface at a point is the product of the principal
curvatures at that point. The tangent plane of any point with positive
Gaussian curvature touches the surface locally at a single point, whereas the
tangent plane of any point with negative Gaussian curvature cuts the surface.

![https://developer.rhino3d.com/images/math-
image91.png](https://developer.rhino3d.com/images/math-image91.png)

A: Positive curvature when surface is bowl-like.  
B: Negative curvature when surface is saddle-like.  
C: Zero curvature when surface is flat in at least one direction (plane,
cylinder).

![](https://developer.rhino3d.com/images/math-image89.png) Figure (61):
Analyzing the surface Gaussian curvature.

### Mean curvature

The mean curvature of a surface at a point is one-half of the sums of the
principal curvatures at that point. Any point with zero mean curvature has
negative or zero Gaussian curvature.

Surfaces with zero mean curvature everywhere are minimal surfaces. Physical
processes which can be modeled by minimal surfaces include the formation of
soap films spanning fixed objects, such as wire loops. A soap film is not
distorted by air pressure (which is equal on both sides) and is free to
minimize its area. This contrasts with a soap bubble, which encloses a fixed
quantity of air and has unequal pressures on its inside and outside. Mean
curvature is useful for finding areas of abrupt change in the surface
curvature.

Surfaces with constant mean curvature everywhere are often referred to as
constant mean curvature (CMC) surfaces. CMC surfaces include the formation of
soap bubbles, both free and attached to objects. A soap bubble, unlike a
simple soap film, encloses a volume and exists in equilibrium where slightly
greater pressure inside the bubble is balanced by the area-minimizing forces
of the bubble itself.

## 3.8 NURBS surfaces

You can think of NURBS surfaces as a grid of NURBS curves that go in two
directions. The shape of a NURBS surface is defined by a number of control
points and the degree of that surface in each one of the two directions (u-
and v-directions). NURBS surfaces are efficient for storing and representing
free-form surfaces with a high degree of accuracy. The mathematical equations
and details of NURBS surfaces are beyond the scope of this text. We will only
focus on the characteristics that are most useful for designers.

![](https://developer.rhino3d.com/images/math-image80.png) Figure (62): NURBS
surface with red isocurves in the u-direction and green isocurves in the
v-direction. ![](https://developer.rhino3d.com/images/math-image78.png) Figure
(63): The control structure of a NURBS surface.
![](https://developer.rhino3d.com/images/math-image84.png) Figure (64): The
parameter rectangle of a NURBS surface.

Evaluating parameters at equal intervals in the 2-D parameter rectangle does
not translate into equal intervals in 3-D space in most cases.

![](https://developer.rhino3d.com/images/math-image82.png) Figure (65):
Evaluating surfaces.

### Characteristics of NURBS surfaces

NURBS surface characteristics are very similar to NURBS curves except there is
one additional parameter. NURBS surfaces hold the following information:

  * Dimension, typically 3
  * Degree in u‑and v‑directions: (sometimes use order which is degree + 1)
  * Control points (points)
  * Weights of control points (numbers)
  * Knots (numbers)

As with the NURBS curves, you will probably not need to know the details of
how to create a NURBS surface, since 3-D modelers will typically provide good
set of tools for this. You can always rebuild surfaces (and curves for that
matter) to a new degree and number of control points. Surface can be open,
closed, or periodic. Here are few examples of surfaces:

Degree-1 surface in both u- and v-directions. All control points lie on the surface. | ![](https://developer.rhino3d.com/images/math-image73.png)  
---|---  
Degree-3 in the u-direction and degree‑1 in the v-direction open surface. The surface corners coincide with corner control points. | ![](https://developer.rhino3d.com/images/math-image71.png)  
Degree-3 in the u-direction and degree 1 in the v-direction closed (non-periodic) surface. Some control points coincide with the surface seam. | ![](https://developer.rhino3d.com/images/math-image76.png)  
Moving control points of a closed (non-periodic) surface causes a kink and the surface does not look smooth. | ![](https://developer.rhino3d.com/images/math-image107.png)  
Degree 3 the u-direction and degree 1 in the v-direction periodic surface. The surface control points do not coincide with the surface seam. | ![](https://developer.rhino3d.com/images/math-image105.png)  
Moving the control points of a periodic surface does not affect surface smoothness or create kinks. | ![](https://developer.rhino3d.com/images/math-image111.png)  
  
### Singularity in NURBS surfaces

For example, if you have a linear edge of a simple plane, and you drag the two
end control points of an edge so they overlap (collapse) at the middle, you
will get a singular edge. You will notice that the surface isocurves converge
at the singular point.

![](https://developer.rhino3d.com/images/math-image109.png) Figure (66):
Collapse two corner points of a rectangular NURBS surface to create a
triangular surface with singularity. The parameter rectangle remains
rectangular.

The above triangular shape can be created without singularity. You can trim a
surface with a triangle polyline. When you examine the underlying NURBS
structure, you see that it remains a rectangular shape.

![](https://developer.rhino3d.com/images/math-image99.png) Figure (67): Trim a
rectangular NURBS surface to create a trimmed triangular surface.

Other common examples of surfaces that are hard to generate without
singularity are the cone and the sphere. The top of a cone and top and bottom
edges of a sphere are collapsed into one point. Whether there is singularity
or not, the parameter rectangle maintains a more or less rectangular region.

### Trimmed NURBS surfaces

NURBS surfaces can be trimmed or untrimmed. Trimmed surfaces use an underlying
NURBS surface and closed curves to trim out part of that surface. Each surface
has one closed curve that defines the outer border (_outer loop_) and can have
non-intersecting closed inner curves to define holes (_inner loops_). A
surface with an outer loop that is the same as that of its underlying NURBS
surface and that has no holes is what we refer to as an _untrimmed_ surface.

![](https://developer.rhino3d.com/images/math-image97.png) Figure (68):
Trimmed surface in modeling space (left) and in parameter rectangle (right).

## 3.9 Polysurfaces

A polysurface consists of two or more(possibly trimmed) NURBS surfaces joined
together. Each surface hasits own structure, parameterization, and isocurve
directions that donot have to match. Polysurfaces are represented using the
boundaryrepresentation (_BRep_). The BRep structure describes surfaces,edges,
and vertices with trimming data and connectivity amongdifferent parts. Trimmed
surface are also represented using BRep datastructure.

![](https://developer.rhino3d.com/images/math-image103.png) Figure (69):
Polysurfaces are made out of joined surfaces with common edges aligning
perfectly within tolerance.

The BRep is a data structure that describes each face in terms of its
underlying surface, surrounding 3-D edges, vertices, parameter space 2-D
trims, and relationship between neighboring faces. BRep objects are also
called solids when they are closed (watertight).

An example polysurface is a simple box that is made out of six untrimmed
surfaces joined together.

![](https://developer.rhino3d.com/images/math-image101.png) Figure (70): Box
made out of six untrimmed surfaces joined in one polysurface.

The same box can be made using trimmed surfaces, such as the top one in the
following example.

![](https://developer.rhino3d.com/images/math-image93.png) Figure (71): Box
faces can be trimmed.

The top and bottom faces of the cylinder in the following example are trimmed
from planar surfaces.

![](https://developer.rhino3d.com/images/math-image92.png) Figure (72) shows
the control points of the underlying surfaces.

We saw that editing NURBS curves and untrimmed surfaces is intuitive and can
be done interactively by moving control points. However, editing trimmed
surfaces and polysurfaces can be challenging. The main challenge is to be able
to maintain joined edges of different faces within the desired tolerance.
Neighboring faces that share common edges can be trimmed and do not usually
have matching NURBS structure, and therefore modifying the object in a way
that deforms that common edge might result in a gap.

![](https://developer.rhino3d.com/images/math-image51.png) Figure (73): Two
triangular faces joined in one polysurface but do not have matching joined
edge. Moving one corner create a hole.

Another challenge is that there is typically less control over the outcome,
especially when modifying trimmed geometry.

![](https://developer.rhino3d.com/images/math-image44.png) Figure (74): Once a
trimmed surface is created, there is limited control to edit the result.
![](https://developer.rhino3d.com/images/math-image42.png) Figure (75): Use
cage edit technique in Rhino to edit polysurfaces.

Trimmed surfaces are described in parameter space using the untrimmed
underlying surface combined with the 2-D trim curves that evaluate to the 3-D
edges within the 3-D surface.

## 3.10 Tutorials

The following tutorials use the concepts learned in this chapter. They use
Rhinoceros 5 and Grasshopper 0.9.

### 3.10.1 Continuity between curves

Examine the continuity between two input curves. Continuity assumes that the
curves meet at the end of the first curve and the start of the second curve.

![https://developer.rhino3d.com/images/math-
image48.png](https://developer.rhino3d.com/images/math-image48.png)

##### Input:

Two input curves.

##### Parameters:

Calculate the following to be able to decide the continuity between two
curves:

![https://developer.rhino3d.com/images/math-
image46.png](https://developer.rhino3d.com/images/math-image46.png)

  * The end point of the first curve ( $$P1$$)
  * The start point of the second curve ( $$P2$$)
  * The tangent at the end of the first curve and at the start of the second curve ( $$T1$$ and $$T2$$).
  * The curvature at the end of the first curve and at the start of the second curve ( $$C1$$ and $$C2$$).

##### Solution:

1\. Reparameterize the input curves. We do that so that we know that the start
of the curve evaluates at $$t=0$$ and the end at $$t=1$$.  
2\. Extract the end and start points of the two curves, and check whether they
coincide. If they do, the two curves are at least $$G0$$ continuous.

![https://developer.rhino3d.com/images/math-
image36.png](https://developer.rhino3d.com/images/math-image36.png)

3\. Calculate tangents.  
4\. Compare the tangents using the dot product. Make sure to unitize vectors.
If the curves are parallel, then we have at least $$G1$$ continuity.

![https://developer.rhino3d.com/images/math-
image34.png](https://developer.rhino3d.com/images/math-image34.png)

5\. Calculate curvature vectors.  
6\. Compare curvature vectors, and if they agree, the two curves are $$G2$$
continuous.

![https://developer.rhino3d.com/images/math-
image40.png](https://developer.rhino3d.com/images/math-image40.png)

7\. Create logic that filters through the three results (G1, G2, and G3) and
select the highest continuity.

![https://developer.rhino3d.com/images/math-
image38.png](https://developer.rhino3d.com/images/math-image38.png)

Using the Grasshopper VBScript component:

![https://developer.rhino3d.com/images/math-
image31.png](https://developer.rhino3d.com/images/math-image31.png)

    
    
    Private Sub RunScript(ByVal c1 As Curve, ByVal c2 As Curve, ByRef A As Object)
    
      'declare variables
      Dim continuity As New String("")
      Dim t1, t2 As Double
      Dim v_c1, v_c2, c_c1, c_c2 As Vector3d
    
      'extract start and end points
      Dim end_c1 = c1.PointAtEnd
      Dim start_c2 = c2.PointAtStart
    
      'check G0 continuity
      If end_c1.DistanceTo(start_c2) = 0 Then
        continuity = "G0"
      End If
    
      'check G1 continuity
      If continuity = "G0" Then
        'calculate tangents
        v_c1 = c1.TangentAtEnd
        v_c2 = c2.TangentAtStart
        'unitize tangent vectors
        v_c1.Unitize
        v_c2.Unitize
        'compare tangents
        If v_c1 * v_c2 = 1.0 Then
          continuity = "G1"
        End If
      End If
    
      'check G2 continuity
      If continuity = "G1" Then
        'extract the parameter at start and end of the curves domain
        t1 = c1.Domain.Max
        t2 = c2.Domain.Min
        'calculate curvature
        c_c1 = c1.CurvatureAt(t1)
        c_c2 = c2.CurvatureAt(t2)
        'unitize curvature vectors
        c_c1.Unitize
        c_c2.Unitize
        'compare vectors
        If c_c1 * c_c2 = 1.0 Then
          continuity = "G2"
        End If
      End If
    
      'Assign output
      A = continuity
    
    End Sub
    

Using the Grasshopper Python component:

![https://developer.rhino3d.com/images/math-
image69.png](https://developer.rhino3d.com/images/math-image69.png)

    
    
    #decclare variables
    continuity = ""
    
    #extract start and end points
    end_c1 = c1.PointAtEnd
    start_c2 = c2.PointAtStart
    
    #check G0 continuity
    if end_c1.DistanceTo(start_c2) == 0:
        continuity = "G0"
    
    #check G1 continuity
    if continuity == "G0":
        #calculate tangents
        v_c1 = c1.TangentAtEnd
        v_c2 = c2.TangentAtStart
        #unitize tangent vectors
        v_c1.Unitize()
        v_c2.Unitize()
        #compare tangents
        dot = v_c1 * v_c2
        if dot == 1.0:
            continuity = "G1"
        else:
            print("Failed G1")
            print(dot)
    
    #check G2 continuity
    if continuity == "G1":
    
        #extract the parameter at start and end of the curves domain
        t1 = c1.Domain.Max
        t2 = c2.Domain.Min
        #calculate curvature
        c_c1 = c1.CurvatureAt(t1)
        c_c2 = c2.CurvatureAt(t2)
        #unitize curvature vectors
        c_c1.Unitize()
        c_c2.Unitize()
        #compare vectors
        dot = c_c1 * c_c2
        if dot == 1.0:
            continuity = "G2"
        else:
            print("Failed G2")
            print(dot)
    
    #assign output
    A = continuity
    

Using the Grasshopper C# component:

![https://developer.rhino3d.com/images/math-
image70.png](https://developer.rhino3d.com/images/math-image70.png)

    
    
    Private Sub RunScript(ByVal c1 As Curve, ByVal c2 As Curve, ByRef A As Object)
    
        //decalre variables
        string continuity = ("");
        double t1, t2;
        Vector3d v_c1, v_c2, c_c1, c_c2;
    
        //extract start and end points
        Point3d end_c1 = c1.PointAtEnd;
        Point3d start_c2 = c2.PointAtStart;
    
        //check G0 continuity
        if( end_c1.DistanceTo(start_c2) == 0){
          continuity = "G0";
        }
    
        //check G1 continuity
        if( continuity == "G0")
        {
          //calculate tangents
          v_c1 = c1.TangentAtEnd;
          v_c2 = c2.TangentAtStart;
          //unitize tangent vectors
          v_c1.Unitize();
          v_c2.Unitize();
          //compare tangents
          if( v_c1 * v_c2 == 1.0 ){
            continuity = "G1";
          }
        }
    
        //check G2 continuity
        if( continuity == "G1" )
        {
          //extract the parameter at start and end of the curves domain
          t1 = c1.Domain.Max;
          t2 = c2.Domain.Min;
          //calculate curvature
          c_c1 = c1.CurvatureAt(t1);
          c_c2 = c2.CurvatureAt(t2);
          //unitize curvature vectors
          c_c1.Unitize();
          c_c2.Unitize();
          //compare vectors
          if( c_c1 * c_c2 == 1.0 ){
            continuity = "G2";
          }
        }
    
        //assign output
        A = continuity;
    
    End Sub
    

### 3.10.2 Surfaces with singularity

Extract singular points in a sphere and a cone.

**Input:**

One sphere and one cone.

![https://developer.rhino3d.com/images/math-
image61.png](https://developer.rhino3d.com/images/math-image61.png)

**Parameters:**

Singularity can be detected through analyzing the 2-D parameter space trims
that have invalid or zero-length corresponding edges. Those trims ought to be
singular.

**Solution:**

  1. Traverse through all trims in the input.
  2. Check if any trim has an invalid edge and flag it as a singular trim.
  3. Extract point locations in 3-D space.

Using the Grasshopper VB component:

![https://developer.rhino3d.com/images/math-
image59.png](https://developer.rhino3d.com/images/math-image59.png)

    
    
    Private Sub RunScript(ByVal srf As Brep, ByRef A As Object)
    
      'Decalre a new list of points
      Dim singular_points As New List( Of Point3d)
    
      'Examine all trims in the input
      For Each trim As BrepTrim In srf.Trims
    
        'Null edge of a trim indicates a singularity
        If trim.Edge Is Nothing Then
    
          'Find the 2D parameter space point of the start or end of the trim
          Dim pt2d = New Point2d(trim.PointAtStart)
    
          'Evaluate trim end point on the object surface
          Dim pt3d = trim.Face.PointAt(pt2d.x, pt2d.y)
    
          'Add 3D point to the list of singular points
          singular_points.Add(pt3d)
        End If
    
      Next
    
      'Asign output
      A = singular_points
    
    End Sub
    

Using the Grasshopper Python component:

![https://developer.rhino3d.com/images/math-
image53.png](https://developer.rhino3d.com/images/math-image53.png)

    
    
    #Decalre a new list of points
    singular_points = []
    
    #Examine all trims in the input brep
    for trim in srf.Trims:
    
    	#Null edge of a trim indicates a singularity
    	if trim.Edge == None:
    		#Find the 2D parameter space point at trim start or end
    		pt2d = trim.PointAtStart
    
    		#Evaluate trim end point on the object surface
    		pt3d = trim.Face.PointAt(pt2d.X, pt2d.Y)
    
    		#Add 3D point to the list of singular points
    		singular_points.append(pt3d)
    
    #Asign output
    A = singular_points
    

Using the Grasshopper C# component:

![https://developer.rhino3d.com/images/math-
image63.png](https://developer.rhino3d.com/images/math-image63.png)

    
    
    private void RunScript(Brep srf, ref object A)
    {
      //Decalre a new list of points
      List < Point3d > singular_points = new List<Point3d>();
    
      //Examine all trims in the input
      foreach( BrepTrim trim in srf.Trims)
      {
        //Null edge of a trim indicates a singularity
        if( trim.Edge == null)
        {
          //Find the 2D parameter space point of the start or end of the trim
          Point2d pt2d = new Point2d(trim.PointAtStart);
    
          //Evaluate trim end point on the object surface
          Point3d pt3d = trim.Face.PointAt(pt2d.X, pt2d.Y);
    
          //Add 3D point to the list of singular points
          singular_points.Add(pt3d);
        }
      }
    
      //Asign output   
      A = singular_points
    }
    

## Download Sample Files

Download the
[__](https://www.rhino3d.com/download/rhino/6/essentialmathematics/) [download
samplesand
tutorials](https://www.rhino3d.com/download/rhino/6/essentialmathematics/)
archive, containing all the example Grasshopper and code files in this guide.

## Next Steps

If you would like to research more, check out the
[References](https://developer.rhino3d.com/guides/general/essential-
mathematics/references/) guide to learn more about the detailed structure of
NURBS curves and surfaces.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/general/essential-
mathematics/parametric-curves-surfaces/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/general/essential-
mathematics/parametric-curves-surfaces/index.md) [
Admin](https://developer.rhino3d.com/admin)

[Find a Reseller](https://www.rhino3d.com/sales)

[Shop online](https://www.rhino3d.com/store) or find a
[Reseller](https://www.rhino3d.com/sales)

[Find a Reseller](https://www.rhino3d.com/sales)

[Privacy Policy](https://www.rhino3d.com/privacy) •
[About](https://www.rhino3d.com/mcneel/about) • [Contact
Us](https://www.rhino3d.com/mcneel/contact) • [
Language](https://www.rhino3d.com/language "Change to a different region or
language")

[Copyright © 1993-2025 Robert McNeel & Associates. All Rights
Reserved.](https://www.rhino3d.com/mcneel/about)

[](https://www.facebook.com/McNeelRhinoceros/)
[](https://twitter.com/bobmcneel) [](https://www.linkedin.com/groups/75313/)
[](https://www.youtube.com/user/RhinoGuide/videos) [](https://vimeo.com/rhino)
[![Blogger
icon](https://developer.rhino3d.com/images/blogger.svg)](http://blog.rhino3d.com/)
[![Food4Rhino](https://developer.rhino3d.com/images/f4r_icon_01.svg)](https://www.food4rhino.com)

