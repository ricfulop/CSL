---
url: https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-lists-dictionaries/
scraped_at: 2025-09-08T15:37:44.200756
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

[6 Tuples, Lists, and
Dictionaries](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/)

  * 6.1 Tuples
  * 6.2 Lists
    * 6.2.1 List Comprehension
  * 6.3 Dictionaries
  * 6.4 Points and Vectors
  * 6.5 An AddVector() example
  * 6.6 Nested Lists
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) / [Rhino.Python
101](https://developer.rhino3d.com/en/guides/rhinopython/primer-101/) /

6 Tuples, Lists, and Dictionaries

by [Skylar Tibbits](https://discourse.mcneel.com/u//), [Arthur van der
Harten](https://discourse.mcneel.com/u/aharten/), and [Steve
Baer](https://discourse.mcneel.com/u/stevebaer/) (Last updated: Wednesday,
December 5, 2018)

## 6.1 Tuples

We’ve already been using tuples and lists in examples and I’ve always told you
not to worry about it. Those days are officially over. Now is the time to
panic. Perhaps it’s best if we just get the obvious stuff out of the way
first:

**Tuples, Lists and Dictionaries are just a collection of things!**

That’s really all there is to it. Sometimes -in fact quite often- you want to
store a large or unknown amount of things. You could of course declare 15,000
different variables by hand but that is generally considered to be bad
practice. Remember, Tuples, Lists and Dictionaries always start counting at
zero, while us humans are normally used to start counting at one. Try it by
counting the number of fingers on your right hand. Chances are you are someone
who has just counted to five. Code would disagree with you, it would only have
counted to four:

![https://developer.rhino3d.com/images/primer-
arraycountingfingers.png](https://developer.rhino3d.com/images/primer-
arraycountingfingers.png)

It helps to refer to numbers as ‘indices’ when you use the zero-based counting
system just to avoid confusion. So when we talk about the ‘first element’ of a
tuple we actually mean ’the element with index 0’. I know this all sounds
strange, but zero-based counting systems habitually confuse even the most die-
hard programmer.

A tuple consists of a number of values separated by commas, for instance:

    
    
    t = 12345, 5421, 'hello!' # Creating a Tuple with a variable name t
    print(t[0]) # print the first value of the Tuple t
    # This returns 12345 - the first value inside the Tuple
    print(t)
    # This returns (12345, 54321, 'hello!') - all of the values within the Tuple
    

Tuples can be used for coordinates (x,y) or any other time you need to store
various elements. Tuples may contain multiple variables, nested Tuples, Lists
or other objects. If you remember from section 4.5, Tuples are immutable,
meaning that they cannot be changed! (Refer to section 4.5 on Mutability) That
means that we cannot create a Tuple then remove an element, instead we need to
create an entirely new Tuple that contains the desired change. A number of
RhinoscriptSyntax methods return tuples rather than lists for their
simplicity. When utilizing the RhinoscriptSyntax methods make sure to be
particularly careful with the input and return types (numbers, strings,
tuples, lists etc) and understand how to pass or use each of them. This is a
common source of errors in people’s code, so pay special attention to read the
methods found in the RhinoscriptSyntax help file!

## 6.2 Lists

Lists are just like Tuples, however they can be changed (mutable), they use
brackets rather than parenthesis and have far more powerful built-in
functionality! Lists can be added to, items can be removed, they can be
sorted, sliced apart, nested with multiple levels of inner lists and packed
with other objects. Lists are very powerful!

Download and open
[__5_4_TwistAndShout.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/5_4_TwistAndShout.py).

    
    
    myList = [] #This creates an empty list with the variable name myList
    myList.append(5)
    myList.append(6)
    print myList[0]
    # This returns 5 - the first element (0th item) in the list
    print(myList)
    # This returns [5,6] - the entire contents of the list myList
    

Lists also can be sliced by using the following syntax:

    
    
    myList = [1,2,3,4] #This creates a list with elements 1,2,3,4
    print(myList[1:3])
    #This returns [2,3] - the 1st and 2nd elements of the list
    

Similar to the range() function, the syntax for slicing list[start:end] -
begins with the index of “start” (from the 0th element) and finishes at 1 less
than the index “end.” To create a copy of a list we can also use a similar
syntax:

    
    
    myList = [1,2,3,4] #This creates a list with elements 1,2,3,4
    dupList = myList[:]
    

Some useful methods for lists:

Method |  |  | Description  
---|---|---|---  
list.append(x) |  |  | Adds an item to the end of a list.  
list.insert(i,x) |  |  | Inserts item i at location x.  
list.remove(x) |  |  | Removes the first item from the list who’s value is x.  
list.count(s) |  |  | Counts how many times an item x is found within the list.  
list.append(x) |  |  | Adds an item to the end of a list.  
list.sort() |  |  | Sorts the elements of the list.  
list.reverse() |  |  | Reverses the elements of the list.  
  
### 6.2.1 List Comprehension

List comprehensions are a way of utilizing the functionality of Lists and
For…Loops with very concise syntax. The list comprehension begins with an
expression then has a For…Loop - effectively executing the expression for the
number of times specified in the For…Loop. This will create a List with the
resultant values from the expression. For example:

    
    
    myList = [2,4,6] #This creates a list with elements 2,4,6
    print([3*x for x in myList])
    # This returns [6,12,18] as the resultant calculation from the List Comprehension
    

List comprehensions can become far more complex and include more complicated
expressions, loops and conditional statements. One last example:

    
    
    myList = [2,4,6] #This creates a list with elements 2,4,6
    print([3*x for x in myList if x>3])
    # This returns [12,18] as the resultant calculation from the expression, loop and conditional
    

The following example should teach you almost all there is to know about
lists, except nesting:

Download and open
[__6_2_1_MyFavouriteThings.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/6_2_1_MyFavouriteThings.py).

    
    
    import rhinoscriptsyntax as rs
    
    
    def myfavoritethings():
        things = []
    
        while True:
            count = len(things)
            prompt = "What is your {}th most favorite thing?".format(count+1)
    
            if len(things)==0:
                prompt = "What is your most favorite thing?"
            elif count==1:
                prompt = "What is your second most favorite thing?"
            elif count==2:
                prompt = "What is your third most favourite thing?"
    
            answer = rs.GetString(prompt)
            if answer is None: break
            things.append(answer)
        if len(things)==0: return
    
        print("Your", len(things)+1, "favorite things are:")
        for i,thing in enumerate(things): print(i+1, ".", thing)
    
    
    if __name__=="__main__":
        myfavoritethings()
    

Line | Description  
---|---  
4 | We do not know how many favourite things the user has, so there's no way we can set the list to a certain size in advance. Luckily, we do not have to. Items can be appended to a list on an as needed basis!  
8 | The function len() returns the length of a list object. The very first time this line is run, count will be 0.  
19 | If the user does not enter an answer to our question regarding his/her Nth favorite thing, we will exit the loop and move into the last task of the script on lines 21 and 22.  
20 | We've just asked the user what his/her Nth favourite thing was, and he/she answered truthfully. This means that it is time to store the answer in a safe place. A list is a convenient place to store an arbitrarily long collection of data. The append function shown will add the entry to the end of the list.  
21 | It is possible the user has not entered any String. If this is the case then the result of len(things) will still have a its initial value of zero. There is nothing for us to do in this case and we should abort the subroutine.  
23 | After the loop has completed and we've made certain the array contains some actual data, we print all the gathered information to the command history. First we will tell the user how many favourite things he/she entered.  
24 | Using a For...loop, we can iterate through the items in the list. Note that this For...loop has two iteration variables - one to keep track of the index of the list item, and one to get the actual list item. This is convenient, as it is not necessary to explicitly retrieve the item in the list using the index. We then print the index of the user's nth favority thing, and the favorite thing.  
  
## 6.3 Dictionaries

Dictionaries go one step further than lists because they store a “key” and an
associated value. Every dictionary contains a series of key : value
associations. This is very similar to actual word-based dictionaries that
contain words and their associated definition. Python Dictionaries can use any
immutable type for the “key”, such as; strings, numbers, Tuples (they can only
contain strings, numbers or tuples and NOT lists). The value can be any
mutable or immutable item that will become associated to the key (this
includes, lists or other dictionaries). Lets see an example:

    
    
    emptyDict = {} #This creates an empty Dictionary
    myDict = {'a':1,'b':2,'c':3} #This creates a Dictionary with its associated Key:Value pairs
    myDict['d'] = 4 #This Adds a key:value to the Dictionary
    myDict['a'] = 2 #This Changes the key "a"'s value to 2 rather than 1
    print (myDict['a'])
    #This returns 2 - the associated value to the key "a"
    print (myDict)
    #This returns {'a': 2, 'c': 3, 'b': 2, 'd': 4} - the entire Dictionary
    print (myDict.keys())
    #This returns ['a', 'c', 'b', 'd'] - a list containing all of the Keys
    del myDict['b'] # This deletes the Key "b" and its associated value of 2
    

Because of the associated Key:Value relationship, Dictionaries are great for
representing points and giving them an associated name based on the points
relationship to their neighbors. Let’s say we have a surface and we want to
extract points across the surface with rows and columns. Each point has a 3D
point coordinate [x,y,z] which is represented as a list who’s first element 0
corresponds to x, element 1 corresponds to y and element 2 corresponds to z.
If we wanted to store these points we have 2 options. We could create a list
with internal lists that contain the point coordinates (one long linear
organization of points) or we could use a Dictionary to add point coordinates
as values and have a Key that is a name in relation to its Row/Column
position. The second option then allows us to take any point on the surface
and know its 4, 8 or however many neighbors because they are named
accordingly. The first option would only allow us to know the neighbor
direction in front or behind it in line. We will get into this more later, but
this should wet your appetite for the exciting potential of lists and
dictionaries for geometric information!

## 6.4 Points and Vectors

As was just explained, points are represented by lists containing three values
- [x,y,z]. This notation is used for both points and vectors. First, a point
example:

Download and open
[__6_4_PointSpiral.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/6_4_PointSpiral.py).

    
    
    import rhinoscriptsyntax as rs
    import math
    
    def pointspiral():
        t = -5
        while t<=5:
            point = t*math.sin(5*t), t*math.cos(5*t), t
            print(point)
            rs.AddPoint(point)
            t+=0.025
    
    
    if __name__=="__main__":
        pointspiral()
    

![https://developer.rhino3d.com/images/primer-
pointspiral.svg](https://developer.rhino3d.com/images/primer-pointspiral.svg)

The variable arrPoint is declared as an empty list, the elements are assigned
different values on lines 7 to 9 inside the body of the loop. On line 10 the
list is printed and on line 11 it is used as the point coordinates to create a
3D point in space.

Vectors are a slightly new concept. Those of you who are familiar with the
essentials of geometrical mathematics will have no problems with this concept…
in fact you probably all are familiar with the essentials of geometrical
mathematics or you wouldn’t be learning how to program a 3D CAD platform.

Vectors are indistinguishable from points. That is, they are both lists of
three numbers so there’s absolutely no way of telling whether a certain list
represents a point or a vector. There is a practical difference though; points
are absolute, vectors are relative. When we treat a list of three doubles as a
point it represents a certain coordinate in space, when we treat it as a
vector it represents a certain direction. You see, a vector is an arrow in
space which always starts at the world origin (0.0, 0.0, 0.0) and ends at the
specified coordinate.

![https://developer.rhino3d.com/images/primer-
vectordefinition.svg](https://developer.rhino3d.com/images/primer-
vectordefinition.svg)

The picture on the right shows two vector definitions; a purple and a blue
one. The blue one happens to have all positive components while the purple one
has only negative components. Both vectors have a different direction and a
different length. When I say vectors are relative, I mean that they only
indicate the difference between the start and end points of the arrow, i.e.
vectors are not actual geometrical entities, they are only information! The
blue vector could represent the tangent direction of the black curve at
parameter {t}. If we also know the point value of the curve at parameter {t},
we know what the tangent of the curve looks like; we know where in space the
tangent belongs. The vector itself does not contain this information; the
orange and the blue vector are identical in every respect.

The addition of vector definitions in IronPython is accompanied by a whole
group of point/vector related methods which perform the basic operations of
‘vector mathematics’. Addition, subtraction, multiplication, dot and cross
products, so on and so forth. The table on the following page is meant as a
reference table, do not waste your time memorizing it.

I will be using standard mathematical notation:

  * A lowercase letter represents a number
  * A lowercase letter with a dot above it represents a point
  * A lowercase letter with an arrow above it represents a vector
  * Vertical bars are used to denote vector length

Notation | Implementation | Description | Example  
---|---|---|---  
$$d =|\dot{p}-\dot{r}|$$ | Distance(Pt1, Pt2) | Compute the distance between two points. | ![](https://developer.rhino3d.com/images/primer-distance.svg)  
$$\dot{r} = a \times \dot{p}$$ | PointScale(Pt1, dblA) | Multiply the components of the point by the specified factor. This operation is the equivalent of a 3DScaling around the world origin. | ![](https://developer.rhino3d.com/images/primer-pointscale.svg)  
$$\dot{r} = \frac{\dot{p}}{a}$$ | PointDivide(Pt1, dblA) | Divide the components of the point by the specified factor. This is the equivalent of _PointScale(Pt1, a-1)_. | ![](https://developer.rhino3d.com/images/primer-pointdivide.svg)  
$$? \dot{r} = \dot{p} \pm t$$ | PointCompare(Pt1, Pt2, dblT) | Check to see if two points are more or less identical. Two points are identical if the length of the vector between them is less than the specified tolerance. | ![](https://developer.rhino3d.com/images/primer-pointcompare.svg)  
$$\dot{r} = \dot{p} \times \mathbb{M}$$ | PointTransform(Pt1, arrM) | Transform the point using a linear transformation matrix.  | ![](https://developer.rhino3d.com/images/primer-pointtransform.svg)  
$$\overrightarrow{w} = \left(\frac{1}{|\overrightarrow{v}|} \right) \times \overrightarrow{v}$$ | VectorUnitize(Vec1) | Divide all components by the inverse of the length of the vector. The resulting vector has a length of 1.0 and is called the unit-vector. Unitizing is sometimes referred to as "normalizing". | ![](https://developer.rhino3d.com/images/primer-vectorunitize.svg)  
$$l = |\overrightarrow{v}|$$ | VectorLength(Vec1) | Compute the square root of the sum of the squares of all the components. Standard Pythagorean distance equation. | ![](https://developer.rhino3d.com/images/primer-vectorlength.svg)  
$$\overrightarrow{w} = -\overrightarrow{v}$$ | VectorReverse(Vec1) | Negate all the components of a vector to invert the direction. The length of the vector is maintained. | ![](https://developer.rhino3d.com/images/primer-vectorreverse.svg)  
$$? \overrightarrow{w} = \overrightarrow{v} \pm t$$ | VectorCompare(Vec1, Vec2, dblT) | Check to see if two vectors are more or less identical. This is the equivalent of _PointCompare()_. | ![](https://developer.rhino3d.com/images/primer-vectorcompare.svg)  
$$\overrightarrow{w} =\frac{\overrightarrow{v}}{a}$$ | VectorDivide(Vec1, dblA) | Divide the components of the vector by the specified factor. This is the equivalent of *PointDivide()*. | ![](https://developer.rhino3d.com/images/primer-vectordivide.svg)  
$$\dot{r} = \dot{p} + \overrightarrow{v}$$ | PointAdd(Pt1, Vec1) | Add the components of the vector to the components of the point. Point-Vector summation is the equivalent of moving the point along the vector. | ![](https://developer.rhino3d.com/images/primer-pointadd.svg)  
$$\dot{r} = \dot{p} - \overrightarrow{v}$$ | PointSubtract(Pt1, Vec1) | Subtract the components of the vector from the components of the point. Point-Vector subtraction is the equivalent of moving the point along the reversed vector. | ![](https://developer.rhino3d.com/images/primer-pointsubtract.svg)  
$$\overrightarrow{v} = \dot{p} - \dot{r}$$ | PointSubtract(Pt1, Vec1) | Subtract the components of the vector from the components of the point. Point-Vector subtraction is the equivalent of moving the point along the reversed vector. | ![](https://developer.rhino3d.com/images/primer-vectorcreate.svg)  
$$\overrightarrow{u} = \overrightarrow{v} + \overrightarrow{w}$$ | VectorAdd(Vec1, Vec2) | Add the components of Vec1 to the components of Vec2. This is equivalent to standard vector summation. | ![](https://developer.rhino3d.com/images/primer-vectoradd.svg)  
$$\overrightarrow{u} = \overrightarrow{v} - \overrightarrow{w}$$ | VectorSubtract(Vec1, Vec2) | Subtract the components of Vec1 from the components of Vec2. This is equivalent of *VectorAdd(Vec1, -Vec2)*. | ![](https://developer.rhino3d.com/images/primer-vectorsubtract.svg)  
$$\alpha = \overrightarrow{v} \times \overrightarrow{w}$$ | VectorDotProduct(Vec1, Vec2)  
-or-  
VectorMultiply(Vec1, Vec2) | Calculate the sum of the products of the corresponding components. In practical, everyday-life the DotProduct can be used to compute the angle between vectors since the DotProduct of two vectors v and w equals: |v||w| cos(a) | ![](https://developer.rhino3d.com/images/primer-vectordotproduct.svg)  
$$\overrightarrow{u} = \overrightarrow{v} \times \overrightarrow{w}$$ | VectorCrossProduct(Vec1, Vec2) | The cross-product of two vectors v and w, is a third vector which is perpendicular to both v and w. | ![](https://developer.rhino3d.com/images/primer-vectorcrossproduct.svg)  
$$\overrightarrow{u} = \overrightarrow{v} \times (\sphericalangle\alpha)\overrightarrow{w}$$ | VectorRotate(Vec1, dblA, VecA) | Rotate a vector a specified number of degrees around an axis-vector. | ![](https://developer.rhino3d.com/images/primer-vectorrotate.svg)  
![https://developer.rhino3d.com/images/primer-
addvector.svg](https://developer.rhino3d.com/images/primer-addvector.svg)

IronPython has no method for displaying vectors, which is a pity since this
would be very useful for visual feedback. I shall define a function here
called _AddVector()_ which we will use in examples to come. The function must
be able to take two arguments; one vector definition and a point definition.
If the point array is not defined the vector will be drawn starting at the
world origin.

    
    
    def AddVector(vecdir, base_point=[0,0,0]):
           tip_point = rs.PointAdd(base_point, vecdir)
           line = rs.AddLine(base_point, tip_point)
           if line: return rs.CurveArrows(line, 2)
    

Line | Description  
---|---  
1 | Standard function declaration. The function takes two arguments, if the first one does not represent a proper vector array the function will not do anything, if the second one does not represent a proper point array the function will draw the vector from the world origin.  
2 | Declare and compute the coordinate of the arrow tip. This will potentially fail if ptBase or vecDir are not proper arrays. However, the script will continue instead of crash due to the exception handling.  
3 | Here we are calling the RhinoScriptSyntax method rs.AddLine() and we're storing the return value directly into the line variable. There are three possible scenarios at this point: 

  1. The method completed successfully
  2. The method failed, but it didn't crash
  3. The method crashed

In the case of scenario 1, the line variable now contains the object ID for a
newly added line object. This is exactly what we want the function to return
on success. In case of scenario #2, the line variable will be set to None. The
last option means that there was no return value for AddLine() and hence line
will also be None.  
4 | Check for scenario 2 and 3, and if they did not occur, go ahead and and add an arrow head using the CurveArrows method. If they did, this method will not be exectuted, and the script simply does not returns *None*.  
  
## 6.5 An AddVector() example

Download and open
[__6_5_AddVectorExample.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/6_5_AddVectorExample.py).
![https://developer.rhino3d.com/images/primeraddvectorexample.svg](https://developer.rhino3d.com/images/primeraddvectorexample.svg)

    
    
    # This script will compute a bunch of cross-product vector based on a pointcloud
    import rhinoscriptsyntax as rs
    
    
    def vectorfield():
        cloud_id = rs.GetObject("Input pointcloud", 2, True, True)
        if cloud_id is None: return
    
        points = rs.PointCloudPoints(cloud_id)
        base_point = rs.GetPoint("Vector field base point")
        if base_point is None: return
    
        for point in points:
            vecbase = rs.VectorCreate(point, base_point)
            vecdir = rs.VectorCrossProduct(vecbase, (0,0,1))
            if vecdir:
                vecdir = rs.VectorUnitize(vecdir)
                vecdir = rs.VectorScale(vecdir, 2.0)
                AddVector(vecdir, point)
    
    
    def AddVector(vecdir, base_point):
        tip_point = rs.PointAdd(base_point, vecdir)
        line = rs.AddLine(base_point, tip_point)
        if line: rs.CurveArrows(line, 2)
    
    
    if __name__=="__main__":
        vectorfield()
    

Line | Description  
---|---  
9 | The _listpoints_ variable is a list which contains all the coordinates of a pointcloud object. This is an example of a nested list (see paragraph 6.6).  
13 | The variable _point_ , which is taken from the _listpoints_ variable, contains an array of three doubles; a standard Rhino point definition. We use that point to construct a new vector definition which points from the Base point to _arrPoints(i)_.  
14 | The *rs.VectorCrossProduct()* method will return a vector which is perpendicular to vecBase and the world z-axis. If you feel like doing some homework, you can try to replace the hard-coded direction ([0,0,1]) with a second variable point a la *base_point*.  
15 | _rs.VectorCrossProduct()_ will fail if one of the input vectors is zero-length or if both input vectors are parallel. In those cases we will not add a vector to the document.  
17 & 18 | Here we make sure the _vecdir_ vector is two units long. First we unitize the vector, making it one unit long, then we double the length.  
19 | Finally, place a call to the _AddVector()_ function we defined on page 40. If you intend to run this script, you must also include the _AddVector()_ function in the same script.  
  
## 6.6 Nested Lists

> I wonder why, I wonder why.  
>  I wonder why I wonder.  
>  I wonder why I wonder why.  
>  I wonder why I wonder.

> -Richard P. Feynman-

![https://developer.rhino3d.com/images/primer-
nestedarrays.svg](https://developer.rhino3d.com/images/primer-
nestedarrays.svg)

There’s nothing to it. A list (or tuple or dictionary for that matter) becomes
nested when it is stored inside another list The VectorField example on the
previous page deals with a list of points (a list of lists, each with three
doubles). The image on the right is a visualization of such a structure. The
left most column represents the base list, the one containing all coordinates.
It can be any size you like, there’s no limit to the amount of points you can
store in a single list. Every element of this base list is a standard Rhino
point. In the case of point-lists all the nested lists are three elements
long, but this is not a requisite, you can store anything you want in a list.

Nesting can be done with tuples, lists or dictionaries. It simply means that
you can put lists in lists, or tuples in tuples, dictionaries in dictionaries
or even lists inside of dictionaries and so on. Nesting can be done
infinitely, you can have a list that contains a list with a list inside of it,
another list inside of that list and so on. Nesting can easily be done by
utilizing a Loop that allows you to iterate and either extract or place other
items inside of the lists.

Accessing nested lists follows the same rules as accessing regular lists.
Using the VectorField example:

    
    
        arrSeventhPoint = arrPoints[6] #arrSeventhPoint now equals the 7th (starting from 0th) element
        arrLastPoint = arrPoints[len(arrPoints)] #arrLastPoint now equals the last point in the list
    

Len() can be used to get the length of a list. In this case we are saying that
arrLastPoint equals the last element in the list called arrPoints because we
have given it the numeric value that is the length of the list. This shows how
to extract entire nested lists. Assuming the illustration on this page
represents _arrPoints_ , _arrSeventhPoint_ will be identical to _[0.3, -1.5,
4.9]_. If we want to access individual coordinates directly we can use another
bracket to explode out the z value:

    
    
    dblSeventhPointHeight = arrPoints[6][2]
    #2 corresponds to the 3rd element (the Z coordinate) within that nested list.
    

The above code will store the third element of the nested list stored in the
seventh element of the base list in _dblSeventhPointHeight_. This corresponds
with the orange block.

Nested lists can be parsed using nested loops like so:

    
    
    for i in range(0,len(arrPoints)):
        for j in range(0,2):
            print("Coordinate(" + i + ", " + j + ") = " + arrPoints[i][j])
    

![https://developer.rhino3d.com/images/primer-
nestedarrayparsehistory.png](https://developer.rhino3d.com/images/primer-
nestedarrayparsehistory.png)

Remember the scaling script from before? We’re now going to take curve-length
adjustment to the next level using nested lists. The logic of this script will
be the same, but the algorithm for shortening a curve will be replaced with
the following one (the illustration shows the first eight iterations of the
algorithm):

![https://developer.rhino3d.com/images/primer-
curvesmoothing.svg](https://developer.rhino3d.com/images/primer-
curvesmoothing.svg)

Every control-point or ‘vertex’ of the original curve (except the ones at the
end) will be averaged with its neighbors in order to smooth the curve. With
every iteration the curve will become shorter and we will abort as soon a
certain threshold length has been reached. The curve can never become shorter
than the distance between the first and last control-point, so we need to make
sure our goals are actually feasible before we start a potentially endless
loop. Note that the algorithm is approximating, it may not be endless but it
could still take a long time to complete. We will not support closed or
periodic curves.

We’re going to put the vector math bit in a separate function. This function
will compute the {vM} vector given the control points {pN-1; p; pN+1} and a
smoothing factor {s}. Since this function is not designed to fail, we will not
be adding any error checking, if the thing crashes we’ll have to fix the bug.
Instead of using variable naming conventions, I’ll use the same codes as in
the diagram:

Download and open
[__6_6_IterativeSmoothCurve.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/6_6_IterativeSmoothCurve.py).

    
    
    def smoothingvector(point, prev_point, next_point, s):
        pm = (prev_point+next_point)/2.0
        va = rs.VectorCreate(pm, point)
        vm = rs.VectorScale(va, s)
        return vm
    

Line | Description  
---|---  
2 | The smoothingvector function definition takes input of Rhino.Point3d. This object type allows for explicit point addition. The act of adding two Point3d objects together results in vector addition of the two points. The act of dividing the resulting point by 2.0 simply divides the three components (x,y and z) by 2.  
3 | The VectorCreate() function is called in order to obtain a Rhino.Vector3d with information about the directional components of a vector between points Pm, and point, P being the origin. The math is effectively the same as Pm - Point = Va, but this operation would not have yielded a Rhion.Vector3d object. The VectorCreate() function creates this object efficiently.  
4 | Finally, we call the _Rhino.VectorScale()_ function, which takes a Rhino.Vector3d object, and scales it according to a predetermined scaling factor 's'. When we use this algorithm, we must make sure to set 's' to be something sensible, or the loop might become endless: 0.0 1 {s} # 1.0  
5 | We return the vector vm.  
  
We’ll also put the entire curve-smoothing algorithm in a separate function.
Since it’s fairly hard to adjust existing objects in Rhino, we’ll be adding a
new curve and deleting the existing one:

    
    
    def smoothcurve(curve_id, s):
        curve_points = rs.CurvePoints(curve_id)
        new_curve_points = []
    
        new_curve_points.append(curve_points[0])
        for i in range(1, len(curve_points)-1):
            vm = smoothingvector(curve_points[i], curve_points[i-1], curve_points[i+1], s)
            new_curve_points.append( rs.PointAdd(curve_points[i], vm) )
        new_curve_points.append(curve_points[-1])
    
        knots = rs.CurveKnots(curve_id)
        degree = rs.CurveDegree(curve_id)
        weights = rs.CurveWeights(curve_id,0)
        newcurve_id = rs.AddNurbsCurve(new_curve_points, knots, degree, weights)
        if newcurve_id: rs.DeleteObject(curve_id)
        return newcurve_id
    

Line | Description  
---|---  
2 | Retrieve the nested list of curve control points, and store it in curve_points.  
3 | We need a second list to contain the new points, while leaving the initial curve_points list intact.  
5 | This loop will start at one and stop one short of the length of the curve_points list. In other words, we're skipping the first and last items in the array.  
7 | Compute the smoothing vector using the current control point, the previous one (_i-1_) and the next one (_i+1_). Since we're omitting the first and last point in the array, every point we're dealing with has two neighbors.  
8 | Set the new control point position. The new coordinate equals the old coordinate plus the smoothing vector.  
9...10 | We'll be adding a new curve to the document which is identical to the existing one, but with different control point positions. A nurbs curve is defined by four different blocks of data: control points, knots, weights and degree (see paragraph 7.7 Nurbs Curves). We just need to copy the other bits from the old curve.  
14 | Create a new nurbs curve and store the object ID in the variable newcurve_id.  
15 | Delete the original curve.  
  
The top-level subroutine doesn’t contain anything you’re not already familiar
with:

    
    
    def iterativeshortencurve():
        curve_id = rs.GetObject("Open curve to smooth", 4, True)
        if curve_id is None or rs.IsCurveClosed(curve_id): return
        
        min = rs.Distance(rs.CurveStartPoint(curve_id), rs.CurveEndPoint(curve_id))
        max = rs.CurveLength(curve_id)
        goal = rs.GetReal("Goal length", 0.5*(min+max) , min, max)
        if goal is None: return
    
        while rs.CurveLength(curve_id)>goal:
            rs.EnableRedraw(False)
            curve_id = smoothcurve(curve_id, 0.1)
            rs.EnableRedraw(True)
            if curve_id is None: break
    

## Next Steps

Tuples, Lists and Dictionaries are very powerful in Python. Let’s make a quick
stop to learn about [class
syntax](https://developer.rhino3d.com/guides/rhinopython/primer-101/7-classes/#class-
syntax).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

