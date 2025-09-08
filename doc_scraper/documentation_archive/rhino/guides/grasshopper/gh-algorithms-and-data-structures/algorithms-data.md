---
url: https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-structures/algorithms-data/#19-tutorials-algorithms-and-data
scraped_at: 2025-09-08T15:40:58.841904
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

[Chapter 1: Algorithms and
Data](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-and-data-
structures/algorithms-data/)

  * 1.1 Algorithmic design
  * 1.2 Algorithms parts
  * 1.3 Designing algorithms: the 4-step process
  * 1.4 Data
  * 1.5 Data sources
  * 1.6 Data types
  * 1.7 Processing Data
    * 1.7.1 Numeric operations
    * 1.7.2 Logical operations
    * 1.7.3 Data analysis
    * 1.7.4 Data Sorting
    * 1.7.5 Data Selection
    * 1.7.6 Mapping
  * 1.8 Pitfalls of algorithmic design
    * 1.8.1 Invalid or wrong input type
    * 1.8.2 Unintended input
    * 1.8.3 Incorrect order of operation
    * 1.8.4 Mismatched data structures
    * 1.8.5 Long processing time
    * 1.8.6 Poor organization
  * 1.9 Tutorials: algorithms and data
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [Grasshopper
Guides](https://developer.rhino3d.com/en/guides/grasshopper/) / [Essential
Algorithms and Data Structures for
Grasshopper](https://developer.rhino3d.com/en/guides/grasshopper/gh-
algorithms-and-data-structures/) /

Chapter 1: Algorithms and Data

by [Rajaa Issa](https://discourse.mcneel.com/u/rajaa/) (Last updated: Monday,
July 15, 2024)

## 1.1 Algorithmic design

