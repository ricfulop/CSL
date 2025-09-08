---
url: https://lists.openscad.org/empathy/thread/IYHWMISYOLPWRQXEL4SVWZGJHEXKVTBC
scraped_at: 2025-09-08T16:28:31.749772
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

###  Re: New feature in 2025.07.11: the object() function

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Fri, Aug 15, 2025 3:07 AM

____

Also as someone else noted the task of rewriting to use the new

feature is

____

a big one and not backwards compatible (except in the case of changes

that

____

are entirely internal).

I'd like to pick out an example: VNFs.

"(VNF) holds the data used by polyhedron() to construct objects: a  
vertex list and a list of faces."

So currently it's a 2-element list, we have functions:

function vnf_vertices(vnf) = vnf[0];  
function vnf_faces(vnf) = vnf[1];

What if numerical indices of an object were instead the fields of an  
object in the order they're given? Then you could change the following  
line (which is creating a vnf right now)

[face, [faceidxs]]

with

new_vnf(face,faceidxs)

and all user code would continue working (provided new_vnf() calls  
object appropriately) in between that's referencing by index.

Numbers aren't valid identifiers anyway, so you aren't losing much  
besides having keys be numerical.

Then, all receiver functions can have a cast_to_vnf(maybe_vnf) =  
is_object(maybe_vnf,... what defines vnf class?...) || assert(...)  
new_vnf(maybe_vnf[0],maybe_vnf[1]);

Then in some years it can be ripped out or use an option flags to skip  
check efficiently?

====================

____

An object has each of its members copied into the new object.

I assume this is done for efficiency and implementation reasons, but  
this precludes having OO inheritance and makes it much more of a  
`record` than an `object`.

====================

____

Methods: If a function reference comes from an object or a vector, it  
should see a special variable $this that refers to the containing object  
or vector.

All other "special" $-variables are dynamically scoped. I do not think  
the dollar sign should be used, as this is statically scoped. These  
methods would all be new, so having the an implicit local variable  
`this` should be backward-compatible (just like I can override `circle`  
today).

> Also as someone else noted the task of rewriting to use the new feature is >
> a big one and not backwards compatible (except in the case of changes that >
> are entirely internal). I'd like to pick out an example: VNFs. "(VNF) holds
> the data used by polyhedron() to construct objects: a vertex list and a list
> of faces." So currently it's a 2-element list, we have functions: function
> vnf_vertices(vnf) = vnf[0]; function vnf_faces(vnf) = vnf[1]; What if
> numerical indices of an object were instead the fields of an object in the
> order they're given? Then you could change the following line (which is
> creating a vnf right now) [face, [faceidxs]] with new_vnf(face,faceidxs) and
> all user code would continue working (provided new_vnf() calls object
> appropriately) in between that's referencing by index. Numbers aren't valid
> identifiers anyway, so you aren't losing much besides having keys be
> numerical. Then, all receiver functions can have a cast_to_vnf(maybe_vnf) =
> is_object(maybe_vnf,... what defines vnf class?...) || assert(...)
> new_vnf(maybe_vnf[0],maybe_vnf[1]); Then in some years it can be ripped out
> or use an option flags to skip check efficiently? ==================== > An
> object has each of its members copied into the new object. I assume this is
> done for efficiency and implementation reasons, but this precludes having OO
> inheritance and makes it much more of a `record` than an `object`.
> ==================== >Methods: If a function reference comes from an object
> or a vector, it > should see a special variable $this that refers to the
> containing object > or vector. All other "special" $-variables are
> dynamically scoped. I do not think the dollar sign should be used, as this
> is statically scoped. These methods would all be new, so having the an
> implicit local variable `this` should be backward-compatible (just like I
> can override `circle` today).

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Fri, Aug 15, 2025 6:13 AM

On 8/15/2025 5:07 AM, Cory Cross via Discuss wrote:

____

What if numerical indices of an object were instead the fields of an  
object in the order they're given?

I'm not really comfortable with that, but I can't really articulate  
why. I think of objects as unordered; I made them have some order only  
because I didn't like the presentation when echo() displayed them in  
random order. But once it has an order, I can't articulate why we  
shouldn't document and use that order.

____

Numbers aren't valid identifiers anyway, so you aren't losing much  
besides having keys be numerical.

