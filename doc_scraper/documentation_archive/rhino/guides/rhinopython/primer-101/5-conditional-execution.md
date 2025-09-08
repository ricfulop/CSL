---
url: https://developer.rhino3d.com/guides/rhinopython/primer-101/5-conditional-execution/
scraped_at: 2025-09-08T15:37:43.024207
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

[5 Conditional
Statements](https://developer.rhino3d.com/guides/rhinopython/primer-101/5-conditional-
execution/)

  * 5.1 What if?
  * 5.2 Looping
  * 5.3 Conditional Loops
  * 5.4 Incremental Loops
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) / [Rhino.Python
101](https://developer.rhino3d.com/en/guides/rhinopython/primer-101/) /

5 Conditional Statements

by [Skylar Tibbits](https://discourse.mcneel.com/u//), [Arthur van der
Harten](https://discourse.mcneel.com/u/aharten/), and [Steve
Baer](https://discourse.mcneel.com/u/stevebaer/) (Last updated: Saturday,
April 24, 2021)

## 5.1 What if?

What if I were to fling this rock at that bear? What if I were to alleviate
that moose from its skin and wear it myself instead? It’s questions like these
that signify abstract thought, perhaps the most stunning of all human traits.
As a programmer, you need to take abstract thought to the next level; the
very-very-conscious level.

A major part of programming is recovering from screw-ups. A piece of code does
not always behave in a straightforward manner and we need to catch these
aberrations before they propagate too far. Other times we design our code to
deal with more than one situation. In any case, there’s always a lot of
conditional evaluation going on, a lot of ‘what if’ questions. Let’s take a
look at three conditionals of varying complexity:

  1. If the object is a curve, delete it.
  2. If the object is a short curve, delete it.
  3. If the object is a short curve, delete it, otherwise move it to the “curves” layer.

The first conditional statement evaluates a single boolean value; an object is
either is a curve or it is not. There’s no middle ground. The second
conditional must also evaluate the constraint ‘short’. Curves don’t become
short all of a sudden any more than people grow tall all of a sudden. We need
to come up with a boolean way of talking about ‘short’ before we can evaluate
it. The third conditional is identical to the second one, except it defines
more behavioral patterns depending on the outcome of the evaluation.

The translation from English into Python is not very difficult. We just need
to learn how conditional syntax works.

Problem 1:

Download and open
[__5_1_DeleteCurveOnTuesdays.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/5_1_DeleteCurveOnTuesdays.py).

    
    
    if (rs.IsCurve(strObjectID)):
        rs.DeleteObject(strObjectID)
    

Problem 2:

    
    
    if (rs.IsCurve(strObjectID)):
        if (rs.CurveLength(strObjectID) < 0.01):
            rs.DeleteObject(strObjectID)
    

Problem 3:

    
    
    if (rs.IsCurve(strObjectID)):
        if (rs.CurveLength(strObjectID) < 0.01):
            rs.DeleteObject(strObjectID)
        else:
            rs.ObjectLayer(strObjectID, "Curves")
    

The most common conditional evaluation is the If…Then statement. If…Then
allows you to bifurcate the flow of a program. The simplest If…Then structure
can be used to shield certain lines of code. It always follows the same
format:

    
    
    if (SomethingOrOther):
        DoSomething()
        DoSomethingElseAsWell()
    

The bit of code that is indented after the _if():_ is evaluated and when it
turns out to be True, the block of code between the first and last line will
be executed. If _SomethingOrOther_ turns out to be False, lines 2 and 3 are
skipped and the script goes on with whatever comes after line 3.

In case of very simple If…Then structures, such as the first example, it is
possible to use a shorthand notation which only takes up a single line instead
of three. The shorthand for If…Then looks like:

    
    
    if (SomethingOrOther): DoSomething()
    

Whenever you need an If…Then…Else structure, you can use the following syntax:

    
    
        if (SomethingOrOther):
        DoSomething()
    else:
        DoSomethingElse()
    

If _SomethingOrOther_ turns out to be True, then the bit of code between lines
1 and 3 are executed. This block can be as long as you like of course.
However, if _SomethingOrOther_ is False, then the code after else is executed.
So in the case of If…Else, one -and only one- of the two blocks of code is put
to work.

You can nest If…Then structures as deep as you like, though code readability
will suffer from too much indenting. The following example uses four nested
If…Then structures to delete short, closed curves.

    
    
        if (rs.IsCurve(strObjectID)):
        if (rs.CurveLength(strObjectID) < 1.0):
            if (rs.IsCurveClosed(strObjectID)):
                rs.DeleteObject(strObjectID)
    

When you feel you need to split up the code stream into more than two flows
and you don’t want to use nested structures, you can instead switch to
something which goes by the name of the If…Elif…Else statement.

As you may or may not know, the Make2D command in Rhino has a habit of
creating some very tiny curve segments. We could write a script which deletes
these segments automatically, but where would we draw the line between ‘short’
and ’long’? We could be reasonably sure that anything which is shorter than
the document absolute tolerance value can be removed safely, but what about
curves which are slightly longer? Rule #1 in programming: When in doubt, make
the user decide. That way you can blame them when things go wrong.

A good way of solving this would be to iterate through a predefined set of
curves, delete those which are definitely short, and select those which are
ambiguous. The user can then decide for himself whether those segments deserve
to be deleted or retained. We won’t discuss the iteration part here. The
conditional bit of the algorithm looks like this:

    
    
    dblCurveLength = rs.CurveLength(strObjectID)
    
    if (dblCurveLength != None):
        if (dblCurveLength < rs.UnitAbsoluteTolerance()):
            rs.DeleteObject(strObjectID)
        elif (dblCurveLength < (10 * rs.UnitAbsoluteTolerance())):
            rs.SelectObject(strObjectID)
        else:
            rs.UnselectObject(strObjectID)
    

In Python you can say the same thing in many different ways. The above snippet
could have been written as a nested If…Then structure, but then it would not
resemble the way we think about the problem.

## 5.2 Looping

Executing certain lines of code more than once is called looping in
programming slang. There are two types of loops; conditional and incremental
which can be described respectively as:

    
    
    Keep adding milk until the dough is kneadable
    Add five spoons of cinnamon
    

Conditional loops will keep repeating until some condition is met where as
incremental loops will run a predefined number of times. Life isn’t as simple
as that though, and there are many different syntax specifications for loops
in Python, we’ll only discuss the two most important ones in depth.

## 5.3 Conditional Loops

Sometimes we do not know how many iterations we will need in advance, so we
need a loop which is potentially capable of running an infinite number of
times. This type is called a Do…Loop. In the most basic form it looks like
this:

    
    
    while (something is true):
        DoSomething()
        if (condition is met):
            break
    

All the lines indented after the while keyword will be repeated until we abort
the loop ourselves. If we do not abort the loop, I.e. if we omit the break
statement or if our condition just never happens to be met, the loop will
continue forever. This sounds like an easy problem to avoid but it is in fact
a very common bug.

In Python it does not signify the end of the world to have a truly infinite
loop. The following example script contains an endless While…Loop which can
only be cancelled by shutting down the application.

Download and open
[__5_3_ViewportClock.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/5_3_ViewportClock.py).

    
    
    import rhinoscriptsyntax as rs
    import datetime as dt
    
    def viewportclock():
        now = dt.datetime.now()
        textobject_id = rs.AddText(str(now), (0,0,0), 20)
        if textobject_id is None: return
        rs.ZoomExtents(None, True)
        while True:
            rs.Sleep(1000)
            now = dt.datetime.now()
            rs.TextObjectText(textobject_id, str(now))
    
    if __name__=="__main__":
        viewportclock()
    

![https://developer.rhino3d.com/images/primer-
viewportclock.svg](https://developer.rhino3d.com/images/primer-
viewportclock.svg)

Here’s how it works:

Line  |  Description   
---|---  
1 & 2  |  Import calls referencing external code - in this case, Rhinoscriptsyntax and datetime. We assign each of them an alias using the 'as' keyword in order simplify function calls later.   
4 | Main Function declaration  
5 | We create a time object which contains a record the date and time of the function call datetime.now().  
6 |  We create a new Rhino Text object to display the date and time from step 5. ` rs.AddText (Text, point_or_plane , Height=1.0 , Font="Arial" ,font_style=0 ) ` Five arguments, the last three of which have default assignments, and so are optional. When adding a text object to Rhino we must specify the text string and the location for the object. There are no defaults for this. The height of the text, font name and style do have default values. However, since we’re not happy with the default height, we will override it to be much bigger: ` textobject_id = rs.AddText(str(now), (0,0,0), 20) ` The Text argument must contain a String description of the current system time. We will simply nest casting function to get it. Since a cast operation for a datetime object is a well known and solid operation, we do not have to check for a Null variable and we can put it ‘inline’. This will give us the date and the time. we could have pared this down to just the time by calling the _dt.datetime.time(now)_ function. Neither of these return a String type variable, so before we pass it into Rhino we have to cast it to a proper String using the _str()_ function. This is analogous with our code on page 20. The _point_or_plane_ argument requires a list of doubles. We haven’t done lists yet, but it essentially means we have to supply the x, y and z coordinates of the text insertion point. _(0,0,0)_ means the same as the world origin. The default height of text objects is 1.0 units, but we want our clock to look big since big things look expensive. Therefore we’re overriding it to be 20 units instead.  
7 | I don't think there's anything here that could possibly go wrong, but it never hurts to be sure. Just in case the text object hasn't been created we need to abort the subroutine in order to prevent an error later on.  
9 | We start an infinite While... loop, lines 10, 11 and 12 will be repeated for all eternity.  
10 | There's no need to update our clock if the text remains the same, so we really only need to change the text once every second. The *Rhino.Sleep()* method will pause Rhino for the specified amount of milliseconds. We're forcing the loop to take it easy, by telling it to take some time off on every iteration. We could remove this line and the script will simply update the clock many times per second. This kind of reckless behaviour will quickly flood the undo buffer.  
11 | Here we update our now object. This will give us an updated datetime object.  
12 | This is the cool bit. Here we replace the text in the object with a new String representing the current system time.  
14 & 15 | This is where the viewport clock function is called. In IronPython, the main function call must be executed after the definition of the function. The if __name__ == "__main__": ... trick exists in Python so that our Python files can act as either reusable modules, or as standalone programs.   
![https://developer.rhino3d.com/images/primer-
iterativecurvescaler.svg](https://developer.rhino3d.com/images/primer-
iterativecurvescaler.svg)

A simple example of a non-endless loop which will terminate itself would be an
iterative scaling script. Imagine we need a tool which makes sure a curve does
not exceed a certain length {L}. Whenever a curve does exceed this predefined
value it must be scaled down by a factor {F} until it no longer exceeds {L}.

This approach means that curves that turn out to be longer than {L} will
probably end up being shorter than {L}, since we always scale with a fixed
amount. There is no mechanism to prevent undershooting. Curves that start out
by being shorter than {L} should remain untouched.

A possible solution to this problem might look like this:

Download and open
[__5_3_IterateCurveScaling.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/5_3_IterateCurveScaling.py).

    
    
    # Iteratively scale down a curve until it becomes shorter than a certain length
    import rhinoscriptsyntax as rs
    
    
    def fitcurvetolength():
        curve_id = rs.GetObject("Select a curve to fit to length", 4, True, True)
        if curve_id is None: return
        
        length = rs.CurveLength(curve_id)
    
        length_limit = rs.GetReal("Length limit", 0.5 * length, 0.01 * length, length)
        if length_limit is None: return
    
        while True:
            if rs.CurveLength(curve_id)<=length_limit: break
            curve_id = rs.ScaleObject(curve_id, (0,0,0), (0.95, 0.95, 0.95))
            if curve_id is None:
                print("Something went wrong...")
                return
    
        print("New curve length: ", rs.CurveLength(curve_id))
    
    
    if __name__=="__main__":
        fitcurvetolength()
    

Line  |  Description   
---|---  
1...4  |  This should be familiar by now   
5 | Prompt the user to pick a single curve object, we're allowing preselection.  
6 | Check that the user picked an object, and that its id was written to our curve_id variable. Exit if not.  
8 | Retrieve the current curve length. This function should not fail, no need to check for Null.  
10 | Prompt the user for a length limit value. The value must be chosen between the current curve length and 1% of the current curve length. We're setting the default to half the current curve length.  
13 | Start a While... loop  
14 | This is the break-away conditional. If the curve length no longer exceeds the preset limit, the break statement will take us directly to line 20.  
15 | If the length of the curve did exceed the preset limit, this line will be executed. The _rs.ScaleObject()_ method takes four arguments, the last one of which is optional. We do not override it. We do need to specify which object we want rescaled _(curve_id)_ , what the center of the scaling operation will be (_(0,0,0)_ ; the world origin) and the scaling factors along x, y and z (95% in all directions).  
19 | This line ends all indented code, which instructs the interpreter to go back to line 13  
21 | Eventually all curves will become shorter than the limit length and the While... loop will abort. We print out a message to the command line informing the user of the new curve length.  
  
## 5.4 Incremental Loops

When the number of iterations is known in advance, we could still use a
While…Loop statement, but we’ll have to do the bookkeeping ourselves. This is
rather cumbersome since it involves us declaring, incrementing and evaluating
variables. The For…statement is a loop which takes care of all this hassle.
The underlying idea behind For… loops is to have a value incremented by a
fixed amount every iteration until it exceeds a preset threshold:

    
    
    group = 10
    for item in group:
        AddSpoonOfCinnamon()
    

This loop will operate for each item in the group, adding a spoon of cinnamon
and will exit when we come to the last item of the group.

We can also use the range() function for more control:

    
    
    for i in range(A,B,N):
        AddSpoonOfCinnamon()
    

The variable i starts out by being equal to A and it is incremented by N until
it becomes 1 less than B. In other words, B is the total amount that you want
to increment up to. Remember, that in programming, we always start with 0,
therefore the total increment amount will be 1 more than we actually want! N
signifies the “Step” value which is optional and if we do not override it the
default stepsize of 1.0 will be used. If we have a stepsize of 2, it will
increment every-other time. In the example above the variable i is not used in
the loop itself, we’re using it for counting purposes only.

If we want to abort a For… loop ahead of time, we can use break in order to
short-circuit the process. Creating mathematical graphs is a typical example
of the usage of For…Loops:

Download and open
[__5_4_DrawSineWave.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/5_4_DrawSineWave.py).

    
    
    # Draw a sine wave using points
    import rhinoscriptsyntax as rs
    import math
    
    def drawsinewave():
        a = -8.0
        b = 8.0
        step = 0.25
        x = a
        while x<=b:
            y = 2*math.sin(x)
            rs.AddPoint( (x,y,0) )
            x += step
    
    
    if __name__=="__main__":
        drawsinewave()   
    

![https://developer.rhino3d.com/images/primer-
sinewave.svg](https://developer.rhino3d.com/images/primer-sinewave.svg)

The above example draws a sine wave graph in a certain numeric domain with a
certain accuracy. There is no user input since that is not the focus of this
paragraph, but you can change the values in the script. The numeric domain
we’re interested in ranges from -8.0 to +8.0 and with the current stepsize of
0.25 that means we’ll be running this loop 64 times. 64 = Step-1 × (B - A))

The For…loop will increment the value of x automatically with the specified
stepsize, so we don’t have to worry about it when we use x on line 10. We
should be careful not to change x inside the loop since that will play havoc
with the logic of the iterations.

Loop structures can be nested at will, there are no limitations, but you’ll
rarely encounter more than three. The following example shows how nested
For…Loops can be used to compute distributions:

Download and open
[__5_4_TwistAndShout.py](https://developer.rhino3d.com/samples/rhinopython/rhinopython101/5_4_TwistAndShout.py).

    
    
    import rhinoscriptsyntax as rs
    import math
    
    
    def twistandshout():
        twist_angle = 0.0
        rs.EnableRedraw(False)
        z = 0
        while z<=5:
            twist_angle += math.pi/30
            a = 0
            while a<2*math.pi:
                x = 5 * math.sin(a + twist_angle)
                y = 5 * math.cos(a + twist_angle)
                rs.AddSphere((x,y,z), 0.5)
                a += math.pi/15
            z += 0.5
        rs.EnableRedraw(True)
    
    
    if __name__=="__main__":
        twistandshout()
    

![https://developer.rhino3d.com/images/primer-
twistandshout.svg](https://developer.rhino3d.com/images/primer-
twistandshout.svg)

The master loop increments the z variable from 0.0 to 5.0 with a default step
size of 0.5. The z variable is used directly as the z-coordinate for all the
sphere centers. For every iteration of the master loop, we also want to
increment the twist angle with a fixed amount. We can only use the For…Loop to
automatically increment a single variable, so we have to do this one ourselves
on line 8.

The master loop will run a total of ten times and the nested loop is designed
to run 30 times. But because the nested loop is started every time the master
loop performs another iteration, the code between lines 11 and 14 will be
executed 10×30 = 300 times. Whenever you start nesting loops, the total number
of operations your script performs will grow exponentially.

The _rs.EnableRedraw()_ calls before and after the master loop are there to
prevent the viewport from updating while the spheres are inserted. The script
completes much faster if it doesn’t have to redraw 330 times. If you comment
out the _rs.EnableRedraw()_ call you can see the order in which spheres are
added, it may help you understand how the nested loops work together.

## Next Steps

Now it should be coming together on how Python works. Just a few more details.
Learn more about Python’s advanced variables in [Tuples, Lists, and
Dictionaries](https://developer.rhino3d.com/guides/rhinopython/primer-101/6-tuples-
lists-dictionaries/).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/primer-101/5-conditional-
execution/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/primer-101/5-conditional-
execution/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

