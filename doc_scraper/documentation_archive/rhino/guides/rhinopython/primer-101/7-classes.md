---
url: https://developer.rhino3d.com/guides/rhinopython/primer-101/7-classes/
scraped_at: 2025-09-08T15:37:45.123513
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

[7
Classes](https://developer.rhino3d.com/guides/rhinopython/primer-101/7-classes/)

  * 7.1 Class Syntax
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) / [Rhino.Python
101](https://developer.rhino3d.com/en/guides/rhinopython/primer-101/) /

7 Classes

by [Skylar Tibbits](https://discourse.mcneel.com/u//), [Arthur van der
Harten](https://discourse.mcneel.com/u/aharten/), and [Steve
Baer](https://discourse.mcneel.com/u/stevebaer/) (Last updated: Wednesday,
December 5, 2018)

## 7.1 Class Syntax

Classes are useful mechanism for organization above what we have already
mentioned: variables, flow control and functions. Classes give us another
level of functionality and actually define a specific type of programming
called Object-Oriented Programming. This means that we can create objects,
rather than simply procedures or variables. Object-Oriented Programming gives
us the ability to create a class with internal attributes, functions and any
number of other characteristics and then create multiple instances. Classes
offer you a possibility to organize your code based on objects, these objects
can relate to one another with inheritance, add or remove
information/characteristics through functions and actually exhibit
“polymorphism”! (Sounds fancy!)

Polymorphism, another exciting feature of Object-Orient Programming, is the
ability to create one object or class that can exhibit multiple
characteristics and commonly respond to similar functions. For example, if we
have a function that asks for a “Person’s” age and returns their birth year,
we could pass in a “Professor” or we could pass in a “Person” although they
are actually different objects they can respond to the same question (this is
like acting as different people at different times, depending on the
question)!

Classes can be used describe geometry - i.e. a surface is an object that has
multiple characteristics, curvature, centroid, number of U & V points etc. We
can also ask for information about a surface based on functions embedded
within the class; like returning the surface area or the bounding box etc! We
can also create our own types of objects like “Connections” or “Apertures” etc
- with functionality and specific attributes, while each one being slightly
unique! Classes are very powerful, but at first glance are often difficult to
wrap your head around!!

Ok, enough talking - lets see some code (because that’s much easier to
understand…)! To create a class the syntax is:

    
    
    class MyClass:
        """A simple example"""
        x = 10
        def test(self):
            return 'hello'
    
    obj = MyClass()
    print(obj.x)
    print(obj.test())
    

Line  |  Description   
---|---  
1  |  Standard class declaration, this class is called "MyClass"   
2 | Standard class declaration, this class is called "MyClass"  
3 | Declare a variable x = 10.  
4 | Create a function within the class that returns 'hello'  
7 | Create an instance of MyClass() called obj  
8 | This print statement will return >> 10  
9 | This print statement will return >> 'hello'  
  
Now, if we change the value of x and print the result:

    
    
    obj.x = 5
    print(obj.x)
    
    
    
    >> 5
    

The result is 5, showing that we can change the attributes of an object and
call functions outside of the class! Regarding the strange use of “self”, the
Python documentation explains, _" Often, the first argument of a method is
called self. This is nothing more than a convention: the name self has
absolutely no special meaning to Python. Note, however, that by not following
the convention your code may be less readable to other Python programmers, and
it is also conceivable that a class browser program might be written that
relies upon such a convention."_

Often, a class will have a function called **init** \- this forces the class
to give certain attributes whenever it is created (rather than adding them
later). For example:

    
    
    class Harder:
        def __init__(self,m,n):
            self.i = m
            self.j = n
    newObj = Harder(10,20)
    print(newObj.i)
    print(newObj.j)
    

Line  |  Description   
---|---  
1  |  Standard class declaration, this class is called "Harder"   
2 | This line initializes a number of variables that must be described when creating an instance of the class  
3-4 | Sets internal variables i & j to the input variables m & n  
5 | Creates an instance of the class Harder() called newObj  
6 | The print call returns the value of i (which was initially m) = 10  
7 | The print call returns the value of j (which was initially n) = 20  
  
Now for an example of inheritance, or the ability for a class to take on the
qualities of another class, yet have its own differences (Polymorphism!):

    
    
    class Weird(MyClass):
        k = 17
    
    newerObj = Weird()
    print(newerObj.test())
    

Line  |  Description   
---|---  
1  |  Standard class declaration, this class is called "Weird." However, this time we put another class in parenthesis - this means that it inherits all of the properties of the class, MyClass()!   
2 | Standard variable k = 17  
4 | Creates an instance of the class Weird() called newerObj  
5 | The print call returns 'hello'! (Weird...right!?) This means that it referenced the previous class and returned 'hello', because Weird is an child of MyClass()  
  
You can use isinstance(newerObj,MyClass) to check if one object is an instance
of another object.

Classes can be nested, they can have multiple functions, create powerful
systems with polymorphism, privacy and modularity of your code! Like I said,
classes are very powerful and sometimes difficult to wrap your head around at
first (don’t get hung up on them….work your way into it)! We are certainly not
doing them justice here by explaining them in just 2 short pages! However,
their complete depths are certainly out of the scope of this primer and you
can find more information on Python classes from the resources at the
beginning of this primer or at: <http://docs.python.org/tutorial/classes.html>

## Next Steps

Classes are the last of the pure Python units. The last chapter is all about
[geometry](https://developer.rhino3d.com/guides/rhinopython/primer-101/8-geometry/)
in Rhino and Python.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/primer-101/7-classes/index.md)
[
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/primer-101/7-classes/index.md)
[ Admin](https://developer.rhino3d.com/admin)

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