I'd like objects to allow non-string keys in the future.

____

____

An object has each of its members copied into the new object.

I assume this is done for efficiency and implementation reasons, but  
this precludes having OO inheritance and makes it much more of a  
`record` than an `object`.

As they are immutable, you can't tell the difference.

There's more than one style of OO inheritance. What we've got here is  
more like the JavaScript "prototype object" style of inheritance: you  
can take an object that you like, and make a modified copy of it.

____

____

Methods: If a function reference comes from an object or a vector, it  
should see a special variable $this that refers to the containing

object

____

or vector.

All other "special" $-variables are dynamically scoped. I do not think  
the dollar sign should be used, as this is statically scoped. These  
methods would all be new, so having the an implicit local variable  
`this` should be backward-compatible (just like I can override  
`circle` today).

Check out the discussion in PR#6022. Neither has exactly the right  
scope, and there are some tricky cases.

On 8/15/2025 5:07 AM, Cory Cross via Discuss wrote: > What if numerical
indices of an object were instead the fields of an > object in the order
they're given? I'm not really comfortable with that, but I can't really
articulate why. I think of objects as unordered; I made them have some order
only because I didn't like the presentation when echo() displayed them in
random order. But once it has an order, I can't articulate why we shouldn't
document and use that order. > Numbers aren't valid identifiers anyway, so you
aren't losing much > besides having keys be numerical. I'd like objects to
allow non-string keys in the future. > > An object has each of its members
copied into the new object. > > I assume this is done for efficiency and
implementation reasons, but > this precludes having OO inheritance and makes
it much more of a > `record` than an `object`. As they are immutable, you
can't tell the difference. There's more than one style of OO inheritance. What
we've got here is more like the JavaScript "prototype object" style of
inheritance: you can take an object that you like, and make a modified copy of
it. > >Methods: If a function reference comes from an object or a vector, it >
> should see a special variable $this that refers to the containing > object >
> or vector. > > All other "special" $-variables are dynamically scoped. I do
not think > the dollar sign should be used, as this is statically scoped.
These > methods would all be new, so having the an implicit local variable >
`this` should be backward-compatible (just like I can override > `circle`
today). Check out the discussion in PR#6022. Neither has exactly the right
scope, and there are some tricky cases.

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Fri, Aug 15, 2025 8:22 AM

On 8/14/25 11:13 PM, Jordan Brown via Discuss wrote:

____

On 8/15/2025 5:07 AM, Cory Cross via Discuss wrote:

____

Numbers aren't valid identifiers anyway, so you aren't losing much  
besides having keys be numerical.

I'd like objects to allow non-string keys in the future.

Hmm, I think it'd actually be simple to use as needed:

function wrap_keys(obj) =  
let ( keys = list(for(k=obj) k),  
key_vec = list(for(i=0:len(keys)-1) { [i, obj[keys[i]]] })  
) object(key_vec,obj);

... or something close to that.

____

____

____

An object has each of its members copied into the new object.

I assume this is done for efficiency and implementation reasons, but  
this precludes having OO inheritance and makes it much more of a  
`record` than an `object`.

As they are immutable, you can't tell the difference.

There's more than one style of OO inheritance. What we've got here is  
more like the JavaScript "prototype object" style of inheritance: you  
can take an object that you like, and make a modified copy of it.

The difference is you can't have super, which ECMAScript does have.

On 8/14/25 11:13 PM, Jordan Brown via Discuss wrote: > On 8/15/2025 5:07 AM,
Cory Cross via Discuss wrote: >> Numbers aren't valid identifiers anyway, so
you aren't losing much >> besides having keys be numerical. > > I'd like
objects to allow non-string keys in the future. Hmm, I think it'd actually be
simple to use as needed: function wrap_keys(obj) = let ( keys =
list(for(k=obj) k), key_vec = list(for(i=0:len(keys)-1) { [i, obj[keys[i]]] })
) object(key_vec,obj); ... or something close to that. >> > An object has each
of its members copied into the new object. >> >> I assume this is done for
efficiency and implementation reasons, but >> this precludes having OO
inheritance and makes it much more of a >> `record` than an `object`. > > > As
they are immutable, you can't tell the difference. > > There's more than one
style of OO inheritance. What we've got here is > more like the JavaScript
"prototype object" style of inheritance: you > can take an object that you
like, and make a modified copy of it. The difference is you can't have super,
which ECMAScript does have.

