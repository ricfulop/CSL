---
url: https://developer.rhino3d.com/guides/rhinoscript/primer-101/5-conditional-execution/
scraped_at: 2025-09-08T15:41:51.237995
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
Execution](https://developer.rhino3d.com/guides/rhinoscript/primer-101/5-conditional-
execution/)

  * 5.1 What if?
  * 5.2 Select Case
  * 5.3 Looping
  * 5.4 Conditional Loops
  * 5.5 Alternate Syntax
  * 5.6 Incremental Loops
  * Next Steps

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoScript
Guides](https://developer.rhino3d.com/en/guides/rhinoscript/) / [RhinoScript
101](https://developer.rhino3d.com/en/guides/rhinoscript/primer-101/) /

5 Conditional Execution

__

Windows only

by [David Rutten](https://discourse.mcneel.com/u/davidrutten/) (Last updated:
Wednesday, December 5, 2018)

## 5.1 What if?

What if I were to fling this rock at that bear? What if I were to alleviate
that moose from its skin and wear it myself instead? It’s questions like these
that signify abstract thought, perhaps the most stunning of all human traits.
It’s no good actually throwing rocks at bears by the way, you’re only going to
upset it and severely diminish your chances of getting back to your cave by
nightfall in one piece. As a programmer, you need to take abstract though to
the next level; the very-very-conscious level.

A major part of programming is recovering from screw-ups. A piece of code does
not always behave in a straightforward manner and we need to catch these
aberrations before they propagate too far. At other times we design our code
to deal with more than one situation. In any case, there’s always a lot of
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
more behavioural patterns depending on the outcome of the evaluation.

The translation from English into VBScript is not very difficult. We just need
to learn how conditional syntax works.

Problem 1:

    
    
    If Rhino.IsCurve(strObjectID) Then
    	Call Rhino.DeleteObject(strObjectID)
    End If
    

Problem 2:

    
    
    If Rhino.IsCurve(strObjectID) Then
    	If Rhino.CurveLength(strObjectID) < 0.01 Then
    	    Call Rhino.DeleteObject(strObjectID)
    	End If
    End If
    

Problem 3:

    
    
    If Rhino.IsCurve(strObjectID) Then
    	If Rhino.CurveLength(strObjectID) < 0.01 Then
    	    Call Rhino.DeleteObject(strObjectID)
    	Else
    	    Call Rhino.ObjectLayer(strObjectID, "Curves")
    	End If
    End If
    

The most common conditional evaluation is the _If…Then statement_. _If…Then_
allows you to bifurcate the flow of a program. The simplest _If…Then_
structure can be used to shield of certain lines of code. It always follows
the same format:

    
    
    If SomethingOrOther Then
        DoSomething()
        DoSomethingElseAsWell()
    End If
    

The bit of code between the If and the Then on line 1 is evaluated and when it
turns out to be True, the block of code between the first and last line will
be executed. If SomethingOrOther turns out to be False, lines 2 and 3 are
skipped and the script goes on with whatever comes after line 4. In case of
very simple _If…Then_ structures, such as the first example on the previous
page, it is possible to use a shorthand notation which only takes up a single
line instead of three. The shorthand for _If…Then_ looks like:

    
    
    If SomethingOrOther Then DoSomething()
    

Whenever you want to put more than one action into an If…Then block, you have
to use the regular notation. The _If…Then…Else_ syntax has a similar shorthand
but you will rarely see it used. It’s better to keep the lines of code short
since that will improve readability. Whenever you need an _If…Then…Else_
structure, I suggest you use the following syntax:

    
    
    If SomethingOrOther Then
        DoSomething()
    Else
        DoSomethingElse()
    End If
    

If SomethingOrOther turns out to be True, then the bit of code between lines 1
and 3 are executed. This block can be as long as you like of course. However,
if SomethingOrOther is False, then the code between _Else_ and End If is
executed. So in the case of _If…Then…Else_ , one -and only one- of the two
blocks of code is put to work.

You can nest _If…Then_ structures as deep as you like, though code readability
will suffer from too much indenting. The following example uses four nested
_If…Then_ structures to delete short, closed curves on Tuesdays.

    
    
    If Rhino.IsCurve(strObjectID) Then
        If Rhino.CurveLength(strObjectID) < 1.0 Then
            If Rhino.IsCurveClosed(strObjectID) Then
                If WeekDay(Now()) = vbTuesday Then
                    Call Rhino.DeleteObject(strObjectID)
                End If
            End If
        End If
    End If
    

When you feel you need to split up the code stream into more than two flows
and you don’t want to use nested structures, you can instead switch to
something which goes by the name of the _If…Then…ElseIf…Else_ statement.

As you may or may not know, the * _Make2D* command in Rhino has a habit of
creating some very tiny curve segments. We could write a script which deletes
these segments automatically, but where would we draw the line between ‘short’
and ’long’? We could be reasonably sure that anything which is shorter than
the document absolute tolerance value can be removed safely, but what about
curves which are slightly longer? Rule #1 in programming: When in doubt, make
the user decide. That way you can blame them when things go wrong.

A good way of solving this would be to iterate through a predefined set of
curves, delete those which are definitely short, and select those which are
ambiguous. The user can then decide for himself whether those segments deserve
to be deleted or retained. We won’t discuss the iteration part here, for you
need to know more about arrays than you do now. The conditional bit of the
algorithm looks like this:

    
    
    Dim dblCurveLength
    dblCurveLength = Rhino.CurveLength(strObjectID)
    
    If Not IsNull(dblCurveLength) Then
        If dblCurveLength < Rhino.UnitAbsoluteTolerance() Then
            Call Rhino.DeleteObject(strObjectID)
        ElseIf dblCurveLength < (10 * Rhino.UnitAbsoluteTolerance()) Then
            Call Rhino.SelectObject(strObjectID)
        Else
            Call Rhino.UnselectObject(strObjectID)
        End If
    End If
    

Saying “that red dress makes your bottom look big” and “that yellow dress
really brings out the colour of your eyes” essentially means the same thing.
In VBScript you can also say the same thing in different ways, though in
general the “your bottom looks big” approach is preferable in programming. The
above snippet could have been written as a nested If…Then structure, but then
it would not resemble the way we think about the problem.

## 5.2 Select Case

Even though the If…Then…ElseIf…Else statement allows us to split up the code
stream into any number of substreams, it is not a very elegant piece of
syntax. Even very simple conditional evaluation will look rather complex
because of the repeated comparisons. The Select…Case structure was designed to
simplify conditional evaluation which potentially results in many different
code streams. (For those among you who are/were Java or C programmers,
Select…Case in VBScript is the same as switch…case in Java/C). There are a few
drawbacks compared to If…Then…ElseIf…Else statements. For one, a Select…Case
can only evaluate equality, meaning you can only check to see if some variable
is equal to 2, not if it is smaller than 2. The syntax for Select…Case looks
like this:

    
    
    Select Case iVariable
        Case 0
            DoSomething()
        Case 1
            DoSomethingElse()
        Case 2
            DoSomethingTotallyDifferent()
        Case 30, 45, 60, 90, 180
            SurpriseMe()
        Case Else
            DoWhateverItIsYouWouldNormallyDo()
    End Select
    

On line 1, the _iVariable_ represents a value which we will be evaluating for
equality. In this case the _iVariable_ has to be a number, but it could
equally well be a String. Line 2 lists the first evaluation we’ll perform.
Since the _Select…Case_ statement will take care of the comparisons itself, we
only have to supply the value we want to compare to. If iVariable happens to
the be same as 0, the bit of code directly beneath Case 0 (the function call
to DoSomething()) is executed. If _iVariable_ equals 45, then the
_SurpriseMe()_ function is called.

You can supply any number of cases and you can add more comparisons to a case
by comma separating them (line 8). If none of the cases you have specified is
a match, the _Case Else_ bit will be executed. _Case Else_ is optional, you do
not have to implement it. Now, how about an example?

    
    
    Dim intObjectType                        'An Integer to store the Rhino Object-Type code
    intObjectType = Rhino.ObjectType(strObjectID)
    If IsNull(intObjectType) Then Exit Sub   'this probably means the object does not exist; abort
    
    Dim strLayerName                         'A String to store a layer name
    Select Case intObjectType                'Compare the actual type code with the preset ones
        Case 1, 2                            'Points and PointCloud objects
            strLayerName = "Points"
        Case 4                               'Curves
            strLayerName = "Curves"
        Case 8, 16                           'Surfaces and PolySurfaces
            strLayerName = "(Poly)Surfaces"
        Case 32                              'Meshes
            strLayerName = "Meshes"
        Case 256                             'Lights
            strLayerName = "Lights"
        Case 512, 8192                       'Annotations and TextDots
            strLayerName = "Annotations"
        Case 2048, 4096                      'Instanced and Referenced Block definitions
            strLayerName = "Blocks"
        Case Else                            'Icky objects such as Layers, Materials and Grips; abort
            Exit Sub
    End Select
    
    If Not Rhino.IsLayer(strLayerName) Then  'If the layer we are about to assign does not yet exist…
        Call Rhino.AddLayer(strLayerName)    'Create it.
    End If
    
    Call Rhino.ObjectLayer(strObjectID, strLayerName)     'Assign the object to the layer
    

This snippet of code will check the type of the object which is referenced by
the variable _strObjectID_ and it will assign it to a specific layer. Some
object type codes do not belong to ‘real’ objects (such as grips and edges) so
we need the Case Else bit to make sure we don’t try to assign them to a layer.
I’m going to be very naughty right now and not discuss this in detail. The
comments should be enough to help you on your way.

## 5.3 Looping

Executing certain lines of code more than once is called looping in
programming slang. On page 5 I mentioned that there are two types of loops;
conditional and incremental which can be described respectively as:

    
    
    Keep adding milk until the dough is kneadable
    Add five spoons of cinnamon
    

Conditional loops will keep repeating until some condition is met where as
incremental loops will run a predefined number of times. Life isn’t as simple
as that though, and there are as many as eight different syntax specifications
for loops in VBScript, we’ll only discuss the two most important ones in
depth.

## 5.4 Conditional Loops

Sometimes we do not know how many iterations we will need in advance, so we
need a loop which is potentially capable of running an infinite number of
times. This type is called a Do…Loop. In the most basic form it looks like
this:

    
    
    Do
        DoSomething()
        [If (condition is met) Then Exit Do]
    Loop
    

All the lines between the Do keyword and the Loop keyword will be repeated
until we abort the loop ourselves. If we do not abort the loop, I.e. if we
omit the `Exit Do` statement or if our condition just never happens to be met,
the loop will continue forever. This sounds like an easy problem to avoid but
it is in fact a very common bug.

In VBScript it does not signify the end of the world to have a truly infinite
loop. Scripts are always run under the supervision of the RhinoScript plug-in.
Jamming the Escape key several times in a row is pretty likely to gut any
script which happens to be running. The following example script contains an
endless _Do…Loop_ which can only be cancelled by the user pressing (and
holding) escape.

![https://developer.rhino3d.com/images/primer-
viewportclock.svg](https://developer.rhino3d.com/images/primer-
viewportclock.svg)

    
    
    Option Explicit
    'Display an updating digital clock in all viewports
    
    ViewportClock()
    Sub ViewportClock()
        Dim strTextObjectID
        strTextObjectID = Rhino.AddText(CStr(Time()), Array(0,0,0), 20)
        If IsNull(strTextObjectID) Then Exit Sub
    
        Do
            Call Rhino.Sleep(1000)
            Call Rhino.TextObjectText(strTextObjectID, CStr(Time()))
        Loop
    End Sub
    

Here’s how it works:

Line  |  Description   
---|---  
1 & 2  |  _Option Explicit_ declaration and comments about who's who and what's what   
4 | Main Function call  
5 | Main function declaration  
6 |  We declare a variable which is capable of storing a Rhino object ID.   
7 | We create a new Rhino Text object. The RhinoScript helpfile tells us how to approach this particular method: ` Rhino.AddText (strText, arrPoint [, dblHeight [, strFont [, intStyle]]]) ` Five arguments, the last three of which are optional. When adding a text object to Rhino we must specify the text string and the location for the object. There are no defaults for this. The height of the text, font name and style do have default values. However, since we’re not happy with the default height, we will override it to be much bigger: ` strTextObjectID = Rhino.AddText(CStr(Time()), Array(0,0,0), 20) ` The _strText_ argument must contain a String description of the current system time. We will simply nest two native VBScript functions to get it. Since these functions are not designed to fail we do not have to check for a Null variable and we can put them ‘inline’. _Time()_ returns a variable which contains only the system time, not the date. We could also have used the _Now()_ function (as on page 20) in which case we would have gotten both the date and the time. _Time()_ does not return a String type variable, so before we pass it into Rhino we have to convert it to a proper String using the _CStr()_ function. This is analogous with our code on page 20. The _arrPoint_ argument requires an array of doubles. We haven’t done arrays yet, but it essentially means we have to supply the x, y and z coordinates of the text insertion point. `Array(0,0,0` means the same as the world origin. The default height of text objects is 1.0 units, but we want our clock to look big since big things look expensive. Therefore we’re overriding it to be 20 units instead.  
8 | I don't think there's anything here that could possibly go wrong, but it never hurts to be sure. Just in case the text object hasn't been created we need to abort the subroutine in order to prevent an error later on.  
10 | We start an infinite _Do…Loop_ , lines 11 and 12 will be repeated for all eternity.  
11 | There's no need to update our clock if the text remains the same, so we really only need to change the text once every second. The _Rhino.Sleep()_ method will pause Rhino for the specified amount of milliseconds. We're forcing the loop to take it easy, by telling it to take some time off on every iteration. We could remove this line and the script will simply update the clock many times per second. This kind of reckless behaviour will quickly flood the undo buffer.  
12 | This is the cool bit. Here we replace the text in the object with a new String representing the current system time.  
13 | End of the *Do…Loop*, tells the interpreter to go back to line 10   
14 | End of the Subroutine. This line will never be called because the script is not capable of actually breaking out of the loop itself. Once the user presses the Escape key the whole script will be cancelled. We still need to add it since every single _Sub_ statement needs to have a matching _End Sub_.   
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
by being shorter than {L} should remain unmolested.

A possible solution to this problem might look like this:

    
    
    Option Explicit
    'Iteratively scale down a curve until it becomes shorter than a certain length
    
    FitCurveToLength()
    Sub FitCurveToLength()
        Dim strCurveID
        strCurveID = Rhino.GetObject("Select a curve to fit to length", 4, True, True)
        If IsNull(strCurveID) Then Exit Sub
    
        Dim dblLength
        dblLength = Rhino.CurveLength(strCurveID)
    
        Dim dblLengthLimit
        dblLengthLimit = Rhino.GetReal("Length limit", 0.5 * dblLength, 0.01 * dblLength, dblLength)
        If IsNull(dblLengthLimit) Then Exit Sub
    
        Do
            If Rhino.CurveLength(strCurveID) <= dblLengthLimit Then Exit Do
    
            strCurveID = Rhino.ScaleObject(strCurveID, Array(0,0,0), Array(0.95, 0.95, 0.95))
            If IsNull(strCurveID) Then
                Call Rhino.Print("Something went wrong...")
                Exit Sub
            End If
        Loop
    
        Call Rhino.Print("New curve length: " & Rhino.CurveLength(strCurveID))
    End Sub
    

Line  |  Description   
---|---  
1...6  |  This should be familiar by now   
7 | Prompt the user to pick a single curve object, we're allowing preselection.  
11 | Retrieve the current curve length. This function should not fail, no need to check for Null.  
14 | Prompt the user for a length limit value. The value has be chosen between the current curve length and 1% of the current curve length. We're setting the default to half the current curve length.  
17 | Start a Do…Loop  
18 | This is the break-away conditional. If the curve length no longer exceeds the preset limit, the Exit Do statement will take us directly to line 26.  
20 | If the length of the curve did exceed the preset limit, this line will be executed. The _Rhino.ScaleObject()_ method takes four arguments, the last one of which is optional. We do not override it. We do need to specify which object we want rescaled (_strCurveID_), what the center of the scaling operation will be (_Array(0,0,0);_ the world origin) and the scaling factors along x, y and z (95% in all directions).  
25 | Instructs the interpreter to go back to line 17  
27 | Eventually all curves will become shorter than the limit length and the _Do…Loop_ will abort. We print out a message to the command line informing the user of the new curve length.  
  
## 5.5 Alternate Syntax

Do…Loops are almost always conditional. The infinite loop example of the
viewport clock is a rare exception. If the condition for the continuation of
the loop is fairly complicated we will probably want to do it ourselves. In
simple cases we could use one of the alternative loop syntax rules, which has
the conditional evaluation baked in:

    
    
    Do While SomeCondition
        DoSomething()
    Loop
    

This kind of loop syntax will abort the loop when `SomeCondition` is no longer
True. In light of the curve scaling example, we could have put the curve
length condition in the loop definition itself, like so:

    
    
    Do While Rhino.CurveLength(strCurveID) > dblLengthLimit
        strCurveID = Rhino.ScaleObject(strCurveID, Array(0,0,0), Array(0.95, 0.95, 0.95))
        If IsNull(strCurveID) Then
            Rhino.Print "Something went wrong..."
            Exit Sub
        End If
    Loop
    

We can still add any number of additional evaluations inside the body of the
loop if we want, but the syntax above will behave exactly the same as the
original code on the previous page.

If we want the loop to terminate when a condition becomes True instead of
False, we can use the _Until_ keyword instead of the _While_ keyword. This is
just a syntactic trick, using _Until_ is exactly the same as using _While_
with an additional _Not_ operator:

    
    
    Do Until SomeCondition
        DoSomething()
    Loop
    

The problem you might have with both these options is that the body of the
loop might not be executed at all. If the curve which is indicated by
`strCurveID` is already shorter than `dblLengthLimit` to begin with the entire
loop is skipped. If you want your loop to run at least once and evaluate
itself at the end rather than at the beginning, you can put the _While/Until_
conditional after the _Loop_ keyword instead:

    
    
    Do
        DoSomething()
    Loop While SomeCondition
    

Now, you are guaranteed that _DoSomething()_ will be called at least once.

## 5.6 Incremental Loops

When the number of iterations is known in advance, we could still use a
Do…Loop statement, but we’ll have to do the bookkeeping ourselves. This is
rather cumbersome since it involves us declaring, incrementing and evaluating
variables. The For…Next statement is a loop which takes care of all this
hassle. The underlying idea behind For…Next loops is to have a value
incremented by a fixed amount every iteration until it exceeds a preset
threshold:

    
    
    Dim i
    For i = A To B [Step N]
        AddSpoonOfCinnamon()
    Next
    

The variable i starts out by being equal to _A_ and it is incremented by _N_
until it becomes larger than _B_. Once _i > B_ the loop will terminate. The
Step keyword is optional and if we do not override it the default stepsize of
1.0 will be used. In the example above the variable _i_ is not used in the
loop itself, we’re using it for counting purposes only.

If we want to abort a _For…Next_ loop ahead of time, we can place a call to
_Exit For_ in order to short-circuit the process.

Creating mathematical graphs is a typical example of the usage of _For…Next_ :

![https://developer.rhino3d.com/images/primer-
sinewave.svg](https://developer.rhino3d.com/images/primer-sinewave.svg)

    
    
    Option Explicit
    'Draw a sine wave using points
    
    DrawSineWave()
    Sub DrawSineWave()
        Dim x, y
        Dim dblA, dblB, dblStep
    
        dblA = -8.0
        dblB = 8.0
        dblStep = 0.25
    
        For x = dblA To dblB Step dblStep
            y = 2*Sin(x)
    
            Call Rhino.AddPoint(Array(x, y, 0))
        Next
    End Sub    
    

The above example draws a sine wave graph in a certain numeric domain with a
certain accuracy. There is no user input since that is not the focus of this
paragraph, but you can change the values in the script. The numeric domain
we’re interested in ranges from -8.0 to +8.0 and with the current stepsize of
0.25 that means we’ll be running this loop 65 times. 65 is one more than the
expected number 64 (64 = dblStep-1 × (dblB - dblA)) since the loop will start
at `dblA` and it will stop only after `dblB` has been exceeded.

The _For…Next_ loop will increment the value of x automatically with the
specified stepsize, so we don’t have to worry about it when we use x on line
14. We should be careful not to change x inside the loop since that will play
havoc with the logic of the iterations.

Loop structures can be nested at will, there are no limitations, but you’ll
rarely encounter more than three. The following example shows how nested
_For…Next_ structures can be used to compute distributions:

![https://developer.rhino3d.com/images/primer-
twistandshout.svg](https://developer.rhino3d.com/images/primer-
twistandshout.svg)

    
    
    Sub TwistAndShout()
        Dim z, a
        Dim pi, dblTwistAngle
        pi = Rhino.Pi()
        dblTwistAngle = 0.0
    
        Call Rhino.EnableRedraw(False)
        For z = 0.0 To 5.0 Step 0.5
            dblTwistAngle = dblTwistAngle + (pi/30)
    
            For a = 0.0 To 2*pi Step (pi/15)
                Dim x, y
                x = 5 * Sin(a + dblTwistAngle)
                y = 5 * Cos(a + dblTwistAngle)
                Call Rhino.AddSphere(Array(x,y,z), 0.5)
            Next
        Next
        Call Rhino.EnableRedraw(True)
    End Sub
    

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
Leanr more about Python’s advanced variables in
[Arrays](https://developer.rhino3d.com/guides/rhinoscript/primer-101/6-arrays/).

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinoscript/primer-101/5-conditional-
execution/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinoscript/primer-101/5-conditional-
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

