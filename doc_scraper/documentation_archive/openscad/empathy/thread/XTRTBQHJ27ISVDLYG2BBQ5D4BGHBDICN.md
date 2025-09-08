---
url: https://lists.openscad.org/empathy/thread/XTRTBQHJ27ISVDLYG2BBQ5D4BGHBDICN
scraped_at: 2025-09-08T16:28:22.804340
title: Untitled
---

[ ![](/empathy/images/logo.png) ]( https://lists.openscad.org/empathy)

____

Hi,

Guest

![Pic](/empathy/images/default.jpg)

__

Sign In

Remember Me

Sign In

[ Click here to sign up for new account. ](/register)

[ Forgot your password? ](/password/reset)

###
[discuss@lists.openscad.org](https://lists.openscad.org/empathy/list/discuss.lists.openscad.org)

OpenSCAD general discussion Mailing-list

[View all
threads](https://lists.openscad.org/empathy/list/discuss.lists.openscad.org)

###  New feature in 2025.07.11: the object() function

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Sun, Jul 13, 2025 10:20 PM

    
    
      Quick summary:
    

  * 2025.07.11 adds the the object() function, which creates an object   
(in the style returned by textmetrics(), fontmetrics(), and import()  
of a JSON file).

  * It accumulates the object by processing the arguments left to right,   
with later settings for a particular member replacing earlier settings.

  * There are three forms for an argument:   
o /name/=/value/ - sets that name (a constant identifier) to that  
value.  
o A vector with a list of [/name/, /value/] vectors, or [/name/]  
to remove a member, where the names can be any string expression.  
o An object has its members copied.

  * There is a new function has_key(/obj/, /name/) that returns true if   
the object contains the named key.

  * These functions are currently experimental and so must be enabled   
before you can use them.

Overview:

An "object" is a collection of names and associated values. In other  
languages this data structure might be called an object (JavaScript), a  
dictionary (Python), an associative array (some UNIX shells, awk), or a  
structure (C, sort of),

This change adds a function that creates an object from a series of  
names, values, and other objects, and a function that queries whether a  
particular member is present. These are mostly-normal functions; there  
is no new syntax introduced.

    
    
      Background:
    

OpenSCAD has had an internal implementation of objects for several  
years, added to support the textmetrics() and fontmetrics() functions,  
and later import() of a JSON file. This existing mechanism includes  
mechanisms for accessing the members of the object and for walking  
through the entries. It does _not_ include a mechanism for the user's  
program to create an object.

Given an object /o/, the current operations are:

  * /o/./name/ yields the value of the /name/ member, where /name/ must   
be an identifier (alphabetic, numeric, underscore, starting with  
alphabetic or underscore). This syntax is very "clean", but does  
not allow for names that are derived from expressions or for names  
that are not suitable for use as identifiers. An undefined name is  
not an error; it yields undefined.

  * /o/[/name/] also yields the value of the /name/ member, but /name/   
can be an any string expression. This syntax is a bit more awkward  
than the /o/./name/ syntax, but allows for dynamically-created names  
and for names that are not suitable as identifiers. Again, and  
undefined name yields undefined.

  * for (/name/ = /o/) ... is the object equivalent of the vector   
for(...). It walks the object, setting /name/ to each member name  
in sequence. This mechanism is usable as both a normal statement  
and as a list comprehension element. Note that it yields only the  
name; the value is accessible as /o/[/name/]. Formally the entries  
should be assumed to be in no specific order, but for aesthetic  
reasons they are reported in the order they were added to the object.

  * is_object(/v/) returns true if /v/ is an object.

  * echo(/o/) and str(/o/) produce textual representations of objects.   
(Note: the textual form looks sort of like syntax, but is not legal  
OpenSCAD syntax. It is likely to change in the future; see _Future  
Directions_ below.)

Details:

The object() function constructs a new object, processing each argument  
in sequence from left to right, with later settings replacing earlier  
settings. There are three variations of arguments; they can be mixed in  
any way.

  * A named parameter /name/=/value/   
o Sets the specified name to the specified value. As with all  
named arguments to functions, the name must be an identifier.

  * a vector [ /v1/, /v2/, ... ]   
o /v1/, /v2/, ... are each two- or one-element vectors  
o [/name/, /value/]  
\+ Sets the specified name to the specified value. The name  
can be any string expression.  
o [/name/]  
\+ Removes the specified name from the object being  
accumulated. (Note that this is subtly different from  
setting it to undefined, in that it will not be reported for  
has_key() or when walking the names of the object.)

  * an object /o/   
o An object has each of its members copied into the new object.

The values contained in an object can (of course) be of any data type:  
numbers, strings, vectors, function references, objects, et cetera.

There is also a new function has_key(/o/, /name/) that returns true if  
the object has a member with the specified name.

    
    
      Examples:
    

  * Create an object; access its members:   
o = object(a=1, b=2);  
echo(o.a, o["b"]);

  * Create an object with varying names, and access them:   
names = [ "apple", "banana", "string bean" ];  
o = object([ for (name=names) [name, 123] ]);  
for (name=names) echo(name, o[name]);

  * Create an object, then create modified copies of that object:   
// Ancient planets  
planets = object(mercury=1, venus=2, earth=3, mars=4, jupiter=5,  
saturn=6);  
planets1781 = object(planets, uranus=7); // Uranus discovered  
planets1846 = object(planets1781, neptune=8); // Neptune discovered  
planets1930 = object(planets1846, pluto=9); // Pluto discovered  
planets2006 = object(planets1930, [["pluto"]]); // Pluto un-planeted

  * Check whether a member is present:   
echo(has_key(planets1846, "neptune")); // true  
echo(has_key(planets2006, "pluto")); // false

Future Directions and Related Projects:

This is the second phase (after the textmetrics() work) of a longer-term  
plan to introduce "object" features into OpenSCAD.

Object literals, object comprehension: OEP8a  
<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>  
adds a syntax for creating objects, including object comprehensions,  
roughly modeled on JavaScript object syntax, so that { a: 1, b: 2 } is  
equivalent to object(a=1, b=2). Changes echo() and str() to represent  
objects using this syntax.

OEP8  
<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References>  
further adds geometry as data and module references.

No formal proposals:

Methods: If a function reference comes from an object or a vector, it  
should see a special variable $this that refers to the containing object  
or vector. Note that although there's no inheritance per se, making a  
modified copy of an object is a lot like the prototype-based OO  
<https://en.wikipedia.org/wiki/Prototype-based_programming>.

Variable parameter lists: a syntax for a parameter lists that says  
"return the rest of the parameters in this variable", as a vector (for  
positional arguments) or an object (for named arguments).

Spread syntax: a syntax for adding a vector to an argument list as  
positional arguments, or adding an object to an argument list as named  
arguments.

Sets: Some kind of syntactic sugar to make it easy to create an object  
containing boolean "true", to make it easy to define a set (in the  
mathematical sense) and query whether particular items are present in it.

    
    
      Questions:
    

  * What should these things be called?   
o They're modeled on JavaScript objects, but to a Python person  
they look more like dictionaries and to a C person they look  
more like structures.  
o Are they really "objects", when they don't have OO features?  
See _Future Directions_ about methods.  
o In OpenSCAD, doesn't "object" already mean a geometric figure?

Credits / History:

  * I did the original textmetrics() work.

  * Revar Desmera did the original implementation of object().

  * Peter Kriens drove this final integration, cleaning up the   
implementation, fixing a bug, and writing test cases.

Quick summary: * 2025.07.11 adds the the object() function, which creates an
object (in the style returned by textmetrics(), fontmetrics(), and import() of
a JSON file). * It accumulates the object by processing the arguments left to
right, with later settings for a particular member replacing earlier settings.
* There are three forms for an argument: o /name/=/value/ - sets that name (a
constant identifier) to that value. o A vector with a list of [/name/,
/value/] vectors, or [/name/] to remove a member, where the names can be any
string expression. o An object has its members copied. * There is a new
function has_key(/obj/, /name/) that returns true if the object contains the
named key. * These functions are currently experimental and so must be enabled
before you can use them. Overview: An "object" is a collection of names and
associated values. In other languages this data structure might be called an
object (JavaScript), a dictionary (Python), an associative array (some UNIX
shells, awk), or a structure (C, sort of), This change adds a function that
creates an object from a series of names, values, and other objects, and a
function that queries whether a particular member is present. These are
mostly-normal functions; there is no new syntax introduced. Background:
OpenSCAD has had an internal implementation of objects for several years,
added to support the textmetrics() and fontmetrics() functions, and later
import() of a JSON file. This existing mechanism includes mechanisms for
accessing the members of the object and for walking through the entries. It
does *not* include a mechanism for the user's program to create an object.
Given an object /o/, the current operations are: * /o/./name/ yields the value
of the /name/ member, where /name/ must be an identifier (alphabetic, numeric,
underscore, starting with alphabetic or underscore). This syntax is very
"clean", but does not allow for names that are derived from expressions or for
names that are not suitable for use as identifiers. An undefined name is not
an error; it yields undefined. * /o/[/name/] also yields the value of the
/name/ member, but /name/ can be an any string expression. This syntax is a
bit more awkward than the /o/./name/ syntax, but allows for dynamically-
created names and for names that are not suitable as identifiers. Again, and
undefined name yields undefined. * for (/name/ = /o/) ... is the object
equivalent of the vector for(...). It walks the object, setting /name/ to each
member name in sequence. This mechanism is usable as both a normal statement
and as a list comprehension element. Note that it yields only the name; the
value is accessible as /o/[/name/]. Formally the entries should be assumed to
be in no specific order, but for aesthetic reasons they are reported in the
order they were added to the object. * is_object(/v/) returns true if /v/ is
an object. * echo(/o/) and str(/o/) produce textual representations of
objects. (Note: the textual form looks sort of like syntax, but is not legal
OpenSCAD syntax. It is likely to change in the future; see *Future Directions*
below.) Details: The object() function constructs a new object, processing
each argument in sequence from left to right, with later settings replacing
earlier settings. There are three variations of arguments; they can be mixed
in any way. * A named parameter /name/=/value/ o Sets the specified name to
the specified value. As with all named arguments to functions, the name must
be an identifier. * a vector [ /v1/, /v2/, ... ] o /v1/, /v2/, ... are each
two- or one-element vectors o [/name/, /value/] \+ Sets the specified name to
the specified value. The name can be any string expression. o [/name/] \+
Removes the specified name from the object being accumulated. (Note that this
is subtly different from setting it to undefined, in that it will not be
reported for has_key() or when walking the names of the object.) * an object
/o/ o An object has each of its members copied into the new object. The values
contained in an object can (of course) be of any data type: numbers, strings,
vectors, function references, objects, et cetera. There is also a new function
has_key(/o/, /name/) that returns true if the object has a member with the
specified name. Examples: * Create an object; access its members: o =
object(a=1, b=2); echo(o.a, o["b"]); * Create an object with varying names,
and access them: names = [ "apple", "banana", "string bean" ]; o = object([
for (name=names) [name, 123] ]); for (name=names) echo(name, o[name]); *
Create an object, then create modified copies of that object: // Ancient
planets planets = object(mercury=1, venus=2, earth=3, mars=4, jupiter=5,
saturn=6); planets1781 = object(planets, uranus=7); // Uranus discovered
planets1846 = object(planets1781, neptune=8); // Neptune discovered
planets1930 = object(planets1846, pluto=9); // Pluto discovered planets2006 =
object(planets1930, [["pluto"]]); // Pluto un-planeted * Check whether a
member is present: echo(has_key(planets1846, "neptune")); // true
echo(has_key(planets2006, "pluto")); // false Future Directions and Related
Projects: This is the second phase (after the textmetrics() work) of a longer-
term plan to introduce "object" features into OpenSCAD. Object literals,
object comprehension: OEP8a
<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>
adds a syntax for creating objects, including object comprehensions, roughly
modeled on JavaScript object syntax, so that { a: 1, b: 2 } is equivalent to
object(a=1, b=2). Changes echo() and str() to represent objects using this
syntax. OEP8
<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References> further adds geometry as data and module
references. No formal proposals: Methods: If a function reference comes from
an object or a vector, it should see a special variable $this that refers to
the containing object or vector. Note that although there's no inheritance per
se, making a modified copy of an object is a lot like the prototype-based OO
<https://en.wikipedia.org/wiki/Prototype-based_programming>. Variable
parameter lists: a syntax for a parameter lists that says "return the rest of
the parameters in this variable", as a vector (for positional arguments) or an
object (for named arguments). Spread syntax: a syntax for adding a vector to
an argument list as positional arguments, or adding an object to an argument
list as named arguments. Sets: Some kind of syntactic sugar to make it easy to
create an object containing boolean "true", to make it easy to define a set
(in the mathematical sense) and query whether particular items are present in
it. Questions: * What should these things be called? o They're modeled on
JavaScript objects, but to a Python person they look more like dictionaries
and to a C person they look more like structures. o Are they really "objects",
when they don't have OO features? See *Future Directions* about methods. o In
OpenSCAD, doesn't "object" already mean a geometric figure? Credits / History:
* I did the original textmetrics() work. * Revar Desmera did the original
implementation of object(). * Peter Kriens drove this final integration,
cleaning up the implementation, fixing a bug, and writing test cases.

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Sun, Jul 13, 2025 10:44 PM

Here's a program that I threw together that exercises the new object  
features.

It provides a framework for doing a general animation - at this time, do  
this, at that time, do that. For an example of doing that without a  
framework like this, look at <https://openscad.org/advent-calendar-2023/>  
at day 24.

Remember that this requires 2025.07.11. Zoom as desired.

// Best view is looking straight down at the origin.  
$vpr = [0,0,0];  
$vpt = [0,0,0];

// Demonstration animation. Use FPS=10 and steps=100.  
// Zoom as desired.

// This vector is a description of everything that happens  
// during the animation. You want a wide window to read it.  
// The only thing that's defined is "t", the timestamp for that  
// particular entry. The rest are up to your program.  
// For this animation:  
// pos1, pos2: the {red, green} stick man's position  
// arm1, arm2: the {red, green} stick man's arm angle  
// says1, says2: what the {red, green} stick man is saying  
timeline = [  
object(t=0, pos1=[-50,0,0], arm1=-30, says1="", pos2=[50,0], arm2=-30,
says2="" ),  
object(t=2.5, arm1=-30 ),  
object(t=3, arm1=50, says1="Hey, George!" ),  
object(t=3.5, arm1=-30 ),  
object(t=5, says1="" ),  
object(t=5.5, arm2=-30, ),  
object(t=6, arm2=50, says2="Hey, Fred!" ),  
object(t=6.5, arm2=-30 ),  
object(t=7, says2="" ),  
object(t=12, pos1=[-5,0,0], pos2=[5,0] ),  
object(t=13, says1="Can I go past?" ),  
object(t=14, says1="" ),  
object(t=15, says2="Sorry, no." ),  
object(t=16, says2="" ),  
object(t=17, says1="I hate living on a number line!" ),  
object(t=19, says1="" ),  
object(t=19.5, says2="Me too!" ),  
object(t=20.5, says2="" ),  
object(t=22, pos1=[-5,0,0], arm2=-30, says1="", pos2=[5,0], arm2=-30, says2=""
),  
];

// Now, create the current frame of the animation.

// Get the current values of all of the timeline columns.  
a = animate(timeline);  
// Using those values, create the model at this moment. There are two stick
men.  
translate(a.pos1) {  
color("red") stickman(a.says1, a.arm1);  
}  
translate(a.pos2) {  
color("green") stickman(a.says2, a.arm2);  
}

// Create a stick man, holding his arms at the specified angle and saying
what's specified.  
module stickman(says, arm) {  
square([1,8], center=true);  
translate([0,5]) circle(2);  
translate([0,2])  
rotate(arm)  
translate([0,-0.5])  
square([4,1]);  
translate([0,2])  
rotate(180-arm)  
translate([0,-0.5])  
square([4,1]);  
translate([0,-4])  
rotate(200)  
translate([-0.5,0])  
square([1,5]);  
translate([0,-4])  
rotate(160)  
translate([-0.5,0])  
square([1,5]);  
translate([0, 8]) text(says, halign="center", valign="baseline", size=3);  
}

// The rest is generic support for using a timeline like that.

// Extract one column from an animation timeline, extracting only  
// those entries where that column is present.  
function animate_extract(list, key) = [  
for (e = list) if (!is_undef(e[key])) [ e.t, e[key] ]  
];

// Get the duration of the timeline, the timestamp of the  
// last entry in the timeline.  
function animate_duration(list) = list[len(list)-1].t;

// Given $t, a timeline and a key, interpolate the current value  
// of the key.  
function animate_interpolate(list, key) =  
xlookup($t * animate_duration(list), animate_extract(list, key));

// Get a list of all keys used in the timeline.  
function animate_keys(list) =  
let (o = object(  
[  
for (e = list)  
for (k = e)  
[ k, true ]  
]  
))  
[ for (k = o) k ];

// Given $t and a timeline, return an aggregated object with the  
// current values of all of the columns of the timeline.  
function animate(timeline) =  
let(keys = animate_keys(timeline))  
object(  
[  
for (k = keys) [ k, animate_interpolate(timeline, k) ]  
]  
);

// lookup() on steroids. Given a value and a lookup-like list,  
// do the lookup and interpolation that lookup() does... but have  
// it also work for strings, booleans, and identical-length lists  
// of numbers.  
function xlookup(val, list) =  
is_num(list[0][1]) ? lookup(val, list)  
: is_string(list[0][1]) ? lookup_string(val, list)  
: is_bool(list[0][1]) ? lookup_bool(val, list)  
: is_list(list[0][1]) ? lookup_list(val, list)  
: assert(false, "don't know how to lookup that type");

// Given a value and a lookup list, return the index of the entry  
// before (or matching) the value.  
function lookup_prev(val, list) =  
let (tmp = [ for (i = [0:1:len(list)-1]) [ list[i][0], i ] ])  
floor(lookup(val, tmp));

//Given a value and a lookup list, return the index of the entry  
// after (or matching) the value.  
function lookup_next(val, list) =  
let (tmp = [ for (i = [0:1:len(list)-1]) [ list[i][0], i ] ])  
ceil(lookup(val, tmp));

// Given a value and a lookup list containing strings, return the  
// string before (or matching) the value.  
function lookup_string(val, list) = list[lookup_prev(val, list)][1];

// Given a value and a lookup list containing booleans, return the  
// boolean before (or matching) the value.  
function lookup_bool(val, list) = list[lookup_prev(val, list)][1];

// Given a value and a lookup list containing same-length lists of  
// numbers, interpolate values for the list. Note that because  
// lookup_prev() and lookup_next() return the same entry on an exact  
// match, and that leads to 0*0/0, that case has to be handled  
// specially.  
function lookup_list(val, list) =  
let(  
p = lookup_prev(val, list),  
n = lookup_next(val, list)  
)  
p == n  
? list[p][1]  
: list[p][1]  
\+ (list[n][1]-list[p][1])  
* (val - list[p][0]) / (list[n][0] - list[p][0]);

Here's a program that I threw together that exercises the new object features.
It provides a framework for doing a general animation - at this time, do this,
at that time, do that. For an example of doing that without a framework like
this, look at https://openscad.org/advent-calendar-2023/ at day 24. Remember
that this requires 2025.07.11. Zoom as desired. // Best view is looking
straight down at the origin. $vpr = [0,0,0]; $vpt = [0,0,0]; // Demonstration
animation. Use FPS=10 and steps=100. // Zoom as desired. // This vector is a
description of everything that happens // during the animation. You want a
wide window to read it. // The only thing that's defined is "t", the timestamp
for that // particular entry. The rest are up to your program. // For this
animation: // pos1, pos2: the {red, green} stick man's position // arm1, arm2:
the {red, green} stick man's arm angle // says1, says2: what the {red, green}
stick man is saying timeline = [ object(t=0, pos1=[-50,0,0], arm1=-30,
says1="", pos2=[50,0], arm2=-30, says2="" ), object(t=2.5, arm1=-30 ),
object(t=3, arm1=50, says1="Hey, George!" ), object(t=3.5, arm1=-30 ),
object(t=5, says1="" ), object(t=5.5, arm2=-30, ), object(t=6, arm2=50,
says2="Hey, Fred!" ), object(t=6.5, arm2=-30 ), object(t=7, says2="" ),
object(t=12, pos1=[-5,0,0], pos2=[5,0] ), object(t=13, says1="Can I go past?"
), object(t=14, says1="" ), object(t=15, says2="Sorry, no." ), object(t=16,
says2="" ), object(t=17, says1="I hate living on a number line!" ),
object(t=19, says1="" ), object(t=19.5, says2="Me too!" ), object(t=20.5,
says2="" ), object(t=22, pos1=[-5,0,0], arm2=-30, says1="", pos2=[5,0],
arm2=-30, says2="" ), ]; // Now, create the current frame of the animation. //
Get the current values of all of the timeline columns. a = animate(timeline);
// Using those values, create the model at this moment. There are two stick
men. translate(a.pos1) { color("red") stickman(a.says1, a.arm1); }
translate(a.pos2) { color("green") stickman(a.says2, a.arm2); } // Create a
stick man, holding his arms at the specified angle and saying what's
specified. module stickman(says, arm) { square([1,8], center=true);
translate([0,5]) circle(2); translate([0,2]) rotate(arm) translate([0,-0.5])
square([4,1]); translate([0,2]) rotate(180-arm) translate([0,-0.5])
square([4,1]); translate([0,-4]) rotate(200) translate([-0.5,0])
square([1,5]); translate([0,-4]) rotate(160) translate([-0.5,0])
square([1,5]); translate([0, 8]) text(says, halign="center",
valign="baseline", size=3); } // The rest is generic support for using a
timeline like that. // Extract one column from an animation timeline,
extracting only // those entries where that column is present. function
animate_extract(list, key) = [ for (e = list) if (!is_undef(e[key])) [ e.t,
e[key] ] ]; // Get the duration of the timeline, the timestamp of the // last
entry in the timeline. function animate_duration(list) = list[len(list)-1].t;
// Given $t, a timeline and a key, interpolate the current value // of the
key. function animate_interpolate(list, key) = xlookup($t *
animate_duration(list), animate_extract(list, key)); // Get a list of all keys
used in the timeline. function animate_keys(list) = let (o = object( [ for (e
= list) for (k = e) [ k, true ] ] )) [ for (k = o) k ]; // Given $t and a
timeline, return an aggregated object with the // current values of all of the
columns of the timeline. function animate(timeline) = let(keys =
animate_keys(timeline)) object( [ for (k = keys) [ k,
animate_interpolate(timeline, k) ] ] ); // lookup() on steroids. Given a value
and a lookup-like list, // do the lookup and interpolation that lookup()
does... but have // it also work for strings, booleans, and identical-length
lists // of numbers. function xlookup(val, list) = is_num(list[0][1]) ?
lookup(val, list) : is_string(list[0][1]) ? lookup_string(val, list) :
is_bool(list[0][1]) ? lookup_bool(val, list) : is_list(list[0][1]) ?
lookup_list(val, list) : assert(false, "don't know how to lookup that type");
// Given a value and a lookup list, return the index of the entry // before
(or matching) the value. function lookup_prev(val, list) = let (tmp = [ for (i
= [0:1:len(list)-1]) [ list[i][0], i ] ]) floor(lookup(val, tmp)); //Given a
value and a lookup list, return the index of the entry // after (or matching)
the value. function lookup_next(val, list) = let (tmp = [ for (i =
[0:1:len(list)-1]) [ list[i][0], i ] ]) ceil(lookup(val, tmp)); // Given a
value and a lookup list containing strings, return the // string before (or
matching) the value. function lookup_string(val, list) = list[lookup_prev(val,
list)][1]; // Given a value and a lookup list containing booleans, return the
// boolean before (or matching) the value. function lookup_bool(val, list) =
list[lookup_prev(val, list)][1]; // Given a value and a lookup list containing
same-length lists of // numbers, interpolate values for the list. Note that
because // lookup_prev() and lookup_next() return the same entry on an exact
// match, and that leads to 0*0/0, that case has to be handled // specially.
function lookup_list(val, list) = let( p = lookup_prev(val, list), n =
lookup_next(val, list) ) p == n ? list[p][1] : list[p][1] \+
(list[n][1]-list[p][1]) * (val - list[p][0]) / (list[n][0] - list[p][0]);

![](https://www.gravatar.com/avatar/b748bb54f164c5fafb7e920f624d4cd0?d=blank&s=100)

NS

Nathan Sokalski

Mon, Jul 14, 2025 1:20 AM

I think this is a great step, it will definitely be great when creating
libraries, especially ones with values that would be the equivalent of
enumerations in other languages. I have created multiple libraries, but it was
always inappropriate to use the "include" command, because so many libraries
had variables with similar names, this will definitely improve the
organization of shared libraries. Even though this is currently in the
experimental stage, is there anywhere that the current [planned] syntax is
available? I did not see the object() function on the Cheat Sheet (which is
understandable)? Thanks again!

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)[mailto:njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

From: Jordan Brown via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Sent: Sunday, July 13, 2025 6:20 PM  
To: OpenSCAD [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
Cc: Jordan Brown
[openscad@jordan.maileater.net](mailto:openscad@jordan.maileater.net)  
Subject: [OpenSCAD] New feature in 2025.07.11: the object() function

Quick summary:

  * 2025.07.11 adds the the   
object()  
function, which creates an object (in the style returned by  
textmetrics()  
,  
fontmetrics()  
, and  
import()  
of a JSON file).

  * It accumulates the object by processing the arguments left to right, with later settings for a particular member replacing earlier settings.
  * There are three forms for an argument:   
*   
name=value

  * sets that name (a constant identifier) to that value. 
    * A vector with a list of   
[name, value]  
vectors, or  
[name]  
to remove a member, where the names can be any string expression.

    * An object has its members copied.

  * There is a new function   
has_key(obj, name)  
that returns true if the object contains the named key.

  * These functions are currently experimental and so must be enabled before you can use them.

Overview:

An "object" is a collection of names and associated values. In other languages
this data structure might be called an object (JavaScript), a dictionary
(Python), an associative array (some UNIX shells, awk), or a structure (C,
sort of),

This change adds a function that creates an object from a series of names,
values, and other objects, and a function that queries whether a particular
member is present. These are mostly-normal functions; there is no new syntax
introduced.

Background:

OpenSCAD has had an internal implementation of objects for several years,
added to support the

textmetrics()  
and  
fontmetrics()  
functions, and later  
import()  
of a JSON file. This existing mechanism includes mechanisms for accessing the
members of the object and for walking through the entries. It does not include
a mechanism for the user's program to create an object.

Given an object

o  
, the current operations are:

  * 

o.name  
yields the value of the  
name  
member, where  
name  
must be an identifier (alphabetic, numeric, underscore, starting with
alphabetic or underscore). This syntax is very "clean", but does not allow for
names that are derived from expressions or for names that are not suitable for
use as identifiers. An undefined name is not an error; it yields  
undefined  
.  
*   
o[name]  
also yields the value of the  
name  
member, but  
name  
can be an any string expression. This syntax is a bit more awkward than the  
o.name  
syntax, but allows for dynamically-created names and for names that are not
suitable as identifiers. Again, and undefined name yields  
undefined  
.  
*   
for (name = o) ...  
is the object equivalent of the vector  
for(...)  
. It walks the object, setting  
name  
to each member name in sequence. This mechanism is usable as both a normal
statement and as a list comprehension element. Note that it yields only the
name; the value is accessible as  
o[name]  
. Formally the entries should be assumed to be in no specific order, but for
aesthetic reasons they are reported in the order they were added to the
object.  
*   
is_object(v)  
returns true if  
v  
is an object.  
*   
echo(  
o  
)  
and  
str(o)  
produce textual representations of objects. (Note: the textual form looks sort
of like syntax, but is not legal OpenSCAD syntax. It is likely to change in
the future; see Future Directions below.)

Details:

The

object()  
function constructs a new object, processing each argument in sequence from
left to right, with later settings replacing earlier settings. There are three
variations of arguments; they can be mixed in any way.

  * A named parameter   
name=value  
* Sets the specified name to the specified value. As with all named arguments to functions, the name must be an identifier.
  * a vector   
[ v1, v2, ... ]  
* v1   
, v2  
, ... are each two- or one-element vectors  
*   
[name, value]

    * Sets the specified name to the specified value. The name can be any string expression.   
*   
[name]

    * Removes the specified name from the object being accumulated. (Note that this is subtly different from setting it to   
undefined  
, in that it will not be reported for  
has_key()  
or when walking the names of the object.)

  * an object   
o  
* An object has each of its members copied into the new object.

The values contained in an object can (of course) be of any data type:
numbers, strings, vectors, function references, objects, et cetera.

There is also a new function  
has_key(o, name)  
that returns true if the object has a member with the specified name.  
Examples:

  * Create an object; access its members:

o = object(a=1, b=2);  
echo(o.a, o["b"]);

  * Create an object with varying names, and access them:   
names = [ "apple", "banana", "string bean" ];  
o = object([ for (name=names) [name, 123] ]);  
for (name=names) echo(name, o[name]);

  * Create an object, then create modified copies of that object:   
// Ancient planets  
planets = object(mercury=1, venus=2, earth=3, mars=4, jupiter=5, saturn=6);  
planets1781 = object(planets, uranus=7); // Uranus discovered  
planets1846 = object(planets1781, neptune=8); // Neptune discovered  
planets1930 = object(planets1846, pluto=9); // Pluto discovered  
planets2006 = object(planets1930, [["pluto"]]); // Pluto un-planeted

  * Check whether a member is present:   
echo(has_key(planets1846, "neptune")); // true  
echo(has_key(planets2006, "pluto")); // false

Future Directions and Related Projects:

This is the second phase (after the

textmetrics()  
work) of a longer-term plan to introduce "object" features into OpenSCAD.

Object literals, object comprehension:
OEP8a<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>
adds a syntax for creating objects, including object comprehensions, roughly
modeled on JavaScript object syntax, so that

{ a: 1, b: 2 }  
is equivalent to  
object(a=1, b=2)  
. Changes  
echo()  
and  
str()  
to represent objects using this syntax.

OEP8<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References> further adds geometry as data and module
references.

No formal proposals:

Methods: If a function reference comes from an object or a vector, it should
see a special variable

$this  
that refers to the containing object or vector. Note that although there's no
inheritance per se, making a modified copy of an object is a lot like the
prototype-based OO<https://en.wikipedia.org/wiki/Prototype-based_programming>.

Variable parameter lists: a syntax for a parameter lists that says "return the
rest of the parameters in this variable", as a vector (for positional
arguments) or an object (for named arguments).

Spread syntax: a syntax for adding a vector to an argument list as positional
arguments, or adding an object to an argument list as named arguments.

Sets: Some kind of syntactic sugar to make it easy to create an object
containing boolean "true", to make it easy to define a set (in the
mathematical sense) and query whether particular items are present in it.

Questions:

  * What should these things be called?   
* They're modeled on JavaScript objects, but to a Python person they look more like dictionaries and to a C person they look more like structures.   
* Are they really "objects", when they don't have OO features? See Future Directions about methods.   
* In OpenSCAD, doesn't "object" already mean a geometric figure?

Credits / History:

  * I did the original textmetrics() work.
  * Revar Desmera did the original implementation of   
object()  
.

  * Peter Kriens drove this final integration, cleaning up the implementation, fixing a bug, and writing test cases.

I think this is a great step, it will definitely be great when creating
libraries, especially ones with values that would be the equivalent of
enumerations in other languages. I have created multiple libraries, but it was
always inappropriate to use the "include" command, because so many libraries
had variables with similar names, this will definitely improve the
organization of shared libraries. Even though this is currently in the
experimental stage, is there anywhere that the current [planned] syntax is
available? I did not see the object() function on the Cheat Sheet (which is
understandable)? Thanks again! Nathan Sokalski
njsokalski@hotmail.com<mailto:njsokalski@hotmail.com>
________________________________ From: Jordan Brown via Discuss
<discuss@lists.openscad.org> Sent: Sunday, July 13, 2025 6:20 PM To: OpenSCAD
<discuss@lists.openscad.org> Cc: Jordan Brown <openscad@jordan.maileater.net>
Subject: [OpenSCAD] New feature in 2025.07.11: the object() function Quick
summary: * 2025.07.11 adds the the object() function, which creates an object
(in the style returned by textmetrics() , fontmetrics() , and import() of a
JSON file). * It accumulates the object by processing the arguments left to
right, with later settings for a particular member replacing earlier settings.
* There are three forms for an argument: * name=value \- sets that name (a
constant identifier) to that value. * A vector with a list of [name, value]
vectors, or [name] to remove a member, where the names can be any string
expression. * An object has its members copied. * There is a new function
has_key(obj, name) that returns true if the object contains the named key. *
These functions are currently experimental and so must be enabled before you
can use them. Overview: An "object" is a collection of names and associated
values. In other languages this data structure might be called an object
(JavaScript), a dictionary (Python), an associative array (some UNIX shells,
awk), or a structure (C, sort of), This change adds a function that creates an
object from a series of names, values, and other objects, and a function that
queries whether a particular member is present. These are mostly-normal
functions; there is no new syntax introduced. Background: OpenSCAD has had an
internal implementation of objects for several years, added to support the
textmetrics() and fontmetrics() functions, and later import() of a JSON file.
This existing mechanism includes mechanisms for accessing the members of the
object and for walking through the entries. It does not include a mechanism
for the user's program to create an object. Given an object o , the current
operations are: * o.name yields the value of the name member, where name must
be an identifier (alphabetic, numeric, underscore, starting with alphabetic or
underscore). This syntax is very "clean", but does not allow for names that
are derived from expressions or for names that are not suitable for use as
identifiers. An undefined name is not an error; it yields undefined . *
o[name] also yields the value of the name member, but name can be an any
string expression. This syntax is a bit more awkward than the o.name syntax,
but allows for dynamically-created names and for names that are not suitable
as identifiers. Again, and undefined name yields undefined . * for (name = o)
... is the object equivalent of the vector for(...) . It walks the object,
setting name to each member name in sequence. This mechanism is usable as both
a normal statement and as a list comprehension element. Note that it yields
only the name; the value is accessible as o[name] . Formally the entries
should be assumed to be in no specific order, but for aesthetic reasons they
are reported in the order they were added to the object. * is_object(v)
returns true if v is an object. * echo( o ) and str(o) produce textual
representations of objects. (Note: the textual form looks sort of like syntax,
but is not legal OpenSCAD syntax. It is likely to change in the future; see
Future Directions below.) Details: The object() function constructs a new
object, processing each argument in sequence from left to right, with later
settings replacing earlier settings. There are three variations of arguments;
they can be mixed in any way. * A named parameter name=value * Sets the
specified name to the specified value. As with all named arguments to
functions, the name must be an identifier. * a vector [ v1, v2, ... ] * v1 ,
v2 , ... are each two- or one-element vectors * [name, value] * Sets the
specified name to the specified value. The name can be any string expression.
* [name] * Removes the specified name from the object being accumulated. (Note
that this is subtly different from setting it to undefined , in that it will
not be reported for has_key() or when walking the names of the object.) * an
object o * An object has each of its members copied into the new object. The
values contained in an object can (of course) be of any data type: numbers,
strings, vectors, function references, objects, et cetera. There is also a new
function has_key(o, name) that returns true if the object has a member with
the specified name. Examples: * Create an object; access its members: o =
object(a=1, b=2); echo(o.a, o["b"]); * Create an object with varying names,
and access them: names = [ "apple", "banana", "string bean" ]; o = object([
for (name=names) [name, 123] ]); for (name=names) echo(name, o[name]); *
Create an object, then create modified copies of that object: // Ancient
planets planets = object(mercury=1, venus=2, earth=3, mars=4, jupiter=5,
saturn=6); planets1781 = object(planets, uranus=7); // Uranus discovered
planets1846 = object(planets1781, neptune=8); // Neptune discovered
planets1930 = object(planets1846, pluto=9); // Pluto discovered planets2006 =
object(planets1930, [["pluto"]]); // Pluto un-planeted * Check whether a
member is present: echo(has_key(planets1846, "neptune")); // true
echo(has_key(planets2006, "pluto")); // false Future Directions and Related
Projects: This is the second phase (after the textmetrics() work) of a longer-
term plan to introduce "object" features into OpenSCAD. Object literals,
object comprehension:
OEP8a<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>
adds a syntax for creating objects, including object comprehensions, roughly
modeled on JavaScript object syntax, so that { a: 1, b: 2 } is equivalent to
object(a=1, b=2) . Changes echo() and str() to represent objects using this
syntax.
OEP8<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References> further adds geometry as data and module
references. No formal proposals: Methods: If a function reference comes from
an object or a vector, it should see a special variable $this that refers to
the containing object or vector. Note that although there's no inheritance per
se, making a modified copy of an object is a lot like the prototype-based
OO<https://en.wikipedia.org/wiki/Prototype-based_programming>. Variable
parameter lists: a syntax for a parameter lists that says "return the rest of
the parameters in this variable", as a vector (for positional arguments) or an
object (for named arguments). Spread syntax: a syntax for adding a vector to
an argument list as positional arguments, or adding an object to an argument
list as named arguments. Sets: Some kind of syntactic sugar to make it easy to
create an object containing boolean "true", to make it easy to define a set
(in the mathematical sense) and query whether particular items are present in
it. Questions: * What should these things be called? * They're modeled on
JavaScript objects, but to a Python person they look more like dictionaries
and to a C person they look more like structures. * Are they really "objects",
when they don't have OO features? See Future Directions about methods. * In
OpenSCAD, doesn't "object" already mean a geometric figure? Credits / History:
* I did the original textmetrics() work. * Revar Desmera did the original
implementation of object() . * Peter Kriens drove this final integration,
cleaning up the implementation, fixing a bug, and writing test cases.

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Mon, Jul 14, 2025 2:23 AM

This is definitely a great step, and will be a great help for libraries and  
more complicated code, but my thinking was more in code clarity and  
simplification, and cleaner interfaces to (library) functions that need to  
return multiple values. Right now such functions have to return a list  
which has arbitrary index values.

Were you thinking that libraries would be constructed so that the entire  
library is inside an object?

On Sun, Jul 13, 2025 at 9:21 PM Nathan Sokalski via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I think this is a great step, it will definitely be great when creating  
libraries, especially ones with values that would be the equivalent of  
enumerations in other languages. I have created multiple libraries, but it  
was always inappropriate to use the "include" command, because so many  
libraries had variables with similar names, this will definitely improve  
the organization of shared libraries. Even though this is currently in the  
experimental stage, is there anywhere that the current [planned] syntax is  
available? I did not see the object() function on the Cheat Sheet (which is  
understandable)? Thanks again!

Nathan Sokalski  
[njsokalski@hotmail.com](mailto:njsokalski@hotmail.com)

* * *

_From:_ Jordan Brown via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
_Sent:_ Sunday, July 13, 2025 6:20 PM  
_To:_ OpenSCAD [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)  
_Cc:_ Jordan Brown
[openscad@jordan.maileater.net](mailto:openscad@jordan.maileater.net)  
_Subject:_ [OpenSCAD] New feature in 2025.07.11: the object() function

Quick summary:

    
    
    - 2025.07.11 adds the the
    object()
     function, which creates an object (in the style returned by
    textmetrics()
    ,
    fontmetrics()
    , and
    import()
     of a JSON file).
    - It accumulates the object by processing the arguments left to right,
    with later settings for a particular member replacing earlier settings.
    - There are three forms for an argument:
       - *name*=*value*
        - sets that name (a constant identifier) to that value.
       - A vector with a list of
       [*name*, *value*]
        vectors, or
       [*name*]
        to remove a member, where the names can be any string expression.
       - An object has its members copied.
    - There is a new function
    has_key(*obj*, *name*)
     that returns true if the object contains the named key.
    - These functions are currently experimental and so must be enabled
    before you can use them.
    

Overview:

An "object" is a collection of names and associated values. In other  
languages this data structure might be called an object (JavaScript), a  
dictionary (Python), an associative array (some UNIX shells, awk), or a  
structure (C, sort of),

This change adds a function that creates an object from a series of names,  
values, and other objects, and a function that queries whether a particular  
member is present. These are mostly-normal functions; there is no new  
syntax introduced.  
Background:

OpenSCAD has had an internal implementation of objects for several years,  
added to support the  
textmetrics()  
and  
fontmetrics()  
functions, and later  
import()  
of a JSON file. This existing mechanism includes mechanisms for  
accessing the members of the object and for walking through the entries.  
It does _not_ include a mechanism for the user's program to create an  
object.

Given an object  
_o_  
, the current operations are:

    
    
    - *o*.*name*
     yields the value of the
    *name*
     member, where
    *name*
     must be an identifier (alphabetic, numeric, underscore, starting with
    alphabetic or underscore).  This syntax is very "clean", but does not allow
    for names that are derived from expressions or for names that are not
    suitable for use as identifiers.  An undefined name is not an error; it
    yields
    undefined
    .
    - *o*[*name*]
     also yields the value of the
    *name*
     member, but
    *name*
     can be an any string expression.  This syntax is a bit more awkward
    than the
    *o*.*name*
     syntax, but allows for dynamically-created names and for names that
    are not suitable as identifiers.  Again, and undefined name yields
    undefined
    .
    - for (*name* = *o*) ...
     is the object equivalent of the vector
    for(...)
    .  It walks the object, setting
    *name*
     to each member name in sequence.  This mechanism is usable as both a
    normal statement and as a list comprehension element.  Note that it yields
    only the name; the value is accessible as
    *o*[*name*]
    .  Formally the entries should be assumed to be in no specific order,
    but for aesthetic reasons they are reported in the order they were added to
    the object.
    - is_object(*v*)
     returns true if
    *v*
     is an object.
    - echo(
    * o *
    )
     and
    str(*o*)
     produce textual representations of objects.  (Note:  the textual form
    looks sort of like syntax, but is not legal OpenSCAD syntax.  It is likely
    to change in the future; see *Future Directions* below.)
    

Details:

The  
object()  
function constructs a new object, processing each argument in sequence  
from left to right, with later settings replacing earlier settings. There  
are three variations of arguments; they can be mixed in any way.

    
    
    - A named parameter
    *name*=*value*
    - Sets the specified name to the specified value.  As with all named
       arguments to functions, the name must be an identifier.
    - a vector
    [ *v1*, *v2*, ... ]
    - *v1*
       , *v2*
       , ... are each two- or one-element vectors
       - [*name*, *value*]
       - Sets the specified name to the specified value.  The name can be
          any string expression.
       - [*name*]
       - Removes the specified name from the object being accumulated.
          (Note that this is subtly different from setting it to
          undefined
          , in that it will not be reported for
          has_key()
           or when walking the names of the object.)
          - an object
    *o*
    - An object has each of its members copied into the new object.
    

The values contained in an object can (of course) be of any data type:  
numbers, strings, vectors, function references, objects, et cetera.

There is also a new function  
has_key(_o_ , _name_)  
that returns true if the object has a member with the specified name.  
Examples:

    
    
    - Create an object; access its members:
    
    o = object(a=1, b=2);
    echo(o.a, o["b"]);
    - Create an object with varying names, and access them:
    names = [ "apple", "banana", "string bean" ];
    o = object([ for (name=names) [name, 123] ]);
    for (name=names) echo(name, o[name]);
    - Create an object, then create modified copies of that object:
    // Ancient planets
    planets = object(mercury=1, venus=2, earth=3, mars=4, jupiter=5,
    saturn=6);
    planets1781 = object(planets, uranus=7);        // Uranus discovered
    planets1846 = object(planets1781, neptune=8);   // Neptune discovered
    planets1930 = object(planets1846, pluto=9);     // Pluto discovered
    planets2006 = object(planets1930, [["pluto"]]); // Pluto un-planeted
    - Check whether a member is present:
    echo(has_key(planets1846, "neptune")); // true
    echo(has_key(planets2006, "pluto"));   // false
    

Future Directions and Related Projects:

This is the second phase (after the  
textmetrics()  
work) of a longer-term plan to introduce "object" features into OpenSCAD.

Object literals, object comprehension: OEP8a  
<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>
adds  
a syntax for creating objects, including object comprehensions, roughly  
modeled on JavaScript object syntax, so that  
{ a: 1, b: 2 }  
is equivalent to  
object(a=1, b=2)  
. Changes  
echo()  
and  
str()  
to represent objects using this syntax.

OEP8  
<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References> further  
adds geometry as data and module references.

No formal proposals:

Methods: If a function reference comes from an object or a vector, it  
should see a special variable  
$this  
that refers to the containing object or vector. Note that although  
there's no inheritance per se, making a modified copy of an object is a lot  
like the prototype-based OO  
<https://en.wikipedia.org/wiki/Prototype-based_programming>.

Variable parameter lists: a syntax for a parameter lists that says  
"return the rest of the parameters in this variable", as a vector (for  
positional arguments) or an object (for named arguments).

Spread syntax: a syntax for adding a vector to an argument list as  
positional arguments, or adding an object to an argument list as named  
arguments.

Sets: Some kind of syntactic sugar to make it easy to create an object  
containing boolean "true", to make it easy to define a set (in the  
mathematical sense) and query whether particular items are present in it.  
Questions:

    
    
    - What should these things be called?
       - They're modeled on JavaScript objects, but to a Python person
       they look more like dictionaries and to a C person they look more like
       structures.
       - Are they really "objects", when they don't have OO features?  See *Future
       Directions* about methods.
       - In OpenSCAD, doesn't "object" already mean a geometric figure?
    

Credits / History:

    
    
    - I did the original textmetrics() work.
    - Revar Desmera did the original implementation of
    object()
    .
    - Peter Kriens drove this final integration, cleaning up the
    implementation, fixing a bug, and writing test cases.
    

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

This is definitely a great step, and will be a great help for libraries and
more complicated code, but my thinking was more in code clarity and
simplification, and cleaner interfaces to (library) functions that need to
return multiple values. Right now such functions have to return a list which
has arbitrary index values. Were you thinking that libraries would be
constructed so that the entire library is inside an object? On Sun, Jul 13,
2025 at 9:21 PM Nathan Sokalski via Discuss < discuss@lists.openscad.org>
wrote: > I think this is a great step, it will definitely be great when
creating > libraries, especially ones with values that would be the equivalent
of > enumerations in other languages. I have created multiple libraries, but
it > was always inappropriate to use the "include" command, because so many >
libraries had variables with similar names, this will definitely improve > the
organization of shared libraries. Even though this is currently in the >
experimental stage, is there anywhere that the current [planned] syntax is >
available? I did not see the object() function on the Cheat Sheet (which is >
understandable)? Thanks again! > > Nathan Sokalski > njsokalski@hotmail.com >
> \------------------------------ > *From:* Jordan Brown via Discuss
<discuss@lists.openscad.org> > *Sent:* Sunday, July 13, 2025 6:20 PM > *To:*
OpenSCAD <discuss@lists.openscad.org> > *Cc:* Jordan Brown
<openscad@jordan.maileater.net> > *Subject:* [OpenSCAD] New feature in
2025.07.11: the object() function > > Quick summary: > > \- 2025.07.11 adds
the the > object() > function, which creates an object (in the style returned
by > textmetrics() > , > fontmetrics() > , and > import() > of a JSON file). >
\- It accumulates the object by processing the arguments left to right, > with
later settings for a particular member replacing earlier settings. > \- There
are three forms for an argument: > \- *name*=*value* > \- sets that name (a
constant identifier) to that value. > \- A vector with a list of > [*name*,
*value*] > vectors, or > [*name*] > to remove a member, where the names can be
any string expression. > \- An object has its members copied. > \- There is a
new function > has_key(*obj*, *name*) > that returns true if the object
contains the named key. > \- These functions are currently experimental and so
must be enabled > before you can use them. > > Overview: > > An "object" is a
collection of names and associated values. In other > languages this data
structure might be called an object (JavaScript), a > dictionary (Python), an
associative array (some UNIX shells, awk), or a > structure (C, sort of), > >
This change adds a function that creates an object from a series of names, >
values, and other objects, and a function that queries whether a particular >
member is present. These are mostly-normal functions; there is no new > syntax
introduced. > Background: > > OpenSCAD has had an internal implementation of
objects for several years, > added to support the > textmetrics() > and >
fontmetrics() > functions, and later > import() > of a JSON file. This
existing mechanism includes mechanisms for > accessing the members of the
object and for walking through the entries. > It does *not* include a
mechanism for the user's program to create an > object. > > Given an object >
*o* > , the current operations are: > > \- *o*.*name* > yields the value of
the > *name* > member, where > *name* > must be an identifier (alphabetic,
numeric, underscore, starting with > alphabetic or underscore). This syntax is
very "clean", but does not allow > for names that are derived from expressions
or for names that are not > suitable for use as identifiers. An undefined name
is not an error; it > yields > undefined > . > \- *o*[*name*] > also yields
the value of the > *name* > member, but > *name* > can be an any string
expression. This syntax is a bit more awkward > than the > *o*.*name* >
syntax, but allows for dynamically-created names and for names that > are not
suitable as identifiers. Again, and undefined name yields > undefined > . > \-
for (*name* = *o*) ... > is the object equivalent of the vector > for(...) > .
It walks the object, setting > *name* > to each member name in sequence. This
mechanism is usable as both a > normal statement and as a list comprehension
element. Note that it yields > only the name; the value is accessible as >
*o*[*name*] > . Formally the entries should be assumed to be in no specific
order, > but for aesthetic reasons they are reported in the order they were
added to > the object. > \- is_object(*v*) > returns true if > *v* > is an
object. > \- echo( > * o * > ) > and > str(*o*) > produce textual
representations of objects. (Note: the textual form > looks sort of like
syntax, but is not legal OpenSCAD syntax. It is likely > to change in the
future; see *Future Directions* below.) > > Details: > > The > object() >
function constructs a new object, processing each argument in sequence > from
left to right, with later settings replacing earlier settings. There > are
three variations of arguments; they can be mixed in any way. > > \- A named
parameter > *name*=*value* > \- Sets the specified name to the specified
value. As with all named > arguments to functions, the name must be an
identifier. > \- a vector > [ *v1*, *v2*, ... ] > \- *v1* > , *v2* > , ... are
each two- or one-element vectors > \- [*name*, *value*] > \- Sets the
specified name to the specified value. The name can be > any string
expression. > \- [*name*] > \- Removes the specified name from the object
being accumulated. > (Note that this is subtly different from setting it to >
undefined > , in that it will not be reported for > has_key() > or when
walking the names of the object.) > \- an object > *o* > \- An object has each
of its members copied into the new object. > > The values contained in an
object can (of course) be of any data type: > numbers, strings, vectors,
function references, objects, et cetera. > > There is also a new function >
has_key(*o*, *name*) > that returns true if the object has a member with the
specified name. > Examples: > > \- Create an object; access its members: > > o
= object(a=1, b=2); > echo(o.a, o["b"]); > \- Create an object with varying
names, and access them: > names = [ "apple", "banana", "string bean" ]; > o =
object([ for (name=names) [name, 123] ]); > for (name=names) echo(name,
o[name]); > \- Create an object, then create modified copies of that object: >
// Ancient planets > planets = object(mercury=1, venus=2, earth=3, mars=4,
jupiter=5, > saturn=6); > planets1781 = object(planets, uranus=7); // Uranus
discovered > planets1846 = object(planets1781, neptune=8); // Neptune
discovered > planets1930 = object(planets1846, pluto=9); // Pluto discovered >
planets2006 = object(planets1930, [["pluto"]]); // Pluto un-planeted > \-
Check whether a member is present: > echo(has_key(planets1846, "neptune")); //
true > echo(has_key(planets2006, "pluto")); // false > > Future Directions and
Related Projects: > > This is the second phase (after the > textmetrics() >
work) of a longer-term plan to introduce "object" features into OpenSCAD. > >
Object literals, object comprehension: OEP8a >
<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>
adds > a syntax for creating objects, including object comprehensions, roughly
> modeled on JavaScript object syntax, so that > { a: 1, b: 2 } > is
equivalent to > object(a=1, b=2) > . Changes > echo() > and > str() > to
represent objects using this syntax. > > OEP8 >
<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References> further > adds geometry as data and module
references. > > No formal proposals: > > Methods: If a function reference
comes from an object or a vector, it > should see a special variable > $this >
that refers to the containing object or vector. Note that although > there's
no inheritance per se, making a modified copy of an object is a lot > like the
prototype-based OO > <https://en.wikipedia.org/wiki/Prototype-
based_programming>. > > Variable parameter lists: a syntax for a parameter
lists that says > "return the rest of the parameters in this variable", as a
vector (for > positional arguments) or an object (for named arguments). > >
Spread syntax: a syntax for adding a vector to an argument list as >
positional arguments, or adding an object to an argument list as named >
arguments. > > Sets: Some kind of syntactic sugar to make it easy to create an
object > containing boolean "true", to make it easy to define a set (in the >
mathematical sense) and query whether particular items are present in it. >
Questions: > > \- What should these things be called? > \- They're modeled on
JavaScript objects, but to a Python person > they look more like dictionaries
and to a C person they look more like > structures. > \- Are they really
"objects", when they don't have OO features? See *Future > Directions* about
methods. > \- In OpenSCAD, doesn't "object" already mean a geometric figure? >
> Credits / History: > > \- I did the original textmetrics() work. > \- Revar
Desmera did the original implementation of > object() > . > \- Peter Kriens
drove this final integration, cleaning up the > implementation, fixing a bug,
and writing test cases. > > _______________________________________________ >
OpenSCAD mailing list > To unsubscribe send an email to discuss-
leave@lists.openscad.org >

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Mon, Jul 14, 2025 2:56 AM

On 7/13/2025 6:20 PM, Nathan Sokalski via Discuss wrote:

____

Even though this is currently in the experimental stage, is there  
anywhere that the current [planned] syntax is available?

I've got it in a PR, but that PR is now several years stale and I'm  
pretty sure it no longer builds. (It's also got some other stuff that I  
think is cool; see PR#4478  
<https://github.com/openscad/openscad/pull/4478> / OEP8  
<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References>.)

____

I did not see the object() function on the Cheat Sheet (which is  
understandable)?

Peter's got a draft of updating the cheat sheet, and one of us will add  
these two functions to the manual.

On 7/13/2025 6:20 PM, Nathan Sokalski via Discuss wrote: > Even though this is
currently in the experimental stage, is there > anywhere that the current
[planned] syntax is available? I've got it in a PR, but that PR is now several
years stale and I'm pretty sure it no longer builds. (It's also got some other
stuff that I think is cool; see PR#4478
<https://github.com/openscad/openscad/pull/4478> / OEP8
<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References>.) > I did not see the object() function on
the Cheat Sheet (which is > understandable)? Peter's got a draft of updating
the cheat sheet, and one of us will add these two functions to the manual.

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Mon, Jul 14, 2025 3:01 AM

On 7/13/2025 7:23 PM, Adrian Mariano via Discuss wrote:

____

Were you thinking that libraries would be constructed so that the  
entire library is inside an object?

Entirely plausible. You can't really do it today because we don't have  
module references.

I forgot to mention in the Futures section that I want to figure out how  
to have a function - call it use(), for discussion purposes, though it  
would be enough different from the "use" directive that I'd probably  
call it something else. You would say something like "foo =  
use("foo.scad");" and foo would get a single object with all of the  
global variables, modules, and functions from foo.scad. (Handwave on  
namespace issues; quite possibly just declare that for this style of  
library you must not have the same names for functions, modules, and  
variables.) That would reduce namespace problems to (a) file names and  
(b) special variable names. And we'd define it to evaluate the  
variables exactly once, at use() time :-)