![](https://www.gravatar.com/avatar/a11af2fdbb73a5b23029ce3c1a94cade?d=blank&s=100)

PK

Peter Kriens

Fri, Aug 15, 2025 8:45 AM

____

On 15 Aug 2025, at 08:13, Jordan Brown via
Discuss[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:  
On 8/15/2025 5:07 AM, Cory Cross via Discuss wrote:

____

What if numerical indices of an object were instead the fields of an object in
the order they're given?

I'm not really comfortable with that, but I can't really articulate why. I
think of objects as unordered; I made them have some order only because I
didn't like the presentation when echo() displayed them in random order. But
once it has an order, I can't articulate why we shouldn't document and use
that order.

In my experience an extremely well defined order is paramount. Without a
defined order we could not even run our tests since it checks the output of
echo, which uses that order.

I ran an open source project for building Java/OSGi tools. We learned the hard
way that the random ordering of hash maps cause many problems, primary in
repeatable builds.

I think it makes perfect sense to support object[n] when n is an integer it
uses it as an index.

____

____

Numbers aren't valid identifiers anyway, so you aren't losing much besides
having keys be numerical.

I'd like objects to allow non-string keys in the future.

I think you want way too much here :-) That would be a map and that is in my
mind a very different beast then an object.

Our 'object' is what a struct or record is in most languages. It has field
names that are known to the code, it is a type. In a map you have a mapping
from one value to another, which is fundamentally different. A map requires
customization for the key types because for performance you need to define a
search algorithm like hashing or ordered so you likely have several different
map types. You probably also will need counting maps, ordered maps, sorted
maps, etc. I fail to see why this should be a standard feature of core
OpenSCAD like `object()`, this is user space stuff.

The `object()` feature wil make this more straightforward to implement but we
should imho not confuse `object()` with a general map. It is basically a
record/struct and there is imho no reason not to index it by an integer.
Especially if this makes porting easier.

____

____

____

An object has each of its members copied into the new object.

I assume this is done for efficiency and implementation reasons, but this
precludes having OO inheritance and makes it much more of a `record` than an
`object`.

As they are immutable, you can't tell the difference.

There's more than one style of OO inheritance. What we've got here is more
like the JavaScript "prototype object" style of inheritance: you can take an
object that you like, and make a modified copy of it.

____

____

____

Methods: If a function reference comes from an object or a vector, it  
should see a special variable $this that refers to the containing object  
or vector.

All other "special" $-variables are dynamically scoped. I do not think the
dollar sign should be used, as this is statically scoped. These methods would
all be new, so having the an implicit local variable `this` should be
backward-compatible (just like I can override `circle` today).

Check out the discussion in PR#6022. Neither has exactly the right scope, and
there are some tricky cases.

____

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

> On 15 Aug 2025, at 08:13, Jordan Brown via Discuss
> <discuss@lists.openscad.org> wrote: > On 8/15/2025 5:07 AM, Cory Cross via
> Discuss wrote: >> What if numerical indices of an object were instead the
> fields of an object in the order they're given? > I'm not really comfortable
> with that, but I can't really articulate why. I think of objects as
> unordered; I made them have some order only because I didn't like the
> presentation when echo() displayed them in random order. But once it has an
> order, I can't articulate why we shouldn't document and use that order. > In
> my experience an extremely well defined order is paramount. Without a
> defined order we could not even run our tests since it checks the output of
> echo, which uses that order. I ran an open source project for building
> Java/OSGi tools. We learned the hard way that the random ordering of hash
> maps cause many problems, primary in repeatable builds. I think it makes
> perfect sense to support object[n] when n is an integer it uses it as an
> index. > >> Numbers aren't valid identifiers anyway, so you aren't losing
> much besides having keys be numerical. > I'd like objects to allow non-
> string keys in the future. > I think you want way too much here :-) That
> would be a map and that is in my mind a very different beast then an object.
> Our 'object' is what a struct or record is in most languages. It has field
> names that are known to the code, it is a type. In a map you have a mapping
> from one value to another, which is fundamentally different. A map requires
> customization for the key types because for performance you need to define a
> search algorithm like hashing or ordered so you likely have several
> different map types. You probably also will need counting maps, ordered
> maps, sorted maps, etc. I fail to see why this should be a standard feature
> of core OpenSCAD like `object()`, this is user space stuff. The `object()`
> feature wil make this more straightforward to implement but we should imho
> not confuse `object()` with a general map. It is basically a record/struct
> and there is imho no reason not to index it by an integer. Especially if
> this makes porting easier. >> > An object has each of its members copied
> into the new object. >> >> I assume this is done for efficiency and
> implementation reasons, but this precludes having OO inheritance and makes
> it much more of a `record` than an `object`. > As they are immutable, you
> can't tell the difference. > > There's more than one style of OO
> inheritance. What we've got here is more like the JavaScript "prototype
> object" style of inheritance: you can take an object that you like, and make
> a modified copy of it. > >> >Methods: If a function reference comes from an
> object or a vector, it >> > should see a special variable $this that refers
> to the containing object >> > or vector. >> >> All other "special"
> $-variables are dynamically scoped. I do not think the dollar sign should be
> used, as this is statically scoped. These methods would all be new, so
> having the an implicit local variable `this` should be backward-compatible
> (just like I can override `circle` today). > Check out the discussion in
> PR#6022. Neither has exactly the right scope, and there are some tricky
> cases. > > _______________________________________________ > OpenSCAD
> mailing list > To unsubscribe send an email to discuss-
> leave@lists.openscad.org