__[ Algorithmic design](https://vimeo.com/showcase/11456959/video/1030214506)

We can define algorithmic design as a design method where the **output** is
achieved through **well-defined steps**. In that sense, many human activities
are algorithmic. Take, for example, baking a cake. You get the **cake**
(output) by using a **recipe** (well-defined steps). Any change in the
ingredients (input) or the baking process results in a different cake. We will
analyze the parts of typical algorithms, and identify a strategy to build
algorithmic solutions from scratch.

Regardless of its complexity, all algorithmic solutions have 3 building
blocks: **input, key process,** and **output**. Note that the key process may
require additional input and processes.

![](ads-002.png) Figure(1): The building blocks of algorithmic solutions

Throughout this text, we will organize and label the solutions to identify the
three blocks clearly. We will also use consistent color coding to visually
distinguish between the parts. This will help us become more comfortable with
reading algorithms and quickly identify input, key processing steps, and
properly collect and display output. Visual cues are important to develop
fluency in algorithmic thinking.

In general, reading existing algorithmic solutions is relatively easy, but
building new ones from scratch is much harder and requires a new set of
skills. While it is useful to know how to read and modify existing solutions,
it is essential to develop algorithmic design skills to build new solutions
from scratch.

## 1.2 Algorithms parts

In Grasshopper, a solution flows from left to right. At the far left are input
values and parameters, and the far right has the output. In between are one or
more key processes, and sometimes additional input and output. Let’s take a
simple example to help identify the three parts of any algorithm (input, key
process, output). The simple addition algorithm includes two numbers (input),
the sum (output) and one key process that takes the numbers and gives the
result. We will use purple for the input, maroon for the key processes and
light blue for the output. We will also group and label the different parts
and adhere to organizing the Grasshopper solutions from left to right.

**Example 1-2-1:** Algorithm to add 2 numbers

![](ads-003.png)

Algorithms may involve intermediate processes. For example, suppose we need to
create a circle (output) using a center and a radius (input). Notice that the
input is not sufficient because we do not know the plane on which the circle
should be created. In this case, we need to generate additional information,
namely the plane of the circle. We will call this an intermediate process and
use brown color to label it.

**Example 1-2-2:** Algorithm to create a circle on the XY-Plane from a center
and a radius

![](ads-004.png)

Some solutions are not written with styles and hence are hard to read and
build on. It is very important that you take the time to organize and label
your solutions to make them easier to understand, debug and use by others.

Tutorial 1-2-3: Read existing algorithm  
---  
Given the following definition, write a description of what the algorithm
does, identify input, the main process(s) and output, then label and color-
code all the parts. Re-write the solution to make it more readable.
![](ads-005.png)  
**Solution...**  
In order to figure out what the algorithm is meant to do, we need to group the
input on the left side, and collect the output on the right side, then
organize the processes in the order of execution. We then step through the
solution from left to right to deduce what it does. We can examine and preview
the output in each step.  
  
The example of the tutorial is meant to create a circle that is twice as large
as another circle that goes through three given points. One of the points is
constructed out of its 3 coordinates.  ![](ads-006.png)  
  
## 1.3 Designing algorithms: the 4-step process

__[ Modeling in Rhino vs
Grasshopper](https://vimeo.com/showcase/11456959/video/1030225149)

__[ The 4-step process to designing
algorithms](https://vimeo.com/showcase/11456959/video/1030216024)

Before we generalize a method to design algorithms, let’s examine an algorithm
we commonly use in real life such as baking a cake. If you already have a
recipe for a cake, you simply get the recommended ingredients, mix them, pour
in a pan, put in a preheated oven for a certain amount of time, then serve. If
the recipe is well documented, then it is relatively straightforward to use.
As you become more proficient in baking cakes, you may start to modify the
recipe. Perhaps add new ingredients (chocolate or nuts) or use different tools
(cupcake container).

![](ads-007.png) Figure(2): Steps to follow existing recipe

When designers write algorithms, they typically try to search for existing
solutions and modify them to fit their purposes. While this is a good entry
point, using existing solutions can be frustrating and time-consuming. Also,
existing solutions have their own flavor and that may influence design
decisions and limit creativity. If designers have unique problems, and they
often do, they have no choice but to create new solutions from scratch; albeit
a much harder endeavor.

Back to our example, the task of baking a cake is much harder if you don’t
have a recipe to follow and have not baked one before. You will have to guess
the ingredients and the process. You will likely end up with bad results in
the first few attempts, until you figure it out! In general, when you create a
new recipe, you have to follow the process in reverse. You start with an image
of the desired cake, you then guess the ingredients, tools and steps. Your
thinking goes along the following lines:

  * The cake needs to be baked, so I need an oven and time,
  * What goes in the oven is a cake batter held by a container,
  * The batter is a mix of ingredients

![](ads-008.png) Figure(3): Steps to invent a new recipe from scratch

We can use a similar methodology to design parametric algorithms from scratch.
Keep in mind that creating new algorithms is a “skill” and it requires
patience, practice and time to develop.

**Algorithmic thinking in 3D modeling vs parametric design**

3D modeling involves a certain level of algorithmic thinking, but it has many
implicit steps and data. For example designing a mass model using a 3D modeler
may involve the following steps:

  1. Think about the output (e.g. a mass out of few intersecting boxes)
  2. Identify a command or series of commands to achieve the output ( e.g. run Box command a few times, Move, Scale or Rotate one or more boxes, then BooleanUnion the geometry).

At that point, you are done!

Data such as the base point for your initial box, width, height, scale factor,
move direction, rotation angle, etc. are requested by the commands, and the
designer does not need to prepare ahead of time. Also, the final output (the
boolean mass) becomes directly available and visible as an object in your
document.

![](ads-009.png) Figure(4): Interactive 3D modeling to create and manipulate
geometry uses visual widgets and guides

Algorithmic solutions are not interactive and require explicit articulation of
data and processes. In the box example, you need to define the box orientation
and dimensions. When copy, you need a vector and when rotate you need to
define the plane and angle of rotation.

![](ads-010.png) Figure(5): Algorithmic solutions involve explicit definition
of geometry, vectors and transformations

**Designing algorithms**

Designing algorithms requires knowledge in geometry, mathematics and
programming. Knowledge in geometry and mathematics is covered in the
[Essential Mathematics for Computational
Design](https://developer.rhino3d.com/guides/general/essential-mathematics/).
As for programming skills, it takes time and practice to build the ability to
formulate design intentions into logical steps to process and manage geometric
data. To help get started, it is useful to think of any **algorithm as a
4-step process** as in the following:

**1\. Output** | Clearly identify the desired outcome  
---|---  
**2\. Key processes** | Identify key steps to reach the outcome  
**3\. Input** | Examine initial data and parameters  
**4\. Intermediate steps** | Define intermediate parameters and processes to generate additional data  
  
Thinking in terms of these 4 steps is key to developing the skill of
algorithmic design. We will start with simple examples to illustrate the
methodology, and gradually apply more complex examples.

**Example 1-3-1: Add two numbers** Use the 4-Step process to write an
algorithm to add two numbers

![](ads-011.png) **1\. Output:  
The sum of the 2 numbers**  
Use the Panel component to collect the sum |  ![](ads-012.png)  
---|---  
**2\. Key processes:  
Addition**  
Use the Addition component that takes 2 numbers and gives the sum | ![](ads-013.png)  
**3\. Input:  
2 numbers**  
Use the Panel component to hold and view the values of input numbers | ![](ads-014.png)  
  
**Example 1-3-2: Create a circle** Use the 4-Step process to create a circle
from a given center and radius

![](ads-015.png) **1\. Output:  
A Circle**  
Use the **Circle** parameter to collect the output | ![](ads-016.png)  
---|---  
**2\. Key processes:**  
Identify a key process that generates a circle from a radius  
Use the **Circle** component in Grasshopper | ![](ads-017.png)  
**3\. Input:**  
Use the given input (center and radius). Feed the radius to the **Circle** component | ![](ads-018.png)  
**4\. Intermediate process:**  
The circle needs a center, and also the plane on which the circle is located. Let's assume the circle is on a plane parallel to the XY-Plane and use the circle center as the origin of the plane | ![](ads-019.png)  
  
**Example 1-3-3: Create a line** Use the 4-Step process to create an algorithm
to generate a line from 2 points. One point is referenced from Rhino, and the
other is created using three coordinates (x=1, y=0.5 and z=3)

![](ads-020.png) **1\. Output:**  
The line geometry. Use the **Geometry** parameter to collect the output | ![](ads-021.png)  
---|---  
**2\. Key processes:**  
Identify a key process that generates a line from 2 points. Use the **Line** component in Grasshopper | ![](ads-022.png)  
**3\. Input:**  
Use the given input (a referenced point and 3 coordinates). Feed one point to one of the ends of the line | ![](ads-023.png)  
**4\. Intermediate process:**  
Before we can use the coordinates as a point, we need to construct a point | ![](ads-024.png)  
  
In more complex algorithms, we will need to analyze the problems, investigate
possible solutions and break them down to pieces whenever possible to make it
more manageable and readable. We will continue to use the 4-step process and
other techniques to solve more complex algorithms throughout the book.

## 1.4 Data

Data is information stored in a computer and processed by a program. Data can
be collected from different sources, it has many types and is stored in well
defined structures so that it can be used efficiently. While there are
commonalities when it comes to data across all scripting languages, there are
also some differences. This book explores data and data structures specific to
Grasshopper.

## 1.5 Data sources

__[ Data and data
sources](https://vimeo.com/showcase/11456959/video/1030590039)

In Grasshopper, there are three main ways to supply data to processes (or what
is called components): internal, referenced and external.

Data sources in Grasshopper  
---  
**1\. Internally set data**  
Data can be set inside any instance of a parameter. Once set, it remains
constant, unless manually changed or overridden by external input. This is a
good way when you do not  
**2\. Referenced data**  
Data can be referenced from Rhino or some external document. For example, you
can reference a point created in a Rhino document. When you move the point in
Rhino, its reference in Grasshopper updates as well. Grasshopper files are
saved separately from Rhino files, and hence if the GH file has referenced
data, the Rhino file needs to be saved and passed along with the GH file to
avoid any loss of data  
![](ads-025.png)  
generally need to change the data after it is set (constant). Data is stored
inside the GH file  
![](ads-026.png)  
**3\. Externally supplied data**  
Data can be supplied from previous processes. This method is best suited for
dynamic data or data controlled parametrically. Externally supplied data to a
parameter takes precedent over the internal or referenced values (when both
exist)  
![](ads-027.png)  
  
## 1.6 Data types

__[ Data types](https://vimeo.com/showcase/11456959/video/1030590459)

__[ Data casting](https://vimeo.com/showcase/11456959/video/1030590809)

All programming languages identify the kind of data used in terms of the
values that can be assigned to and the operations and processes it can
participate in. There are common data types such as **Integer, Number, Text,
Boolean** (Boolean type can be set to **True** or **False**), and others.
Grasshopper lists those under the **Params > Primitives** tab.

![](ads-028.png) Figure(6): Examples of primitive data types common to all
programming languages

Grasshopper supports geometry types that are useful in the context of 3D
modeling such as Point (3 numbers for coordinates), **Line** (2 points),
**NURBS Curve, NURBS Surface, Brep** , and others. All geometry types are
included under the **Params > Geometry** tab in GH.

![](ads-029.png) Figure(7): Examples of geometry data types

There are other mathematics types that designers do not usually use in 3D
modeling, but are very common in parametric design such as Domains, Vectors,
Planes, and Transformation Matrices. GH provides a rich set of tools to help
create, analyze and use these types. To fully understand the mathematical as
well as geometry types such as NURBS curves and surfaces, you can refer to the
[Essential Mathematics for Computational
Design](https://developer.rhino3d.com/guides/general/essential-mathematics/)
book by the author

![](ads-030.png) Figure(8): Examples of data types common in computer graphics

The parameters in GH can be used to convert data from one type to another
(cast). For example if you need to turn a text into a number, you can feed
your text into a **Number** parameter. If the text cannot be converted, you’ll
get an error.

![](ads-031.png) Figure(9): Data conversion (casting) inside parameters in
Grasshopper

Grasshopper components internally convert input to suitable types when
possible. For example, if you feed a “text” to **Addition** component, GH
tries to read the text as a number. If a component can process more than one
type, it uses the input type without conversion. For example, equality in an
expression can compare text as well as numbers. In such case, make sure you
use the intended type to avoid confusion.

![](ads-032.png) Figure(10): Some operations can be performed on multiple
types. Cast to the intended type especially if the component is capable of
processing multiple types (such as Expression in GH)

It is worth noting that sometimes GH components simply ignore invalid input
(null or wrong type). In such cases, you are likely to end up with an
unexpected result and it will be hard to find the bug. It is very important to
verify the output from each component before using it.

![](ads-033.png) Figure(11): Invalid input is ignored and a default value is
used. For example a number inside a Panel component can be interpreted as a
text and hence become invalid input to an Addition component

## 1.7 Processing Data

Algorithmic designs use many data operations and processes. In the context of
this book, we will focus on five categories: numeric and logical operations,
analysis, sorting and selection.

### 1.7.1 Numeric operations

__[ Numeric operations in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030591400)

Numeric operations include operations such as arithmetic, trigonometry,
polynomials and complex numbers. GH has a rich set of numeric operations, and
they are mostly found under the **Math** tab. There are two main ways to
perform operations in GH. First by using designated components for specific
operations such as **Addition, Subtraction** and **Multiplication**.

![](ads-034.png) Figure(12): Examples of numeric operations components in GH

Second, use an **Expression** component where you can combine multiple
operations and perform a rich set of math and trigonometry operations, all in
one expression.

![](ads-035.png) Figure(13): Expression component in GH can be used to perform
multiple operations

The **Expression** component is more robust and readable when you have
multiple operations.

![](ads-036.png) Figure(14): When a chain of operations is involved, using the
Expression component is easier to maintain

Input to Expressions can be treated as text depending on the context.

![](ads-037.png) Figure(15): Expression can process and format text

It is worth mentioning that most numeric input to components allow writing an
expression to modify the inputs inline. For example, the Range component has N
(number of steps) input. If you right mouse click on “N”, you can set an
expression. You always use “x” to represent the supplied input regardless of
the name.

![](ads-038.png) Figure(16): Expression can be set inside the input parameter.
Variable “x” refers to the supplied input value

### 1.7.2 Logical operations

__[ Logical operations in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030591761)

Main logical operations in GH include equalities, sets and logic gates.

![](ads-039.png) Figure(17): Grasshopper has multiple components to perform
Logical operations

Logical operations are used to create conditional flow of data. For example,
if you like to draw a sphere only when the radius is between two values, then
you need to create a logic that blocks the radius when it is not within your
limits.

![](ads-040.png) Figure(18): Data flow control using logical operations

### 1.7.3 Data analysis

__[ Data analysis in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030592921)

There are many tools in GH to examine and preview data. **Panel** is used to
show the full details of the data and its structure, while the **Parameter
Viewer** shows the data structure only. Other analysis components include
**Quick Graph** that plots data in a graph, and **Bounds** to find the limits
in a given set of numbers (the min and max values in the set).

![](ads-041.png) Figure(19): Some of the ways to analyze data in Grasshopper

### 1.7.4 Data Sorting

__[ Data sorting in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030593355)

GH has designated components to sort numeric and geometry data. The Sort List
component can sort a list of numeric keys. It can sort a list of numbers in
ascending order or reverse the order. You can also use the Sort List component
to sort geometry by some numeric keys, for example sort curves by length. GH
has components designated to sort geometry sets such as Sort Points to sort
points by their coordinates.

![](ads-042.png) Figure(20): Sorting numbers in Grasshopper

### 1.7.5 Data Selection

__[ Data selection in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030593936)

3D modeling allows picking specific or a group of objects interactively, but
this is not possible in algorithmic design. Data is selected in GH based on
the location within the data structure, or by a selection pattern. For example
**List** Item component allows selecting elements based on their indices.

![](ads-043.png) Figure(21): Select items from a list in Grasshopper

The **Cull Pattern** component allows using some repeated patterns to select a
subset of the data.

![](ads-044.png) Figure(22): An example to select every other item in a list

As you can see from the examples, selecting specific items or using cull
components yield a subset of the data, and the rest is thrown away. Many times
you only need to isolate a subset to operate on, then recombine back with the
original set. This is possible in GH, but involves more advanced operations.
We will get into the details of these operations when we talk about advanced
data structures in chapter 3.

### 1.7.6 Mapping

__[ Data mapping in
Grasshopper](https://vimeo.com/showcase/11456959/video/1030594157)

That refers to the linear mapping of a range of numbers where each number in a
set is mapped to exactly one value in the new set. GH has a component to
perform linear mapping called **ReMap**. You can use it to scale a set of
numbers from its original range to a new one. This is useful to scale your
range to a domain that suits your algorithm’s needs and limitations.

![](ads-045.png) Figure(23): An example of linear remapping of numbers in
Grasshopper

Converting data involves mapping. For example, you may need to convert an
angle unit from degrees to radians ( GH components accept angles in radians
only).

![](ads-046.png) Figure(24): Convert angles from degrees to radians

As you know, parametric curves have “domains” (the range of parameters that
evaluate to points on the curve). For example, if the domain of a given curve
is between 12.5 to 51.3, evaluating the curve at 12.5 gives the point at the
start of the curve. Many times you need to evaluate multiple curves using
consistent parameters. Reparameterizing the domain of curves to some unified
range helps solve this problem. One common domain to use is “0 To 1”. At the
input of each curve in any GH component, there is the option to
**Reparameterize** which resets the domain of the curve to be “0 to 1”.

![](ads-047.png) Figure(25): Normalize the domain of curves (set to 0-1). Use
Reparameterize input flag in Grasshopper Tutorial 1-7-A: Flow control  
---  
What is the purpose of the following algorithm? Notate and color code to
describe the purpose of each part.  ![](ads-048.png)  
**Solution...**  
**Analyze the algorithm**  
The algorithm has an output that is a sphere, a radius input and some
conditional logic to process the radius.  ![](ads-049.png)  
  
**Notate and color-code the solution**  
From testing the output and following the steps of the solution it becomes
apparent that the intention is to make sure that the radius of the sphere
cannot be less than 1 unit.  
Test with radius greater than 1 (3.4 in the example)  ![](ads-050.png)  
  
Test with radius less than 1 (-2.8 in the example)  ![](ads-051.png)  
  
  
Tutorial 1-7-B: Data processing  
---  
Given a list of numbers of some point coordinates, do the following:  
1\. Analyze the list to understand the data.  
2\. Write an algorithm to convert the list of **Numbers** to a list of
**Points**.  
3\. Change the domain of coordinate values to be between 3 and 9.  
  
Note that the input number list is organized so that the first 3 numbers refer
to the x,y,z of the first point, the second 3 numbers belong to the second
point and so on.  
**Solution...**  
**Analyze the algorithm**  
|  There are 2 inputs: a list of 51 numbers (3 coordinates for each point)
which means that the list has 17 points.  
Using a **QuickGraph** , we can see that the numbers are between 2.60 and 15.89. We can also see that the values are distributed randomly. The other input is the target domain to be from 3 to 9.  |  ![](ads-052.png)  
---|---  
**Use the 4-step process to solve the algorithms**  
**Output: List of points**  
Use the **Parameter Viewer** to view the resulting data structure. To start, it will be empty.  |  ![](ads-054.png)  
---|---  
**Key Process #1: Remap Coordinates**  
Map the coordinates list from its current domain (2.60 to 15.89) to a new
domain (3.0 to 9.0)  
Use **ReMap** component to achieve that  |  ![](ads-055.png)  
**Intermediate processes #1**  
The input domain is missing and can be extracted using **Bounds** component  |  ![](ads-056.png)  
**Key Process #2: Construct Points**  
Construct points from coordinates  
Use **Construct Point (Pt)** component  |  ![](ads-057.png)  
**Intermediate processes #2**  
Extract all X coordinates as one list, Y in another and Z in the third. Use
**Cull Pattern** component with appropriate pattern to extract each coordinate
as a separate list.  
  
The input to **Cull** is the remapped points from process #1  |  ![](ads-058.png)  
**Putting it all together**  
![](ads-059.png)  
  
## 1.8 Pitfalls of algorithmic design

__[ Pitfalls of algorithmic
design](https://vimeo.com/showcase/11456959/video/1032151256)

Writing elegant algorithms that are efficient and easy to read and debug is
hard. We explained in this chapter how to write algorithms with style using
color-coding and labeling. We also articulated a 4-step process to help
develop algorithms. Following these guides help minimize bugs and improve the
readability of the scripts. We will list a few of the common issues that lead
to incorrect or unintended result.

### 1.8.1 Invalid or wrong input type

If the input is of the wrong type or is invalid, GH changes the color of
components to red or orange to indicate an error warning, with feedback about
what the issue might be. This is helpful, but sometimes faulty input goes
unnoticed if the components assign a default value, or calculate an
alternative value to replace the input, that is not what was intended. It is a
good practice to always double check the input (hook to a panel or parameter
viewer and label the input). To avoid using wrong types, it is advisable to
convert to the intended type to ensure accuracy.

![](ads-060.png) Figure(26): Error resulting from wrong input type

### 1.8.2 Unintended input

Input is prone to unintended change via intermediate processes or when
multiple users have writing access to the script. It is very useful to preview
and verify all key input and output. The Panel component is very versatile and
can help check all types of values. Also you can set up guarding logic against
out of range values or to trap undesired values.

![](ads-061.png) Figure(27): Error resulting from unintended input. Cannot
assume curve domain is 0-1 and use 0.5 to evaluate the midpoint
![](ads-062.png) Figure(28): Example of a robust solution to evaluate the
midpoint of a curve

### 1.8.3 Incorrect order of operation

You should try to organize your solutions horizontally or vertically to
clearly see the sequence of operations. You should also check the output from
each step to make sure it is as expected before continuing on your code. There
are also some techniques that help consolidate the script, for example use
**Expression** when multiple numeric and math operations are involved. The
following highlights some unfavorable organization.

![](ads-063.png) Figure(29): Easy to confuse input to operations with poor
organization

The following shows how to rewrite the same code to make it less error prone.

![](ads-064.png) Figure(30): Best practices to align input with processes, or
use Expressions

### 1.8.4 Mismatched data structures

The issue of mismatched data structures as input to the same process or
component is particularly tricky to guard against in GH, and has the potential
to spiral the solution out of memory. It is essential to test the data
structure of all input (except trivial ones) before feeding into any
component. It is also important to examine desired matching under different
scenarios (data matching will be explained at length later).

![](ads-065.png) Figure(31): Mismatched data structures of input can cause
errors in the output

### 1.8.5 Long processing time

Some algorithms are time consuming, and you simply have to wait for it to
process, but there are ways to minimize the wait when it is unnecessary. For
example, at the early cycles of development, you should try to use a smaller
set of data to test your solution with before committing the time to process
the full set of data. It is also a good practice to break the solution into
stages when possible, so you can isolate and disable the time consuming parts.
Also, it is often possible to rewrite your solution to be more optimized and
consume less time. Use the GH **Profiler** to test processing time. When a
solution takes far too long to process or crashes, you should do the
following: before you reopen the solution, disable it, and disconnect the
input that caused the crash.

![](ads-066.png) Figure(32): Grasshopper Profiler widget helps observe
processing time

### 1.8.6 Poor organization

Poorly organized definitions are not easy to debug, understand, reuse or
modify. We can’t stress enough the importance of writing your definitions with
styles, even if it costs extra time to start with. You should always color
code, label everything, give meaningful names to variables, break repeated
operations into modules and preview your input and output.

![](ads-067.png) Figure(33): Poor organization in visual programming make the
code hard to read and debug

## 1.9 Tutorials: algorithms and data

[](Tutorial-1-9-1-Unioned-circles.gh) Tutorial 1.9.1: Unioned circles  
---  
Use the 4-step process to design an algorithm that combines 2 circles, given
the following:  
Both circles are located on the XY-Plane. The first circle (Cir1) has a center
(C1) = (2,2,2) and radius (R1) that is equal to a random number between 3 and
6. The second circle (Cir2) has a center (C2) that is shifted to the right of
the first circle (Cir1) by an amount equal to the radius of the first circle
(R1) along the positive X-Axis. The second circle radius (R2) is 20% bigger,
or in other words (R2) = (R1) * 1.2.  
**Solution...**  
[ _download GH file..._ ](Tutorial-1-9-1-Unioned-circles.gh)  
**Analyze the question and the flow of the solution**  
|  There are 2 inputs: the coordinates of the center of the first circle
(2,2,2) and the XY-Plane where both circles are located. Also, we know that
the second circle is shifted the positive X-Axis direction, The following
diagram shows an overview of the solution:  
![](ads-068.png)  
---  
**Solution steps**  
**Output: Curve for the region union** |  ![](ads-069.png)  
---|---  
**Key Process: Union of 2 circles**  
Use the **Region Union** component that takes curves and a plane  |  ![](ads-070.png)  
**Input: needed to calculate the region union**  
Identify the input needed and use given input when relevant.  
  
The plane for region union has been given. The 2 circles need their own plane and radius. The center of the plane is the center of the circle.  |  ![](ads-071.png)  
**Intermediate processes #1:**  
generate the center and plane of the 1st circle  
Construct a center from the given coordinates. Create a plane using **Plane
Origin** component and use the constructed center and XY-Plane.  
  
The radius is from a random number between 3 and 6. Use **Random** component to create the radius  |  ![](ads-072.png)  
**Intermediate processes #2**  
Generate the center and plane of the 2nd circle  
Calculate the 2nd circle plane by moving the first circle plane along the
x-axis by an amount = first radius  
  
Calculate the 2nd circle radius by multiplying the first radius by 1.2  |  ![](ads-073.png)  
**Putting it all together**  
![](ads-074.png)  
[](Tutorial-1-9-2-Sphere-with-bounds.gh) Tutorial 1.9.2: Sphere with bounds  
---  
Use the 4-step process to draw a sphere with a radius between 2 and 6. If
input is less than 2, then set the radius to 2, and if input radius is greater
than 6, set the radius to 6. Use a number slider to input the radius and set
between 0 and 10 to test. Make sure your solution is well organized, color-
coded and labeled properly.  
**Solution...**  
[ _download GH file..._ ](Tutorial-1-9-2-Sphere-with-bounds.gh)  
**The 4-step process to solve the algorithm**  
|  **Output: The sphere as geometry** |  ![](ads-075.png)  
---|---  
**Key Process: Create a sphere**  
Use the **Sphere** component to create a sphere from a base plane and radius  |  ![](ads-076.png)  
**Input:**  
1\. The radius parameter (0 - 10)  
2\. The bounds of the radius are 2 & 6  |  ![](ads-077.png)  
**Intermediate processes #1:**  
Construct a selection logic of radii and pattern. The radii is a list of the
values from the slider, min and max.  
The list of pattern is generated to select the correct radius value  |  ![](ads-078.png)  
**Intermediate processes #2**  
Generate the center and plane of the 2nd circle  
The selection logic ensures that the radius value falls within the intended range. If the radius input is less than the minimum value of the bounds, then the radius is set to the min value, and if it is greater than the maximum, then the max value is used instead.  |  ![](ads-079.png)  
[](Tutorial-1-9-3-Data-operations.gh) Tutorial 1.9.3: Data operations  
---  
Given the numbers embedded in the **Number** parameter do the following:  
1\. Analyze input in terms of bounds and distribution  
2\. View the data and how it is structured  
3\. Extract even numbers  
4\. Sort numbers descending  
5\. Remap sorted numbers to (100 to 200)  
**Solution...**  
[ _download GH file..._ ](Tutorial-1-9-3-Data-operations.gh) |    
**1- Analyze the input bounds and distribution**  
  
Use the **QuickGraph** to show that the set of numbers are between 3 and 98 and are distributed randomly.  |  ![](ads-081.png)  
---|---  
**2- Analyze the input data structure and values**  
  
Use the **Panel** and **Parameter Viewer** to show that there are 16 elements organized in a list  |  ![](ads-082.png)  
**3- Extract Even numbers**  
  
Create the logic to test if a number is even (divisible by 2 without a remainder) and use **Dispatch** to extract even numbers  |  ![](ads-083.png)  
**4- Sort numbers descending**  
  
The Sort List component sorts numbers in ascending order. Use Reverse List component to further process the list to order descending  |  ![](ads-084.png)  
**5- Remap to 100-200**  
  
Check the input range and use Remap component to scale data to be between 100-200  |  ![](ads-085.png)  
[](Tutorial-1-9-4-Algorithmic-pitfalls.gh) Tutorial 1.9.4: Algorithmic
Pitfalls  
---  
Analyze what the following algorithm is intended to do, identify the errors
that are preventing it from working as intended, then rewrite to fix the
errors. Organize to reflect the algorithm flow, label and color-code.  
**Solution...**  
[ _download GH file..._ ](Tutorial-1-9-4-Algorithmic-pitfalls.gh) |    
The first step is to mark the errors: ![](ads-086.png)  
---  
Next, fix the errors and rewrite the solution with labels and proper color
codes: ![](ads-087.png)  
  
## Next Steps

Those are the algorithms and data. Next, learn [Introduction to Data
Structures](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-
and-data-structures/data-structures/).

This is part 1-3 of the [Essential Algorithms and Data Structures for
Grasshopper](https://developer.rhino3d.com/guides/grasshopper/gh-algorithms-
and-data-structures/).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/grasshopper/gh-
algorithms-and-data-structures/algorithms-data/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/grasshopper/gh-
algorithms-and-data-structures/algorithms-data/index.md) [
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

