---
url: https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/data-structures/#25-tutorials-data-structures
scraped_at: 2025-09-08T15:41:04.834796
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

[Chapter 2: Introduction to Data
Structures](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-
and-data-structures/data-structures/)

  * 2.1 Overview
  * 2.2 Generating lists
  * 2.3 List operations
  * 2.4 List matching
  * 2.5 Tutorials: data structures
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) / [Essential
Algorithms and Data Structures for
Grasshopper](https://developer.rhino3d.com/en/guides/grasshopper/gh-
algorithms-and-data-structures/) /

Chapter 2: Introduction to Data Structures

by [Rajaa Issa](https://discourse.mcneel.com/u/rajaa/) (Last updated: Monday,
July 15, 2024)

All algorithms involve processing input data to generate a new set of data as
output. Data is stored in well-defined structures to help access and
manipulate efficiently. Understanding these structures is the key for
successful algorithmic designs. This chapter includes an in-depth review of
the basic data structures in Grasshopper.  

## 2.1 Overview

__[ Overview of data structures in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030596360)

Grasshopper has three distinct data structures: single item, list of items and
tree of items. GH components execute differently based on input data
structures, and hence it is essential to be fully aware of the data structure
before using. There are tools in GH to help identify the data structure. Those
are Panel and Param Viewer.

![](ads-100.png) Figure(34): Data structures in Grasshopper

Processes in GH execute differently based on the data structure. For example,
the Mass Addition component adds all the numbers in a list and produces a
single number, but when operating on a tree, it produces a list of numbers
representing the sum of each branch.

![](ads-101.png) Figure(35): Components execute differently based on the data
structures. Result of adding numbers from Figure(34)

The wires connecting the data with components in GH offer additional visual
reference to the data structure. The wire from a single item is a simple line,
while the wire connecting a list is drawn as a double line. A wire output from
a tree data structure is a dashed double line. This is very useful to quickly
identify the structure of your data.

Display the data structure | Example  
---|---  
**Item** : single branch with single item  
Wire display: single line  |  ![](ads-102.png)  
**List** : single branch with multiple items  
Wire display: double line  |  ![](ads-103.png)  
**Tree** : multiple branches with any number of items per branch  
Wire display: double dashed line  |  ![](ads-104.png)  
  
## 2.2 Generating lists

__[ Generate lists in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030597432)

There are many ways to generate lists of data in GH. So far we have seen how
to directly embed a list of values inside a parameter or a panel (with
multiline data). There are also special components to generate lists. For
example, to generate a list of numbers, there are three key components:
**Range** , **Series** and **Random**. Lists can be the output of some
components such as **Divide** curve (the output includes lists of points,
tangents and parameters). Use the **Panel** component to preview the values in
a list and **Parameter Viewer** to examine the data structures.

The **Range** component creates equally spaced range of numbers between a min
and max values (called domain) and a number of steps (the number of values in
the resulting list is equal to the number of steps plus one).
![](ads-105.png) Figure(36): Generate a list of 8 numbers using the Range
component in Grasshopper  
---  
The **Series** component also creates an equally spaced list of numbers, but
here you set the starting number, step size and number of elements.
![](ads-106.png) Figure(37): Generate a list of 7 numbers using the Series
component in Grasshopper  
The **Random** component is used to create random numbers using a domain and a
number of elements. If you use the same seed, then you always get the same set
of random numbers.  ![](ads-107.png) Figure(38): Generate a list of numbers
using the Random component in Grasshopper  
The **Divide** component outputs divide points, tangents and parameters on
curve.  ![](ads-108.png) Figure(39): Divide Curve takes a single input (curve)
and generate lists of output  
Tutorial: 2_2_1 Generating lists  
---  
Explore 4 different ways to create circles. Use different data sources and
data structures.  
**Solution...** |    
1\. Directly set a circle in a parameter ![](ads-109.png)  
---  
2\. Set the plane input to the default XY-Plane (internal). Supply a list of
radiuses using **Range** component ![](ads-110.png)  
3\. Supply one value for the center. Normal is set to default (internal) List
of radiuses using **Random** component ![](ads-111.png)  
4\. Create a circle from 3 points:  
A: set internally to one value  
B: Supply one value  
C: Supply a list of values using the **Series** component to set a list of Z
coordinates ![](ads-112.png)  
  