![](https://www.gravatar.com/avatar/bde43989ab37e57b5130f321dd4c6ddf?d=blank&s=100)

JO

jjvb-openscad@bassklampfe.de

Fri, Aug 15, 2025 9:50 AM

Am 15.08.25 um 10:45 schrieb Peter Kriens via Discuss:

____

In my experience an extremely well defined order is paramount. Without  
a defined order we could not even run our tests since it checks the  
output of echo, which uses that order.

I ran an open source project for building Java/OSGi tools. We learned  
the hard way that the random ordering of hash maps cause many  
problems, primary in repeatable builds.

I was part of a big software project, which used Lua as main language.

In Lua there ist no difference between hashmap and array, both are just  
tables (you can even intermix them).  
And – YES - iterating over the key/value pairs using the pairs function  
will give you random order. But it is very (!) performant.

And if you really need stable iteration, you can always (at the cost of  
speed)

  * get all keys from the table
  * sort the keys (by any criteria you need)
  * iterate over the keys and fetch the values.

We also use this for data serialisation, so even if the key order in the  
table is random, saved settings etc are always stable.

We never had issues, neither in automatic test runs nor in repeatable  
builds (getting bitidentical builds by commit id is essential in  
embedded software for industrial use!)

Jm2C

Am 15.08.25 um 10:45 schrieb Peter Kriens via Discuss: > In my experience an
extremely well defined order is paramount. Without > a defined order we could
not even run our tests since it checks the > output of echo, which uses that
order. > > I ran an open source project for building Java/OSGi tools. We
learned > the hard way that the random ordering of hash maps cause many >
problems, primary in repeatable builds. I was part of a big software project,
which used Lua as main language. In Lua there ist no difference between
hashmap and array, both are just tables (you can even intermix them). And –
YES - iterating over the key/value pairs using the pairs function will give
you random order. But it is very (!) performant. And if you really need stable
iteration, you can always (at the cost of speed) \- get all keys from the
table \- sort the keys (by any criteria you need) \- iterate over the keys and
fetch the values. We also use this for data serialisation, so even if the key
order in the table is random, saved settings etc are always stable. We never
had issues, neither in automatic test runs nor in repeatable builds (getting
bitidentical builds by commit id is essential in embedded software for
industrial use!) Jm2C

![](https://www.gravatar.com/avatar/a11af2fdbb73a5b23029ce3c1a94cade?d=blank&s=100)

PK

Peter Kriens

Fri, Aug 15, 2025 10:18 AM

____

On 15 Aug 2025, at 11:50, jjvbhh via
Discuss[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

Am 15.08.25 um 10:45 schrieb Peter Kriens via Discuss:

____

In my experience an extremely well defined order is paramount. Without a
defined order we could not even run our tests since it checks the output of
echo, which uses that order.

I ran an open source project for building Java/OSGi tools. We learned the hard
way that the random ordering of hash maps cause many problems, primary in
repeatable builds.

I was part of a big software project, which used Lua as main language.

In Lua there ist no difference between hashmap and array, both are just tables
(you can even intermix them).  
And – YES - iterating over the key/value pairs using the pairs function will
give you random order. But it is very (!) performant.

We currently have an implementation with a hash map[key,index] and keep the
values in a vector. We only add one index operation in a vector for a [key]
operation. Totally negligible. I ran a profile on some BOSL2 code ... believe
me this will NEVER show up in the top 10.000 even with a 100k members.

____

And if you really need stable iteration, you can always (at the cost of speed)

  * get all keys from the table
  * sort the keys (by any criteria you need)
  * iterate over the keys and fetch the values.   
We also use this for data serialisation, so even if the key order in the table
is random, saved settings etc are always stable.

True, but wouldn't it be nicer if they ALWAYS had a consistent ordering? Your
approach sounds very error prone? Why run the risk?

We had to change our code in hundreds of places. Fortunately, Java has the
LinkedHashMap that provides ordering and is API compatible with HashMap but it
was a huge pain in the ass because it turned out a lot of low level code could
introduce random orderings that would only show up much later in the results.

BTW, Sorting would imho be wrong for this purpose. We looked at sorting
because then we could use binary search. We decided on insertion order because
then then the user can order as they please. Only dilemma was when you copy an
object and find the name already exists. In this case the first one wins and
reuse its position.

____

We never had issues, neither in automatic test runs nor in repeatable builds
(getting bitidentical builds by commit id is essential in embedded software
for industrial use!)

I know!

    
    
    Peter Kriens
    

____

Jm2C

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

> On 15 Aug 2025, at 11:50, jjvbhh via Discuss <discuss@lists.openscad.org>
> wrote: > > Am 15.08.25 um 10:45 schrieb Peter Kriens via Discuss: >> In my
> experience an extremely well defined order is paramount. Without a defined
> order we could not even run our tests since it checks the output of echo,
> which uses that order. >> >> I ran an open source project for building
> Java/OSGi tools. We learned the hard way that the random ordering of hash
> maps cause many problems, primary in repeatable builds. > > I was part of a
> big software project, which used Lua as main language. > > In Lua there ist
> no difference between hashmap and array, both are just tables (you can even
> intermix them). > And – YES - iterating over the key/value pairs using the
> pairs function will give you random order. But it is very (!) performant. We
> currently have an implementation with a hash map[key,index] and keep the
> values in a vector. We only add one index operation in a vector for a [key]
> operation. Totally negligible. I ran a profile on some BOSL2 code ...
> believe me this will NEVER show up in the top 10.000 even with a 100k
> members. > And if you really need stable iteration, you can always (at the
> cost of speed) > \- get all keys from the table > \- sort the keys (by any
> criteria you need) > \- iterate over the keys and fetch the values. > We
> also use this for data serialisation, so even if the key order in the table
> is random, saved settings etc are always stable. > True, but wouldn't it be
> nicer if they ALWAYS had a consistent ordering? Your approach sounds very
> error prone? Why run the risk? We had to change our code in hundreds of
> places. Fortunately, Java has the LinkedHashMap that provides ordering and
> is API compatible with HashMap but it was a huge pain in the ass because it
> turned out a lot of low level code could introduce random orderings that
> would only show up much later in the results. BTW, Sorting would imho be
> wrong for this purpose. We looked at sorting because then we could use
> binary search. We decided on insertion order because then then the user can
> order as they please. Only dilemma was when you copy an object and find the
> name already exists. In this case the first one wins and reuse its position.
> > We never had issues, neither in automatic test runs nor in repeatable
> builds (getting bitidentical builds by commit id is essential in embedded
> software for industrial use!) I know! Peter Kriens > > Jm2C >
> _______________________________________________ > OpenSCAD mailing list > To
> unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Fri, Aug 15, 2025 5:27 PM

____

____

There's more than one style of OO inheritance. What we've got here  
is more like the JavaScript "prototype object" style of inheritance:  
you can take an object that you like, and make a modified copy of it.

The difference is you can't have super, which ECMAScript does have.

I'm afraid my ES/JS experience, though pretty extensive, is for  
work-legacy reasons primarily with a 2006-ish version of JS. At that  
point it didn't have a `super`, but you could carefully build something  
that more or less worked. Have they added a real one?

But yes, that's a concern. See the comment I just added to PR#6022.

A key question is just how far down the rabbit hole we want to go. Do  
we want to turn OpenSCAD into a full-scale OO environment? Can we even  
do that without losing its appeal to beginners? There's already an  
avenue for that, if you're willing to accept the security issues:  
PythonSCAD. Language design and implementation is kind of fun, but is  
reinventing the wheel, usually poorly.

I have some ideas for `super`, but the rabbit hole keeps getting deeper...

>> There's more than one style of OO inheritance. What we've got here >> is
more like the JavaScript "prototype object" style of inheritance: >> you can
take an object that you like, and make a modified copy of it. > The difference
is you can't have super, which ECMAScript does have. I'm afraid my ES/JS
experience, though pretty extensive, is for work-legacy reasons primarily with
a 2006-ish version of JS. At that point it didn't have a `super`, but you
could carefully build something that more or less worked. Have they added a
real one? But yes, that's a concern. See the comment I just added to PR#6022.
A key question is just how far down the rabbit hole we want to go. Do we want
to turn OpenSCAD into a full-scale OO environment? Can we even do that without
losing its appeal to beginners? There's already an avenue for that, if you're
willing to accept the security issues: PythonSCAD. Language design and
implementation is kind of fun, but is reinventing the wheel, usually poorly. I
have some ideas for `super`, but the rabbit hole keeps getting deeper...

![](https://www.gravatar.com/avatar/63a0c2c7be96f2acab6aa0ba54bb1357?d=blank&s=100)

GS

Guenther Sohler

Fri, Aug 15, 2025 5:44 PM

Nope i disagree Here.  
PythonSCAD is Not reinventing the wheel, its a Mix of leveraging existing  
Technology, Bridging 2 worlds(Python and Scad are very interlinked) and  
Quite some offering Features which openscad Refuse to have for Ages

Jordan Brown via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) schrieb am
Fr., 15.  
Aug. 2025, 19:28:

____

There's more than one style of OO inheritance. What we've got here is  
more like the JavaScript "prototype object" style of inheritance: you can  
take an object that you like, and make a modified copy of it.

The difference is you can't have super, which ECMAScript does have.

I'm afraid my ES/JS experience, though pretty extensive, is for  
work-legacy reasons primarily with a 2006-ish version of JS. At that point  
it didn't have a `super`, but you could carefully build something that more  
or less worked. Have they added a real one?

But yes, that's a concern. See the comment I just added to PR#6022.

A key question is just how far down the rabbit hole we want to go. Do we  
want to turn OpenSCAD into a full-scale OO environment? Can we even do  
that without losing its appeal to beginners? There's already an avenue for  
that, if you're willing to accept the security issues: PythonSCAD.  
Language design and implementation is kind of fun, but is reinventing the  
wheel, usually poorly.

I have some ideas for `super`, but the rabbit hole keeps getting deeper...

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Nope i disagree Here. PythonSCAD is Not reinventing the wheel, its a Mix of
leveraging existing Technology, Bridging 2 worlds(Python and Scad are very
interlinked) and Quite some offering Features which openscad Refuse to have
for Ages Jordan Brown via Discuss <discuss@lists.openscad.org> schrieb am Fr.,
15. Aug. 2025, 19:28: > There's more than one style of OO inheritance. What
we've got here is > more like the JavaScript "prototype object" style of
inheritance: you can > take an object that you like, and make a modified copy
of it. > > The difference is you can't have super, which ECMAScript does have.
> > I'm afraid my ES/JS experience, though pretty extensive, is for > work-
legacy reasons primarily with a 2006-ish version of JS. At that point > it
didn't have a `super`, but you could carefully build something that more > or
less worked. Have they added a real one? > > But yes, that's a concern. See
the comment I just added to PR#6022. > > A key question is just how far down
the rabbit hole we want to go. Do we > want to turn OpenSCAD into a full-scale
OO environment? Can we even do > that without losing its appeal to beginners?
There's already an avenue for > that, if you're willing to accept the security
issues: PythonSCAD. > Language design and implementation is kind of fun, but
is reinventing the > wheel, usually poorly. > > I have some ideas for `super`,
but the rabbit hole keeps getting deeper... > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Fri, Aug 15, 2025 5:47 PM

On 8/15/25 10:44 AM, Guenther Sohler via Discuss wrote:

____

Nope i disagree Here.  
PythonSCAD is Not reinventing the wheel, its a Mix of leveraging existing  
Technology, Bridging 2 worlds(Python and Scad are very interlinked) and  
Quite some offering Features which openscad Refuse to have for Ages

I think you misread Jordan; he's saying adding too much OO stuff to the  
OpenSCAD language is reinventing the wheel, and suggests PythonSCAD is  
the better approach. I think he agrees with what you wrote.

On 8/15/25 10:44 AM, Guenther Sohler via Discuss wrote: > Nope i disagree
Here. > PythonSCAD is Not reinventing the wheel, its a Mix of leveraging
existing > Technology, Bridging 2 worlds(Python and Scad are very interlinked)
and > Quite some offering Features which openscad Refuse to have for Ages I
think you misread Jordan; he's saying adding too much OO stuff to the OpenSCAD
language is reinventing the wheel, and suggests PythonSCAD is the better
approach. I think he agrees with what you wrote.

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Fri, Aug 15, 2025 5:51 PM

On 8/15/25 10:27 AM, Jordan Brown via Discuss wrote:

____

____

____

There's more than one style of OO inheritance. What we've got here  
is more like the JavaScript "prototype object" style of  
inheritance: you can take an object that you like, and make a  
modified copy of it.

The difference is you can't have super, which ECMAScript does have.

I'm afraid my ES/JS experience, though pretty extensive, is for  
work-legacy reasons primarily with a 2006-ish version of JS. At that  
point it didn't have a `super`, but you could carefully build  
something that more or less worked. Have they added a real one?

Yes.

____

But yes, that's a concern. See the comment I just added to PR#6022.

I commented there too. For the sake of maximum audience, I'll copy my  
questions/comments here:

You've got some goals and are trying to make /object/ work for them. I  
think the goals are:

  1. Replace hardcoded [1] and [CONSTANT] index into arrays by being able   
to name values by identifier

  2. Be able to namespace functions, modules, and constants.
  3. Be able to assert some piece of data as conforming to some standard   
(i.e. data validation in constructor, expect method X to exist, etc).

Is that correct?

I don't think prototype inheritance is a great fit for a language with  
immutable data types. I think either generic functions or class  
definitions are a better fit. Just because you /can/ use  
/object/+lambdas to keep many things you want doesn't mean you /should/.

On 8/15/25 10:27 AM, Jordan Brown via Discuss wrote: >>> There's more than one
style of OO inheritance. What we've got here >>> is more like the JavaScript
"prototype object" style of >>> inheritance: you can take an object that you
like, and make a >>> modified copy of it. >> The difference is you can't have
super, which ECMAScript does have. > > I'm afraid my ES/JS experience, though
pretty extensive, is for > work-legacy reasons primarily with a 2006-ish
version of JS. At that > point it didn't have a `super`, but you could
carefully build > something that more or less worked. Have they added a real
one? Yes. > But yes, that's a concern. See the comment I just added to
PR#6022. I commented there too. For the sake of maximum audience, I'll copy my
questions/comments here: You've got some goals and are trying to make /object/
work for them. I think the goals are: 1\. Replace hardcoded [1] and [CONSTANT]
index into arrays by being able to name values by identifier 2\. Be able to
namespace functions, modules, and constants. 3\. Be able to assert some piece
of data as conforming to some standard (i.e. data validation in constructor,
expect method X to exist, etc). Is that correct? I don't think prototype
inheritance is a great fit for a language with immutable data types. I think
either generic functions or class definitions are a better fit. Just because
you /can/ use /object/+lambdas to keep many things you want doesn't mean you
/should/.

[Next
page](https://lists.openscad.org/empathy/thread/IYHWMISYOLPWRQXEL4SVWZGJHEXKVTBC?page=2)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