On 7/13/2025 7:23 PM, Adrian Mariano via Discuss wrote: > Were you thinking
that libraries would be constructed so that the > entire library is inside an
object? Entirely plausible. You can't really do it today because we don't have
module references. I forgot to mention in the Futures section that I want to
figure out how to have a function - call it use(), for discussion purposes,
though it would be enough different from the "use" directive that I'd probably
call it something else. You would say something like "foo = use("foo.scad");"
and foo would get a single object with all of the global variables, modules,
and functions from foo.scad. (Handwave on namespace issues; quite possibly
just declare that for this style of library you must not have the same names
for functions, modules, and variables.) That would reduce namespace problems
to (a) file names and (b) special variable names. And we'd define it to
evaluate the variables exactly once, at use() time :-)

![](https://www.gravatar.com/avatar/b337dce56de59030c553069fad5ff3ca?d=blank&s=100)

RD

Revar Desmera

Mon, Jul 14, 2025 4:39 AM

♫ PARTY-TIME! ♬

￼

  * Revar

____

On Jul 13, 2025, at 3:20 PM, Jordan Brown via
Discuss[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

Quick summary:

2025.07.11 adds the the object() function, which creates an object (in the
style returned by textmetrics(), fontmetrics(), and import() of a JSON file).  
It accumulates the object by processing the arguments left to right, with
later settings for a particular member replacing earlier settings.  
There are three forms for an argument:  
name=value - sets that name (a constant identifier) to that value.  
A vector with a list of [name, value] vectors, or [name] to remove a member,
where the names can be any string expression.  
An object has its members copied.  
There is a new function has_key(obj, name) that returns true if the object
contains the named key.  
These functions are currently experimental and so must be enabled before you
can use them.  
Overview:

An "object" is a collection of names and associated values. In other languages
this data structure might be called an object (JavaScript), a dictionary
(Python), an associative array (some UNIX shells, awk), or a structure (C,
sort of),

This change adds a function that creates an object from a series of names,
values, and other objects, and a function that queries whether a particular
member is present. These are mostly-normal functions; there is no new syntax
introduced.

Background:

OpenSCAD has had an internal implementation of objects for several years,
added to support the textmetrics() and fontmetrics() functions, and later
import() of a JSON file. This existing mechanism includes mechanisms for
accessing the members of the object and for walking through the entries. It
does not include a mechanism for the user's program to create an object.

Given an object o, the current operations are:

o.name yields the value of the name member, where name must be an identifier
(alphabetic, numeric, underscore, starting with alphabetic or underscore).
This syntax is very "clean", but does not allow for names that are derived
from expressions or for names that are not suitable for use as identifiers. An
undefined name is not an error; it yields undefined.  
o[name] also yields the value of the name member, but name can be an any
string expression. This syntax is a bit more awkward than the o.name syntax,
but allows for dynamically-created names and for names that are not suitable
as identifiers. Again, and undefined name yields undefined.  
for (name = o) ... is the object equivalent of the vector for(...). It walks
the object, setting name to each member name in sequence. This mechanism is
usable as both a normal statement and as a list comprehension element. Note
that it yields only the name; the value is accessible as o[name]. Formally the
entries should be assumed to be in no specific order, but for aesthetic
reasons they are reported in the order they were added to the object.  
is_object(v) returns true if v is an object.  
echo(o) and str(o) produce textual representations of objects. (Note: the
textual form looks sort of like syntax, but is not legal OpenSCAD syntax. It
is likely to change in the future; see Future Directions below.)  
Details:

The object() function constructs a new object, processing each argument in
sequence from left to right, with later settings replacing earlier settings.
There are three variations of arguments; they can be mixed in any way.

A named parameter name=value  
Sets the specified name to the specified value. As with all named arguments to
functions, the name must be an identifier.  
a vector [ v1, v2, ... ]  
v1, v2, ... are each two- or one-element vectors  
[name, value]  
Sets the specified name to the specified value. The name can be any string
expression.  
[name]  
Removes the specified name from the object being accumulated. (Note that this
is subtly different from setting it to undefined, in that it will not be
reported for has_key() or when walking the names of the object.)  
an object o  
An object has each of its members copied into the new object.  
The values contained in an object can (of course) be of any data type:
numbers, strings, vectors, function references, objects, et cetera.

There is also a new function has_key(o, name) that returns true if the object
has a member with the specified name.  
Examples:

Create an object; access its members:  
o = object(a=1, b=2);  
echo(o.a, o["b"]);  
Create an object with varying names, and access them:  
names = [ "apple", "banana", "string bean" ];  
o = object([ for (name=names) [name, 123] ]);  
for (name=names) echo(name, o[name]);  
Create an object, then create modified copies of that object:  
// Ancient planets  
planets = object(mercury=1, venus=2, earth=3, mars=4, jupiter=5, saturn=6);  
planets1781 = object(planets, uranus=7); // Uranus discovered  
planets1846 = object(planets1781, neptune=8); // Neptune discovered  
planets1930 = object(planets1846, pluto=9); // Pluto discovered  
planets2006 = object(planets1930, [["pluto"]]); // Pluto un-planeted  
Check whether a member is present:  
echo(has_key(planets1846, "neptune")); // true  
echo(has_key(planets2006, "pluto")); // false  
Future Directions and Related Projects:

This is the second phase (after the textmetrics() work) of a longer-term plan
to introduce "object" features into OpenSCAD.

Object literals, object comprehension: OEP8a
<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>
adds a syntax for creating objects, including object comprehensions, roughly
modeled on JavaScript object syntax, so that { a: 1, b: 2 } is equivalent to
object(a=1, b=2). Changes echo() and str() to represent objects using this
syntax.

OEP8
<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References> further adds geometry as data and module
references.

No formal proposals:

Methods: If a function reference comes from an object or a vector, it should
see a special variable $this that refers to the containing object or vector.
Note that although there's no inheritance per se, making a modified copy of an
object is a lot like the prototype-based OO
<https://en.wikipedia.org/wiki/Prototype-based_programming>.

Variable parameter lists: a syntax for a parameter lists that says "return the
rest of the parameters in this variable", as a vector (for positional
arguments) or an object (for named arguments).

Spread syntax: a syntax for adding a vector to an argument list as positional
arguments, or adding an object to an argument list as named arguments.

Sets: Some kind of syntactic sugar to make it easy to create an object
containing boolean "true", to make it easy to define a set (in the
mathematical sense) and query whether particular items are present in it.

Questions:

What should these things be called?  
They're modeled on JavaScript objects, but to a Python person they look more
like dictionaries and to a C person they look more like structures.  
Are they really "objects", when they don't have OO features? See Future
Directions about methods.  
In OpenSCAD, doesn't "object" already mean a geometric figure?  
Credits / History:

I did the original textmetrics() work.  
Revar Desmera did the original implementation of object().  
Peter Kriens drove this final integration, cleaning up the implementation,
fixing a bug, and writing test cases.

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

♫ PARTY-TIME! ♬ ￼ \- Revar > On Jul 13, 2025, at 3:20 PM, Jordan Brown via
Discuss <discuss@lists.openscad.org> wrote: > > Quick summary: > > 2025.07.11
adds the the object() function, which creates an object (in the style returned
by textmetrics(), fontmetrics(), and import() of a JSON file). > It
accumulates the object by processing the arguments left to right, with later
settings for a particular member replacing earlier settings. > There are three
forms for an argument: > name=value - sets that name (a constant identifier)
to that value. > A vector with a list of [name, value] vectors, or [name] to
remove a member, where the names can be any string expression. > An object has
its members copied. > There is a new function has_key(obj, name) that returns
true if the object contains the named key. > These functions are currently
experimental and so must be enabled before you can use them. > Overview: > >
An "object" is a collection of names and associated values. In other languages
this data structure might be called an object (JavaScript), a dictionary
(Python), an associative array (some UNIX shells, awk), or a structure (C,
sort of), > > This change adds a function that creates an object from a series
of names, values, and other objects, and a function that queries whether a
particular member is present. These are mostly-normal functions; there is no
new syntax introduced. > > Background: > > OpenSCAD has had an internal
implementation of objects for several years, added to support the
textmetrics() and fontmetrics() functions, and later import() of a JSON file.
This existing mechanism includes mechanisms for accessing the members of the
object and for walking through the entries. It does not include a mechanism
for the user's program to create an object. > > Given an object o, the current
operations are: > > o.name yields the value of the name member, where name
must be an identifier (alphabetic, numeric, underscore, starting with
alphabetic or underscore). This syntax is very "clean", but does not allow for
names that are derived from expressions or for names that are not suitable for
use as identifiers. An undefined name is not an error; it yields undefined. >
o[name] also yields the value of the name member, but name can be an any
string expression. This syntax is a bit more awkward than the o.name syntax,
but allows for dynamically-created names and for names that are not suitable
as identifiers. Again, and undefined name yields undefined. > for (name = o)
... is the object equivalent of the vector for(...). It walks the object,
setting name to each member name in sequence. This mechanism is usable as both
a normal statement and as a list comprehension element. Note that it yields
only the name; the value is accessible as o[name]. Formally the entries should
be assumed to be in no specific order, but for aesthetic reasons they are
reported in the order they were added to the object. > is_object(v) returns
true if v is an object. > echo(o) and str(o) produce textual representations
of objects. (Note: the textual form looks sort of like syntax, but is not
legal OpenSCAD syntax. It is likely to change in the future; see Future
Directions below.) > Details: > > The object() function constructs a new
object, processing each argument in sequence from left to right, with later
settings replacing earlier settings. There are three variations of arguments;
they can be mixed in any way. > > A named parameter name=value > Sets the
specified name to the specified value. As with all named arguments to
functions, the name must be an identifier. > a vector [ v1, v2, ... ] > v1,
v2, ... are each two- or one-element vectors > [name, value] > Sets the
specified name to the specified value. The name can be any string expression.
> [name] > Removes the specified name from the object being accumulated. (Note
that this is subtly different from setting it to undefined, in that it will
not be reported for has_key() or when walking the names of the object.) > an
object o > An object has each of its members copied into the new object. > The
values contained in an object can (of course) be of any data type: numbers,
strings, vectors, function references, objects, et cetera. > > There is also a
new function has_key(o, name) that returns true if the object has a member
with the specified name. > Examples: > > Create an object; access its members:
> o = object(a=1, b=2); > echo(o.a, o["b"]); > Create an object with varying
names, and access them: > names = [ "apple", "banana", "string bean" ]; > o =
object([ for (name=names) [name, 123] ]); > for (name=names) echo(name,
o[name]); > Create an object, then create modified copies of that object: > //
Ancient planets > planets = object(mercury=1, venus=2, earth=3, mars=4,
jupiter=5, saturn=6); > planets1781 = object(planets, uranus=7); // Uranus
discovered > planets1846 = object(planets1781, neptune=8); // Neptune
discovered > planets1930 = object(planets1846, pluto=9); // Pluto discovered >
planets2006 = object(planets1930, [["pluto"]]); // Pluto un-planeted > Check
whether a member is present: > echo(has_key(planets1846, "neptune")); // true
> echo(has_key(planets2006, "pluto")); // false > Future Directions and
Related Projects: > > This is the second phase (after the textmetrics() work)
of a longer-term plan to introduce "object" features into OpenSCAD. > > Object
literals, object comprehension: OEP8a
<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>
adds a syntax for creating objects, including object comprehensions, roughly
modeled on JavaScript object syntax, so that { a: 1, b: 2 } is equivalent to
object(a=1, b=2). Changes echo() and str() to represent objects using this
syntax. > > OEP8
<https://github.com/openscad/openscad/wiki/OEP8%3A-Objects-%28dictionaries%3F%29%2C-Geometry-
as-data%2C-and-Module-References> further adds geometry as data and module
references. > > No formal proposals: > > Methods: If a function reference
comes from an object or a vector, it should see a special variable $this that
refers to the containing object or vector. Note that although there's no
inheritance per se, making a modified copy of an object is a lot like the
prototype-based OO <https://en.wikipedia.org/wiki/Prototype-
based_programming>. > > Variable parameter lists: a syntax for a parameter
lists that says "return the rest of the parameters in this variable", as a
vector (for positional arguments) or an object (for named arguments). > >
Spread syntax: a syntax for adding a vector to an argument list as positional
arguments, or adding an object to an argument list as named arguments. > >
Sets: Some kind of syntactic sugar to make it easy to create an object
containing boolean "true", to make it easy to define a set (in the
mathematical sense) and query whether particular items are present in it. > >
Questions: > > What should these things be called? > They're modeled on
JavaScript objects, but to a Python person they look more like dictionaries
and to a C person they look more like structures. > Are they really "objects",
when they don't have OO features? See Future Directions about methods. > In
OpenSCAD, doesn't "object" already mean a geometric figure? > Credits /
History: > > I did the original textmetrics() work. > Revar Desmera did the
original implementation of object(). > Peter Kriens drove this final
integration, cleaning up the implementation, fixing a bug, and writing test
cases. > _______________________________________________ > OpenSCAD mailing
list > To unsubscribe send an email to discuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/674702/200)
](https://lists.openscad.org/empathy/attachment/674702)

![](https://www.gravatar.com/avatar/d6de89c90e2e89a85dd10e6c3b5950e2?d=blank&s=100)

JB

Jon Bondy

Mon, Jul 14, 2025 11:55 AM

I would welcome a few simple examples, to get my feet wet. I used  
Pascal for decades, so I am, trying to map this new feature to what I am  
familiar with.

What I see looks like a table with named parameters for each row. I  
have used a similar technique using plain OpenSCAD for many years. I  
simply create a series of named vectors as a dictionary, select a  
specific vector at run-time, and then transfer the vector elements into  
local variables.

Jon

On 7/13/2025 6:44 PM, Jordan Brown via Discuss wrote:

____

Here's a program that I threw together that exercises the new object  
features.

It provides a framework for doing a general animation - at this time,  
do this, at that time, do that. For an example of doing that without  
a framework like this, look at  
<https://openscad.org/advent-calendar-2023/> at day 24.

Remember that this requires 2025.07.11. Zoom as desired.

// Best view is looking straight down at the origin.  
$vpr = [0,0,0];  
$vpt = [0,0,0];

// Demonstration animation. Use FPS=10 and steps=100.  
// Zoom as desired.

// This vector is a description of everything that happens  
// during the animation. You want a wide window to read it.  
// The only thing that's defined is "t", the timestamp for that  
// particular entry. The rest are up to your program.  
// For this animation:  
// pos1, pos2: the {red, green} stick man's position  
// arm1, arm2: the {red, green} stick man's arm angle  
// says1, says2: what the {red, green} stick man is saying  
timeline = [  
object(t=0, pos1=[-50,0,0], arm1=-30, says1="", pos2=[50,0], arm2=-30,
says2="" ),  
object(t=2.5, arm1=-30 ),  
object(t=3, arm1=50, says1="Hey, George!" ),  
object(t=3.5, arm1=-30 ),  
object(t=5, says1="" ),  
object(t=5.5, arm2=-30, ),  
object(t=6, arm2=50, says2="Hey, Fred!" ),  
object(t=6.5, arm2=-30 ),  
object(t=7, says2="" ),  
object(t=12, pos1=[-5,0,0], pos2=[5,0] ),  
object(t=13, says1="Can I go past?" ),  
object(t=14, says1="" ),  
object(t=15, says2="Sorry, no." ),  
object(t=16, says2="" ),  
object(t=17, says1="I hate living on a number line!" ),  
object(t=19, says1="" ),  
object(t=19.5, says2="Me too!" ),  
object(t=20.5, says2="" ),  
object(t=22, pos1=[-5,0,0], arm2=-30, says1="", pos2=[5,0], arm2=-30, says2=""
),  
];

// Now, create the current frame of the animation.

// Get the current values of all of the timeline columns.  
a = animate(timeline);  
// Using those values, create the model at this moment. There are two stick
men.  
translate(a.pos1) {  
color("red") stickman(a.says1, a.arm1);  
}  
translate(a.pos2) {  
color("green") stickman(a.says2, a.arm2);  
}

// Create a stick man, holding his arms at the specified angle and saying
what's specified.  
module stickman(says, arm) {  
square([1,8], center=true);  
translate([0,5]) circle(2);  
translate([0,2])  
rotate(arm)  
translate([0,-0.5])  
square([4,1]);  
translate([0,2])  
rotate(180-arm)  
translate([0,-0.5])  
square([4,1]);  
translate([0,-4])  
rotate(200)  
translate([-0.5,0])  
square([1,5]);  
translate([0,-4])  
rotate(160)  
translate([-0.5,0])  
square([1,5]);  
translate([0, 8]) text(says, halign="center", valign="baseline", size=3);  
}

// The rest is generic support for using a timeline like that.

// Extract one column from an animation timeline, extracting only  
// those entries where that column is present.  
function animate_extract(list, key) = [  
for (e = list) if (!is_undef(e[key])) [ e.t, e[key] ]  
];

// Get the duration of the timeline, the timestamp of the  
// last entry in the timeline.  
function animate_duration(list) = list[len(list)-1].t;

// Given $t, a timeline and a key, interpolate the current value  
// of the key.  
function animate_interpolate(list, key) =  
xlookup($t * animate_duration(list), animate_extract(list, key));

// Get a list of all keys used in the timeline.  
function animate_keys(list) =  
let (o = object(  
[  
for (e = list)  
for (k = e)  
[ k, true ]  
]  
))  
[ for (k = o) k ];

// Given $t and a timeline, return an aggregated object with the  
// current values of all of the columns of the timeline.  
function animate(timeline) =  
let(keys = animate_keys(timeline))  
object(  
[  
for (k = keys) [ k, animate_interpolate(timeline, k) ]  
]  
);

// lookup() on steroids. Given a value and a lookup-like list,  
// do the lookup and interpolation that lookup() does... but have  
// it also work for strings, booleans, and identical-length lists  
// of numbers.  
function xlookup(val, list) =  
is_num(list[0][1]) ? lookup(val, list)  
: is_string(list[0][1]) ? lookup_string(val, list)  
: is_bool(list[0][1]) ? lookup_bool(val, list)  
: is_list(list[0][1]) ? lookup_list(val, list)  
: assert(false, "don't know how to lookup that type");

// Given a value and a lookup list, return the index of the entry  
// before (or matching) the value.  
function lookup_prev(val, list) =  
let (tmp = [ for (i = [0:1:len(list)-1]) [ list[i][0], i ] ])  
floor(lookup(val, tmp));

//Given a value and a lookup list, return the index of the entry  
// after (or matching) the value.  
function lookup_next(val, list) =  
let (tmp = [ for (i = [0:1:len(list)-1]) [ list[i][0], i ] ])  
ceil(lookup(val, tmp));

// Given a value and a lookup list containing strings, return the  
// string before (or matching) the value.  
function lookup_string(val, list) = list[lookup_prev(val, list)][1];

// Given a value and a lookup list containing booleans, return the  
// boolean before (or matching) the value.  
function lookup_bool(val, list) = list[lookup_prev(val, list)][1];

// Given a value and a lookup list containing same-length lists of  
// numbers, interpolate values for the list. Note that because  
// lookup_prev() and lookup_next() return the same entry on an exact  
// match, and that leads to 0*0/0, that case has to be handled  
// specially.  
function lookup_list(val, list) =  
let(  
p = lookup_prev(val, list),  
n = lookup_next(val, list)  
)  
p == n  
? list[p][1]  
: list[p][1]  
\+ (list[n][1]-list[p][1])  
* (val - list[p][0]) / (list[n][0] - list[p][0]);

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

\--  
This email has been checked for viruses by AVG antivirus software.  
[www.avg.com](http://www.avg.com)

I would welcome a few simple examples, to get my feet wet. I used Pascal for
decades, so I am, trying to map this new feature to what I am familiar with.
What I see looks like a table with named parameters for each row. I have used
a similar technique using plain OpenSCAD for many years. I simply create a
series of named vectors as a dictionary, select a specific vector at run-time,
and then transfer the vector elements into local variables. Jon On 7/13/2025
6:44 PM, Jordan Brown via Discuss wrote: > Here's a program that I threw
together that exercises the new object > features. > > It provides a framework
for doing a general animation - at this time, > do this, at that time, do
that. For an example of doing that without > a framework like this, look at >
https://openscad.org/advent-calendar-2023/ at day 24. > > Remember that this
requires 2025.07.11. Zoom as desired. > > // Best view is looking straight
down at the origin. > $vpr = [0,0,0]; > $vpt = [0,0,0]; > > // Demonstration
animation. Use FPS=10 and steps=100. > // Zoom as desired. > > // This vector
is a description of everything that happens > // during the animation. You
want a wide window to read it. > // The only thing that's defined is "t", the
timestamp for that > // particular entry. The rest are up to your program. >
// For this animation: > // pos1, pos2: the {red, green} stick man's position
> // arm1, arm2: the {red, green} stick man's arm angle > // says1, says2:
what the {red, green} stick man is saying > timeline = [ > object(t=0,
pos1=[-50,0,0], arm1=-30, says1="", pos2=[50,0], arm2=-30, says2="" ), >
object(t=2.5, arm1=-30 ), > object(t=3, arm1=50, says1="Hey, George!" ), >
object(t=3.5, arm1=-30 ), > object(t=5, says1="" ), > object(t=5.5, arm2=-30,
), > object(t=6, arm2=50, says2="Hey, Fred!" ), > object(t=6.5, arm2=-30 ), >
object(t=7, says2="" ), > object(t=12, pos1=[-5,0,0], pos2=[5,0] ), >
object(t=13, says1="Can I go past?" ), > object(t=14, says1="" ), >
object(t=15, says2="Sorry, no." ), > object(t=16, says2="" ), > object(t=17,
says1="I hate living on a number line!" ), > object(t=19, says1="" ), >
object(t=19.5, says2="Me too!" ), > object(t=20.5, says2="" ), > object(t=22,
pos1=[-5,0,0], arm2=-30, says1="", pos2=[5,0], arm2=-30, says2="" ), > ]; > >
// Now, create the current frame of the animation. > > // Get the current
values of all of the timeline columns. > a = animate(timeline); > // Using
those values, create the model at this moment. There are two stick men. >
translate(a.pos1) { > color("red") stickman(a.says1, a.arm1); > } >
translate(a.pos2) { > color("green") stickman(a.says2, a.arm2); > } > > //
Create a stick man, holding his arms at the specified angle and saying what's
specified. > module stickman(says, arm) { > square([1,8], center=true); >
translate([0,5]) circle(2); > translate([0,2]) > rotate(arm) >
translate([0,-0.5]) > square([4,1]); > translate([0,2]) > rotate(180-arm) >
translate([0,-0.5]) > square([4,1]); > translate([0,-4]) > rotate(200) >
translate([-0.5,0]) > square([1,5]); > translate([0,-4]) > rotate(160) >
translate([-0.5,0]) > square([1,5]); > translate([0, 8]) text(says,
halign="center", valign="baseline", size=3); > } > > // The rest is generic
support for using a timeline like that. > > // Extract one column from an
animation timeline, extracting only > // those entries where that column is
present. > function animate_extract(list, key) = [ > for (e = list) if
(!is_undef(e[key])) [ e.t, e[key] ] > ]; > > // Get the duration of the
timeline, the timestamp of the > // last entry in the timeline. > function
animate_duration(list) = list[len(list)-1].t; > > // Given $t, a timeline and
a key, interpolate the current value > // of the key. > function
animate_interpolate(list, key) = > xlookup($t * animate_duration(list),
animate_extract(list, key)); > > // Get a list of all keys used in the
timeline. > function animate_keys(list) = > let (o = object( > [ > for (e =
list) > for (k = e) > [ k, true ] > ] > )) > [ for (k = o) k ]; > > // Given
$t and a timeline, return an aggregated object with the > // current values of
all of the columns of the timeline. > function animate(timeline) = > let(keys
= animate_keys(timeline)) > object( > [ > for (k = keys) [ k,
animate_interpolate(timeline, k) ] > ] > ); > > // lookup() on steroids. Given
a value and a lookup-like list, > // do the lookup and interpolation that
lookup() does... but have > // it also work for strings, booleans, and
identical-length lists > // of numbers. > function xlookup(val, list) = >
is_num(list[0][1]) ? lookup(val, list) > : is_string(list[0][1]) ?
lookup_string(val, list) > : is_bool(list[0][1]) ? lookup_bool(val, list) > :
is_list(list[0][1]) ? lookup_list(val, list) > : assert(false, "don't know how
to lookup that type"); > > // Given a value and a lookup list, return the
index of the entry > // before (or matching) the value. > function
lookup_prev(val, list) = > let (tmp = [ for (i = [0:1:len(list)-1]) [
list[i][0], i ] ]) > floor(lookup(val, tmp)); > > //Given a value and a lookup
list, return the index of the entry > // after (or matching) the value. >
function lookup_next(val, list) = > let (tmp = [ for (i = [0:1:len(list)-1]) [
list[i][0], i ] ]) > ceil(lookup(val, tmp)); > > // Given a value and a lookup
list containing strings, return the > // string before (or matching) the
value. > function lookup_string(val, list) = list[lookup_prev(val, list)][1];
> > // Given a value and a lookup list containing booleans, return the > //
boolean before (or matching) the value. > function lookup_bool(val, list) =
list[lookup_prev(val, list)][1]; > > // Given a value and a lookup list
containing same-length lists of > // numbers, interpolate values for the list.
Note that because > // lookup_prev() and lookup_next() return the same entry
on an exact > // match, and that leads to 0*0/0, that case has to be handled >
// specially. > function lookup_list(val, list) = > let( > p =
lookup_prev(val, list), > n = lookup_next(val, list) > ) > p == n > ?
list[p][1] > : list[p][1] > \+ (list[n][1]-list[p][1]) > * (val - list[p][0])
/ (list[n][0] - list[p][0]); > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email todiscuss-leave@lists.openscad.org \-- This email
has been checked for viruses by AVG antivirus software. www.avg.com

![](https://www.gravatar.com/avatar/a11af2fdbb73a5b23029ce3c1a94cade?d=blank&s=100)

PK

Peter Kriens

Mon, Jul 14, 2025 12:32 PM

I am working on an example in the build source code tree. I can share the
current incarnation. Feel free to comment, ask questions so I can elucidate
them, or provide suggestions.

//  
// examples with objects.  
//  
// Objects are immutable. Once an object is created, its values  
// can not be changed.

//  
// Construct a simple object  
//  
rectangle = object( w = 100, h= 20 );  
echo(rectangle); // { w = 100; h = 20; }

//  
// Access is via identifier  
//  
echo( rectangle.w, rectangle.h ); // 100, 20

//  
// Or access is via string key  
//  
echo( rectangle["w"], rectangle["h"] ); // 100, 20

//  
// You can test if a key is present  
//

echo( has_key(rectangle,"w"), has_key(rectangle,"y")); // true, false

//  
// You can use an object as a list of keys, where keys  
// are always strings. For example, you can use them include  
// in comprehension  
//  
values = [ for (k = rectangle) rectangle[k] ];  
echo( values ); // [100, 20]

//  
// To test if a parameter is an object, there is_bool  
// an is_object function:  
//

echo( is_object( rectangle )); // true  
echo( is_object( [] )); // false

//  
// You can use any type as value, key is  
// always a string.

echo( object( name = "OpenSCAD.object", array=[1,2], bool=false) );  
// { name = "OpenSCAD.object"; array = [1, 2]; bool = false; }

//  
// Create a new object based on another object  
//  
volume = object( rectangle, d=10);  
echo(volume); // { w = 100; h = 20; d = 10 }

//  
// If you replace a field, it will take its original  
// position  
//  
echo( object( volume, w=10) ); // { w = 10; h = 20; d = 10 }

//  
// You can copy from multiple objects. This will  
// be assigned in order, later objects override the early ones  
//  
echo( object(rectangle, volume) ); // { w = 100; h = 20; d = 10; }

//  
// Keys can also be created dynamically. For this reason  
// the object() function accepts a list with edit instructions.  
// An element in this list is either ["k"] for a delete  
// or ["k",v] for a new/override key.  
//

echo( object( rectangle, [ ["w"], ["h"]] )); // {}  
echo( object( [ ["w",10], ["h",10]] )); // { w = 10; h = 10; }  
echo( object( rectangle, [ ["z",20]])); // { w = 100; h = 20; z = 20; }

//  
// copy, deletes and set can be combined in one call.  
//  
echo( object( rectangle, [ ["z",20], ["w"]], h=10)); // { h = 10; z = 20; }

//  
// This works for large number of calculated entries  
//

entries = [for ( i = [1:10000] ) [ str("_",floor(i)), floor(i) ] ];  
large = object( entries );  
echo( large._3012 );

//  
// Functions. You can store functions in objects. However,  
// the function can not have access to the object's fields  
// due to OpenSCAD's architecture. To mimic object oriented  
// behavior, often a function that acts as context is  
// useful.  
//

function rect( w =0, h=0) = object( w=w, h=h, area = function() w*h );  
echo( rect(10,10).area()); // 100

____

On 14 Jul 2025, at 13:55, Jon Bondy via
Discuss[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

I would welcome a few simple examples, to get my feet wet. I used Pascal for
decades, so I am, trying to map this new feature to what I am familiar with.

What I see looks like a table with named parameters for each row. I have used
a similar technique using plain OpenSCAD for many years. I simply create a
series of named vectors as a dictionary, select a specific vector at run-time,
and then transfer the vector elements into local variables.

Jon

On 7/13/2025 6:44 PM, Jordan Brown via Discuss wrote:

____

Here's a program that I threw together that exercises the new object features.

It provides a framework for doing a general animation - at this time, do this,
at that time, do that. For an example of doing that without a framework like
this, look at <https://openscad.org/advent-calendar-2023/> at day 24.

Remember that this requires 2025.07.11. Zoom as desired.

// Best view is looking straight down at the origin.  
$vpr = [0,0,0];  
$vpt = [0,0,0];

// Demonstration animation. Use FPS=10 and steps=100.  
// Zoom as desired.

// This vector is a description of everything that happens  
// during the animation. You want a wide window to read it.  
// The only thing that's defined is "t", the timestamp for that  
// particular entry. The rest are up to your program.  
// For this animation:  
// pos1, pos2: the {red, green} stick man's position  
// arm1, arm2: the {red, green} stick man's arm angle  
// says1, says2: what the {red, green} stick man is saying  
timeline = [  
object(t=0, pos1=[-50,0,0], arm1=-30, says1="", pos2=[50,0], arm2=-30,
says2="" ),  
object(t=2.5, arm1=-30 ),  
object(t=3, arm1=50, says1="Hey, George!" ),  
object(t=3.5, arm1=-30 ),  
object(t=5, says1="" ),  
object(t=5.5, arm2=-30, ),  
object(t=6, arm2=50, says2="Hey, Fred!" ),  
object(t=6.5, arm2=-30 ),  
object(t=7, says2="" ),  
object(t=12, pos1=[-5,0,0], pos2=[5,0] ),  
object(t=13, says1="Can I go past?" ),  
object(t=14, says1="" ),  
object(t=15, says2="Sorry, no." ),  
object(t=16, says2="" ),  
object(t=17, says1="I hate living on a number line!" ),  
object(t=19, says1="" ),  
object(t=19.5, says2="Me too!" ),  
object(t=20.5, says2="" ),  
object(t=22, pos1=[-5,0,0], arm2=-30, says1="", pos2=[5,0], arm2=-30, says2=""
),  
];

// Now, create the current frame of the animation.

// Get the current values of all of the timeline columns.  
a = animate(timeline);  
// Using those values, create the model at this moment. There are two stick
men.  
translate(a.pos1) {  
color("red") stickman(a.says1, a.arm1);  
}  
translate(a.pos2) {  
color("green") stickman(a.says2, a.arm2);  
}

// Create a stick man, holding his arms at the specified angle and saying
what's specified.  
module stickman(says, arm) {  
square([1,8], center=true);  
translate([0,5]) circle(2);  
translate([0,2])  
rotate(arm)  
translate([0,-0.5])  
square([4,1]);  
translate([0,2])  
rotate(180-arm)  
translate([0,-0.5])  
square([4,1]);  
translate([0,-4])  
rotate(200)  
translate([-0.5,0])  
square([1,5]);  
translate([0,-4])  
rotate(160)  
translate([-0.5,0])  
square([1,5]);  
translate([0, 8]) text(says, halign="center", valign="baseline", size=3);  
}

// The rest is generic support for using a timeline like that.

// Extract one column from an animation timeline, extracting only  
// those entries where that column is present.  
function animate_extract(list, key) = [  
for (e = list) if (!is_undef(e[key])) [ e.t, e[key] ]  
];

// Get the duration of the timeline, the timestamp of the  
// last entry in the timeline.  
function animate_duration(list) = list[len(list)-1].t;

// Given $t, a timeline and a key, interpolate the current value  
// of the key.  
function animate_interpolate(list, key) =  
xlookup($t * animate_duration(list), animate_extract(list, key));

// Get a list of all keys used in the timeline.  
function animate_keys(list) =  
let (o = object(  
[  
for (e = list)  
for (k = e)  
[ k, true ]  
]  
))  
[ for (k = o) k ];

// Given $t and a timeline, return an aggregated object with the  
// current values of all of the columns of the timeline.  
function animate(timeline) =  
let(keys = animate_keys(timeline))  
object(  
[  
for (k = keys) [ k, animate_interpolate(timeline, k) ]  
]  
);

// lookup() on steroids. Given a value and a lookup-like list,  
// do the lookup and interpolation that lookup() does... but have  
// it also work for strings, booleans, and identical-length lists  
// of numbers.  
function xlookup(val, list) =  
is_num(list[0][1]) ? lookup(val, list)  
: is_string(list[0][1]) ? lookup_string(val, list)  
: is_bool(list[0][1]) ? lookup_bool(val, list)  
: is_list(list[0][1]) ? lookup_list(val, list)  
: assert(false, "don't know how to lookup that type");

// Given a value and a lookup list, return the index of the entry  
// before (or matching) the value.  
function lookup_prev(val, list) =  
let (tmp = [ for (i = [0:1:len(list)-1]) [ list[i][0], i ] ])  
floor(lookup(val, tmp));

//Given a value and a lookup list, return the index of the entry  
// after (or matching) the value.  
function lookup_next(val, list) =  
let (tmp = [ for (i = [0:1:len(list)-1]) [ list[i][0], i ] ])  
ceil(lookup(val, tmp));

// Given a value and a lookup list containing strings, return the  
// string before (or matching) the value.  
function lookup_string(val, list) = list[lookup_prev(val, list)][1];

// Given a value and a lookup list containing booleans, return the  
// boolean before (or matching) the value.  
function lookup_bool(val, list) = list[lookup_prev(val, list)][1];

// Given a value and a lookup list containing same-length lists of  
// numbers, interpolate values for the list. Note that because  
// lookup_prev() and lookup_next() return the same entry on an exact  
// match, and that leads to 0*0/0, that case has to be handled  
// specially.  
function lookup_list(val, list) =  
let(  
p = lookup_prev(val, list),  
n = lookup_next(val, list)  
)  
p == n  
? list[p][1]  
: list[p][1]  
\+ (list[n][1]-list[p][1])  
* (val - list[p][0]) / (list[n][0] - list[p][0]);

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)
[mailto:discuss-leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)

[http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient](http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient) Virus-free.www.avg.com
[http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient](http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient)
[x-msg://58/#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2](x-msg://58/#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2)_______________________________________________  
OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I am working on an example in the build source code tree. I can share the
current incarnation. Feel free to comment, ask questions so I can elucidate
them, or provide suggestions. // // examples with objects. // // Objects are
immutable. Once an object is created, its values // can not be changed. // //
Construct a simple object // rectangle = object( w = 100, h= 20 );
echo(rectangle); // { w = 100; h = 20; } // // Access is via identifier //
echo( rectangle.w, rectangle.h ); // 100, 20 // // Or access is via string key
// echo( rectangle["w"], rectangle["h"] ); // 100, 20 // // You can test if a
key is present // echo( has_key(rectangle,"w"), has_key(rectangle,"y")); //
true, false // // You can use an object as a list of keys, where keys // are
always strings. For example, you can use them include // in comprehension //
values = [ for (k = rectangle) rectangle[k] ]; echo( values ); // [100, 20] //
// To test if a parameter is an object, there is_bool // an is_object
function: // echo( is_object( rectangle )); // true echo( is_object( [] )); //
false // // You can use any type as value, key is // always a string. echo(
object( name = "OpenSCAD.object", array=[1,2], bool=false) ); // { name =
"OpenSCAD.object"; array = [1, 2]; bool = false; } // // Create a new object
based on another object // volume = object( rectangle, d=10); echo(volume); //
{ w = 100; h = 20; d = 10 } // // If you replace a field, it will take its
original // position // echo( object( volume, w=10) ); // { w = 10; h = 20; d
= 10 } // // You can copy from multiple objects. This will // be assigned in
order, later objects override the early ones // echo( object(rectangle,
volume) ); // { w = 100; h = 20; d = 10; } // // Keys can also be created
dynamically. For this reason // the object() function accepts a list with edit
instructions. // An element in this list is either ["k"] for a delete // or
["k",v] for a new/override key. // echo( object( rectangle, [ ["w"], ["h"]]
)); // {} echo( object( [ ["w",10], ["h",10]] )); // { w = 10; h = 10; } echo(
object( rectangle, [ ["z",20]])); // { w = 100; h = 20; z = 20; } // // copy,
deletes and set can be combined in one call. // echo( object( rectangle, [
["z",20], ["w"]], h=10)); // { h = 10; z = 20; } // // This works for large
number of calculated entries // entries = [for ( i = [1:10000] ) [
str("_",floor(i)), floor(i) ] ]; large = object( entries ); echo( large._3012
); // // Functions. You can store functions in objects. However, // the
function can not have access to the object's fields // due to OpenSCAD's
architecture. To mimic object oriented // behavior, often a function that acts
as context is // useful. // function rect( w =0, h=0) = object( w=w, h=h, area
= function() w*h ); echo( rect(10,10).area()); // 100 > On 14 Jul 2025, at
13:55, Jon Bondy via Discuss <discuss@lists.openscad.org> wrote: > > I would
welcome a few simple examples, to get my feet wet. I used Pascal for decades,
so I am, trying to map this new feature to what I am familiar with. > > What I
see looks like a table with named parameters for each row. I have used a
similar technique using plain OpenSCAD for many years. I simply create a
series of named vectors as a dictionary, select a specific vector at run-time,
and then transfer the vector elements into local variables. > > Jon > > > > On
7/13/2025 6:44 PM, Jordan Brown via Discuss wrote: >> Here's a program that I
threw together that exercises the new object features. >> >> It provides a
framework for doing a general animation - at this time, do this, at that time,
do that. For an example of doing that without a framework like this, look at
https://openscad.org/advent-calendar-2023/ at day 24. >> >> Remember that this
requires 2025.07.11. Zoom as desired. >> >> // Best view is looking straight
down at the origin. >> $vpr = [0,0,0]; >> $vpt = [0,0,0]; >> >> //
Demonstration animation. Use FPS=10 and steps=100. >> // Zoom as desired. >>
>> // This vector is a description of everything that happens >> // during the
animation. You want a wide window to read it. >> // The only thing that's
defined is "t", the timestamp for that >> // particular entry. The rest are up
to your program. >> // For this animation: >> // pos1, pos2: the {red, green}
stick man's position >> // arm1, arm2: the {red, green} stick man's arm angle
>> // says1, says2: what the {red, green} stick man is saying >> timeline = [
>> object(t=0, pos1=[-50,0,0], arm1=-30, says1="", pos2=[50,0], arm2=-30,
says2="" ), >> object(t=2.5, arm1=-30 ), >> object(t=3, arm1=50, says1="Hey,
George!" ), >> object(t=3.5, arm1=-30 ), >> object(t=5, says1="" ), >>
object(t=5.5, arm2=-30, ), >> object(t=6, arm2=50, says2="Hey, Fred!" ), >>
object(t=6.5, arm2=-30 ), >> object(t=7, says2="" ), >> object(t=12,
pos1=[-5,0,0], pos2=[5,0] ), >> object(t=13, says1="Can I go past?" ), >>
object(t=14, says1="" ), >> object(t=15, says2="Sorry, no." ), >> object(t=16,
says2="" ), >> object(t=17, says1="I hate living on a number line!" ), >>
object(t=19, says1="" ), >> object(t=19.5, says2="Me too!" ), >>
object(t=20.5, says2="" ), >> object(t=22, pos1=[-5,0,0], arm2=-30, says1="",
pos2=[5,0], arm2=-30, says2="" ), >> ]; >> >> // Now, create the current frame
of the animation. >> >> // Get the current values of all of the timeline
columns. >> a = animate(timeline); >> // Using those values, create the model
at this moment. There are two stick men. >> translate(a.pos1) { >>
color("red") stickman(a.says1, a.arm1); >> } >> translate(a.pos2) { >>
color("green") stickman(a.says2, a.arm2); >> } >> >> // Create a stick man,
holding his arms at the specified angle and saying what's specified. >> module
stickman(says, arm) { >> square([1,8], center=true); >> translate([0,5])
circle(2); >> translate([0,2]) >> rotate(arm) >> translate([0,-0.5]) >>
square([4,1]); >> translate([0,2]) >> rotate(180-arm) >> translate([0,-0.5])
>> square([4,1]); >> translate([0,-4]) >> rotate(200) >> translate([-0.5,0])
>> square([1,5]); >> translate([0,-4]) >> rotate(160) >> translate([-0.5,0])
>> square([1,5]); >> translate([0, 8]) text(says, halign="center",
valign="baseline", size=3); >> } >> >> // The rest is generic support for
using a timeline like that. >> >> // Extract one column from an animation
timeline, extracting only >> // those entries where that column is present. >>
function animate_extract(list, key) = [ >> for (e = list) if
(!is_undef(e[key])) [ e.t, e[key] ] >> ]; >> >> // Get the duration of the
timeline, the timestamp of the >> // last entry in the timeline. >> function
animate_duration(list) = list[len(list)-1].t; >> >> // Given $t, a timeline
and a key, interpolate the current value >> // of the key. >> function
animate_interpolate(list, key) = >> xlookup($t * animate_duration(list),
animate_extract(list, key)); >> >> // Get a list of all keys used in the
timeline. >> function animate_keys(list) = >> let (o = object( >> [ >> for (e
= list) >> for (k = e) >> [ k, true ] >> ] >> )) >> [ for (k = o) k ]; >> >>
// Given $t and a timeline, return an aggregated object with the >> // current
values of all of the columns of the timeline. >> function animate(timeline) =
>> let(keys = animate_keys(timeline)) >> object( >> [ >> for (k = keys) [ k,
animate_interpolate(timeline, k) ] >> ] >> ); >> >> // lookup() on steroids.
Given a value and a lookup-like list, >> // do the lookup and interpolation
that lookup() does... but have >> // it also work for strings, booleans, and
identical-length lists >> // of numbers. >> function xlookup(val, list) = >>
is_num(list[0][1]) ? lookup(val, list) >> : is_string(list[0][1]) ?
lookup_string(val, list) >> : is_bool(list[0][1]) ? lookup_bool(val, list) >>
: is_list(list[0][1]) ? lookup_list(val, list) >> : assert(false, "don't know
how to lookup that type"); >> >> // Given a value and a lookup list, return
the index of the entry >> // before (or matching) the value. >> function
lookup_prev(val, list) = >> let (tmp = [ for (i = [0:1:len(list)-1]) [
list[i][0], i ] ]) >> floor(lookup(val, tmp)); >> >> //Given a value and a
lookup list, return the index of the entry >> // after (or matching) the
value. >> function lookup_next(val, list) = >> let (tmp = [ for (i =
[0:1:len(list)-1]) [ list[i][0], i ] ]) >> ceil(lookup(val, tmp)); >> >> //
Given a value and a lookup list containing strings, return the >> // string
before (or matching) the value. >> function lookup_string(val, list) =
list[lookup_prev(val, list)][1]; >> >> // Given a value and a lookup list
containing booleans, return the >> // boolean before (or matching) the value.
>> function lookup_bool(val, list) = list[lookup_prev(val, list)][1]; >> >> //
Given a value and a lookup list containing same-length lists of >> // numbers,
interpolate values for the list. Note that because >> // lookup_prev() and
lookup_next() return the same entry on an exact >> // match, and that leads to
0*0/0, that case has to be handled >> // specially. >> function
lookup_list(val, list) = >> let( >> p = lookup_prev(val, list), >> n =
lookup_next(val, list) >> ) >> p == n >> ? list[p][1] >> : list[p][1] >> \+
(list[n][1]-list[p][1]) >> * (val - list[p][0]) / (list[n][0] - list[p][0]);
>> >> >> >> _______________________________________________ >> OpenSCAD
mailing list >> To unsubscribe send an email to discuss-
leave@lists.openscad.org <mailto:discuss-leave@lists.openscad.org> > >
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> Virus-free.www.avg.com
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient>
<x-msg://58/#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2>_______________________________________________
> OpenSCAD mailing list > To unsubscribe send an email to discuss-
leave@lists.openscad.org

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Mon, Jul 14, 2025 4:37 PM

On 7/14/2025 4:55 AM, Jon Bondy wrote:

____

I would welcome a few simple examples, to get my feet wet. I used  
Pascal for decades, so I am, trying to map this new feature to what I  
am familiar with.

It's been forty years since I wrote Pascal, so I'm a tad rusty... but  
Wikipedia to the rescue: it's roughly equivalent to a Pascal "record" -  
that is, a data structure with named elements, each of any type.

____

What I see looks like a table with named parameters for each row.

That is indeed the data structure that this example uses. Its big data  
structure is a vector (list, array, nothing new there) of objects  
(dictionaries, records, associative arrays), each of which has some  
number of named members.

____

I have used a similar technique using plain OpenSCAD for many years.  
I simply create a series of named vectors as a dictionary, select a  
specific vector at run-time, and then transfer the vector elements  
into local variables.

Before this addition, there are a number of techniques for creating a  
data structure with named elements. The most obvious is probably the  
vector-of-vectors approach that is one of the forms that object()  
accepts as an input:

    
    
    [[ "a", 1 ], [ "b", 2 ]].
    

Primarily, the difference is in how concise the representation is.  
Contrast:

    
    
    v = [ [ "a", 1 ], [ "b", 2 ] ];
    o = object(a=1, b=2);
    
    echo(find(v, "a"));
    echo(o.a);
    

and of course that difference multiplies as you build more complex data  
structures:

    
    
    vperson = [
        [
            "name", [
                [ "given", "Jordan" ],
                [ "family", "Brown" ]
            ]
        ],
        [
            "birth", [
                [ "year", 1961 ],
                [ "month", 7 ],
                [ "day", 26 ],
            ]
        ]
    ];
    operson = object(
        name = object(given = "Jordan", family="Brown"),
        birth = object(year=1961, month=7, day=26)
    );
    vbirthyear = find(find(vperson, "birth"), "year");
    obirthyear = operson.birth.year;
    

Some of that difference is of course in how I've chosen to lay out the  
two examples, but with four levels of brackets I feel a need for  
indentation to keep them straight.

Another approach is to use a vector with named elements, something like:

    
    
    NAME = 0;
    NAME_GIVEN = 0;
    NAME_FAMILY = 1;
    BIRTH = 1;
    BIRTH_YEAR = 0;
    BIRTH_MONTH = 1;
    BIRTH_DAY = 2;
    
    v2person = [ [ "Jordan", "Brown" ], [ 1961, 7, 26 ] ];
    v2birthyear = v2person[BIRTH][BIRTH_YEAR];
    

but then it's awkward to have the data be sparse (what if I only have a  
family name, no given name?), and construction is awkward because you  
have to make sure you mentioned all of the elements, in the right order.