## 2.3 List operations

__[ Generate lists in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030599906)

Grasshopper offers an extensive list of components for list operations and
list management. We will review the most commonly used ones.  

You can check the length of a list using the **List Length** component, and
access items at specific indices using the **List Item** component.
![](ads-113.png) Figure(40): Examples of list operations in Grasshopper  
---  
Lists can be reversed using the **Reverse List** component, and sorted using
the **Sort List** component.  ![](ads-114.png) Figure(41): Lists can be
reversed or sorted using designated components in Grasshopper  
Components such as **Cull Patterns** and **Dispatch** allow selecting a subset
of the list, or splitting the list based on a pattern.These components are
very commonly used to control data flow and select a subset of the data.
![](ads-115.png) Figure(42): Cull part of a list using components such as Cull
Pattern and Dispatch  
The **Shift List** component allows shifting a list by any number of steps.
That helps align multiple lists to match in a particular order.
![](ads-116.png) Figure(43): Shift operation in Grasshopper  
The **Subset** component is another example to select part of a list based on
a range of indices.  ![](ads-117.png) Figure(44): Select a subset of the list
using a range of indices  
Tutorial: 2_3_1 List operations  
---  
Given two lists of points from dividing two concentric circles, generate the
following patterns: ![](ads-118.png)  
**Solution...** |  __[ Solution video...](https://vimeo.com/showcase/11456959/video/1030600858)  
---  
![](ads-119.png) |  ![](ads-120.png)  
![](ads-121.png) |  ![](ads-122.png)  
![](ads-123.png) |  ![](ads-124.png)  
![](ads-125.png) |  ![](ads-126.png)  
![](ads-127.png) |  ![](ads-128.png)  
![](ads-129.png) |  ![](ads-130.png)  
![](ads-131.png) |  ![](ads-132.png)  
![](ads-133.png) |  ![](ads-134.png)  
![](ads-135.png) |  ![](ads-136.png)  
  
## 2.4 List matching

__[ Generate lists in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030598866)

When the input is a single item or has an equal number of elements in a simple
list, it is easy to imagine how the data is matched. The matching is based on
corresponding indices. Let’s use the **Addition** component to examine list
matching in GH. Note that the same principles apply to all other Grasshopper
components.

![](ads-137.png) Figure(45): Examples of primitive data types common to all
programming languages

There are times when input has variable length lists. In this case, GH reuses
the last item on the shorter list and matches it with the next items in the
longer list.

![](ads-138.png) Figure(46): The default list matching in Grasshopper reuses
the last element of the shorter list

Grasshopper offers alternative ways of data matching: **Long** , **Short** and
**Cross** reference that the user can force to use. The **Long** matching is
the same as the default matching. That is, the last element of the shorter
list is repeated to create a matching length.

![](ads-139.png) Figure(47): Long list matching is the default matching mode
in Grasshopper

The **Short** list matching truncates the long list to match the length of the
short list. All additional elements are ignored and the resulting list has a
length that matches the shorter list.

![](ads-140.png) Figure(48): Short matching of lists omits additional values
in longer lists

The **Cross Reference** matches the first list with each of the elements in
the second list. The resulting list has a length equal to the multiplication
product of the length of input lists. Cross reference is useful when trying to
produce all possible combinations of input data. The order of input affects
the order of the result as shown in Figure (49).

![](ads-141.png) Figure(49): Cross reference matching creates longer lists to
account for all possible permutations

If none of the matching methods produce the desired result, you can explicitly
adjust the lists to match in length based on your requirements. For example,
if you like to repeat the shorter list until it matches the length of the
longer list, then you’ll need to create the logic to achieve that as in the
following example.

![](ads-142.png) Figure(50): Need to create custom script to generate custom
matching Tutorial 2_4_1 List matching  
---  
Use the 4-step method to generate an algorithm that takes 6 numbers (0 to 5)
and turn them into a cube of points as in the image:  
![](ads-143.png)  
**Solution...** |  **Output:**  
A list of 6x6x6 = 216 points constructed from a list of X, Y, Z coordinates  |  ![](ads-144.png)  
---|---  
**Key Process:**  
Use the **Construct Point** component to generate the list of points  |  ![](ads-144A.png)  
**Input:**  
Examine input using the **Parameter Viewer** and **Panel** components.  
The given list has 6 points representing each coordinate along each axis  |  ![](ads-145.png)  
**Intermediate processes:**  
Need to find all possible permutations for the coordinates to create the cube
of 216 points along all 3 axes.  
Use **Cross Reference** matching to generate lists of coordinates that have all possible permutations  |  ![](ads-146.png)  
**Putting it all together**  
![](ads-147.png)  
  
## 2.5 Tutorials: data structures

[](Tutorial-2-5-1-Variable-thickness-pipe.gh) Tutorial 2.5.1: Variable
thickness pipe  
---  
Use the 4-step method to create a surface similar to the one in the image:  
![](ads-148.png)  
**Solution...**  
[ _download GH file..._ ](Tutorial-2-5-1-Variable-thickness-pipe.gh)  
__[Solution video...](https://vimeo.com/showcase/11456959/video/1030601815)  
  
**Algorithm Analysis:**  
We can think of two different ways to generate this surface:  
1\. **Loft** circles created along a line at random locations with random
radii  
2\. Create a profile curve at the circles start points, and **Revolve** around
the line  
![](ads-149.png)  
|  **Output:**  
The surface  |  ![](ads-150.png)  
---|---  
**Key Process:**  
Use the **Loft** component to generate the surface  |  ![](ads-151.png)  
**Input:**  
Line (not given, so create one),  
Number of intervals (not given, assume it is equal 10)  
Thickness range (not given, assume it is equal to 1.0 to 3.0)  |  ![](ads-152.png)  
**Intermediate processes #1:**  
The Loft is created from a list of circles. Use the Circle component that
takes centers, normals and radii lists.  
Use the default Loft options  
|  ![](ads-153.png)  
**Intermediate processes #2:**  
To create a list of random radii, use the **Random** component and the input
thickness range  
|  ![](ads-154.png)  
**Intermediate processes #3:**  
Evaluate the line at random intervals. Use the **Evaluate Curve** component to
extract center points and normals, and use the Random component to generate
the parameters along the curve.  
  
**Problem:**  
The loft follows the order of input curves. however, the parameters (generated from the **Random** component) are not ordered along the line and hence it produces unordered circles. Use the Sort List component to order the parameters before feeding them into the **Evaluate Curve** |  ![](ads-155.png)  
**Putting it all together**  
![](ads-156.png) [](Tutorial-2-5-2-Custom-list-matching.gh) Tutorial 2.5.2:
Custom list matching  
---  
Given the following three lists of numbers: [1, 2], [10, 20, 30] and [0.2,
0.4, 0.6, 0.9, 1], explain the default GH list matching when they are used as
input. Compare the default matching with the Grasshopper **Shortest List**
matching. Finally, use the original lists to create custom matching that
repeats the pattern in the shorter lists to create a periodic matching until
it matches the length of the longest list. For example [1,2] becomes
[1,2,1,2,1].  
**Solution...**  
[ _download GH file..._ ](Tutorial-2-5-2-Custom-list-matching.gh) |  **Construct default GH matching:**  
To test the matching, feed the lists into the coordinates of the Construct
Point component and observe the result  
![](ads-157.png)  
---  
**Analysize GH default matching:**  
The last element of shorter lists is repeated until all lists have the same
length, then elements are matched by indices  
![](ads-158.png)  
**Construct shortest List matching:**  
Omit additional values in longer lists so that the length of all lists equals
the length of the shortest list  
![](ads-159.png)  
**Create repeated custom matching:**  
We know that the longest list has 5 items, but it is a good practice to make
the script generic so it works with any input. First, figure out the length of
the longest list, then use the **Repeat** component to repeat the elements in
shorter lists until they match the length of the longest list  
![](ads-160.png)  
[](Tutorial-2-5-3-Simple-truss.gh) Tutorial 2.5.3: Simple truss  
---  
Use the 4-step method to generate a simple truss as in the image. Use the
given input for the baseline (base of the truss), height, number of runs (or
spans), and the radius of the joint.  
![](ads-161.png)  
**Solution...**  
[ _download GH file..._ ](Tutorial-2-5-3-Simple-truss.gh)  
__[Solution video...](https://vimeo.com/showcase/11456959/video/1030602374) |    
**Algorithm analysis:**  
---  
Define values for the input:  
**L** = create a **Line** along X-Axis  
**H** = assume height=7  
**R** = assume number of runs=10  
**J** = assume joint radius=0.5  
|  
![](ads-162.png)  
Divide the baseline into 20 spans (2* **R**)  |  ![](ads-163.png)  
Move every other point by 7 units (or **H**) in the Z-Axis direction  |  ![](ads-164.png)  
Create 3 sets of ordered points for the beams along the base, top and middle,
then connect each of the 3 sets with a polyline. Create spheres to represent
the joints.  
|  ![](ads-165.png)  
  
**Solution steps:**  
**Output:**  
There are 2 outputs, the beams as curves (polylines) and joints as spheres (surfaces)  |  ![](ads-166.png)  
**Key Process:**  
Need to create the polylines for the top, middle, and bottom beams. Use the
**Polyline** component with a relevant set of points for each.  
Use the **Sphere** component to create joints. Use middle points and joint radius as input.  |  ![](ads-167.png)  
**Input:**  
Specify the inputs and assume values when they are not given:  
line, number of runs, height and joint radius  |  ![](ads-168.png)  
**Intermediate processes #1:**  
Divide the curve with twice the number of runs. Use **Divide** Curve component and **Multiply** the number of runs  |  ![](ads-169.png)  
**Intermediate processes #2:**  
To create top points, select every other point from the list of all divide
points, then move vertically by the height amount.  
Use **Cull Pattern** component to select points and **Move** component to shift vertically  |  ![](ads-169A.png)  
**Intermediate processes #3:**  
To create bottom points, select every other point, in the invert pattern used
to select top points.  
Use **Cull Pattern** component to select points (set the **invert** flag for the pattern input)  |  ![](ads-170.png)  
**Intermediate processes #4:**  
To create middle points, **Weave** the top and bottom points.  |  ![](ads-171.png)  
**Putting it all together**  
![](ads-172.png) [](Tutorial-2-5-4-Pearl-necklace.gh) Tutorial 2.5.4: Pearl
necklace  
---  
Create a necklace with one big pearl in the middle, and gradually smaller size
pearls towards the ends as in the image. The number of pearls is between
15-25.  
![](ads-173.png)  
**Solution...**  
[ _download GH file..._ ](Tutorial-2-5-4-Pearl-necklace.gh) |    
**Algorithm analysis:**  
---  
The workflow to create the necklace follows these general lines:  
1\. Divide the curve into segments of variable distances (widest in the middle
and narrow towards the ends)  
2\. Find length and midpoints of each segment  
3\. Create spheres at midpoints using half the length as radius  
|  
![](ads-174.png)  
  
**Solution steps:**  
**Output:**  
The surfaces  |  ![](ads-175.png)  
**Key Process:**  
Use the Sphere component to generate the pearl surfaces  |  ![](ads-175A.png)  
**Input:**  
Necklace curve,  
Number of pearls as a parameter (can be changed by the user)  |  ![](ads-176.png)  
**Intermediate processes #1:**  
The **Range** component creates equal distances. We need to change to variable distances and for that we can use the **Graph Mapper** component to control the spacing.  |  ![](ads-177.png)  
**Intermediate processes #2:**  
Since we have normalized distances from the start of the curve (parameters are between 0 to 1), we can use the **Evaluate** **Length** component to find the divide points.  |  ![](ads-178.png)  
**Intermediate processes #3:**  
Generate the segments. Use Polyline and Explode components to turn the points
into segments  
Center points are calculated at the middle of the segments. Use Evaluate
Length at mid length  
Radii are calculated as half of each segment length. Use Length and Division
components  
|  ![](ads-179.png)  
**Putting it all together**  
![](ads-180.png)

## Next Steps

Those are the introduction to data structures. Next, learn [Advanced Data
Structures](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-
and-data-structures/advanced-data-structures/).

This is part 2-3 of the [Essential Algorithms and Data Structures for
Grasshopper](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-
and-data-structures/).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/gh-
algorithms-and-data-structures/data-structures/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/gh-
algorithms-and-data-structures/data-structures/index.md) [
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