Future: when and if we move forward with the next step, OEP8a  
<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>,  
this form becomes available:

    
    
    operson = {
        name: { first: "Jordan", last:"Brown" },
        birth: { year: 1961, month: 7, day: 26}
    };
    

On 7/14/2025 4:55 AM, Jon Bondy wrote: > > I would welcome a few simple
examples, to get my feet wet. I used > Pascal for decades, so I am, trying to
map this new feature to what I > am familiar with. > It's been forty years
since I wrote Pascal, so I'm a tad rusty... but Wikipedia to the rescue: it's
roughly equivalent to a Pascal "record" - that is, a data structure with named
elements, each of any type. > What I see looks like a table with named
parameters for each row. > That is indeed the data structure that this example
uses. Its big data structure is a vector (list, array, nothing new there) of
objects (dictionaries, records, associative arrays), each of which has some
number of named members. > I have used a similar technique using plain
OpenSCAD for many years. > I simply create a series of named vectors as a
dictionary, select a > specific vector at run-time, and then transfer the
vector elements > into local variables. > Before this addition, there are a
number of techniques for creating a data structure with named elements. The
most obvious is probably the vector-of-vectors approach that is one of the
forms that object() accepts as an input: [[ "a", 1 ], [ "b", 2 ]]. Primarily,
the difference is in how concise the representation is. Contrast: v = [ [ "a",
1 ], [ "b", 2 ] ]; o = object(a=1, b=2); echo(find(v, "a")); echo(o.a); and of
course that difference multiplies as you build more complex data structures:
vperson = [ [ "name", [ [ "given", "Jordan" ], [ "family", "Brown" ] ] ], [
"birth", [ [ "year", 1961 ], [ "month", 7 ], [ "day", 26 ], ] ] ]; operson =
object( name = object(given = "Jordan", family="Brown"), birth =
object(year=1961, month=7, day=26) ); vbirthyear = find(find(vperson,
"birth"), "year"); obirthyear = operson.birth.year; Some of that difference is
of course in how I've chosen to lay out the two examples, but with four levels
of brackets I feel a need for indentation to keep them straight. Another
approach is to use a vector with named elements, something like: NAME = 0;
NAME_GIVEN = 0; NAME_FAMILY = 1; BIRTH = 1; BIRTH_YEAR = 0; BIRTH_MONTH = 1;
BIRTH_DAY = 2; v2person = [ [ "Jordan", "Brown" ], [ 1961, 7, 26 ] ];
v2birthyear = v2person[BIRTH][BIRTH_YEAR]; but then it's awkward to have the
data be sparse (what if I only have a family name, no given name?), and
construction is awkward because you have to make sure you mentioned all of the
elements, in the right order. Future: when and if we move forward with the
next step, OEP8a
<https://github.com/openscad/openscad/wiki/OEP8a:--Objects-(dictionaries%3F)>,
this form becomes available: operson = { name: { first: "Jordan", last:"Brown"
}, birth: { year: 1961, month: 7, day: 26} };

[Next
page](https://lists.openscad.org/empathy/thread/XTRTBQHJ27ISVDLYG2BBQ5D4BGHBDICN?page=2)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

