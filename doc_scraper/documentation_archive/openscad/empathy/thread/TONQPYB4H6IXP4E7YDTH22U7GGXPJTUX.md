---
url: https://lists.openscad.org/empathy/thread/TONQPYB4H6IXP4E7YDTH22U7GGXPJTUX
scraped_at: 2025-09-08T16:28:28.840313
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

###  $fn and arcs

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Thu, Aug 21, 2025 12:18 PM

Does anybody know the calculation openscad uses for the number of segments  
on an arc of angle theta as a function of $fn? Exactly what kind of  
rounding is used?

Does anybody know the calculation openscad uses for the number of segments on
an arc of angle theta as a function of $fn? Exactly what kind of rounding is
used?

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Thu, Aug 21, 2025 1:42 PM

At least in DxfData:

    
    
          n = static_cast<int>(ceil(n * arc_angle / 360));
    

where n comes from

    
    
          int n = Calc::get_fragments_from_r(radius, fn, fs, fa);
    

which returns $fn so long as it's at least 3:
<https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>

<https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>

Sorry for non-permalinks.

On August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

Does anybody know the calculation openscad uses for the number of segments  
on an arc of angle theta as a function of $fn? Exactly what kind of  
rounding is used?

At least in DxfData: n = static_cast<int>(ceil(n * arc_angle / 360)); where n
comes from int n = Calc::get_fragments_from_r(radius, fn, fs, fa); which
returns $fn so long as it's at least 3:
<https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>
<https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>
Sorry for non-permalinks. On August 21, 2025 8:18:44 AM EDT, Adrian Mariano
via Discuss <discuss@lists.openscad.org> wrote: >Does anybody know the
calculation openscad uses for the number of segments >on an arc of angle theta
as a function of $fn? Exactly what kind of >rounding is used?

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Thu, Aug 21, 2025 2:22 PM

Thanks. The possibility of rounding error exists in the computation.  
Someone observed in BOSL2 that offset behaved irregularly. The existing  
calculation does not match openscad but even with it fixed if I offset a  
regular n gon with $fn = n I get rounding errors and sometimes the ceil  
rounds up giving an extra facet. Openscad seems to avoid this somehow and  
consistently produces just a single facet.

On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

At least in DxfData:

    
    
           n = static_cast<int>(ceil(n * arc_angle / 360));
    

where n comes from

    
    
           int n = Calc::get_fragments_from_r(radius, fn, fs, fa);
    

which returns $fn so long as it's at least 3: <  
<https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>

____

<  
<https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>

____

Sorry for non-permalinks.

On August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

Does anybody know the calculation openscad uses for the number of  
segments on an arc of angle theta as a function of $fn? Exactly what kind  
of rounding is used?

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Thanks. The possibility of rounding error exists in the computation. Someone
observed in BOSL2 that offset behaved irregularly. The existing calculation
does not match openscad but even with it fixed if I offset a regular n gon
with $fn = n I get rounding errors and sometimes the ceil rounds up giving an
extra facet. Openscad seems to avoid this somehow and consistently produces
just a single facet. On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss <
discuss@lists.openscad.org> wrote: > At least in DxfData: > > n =
static_cast<int>(ceil(n * arc_angle / 360)); > > where n comes from > > int n
= Calc::get_fragments_from_r(radius, fn, fs, fa); > > which returns $fn so
long as it's at least 3: < >
https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47 > >
> > < >
https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205 >
> > > Sorry for non-permalinks. > > > On August 21, 2025 8:18:44 AM EDT,
Adrian Mariano via Discuss < > discuss@lists.openscad.org> wrote: > >> Does
anybody know the calculation openscad uses for the number of >> segments on an
arc of angle theta as a function of $fn? Exactly what kind >> of rounding is
used? >> > _______________________________________________ > OpenSCAD mailing
list > To unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/b19e2e8fa3505b0c13f5f8aba31dab95?d=blank&s=100)

MK

Marius Kintel

Thu, Aug 21, 2025 2:45 PM

In C++, OpenSCAD converts n to int first before doing the arc angle
calculation. That may introduce a tiny difference, as if you do the same
calculation in OpenSCAD, it’s kept as double all the way. Not sure if that’s
the root cause though..

-Marius

____

On Aug 21, 2025, at 10:22, Adrian Mariano via
Discuss[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

Thanks. The possibility of rounding error exists in the computation. Someone
observed in BOSL2 that offset behaved irregularly. The existing calculation
does not match openscad but even with it fixed if I offset a regular n gon
with $fn = n I get rounding errors and sometimes the ceil rounds up giving an
extra facet. Openscad seems to avoid this somehow and consistently produces
just a single facet.

On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

At least in DxfData:

    
    
           n = static_cast<int>(ceil(n * arc_angle / 360));
    

where n comes from

    
    
           int n = Calc::get_fragments_from_r(radius, fn, fs, fa);
    

which returns $fn so long as it's at least 3:
<https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>

<https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>

Sorry for non-permalinks.

On August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

Does anybody know the calculation openscad uses for the number of segments on
an arc of angle theta as a function of $fn? Exactly what kind of rounding is
used?

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)
[mailto:discuss-leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)_______________________________________________

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

In C++, OpenSCAD converts n to int first before doing the arc angle
calculation. That may introduce a tiny difference, as if you do the same
calculation in OpenSCAD, it’s kept as double all the way. Not sure if that’s
the root cause though.. -Marius > On Aug 21, 2025, at 10:22, Adrian Mariano
via Discuss <discuss@lists.openscad.org> wrote: > > Thanks. The possibility of
rounding error exists in the computation. Someone observed in BOSL2 that
offset behaved irregularly. The existing calculation does not match openscad
but even with it fixed if I offset a regular n gon with $fn = n I get rounding
errors and sometimes the ceil rounds up giving an extra facet. Openscad seems
to avoid this somehow and consistently produces just a single facet. > > On
Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss <discuss@lists.openscad.org
<mailto:discuss@lists.openscad.org>> wrote: >> At least in DxfData: >> >> n =
static_cast<int>(ceil(n * arc_angle / 360)); >> >> where n comes from >> >>
int n = Calc::get_fragments_from_r(radius, fn, fs, fa); >> >> which returns
$fn so long as it's at least 3:
<https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>
>> >>
<https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>
>> >> Sorry for non-permalinks. >> >> >> On August 21, 2025 8:18:44 AM EDT,
Adrian Mariano via Discuss <discuss@lists.openscad.org
<mailto:discuss@lists.openscad.org>> wrote: >>> Does anybody know the
calculation openscad uses for the number of segments on an arc of angle theta
as a function of $fn? Exactly what kind of rounding is used? >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org <mailto:discuss-
leave@lists.openscad.org>_______________________________________________ >
OpenSCAD mailing list > To unsubscribe send an email to discuss-
leave@lists.openscad.org

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Thu, Aug 21, 2025 5:29 PM

I think the cause is when either angle or 360/(n*arc_angle) isn't perfectly
representable by a double.

I think the best solution is to subtract epsilon before calling ceil. I
haven't thought of any situation this is worse, especially given n is never
less than 3.

On August 21, 2025 10:45:52 AM EDT, Marius Kintel via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

In C++, OpenSCAD converts n to int first before doing the arc angle
calculation. That may introduce a tiny difference, as if you do the same
calculation in OpenSCAD, it’s kept as double all the way. Not sure if that’s
the root cause though..

If I'm remembering my numerical methods lessons correctly, I don't think
that's the reason, as the code correctly multiplies n*arc_angle first, which
will always be less than the maximum representable integer in a double (for
any reasonable n), so it will exact if the angle is representable as a double.

  * Cory Cross

____

-Marius

> On Aug 21, 2025, at 10:22, Adrian Mariano via Discuss
> [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:
>
> Thanks. The possibility of rounding error exists in the computation. Someone
> observed in BOSL2 that offset behaved irregularly. The existing calculation
> does not match openscad but even with it fixed if I offset a regular n gon
> with $fn = n I get rounding errors and sometimes the ceil rounds up giving
> an extra facet. Openscad seems to avoid this somehow and consistently
> produces just a single facet.
>
> On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss
> <[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
> [mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
> wrote:
>

>> At least in DxfData:

>>  
>>  
>>           n = static_cast<int>(ceil(n * arc_angle / 360));

>>  
>>

>> where n comes from

>>  
>>  
>>           int n = Calc::get_fragments_from_r(radius, fn, fs, fa);

>>  
>>

>> which returns $fn so long as it's at least 3:
<https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>

>>

>>
<https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>

>>

>> Sorry for non-permalinks.

>>

>> On August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

>>

>>> Does anybody know the calculation openscad uses for the number of segments
on an arc of angle theta as a function of $fn? Exactly what kind of rounding
is used?

>>

>> * * *

>>

>> OpenSCAD mailing list  
> To unsubscribe send an email to [discuss-
> leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)
> [mailto:discuss-leave@lists.openscad.org](mailto:discuss-
> leave@lists.openscad.org)_______________________________________________  
> OpenSCAD mailing list  
> To unsubscribe send an email to [discuss-
> leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

I think the cause is when either angle or 360/(n*arc_angle) isn't perfectly
representable by a double. I think the best solution is to subtract epsilon
before calling ceil. I haven't thought of any situation this is worse,
especially given n is never less than 3. On August 21, 2025 10:45:52 AM EDT,
Marius Kintel via Discuss <discuss@lists.openscad.org> wrote: >In C++,
OpenSCAD converts n to int first before doing the arc angle calculation. That
may introduce a tiny difference, as if you do the same calculation in
OpenSCAD, it’s kept as double all the way. Not sure if that’s the root cause
though.. If I'm remembering my numerical methods lessons correctly, I don't
think that's the reason, as the code correctly multiplies n*arc_angle first,
which will always be less than the maximum representable integer in a double
(for any reasonable n), so it will exact if the angle is representable as a
double. \- Cory Cross > > -Marius > >> On Aug 21, 2025, at 10:22, Adrian
Mariano via Discuss <discuss@lists.openscad.org> wrote: >> >> Thanks. The
possibility of rounding error exists in the computation. Someone observed in
BOSL2 that offset behaved irregularly. The existing calculation does not match
openscad but even with it fixed if I offset a regular n gon with $fn = n I get
rounding errors and sometimes the ceil rounds up giving an extra facet.
Openscad seems to avoid this somehow and consistently produces just a single
facet. >> >> On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss
<discuss@lists.openscad.org <mailto:discuss@lists.openscad.org>> wrote: >>> At
least in DxfData: >>> >>> n = static_cast<int>(ceil(n * arc_angle / 360)); >>>
>>> where n comes from >>> >>> int n = Calc::get_fragments_from_r(radius, fn,
fs, fa); >>> >>> which returns $fn so long as it's at least 3:
<https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>
>>> >>>
<https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>
>>> >>> Sorry for non-permalinks. >>> >>> >>> On August 21, 2025 8:18:44 AM
EDT, Adrian Mariano via Discuss <discuss@lists.openscad.org
<mailto:discuss@lists.openscad.org>> wrote: >>>> Does anybody know the
calculation openscad uses for the number of segments on an arc of angle theta
as a function of $fn? Exactly what kind of rounding is used? >>>
_______________________________________________ >>> OpenSCAD mailing list >>>
To unsubscribe send an email to discuss-leave@lists.openscad.org
<mailto:discuss-
leave@lists.openscad.org>_______________________________________________ >>
OpenSCAD mailing list >> To unsubscribe send an email to discuss-
leave@lists.openscad.org >

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Thu, Aug 21, 2025 6:02 PM

Representability as a double is not sufficient. You have to also compute  
that representation. Since arccos is involved this is not guaranteed. I  
see issues with n of 5, 6 and 8 which have integer angles of 72, 60 and  
45\. It works for n of 3 and 12.

Subtracting epsilon before the ceil seems ok and of course does fix it.

On Thu, Aug 21, 2025 at 13:30 Cory Cross via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I think the cause is when either angle or 360/(n*arc_angle) isn't  
perfectly representable by a double.

I think the best solution is to subtract epsilon before calling ceil. I  
haven't thought of any situation this is worse, especially given n is never  
less than 3.

On August 21, 2025 10:45:52 AM EDT, Marius Kintel via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

In C++, OpenSCAD converts n to int first before doing the arc angle

calculation. That may introduce a tiny difference, as if you do the same  
calculation in OpenSCAD, it’s kept as double all the way. Not sure if  
that’s the root cause though..

If I'm remembering my numerical methods lessons correctly, I don't think  
that's the reason, as the code correctly multiplies n*arc_angle first,  
which will always be less than the maximum representable integer in a  
double (for any reasonable n), so it will exact if the angle is  
representable as a double.

  * Cory Cross

____

-Marius

____

On Aug 21, 2025, at 10:22, Adrian Mariano via Discuss <

[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

____

Thanks. The possibility of rounding error exists in the computation.

Someone observed in BOSL2 that offset behaved irregularly. The existing  
calculation does not match openscad but even with it fixed if I offset a  
regular n gon with $fn = n I get rounding errors and sometimes the ceil  
rounds up giving an extra facet. Openscad seems to avoid this somehow and  
consistently produces just a single facet.

____

____

On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss <

[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

____

____

At least in DxfData:

    
    
           n = static_cast<int>(ceil(n * arc_angle / 360));
    

where n comes from

    
    
           int n = Calc::get_fragments_from_r(radius, fn, fs, fa);
    

which returns $fn so long as it's at least 3: <

<https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>

____

____

____

<

<https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>

____

____

____

Sorry for non-permalinks.

On August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss <

[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

____

____

____

Does anybody know the calculation openscad uses for the number of

segments on an arc of angle theta as a function of $fn? Exactly what kind  
of rounding is used?

____

____

____

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

<mailto:[discuss-leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)

____

* * *

____

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Representability as a double is not sufficient. You have to also compute that
representation. Since arccos is involved this is not guaranteed. I see issues
with n of 5, 6 and 8 which have integer angles of 72, 60 and 45\. It works for
n of 3 and 12. Subtracting epsilon before the ceil seems ok and of course does
fix it. On Thu, Aug 21, 2025 at 13:30 Cory Cross via Discuss <
discuss@lists.openscad.org> wrote: > I think the cause is when either angle or
360/(n*arc_angle) isn't > perfectly representable by a double. > > I think the
best solution is to subtract epsilon before calling ceil. I > haven't thought
of any situation this is worse, especially given n is never > less than 3. > >
> > On August 21, 2025 10:45:52 AM EDT, Marius Kintel via Discuss < >
discuss@lists.openscad.org> wrote: > >In C++, OpenSCAD converts n to int first
before doing the arc angle > calculation. That may introduce a tiny
difference, as if you do the same > calculation in OpenSCAD, it’s kept as
double all the way. Not sure if > that’s the root cause though.. > > If I'm
remembering my numerical methods lessons correctly, I don't think > that's the
reason, as the code correctly multiplies n*arc_angle first, > which will
always be less than the maximum representable integer in a > double (for any
reasonable n), so it will exact if the angle is > representable as a double. >
> \- Cory Cross > > > > > > > > -Marius > > > >> On Aug 21, 2025, at 10:22,
Adrian Mariano via Discuss < > discuss@lists.openscad.org> wrote: > >> > >>
Thanks. The possibility of rounding error exists in the computation. > Someone
observed in BOSL2 that offset behaved irregularly. The existing > calculation
does not match openscad but even with it fixed if I offset a > regular n gon
with $fn = n I get rounding errors and sometimes the ceil > rounds up giving
an extra facet. Openscad seems to avoid this somehow and > consistently
produces just a single facet. > >> > >> On Thu, Aug 21, 2025 at 09:43 Cory
Cross via Discuss < > discuss@lists.openscad.org
<mailto:discuss@lists.openscad.org>> wrote: > >>> At least in DxfData: > >>> >
>>> n = static_cast<int>(ceil(n * arc_angle / 360)); > >>> > >>> where n comes
from > >>> > >>> int n = Calc::get_fragments_from_r(radius, fn, fs, fa); > >>>
> >>> which returns $fn so long as it's at least 3: < >
https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47 > >
> >>> > >>> < >
https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205 >
> > >>> > >>> Sorry for non-permalinks. > >>> > >>> > >>> On August 21, 2025
8:18:44 AM EDT, Adrian Mariano via Discuss < > discuss@lists.openscad.org
<mailto:discuss@lists.openscad.org>> wrote: > >>>> Does anybody know the
calculation openscad uses for the number of > segments on an arc of angle
theta as a function of $fn? Exactly what kind > of rounding is used? > >>>
_______________________________________________ > >>> OpenSCAD mailing list >
>>> To unsubscribe send an email to discuss-leave@lists.openscad.org >
<mailto:discuss-leave@lists.openscad.org >
>_______________________________________________ > >> OpenSCAD mailing list >
>> To unsubscribe send an email to discuss-leave@lists.openscad.org > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Fri, Aug 22, 2025 8:37 PM

On August 21, 2025 2:02:00 PM EDT, Adrian Mariano via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

Representability as a double is not sufficient. You have to also compute  
that representation. Since arccos is involved this is not guaranteed. I  
see issues with n of 5, 6 and 8 which have integer angles of 72, 60 and  
45\. It works for n of 3 and 12.

Oops, I inverted the equation. (n * arc_angle / 360) of course. Okay, so a
trigonometric function is calculating the angle and returning 72+epsilon (or
more!? hope not), so just subtracting epsilon from the whole equation won't
always work when n>360, so it should be taken from the angle.

  * Cory

____

Subtracting epsilon before the ceil seems ok and of course does fix it.

On Thu, Aug 21, 2025 at 13:30 Cory Cross via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

> I think the cause is when either angle or 360/(n*arc_angle) isn't  
> perfectly representable by a double.
>
> I think the best solution is to subtract epsilon before calling ceil. I  
> haven't thought of any situation this is worse, especially given n is never  
> less than 3.
>
> On August 21, 2025 10:45:52 AM EDT, Marius Kintel via Discuss <  
> [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:
>

>> In C++, OpenSCAD converts n to int first before doing the arc angle  
> calculation. That may introduce a tiny difference, as if you do the same  
> calculation in OpenSCAD, it’s kept as double all the way. Not sure if  
> that’s the root cause though..
>
> If I'm remembering my numerical methods lessons correctly, I don't think  
> that's the reason, as the code correctly multiplies n*arc_angle first,  
> which will always be less than the maximum representable integer in a  
> double (for any reasonable n), so it will exact if the angle is  
> representable as a double.
>
>   * Cory Cross
>

>

>> -Marius

>>

>>> On Aug 21, 2025, at 10:22, Adrian Mariano via Discuss <  
> [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:
>>>

>>> Thanks. The possibility of rounding error exists in the computation.  
> Someone observed in BOSL2 that offset behaved irregularly. The existing  
> calculation does not match openscad but even with it fixed if I offset a  
> regular n gon with $fn = n I get rounding errors and sometimes the ceil  
> rounds up giving an extra facet. Openscad seems to avoid this somehow and  
> consistently produces just a single facet.
>>>

>>> On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss <  
> [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
> [mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
> wrote:
>>>

>>>> At least in DxfData:

>>>>  
>>>>  
>>>>           n = static_cast<int>(ceil(n * arc_angle / 360));

>>>>  
>>>>

>>>> where n comes from

>>>>  
>>>>  
>>>>           int n = Calc::get_fragments_from_r(radius, fn, fs, fa);

>>>>  
>>>>

>>>> which returns $fn so long as it's at least 3: <  
> <https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>
>>

>>> > <  
>
> <https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>
>>

>>> > Sorry for non-permalinks.

>>>>

>>>> On August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss <  
> [discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
> [mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>
> wrote:
>>>>

>>>>> Does anybody know the calculation openscad uses for the number of  
> segments on an arc of angle theta as a function of $fn? Exactly what kind  
> of rounding is used?
>>>>

>>>> * * *

>>>>

>>>> OpenSCAD mailing list  
> To unsubscribe send an email to [discuss-
> leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)  
> <mailto:[discuss-leave@lists.openscad.org](mailto:discuss-
> leave@lists.openscad.org)
>>

>> * * *

>>

>>> OpenSCAD mailing list  
> To unsubscribe send an email to [discuss-
> leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)
>
> * * *
>
> OpenSCAD mailing list  
> To unsubscribe send an email to [discuss-
> leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

On August 21, 2025 2:02:00 PM EDT, Adrian Mariano via Discuss
<discuss@lists.openscad.org> wrote: >Representability as a double is not
sufficient. You have to also compute >that representation. Since arccos is
involved this is not guaranteed. I >see issues with n of 5, 6 and 8 which have
integer angles of 72, 60 and >45\. It works for n of 3 and 12. Oops, I
inverted the equation. (n * arc_angle / 360) of course. Okay, so a
trigonometric function is calculating the angle and returning 72+epsilon (or
more!? hope not), so just subtracting epsilon from the whole equation won't
always work when n>360, so it should be taken from the angle. \- Cory >
>Subtracting epsilon before the ceil seems ok and of course does fix it. > >On
Thu, Aug 21, 2025 at 13:30 Cory Cross via Discuss <
>discuss@lists.openscad.org> wrote: > >> I think the cause is when either
angle or 360/(n*arc_angle) isn't >> perfectly representable by a double. >> >>
I think the best solution is to subtract epsilon before calling ceil. I >>
haven't thought of any situation this is worse, especially given n is never >>
less than 3. >> >> >> >> On August 21, 2025 10:45:52 AM EDT, Marius Kintel via
Discuss < >> discuss@lists.openscad.org> wrote: >> >In C++, OpenSCAD converts
n to int first before doing the arc angle >> calculation. That may introduce a
tiny difference, as if you do the same >> calculation in OpenSCAD, it’s kept
as double all the way. Not sure if >> that’s the root cause though.. >> >> If
I'm remembering my numerical methods lessons correctly, I don't think >>
that's the reason, as the code correctly multiplies n*arc_angle first, >>
which will always be less than the maximum representable integer in a >>
double (for any reasonable n), so it will exact if the angle is >>
representable as a double. >> >> \- Cory Cross >> >> >> >> >> > >> > -Marius
>> > >> >> On Aug 21, 2025, at 10:22, Adrian Mariano via Discuss < >>
discuss@lists.openscad.org> wrote: >> >> >> >> Thanks. The possibility of
rounding error exists in the computation. >> Someone observed in BOSL2 that
offset behaved irregularly. The existing >> calculation does not match
openscad but even with it fixed if I offset a >> regular n gon with $fn = n I
get rounding errors and sometimes the ceil >> rounds up giving an extra facet.
Openscad seems to avoid this somehow and >> consistently produces just a
single facet. >> >> >> >> On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss
< >> discuss@lists.openscad.org <mailto:discuss@lists.openscad.org>> wrote: >>
>>> At least in DxfData: >> >>> >> >>> n = static_cast<int>(ceil(n * arc_angle
/ 360)); >> >>> >> >>> where n comes from >> >>> >> >>> int n =
Calc::get_fragments_from_r(radius, fn, fs, fa); >> >>> >> >>> which returns
$fn so long as it's at least 3: < >>
https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47 >>
> >> >>> >> >>> < >>
https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205 >>
> >> >>> >> >>> Sorry for non-permalinks. >> >>> >> >>> >> >>> On August 21,
2025 8:18:44 AM EDT, Adrian Mariano via Discuss < >>
discuss@lists.openscad.org <mailto:discuss@lists.openscad.org>> wrote: >> >>>>
Does anybody know the calculation openscad uses for the number of >> segments
on an arc of angle theta as a function of $fn? Exactly what kind >> of
rounding is used? >> >>> _______________________________________________ >>
>>> OpenSCAD mailing list >> >>> To unsubscribe send an email to discuss-
leave@lists.openscad.org >> <mailto:discuss-leave@lists.openscad.org >>
>_______________________________________________ >> >> OpenSCAD mailing list
>> >> To unsubscribe send an email to discuss-leave@lists.openscad.org >> > >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/a4bf179813f41a0e3dd5b77e8902b52c?d=blank&s=100)

AM

Adrian Mariano

Fri, Aug 22, 2025 10:28 PM

Why would it matter if n>360? I don't see that it makes a difference if  
you subtract epsilon from angle or from the whole expression. I did the  
latter because it was simpler.

On Fri, Aug 22, 2025 at 4:38 PM Cory Cross via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

On August 21, 2025 2:02:00 PM EDT, Adrian Mariano via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

Representability as a double is not sufficient. You have to also compute  
that representation. Since arccos is involved this is not guaranteed. I  
see issues with n of 5, 6 and 8 which have integer angles of 72, 60 and  
45\. It works for n of 3 and 12.

Oops, I inverted the equation. (n * arc_angle / 360) of course. Okay, so a  
trigonometric function is calculating the angle and returning 72+epsilon  
(or more!? hope not), so just subtracting epsilon from the whole equation  
won't always work when n>360, so it should be taken from the angle.

  * Cory

____

Subtracting epsilon before the ceil seems ok and of course does fix it.

On Thu, Aug 21, 2025 at 13:30 Cory Cross via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I think the cause is when either angle or 360/(n*arc_angle) isn't  
perfectly representable by a double.

I think the best solution is to subtract epsilon before calling ceil. I  
haven't thought of any situation this is worse, especially given n is

never

____

____

less than 3.

On August 21, 2025 10:45:52 AM EDT, Marius Kintel via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

In C++, OpenSCAD converts n to int first before doing the arc angle

calculation. That may introduce a tiny difference, as if you do the same  
calculation in OpenSCAD, it’s kept as double all the way. Not sure if  
that’s the root cause though..

If I'm remembering my numerical methods lessons correctly, I don't think  
that's the reason, as the code correctly multiplies n*arc_angle first,  
which will always be less than the maximum representable integer in a  
double (for any reasonable n), so it will exact if the angle is  
representable as a double.

  * Cory Cross

____

-Marius

____

On Aug 21, 2025, at 10:22, Adrian Mariano via Discuss <

[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

____

Thanks. The possibility of rounding error exists in the computation.

Someone observed in BOSL2 that offset behaved irregularly. The existing  
calculation does not match openscad but even with it fixed if I offset a  
regular n gon with $fn = n I get rounding errors and sometimes the ceil  
rounds up giving an extra facet. Openscad seems to avoid this somehow

and

____

____

consistently produces just a single facet.

____

____

On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss <

[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

____

____

At least in DxfData:

    
    
           n = static_cast<int>(ceil(n * arc_angle / 360));
    

where n comes from

    
    
           int n = Calc::get_fragments_from_r(radius, fn, fs, fa);
    

which returns $fn so long as it's at least 3: <

<https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47>

____

____

____

____

____

<

<https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205>

____

____

____

____

____

Sorry for non-permalinks.

On August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss <

[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

____

____

____

Does anybody know the calculation openscad uses for the number of

segments on an arc of angle theta as a function of $fn? Exactly what

kind

____

____

of rounding is used?

____

____

____

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

<mailto:[discuss-leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)

____

* * *

____

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Why would it matter if n>360? I don't see that it makes a difference if you
subtract epsilon from angle or from the whole expression. I did the latter
because it was simpler. On Fri, Aug 22, 2025 at 4:38 PM Cory Cross via Discuss
< discuss@lists.openscad.org> wrote: > > > On August 21, 2025 2:02:00 PM EDT,
Adrian Mariano via Discuss < > discuss@lists.openscad.org> wrote: >
>Representability as a double is not sufficient. You have to also compute >
>that representation. Since arccos is involved this is not guaranteed. I >
>see issues with n of 5, 6 and 8 which have integer angles of 72, 60 and >
>45\. It works for n of 3 and 12. > > Oops, I inverted the equation. (n *
arc_angle / 360) of course. Okay, so a > trigonometric function is calculating
the angle and returning 72+epsilon > (or more!? hope not), so just subtracting
epsilon from the whole equation > won't always work when n>360, so it should
be taken from the angle. > > \- Cory > > > > > >Subtracting epsilon before the
ceil seems ok and of course does fix it. > > > >On Thu, Aug 21, 2025 at 13:30
Cory Cross via Discuss < > >discuss@lists.openscad.org> wrote: > > > >> I
think the cause is when either angle or 360/(n*arc_angle) isn't > >> perfectly
representable by a double. > >> > >> I think the best solution is to subtract
epsilon before calling ceil. I > >> haven't thought of any situation this is
worse, especially given n is > never > >> less than 3. > >> > >> > >> > >> On
August 21, 2025 10:45:52 AM EDT, Marius Kintel via Discuss < > >>
discuss@lists.openscad.org> wrote: > >> >In C++, OpenSCAD converts n to int
first before doing the arc angle > >> calculation. That may introduce a tiny
difference, as if you do the same > >> calculation in OpenSCAD, it’s kept as
double all the way. Not sure if > >> that’s the root cause though.. > >> > >>
If I'm remembering my numerical methods lessons correctly, I don't think > >>
that's the reason, as the code correctly multiplies n*arc_angle first, > >>
which will always be less than the maximum representable integer in a > >>
double (for any reasonable n), so it will exact if the angle is > >>
representable as a double. > >> > >> \- Cory Cross > >> > >> > >> > >> > >> >
> >> > -Marius > >> > > >> >> On Aug 21, 2025, at 10:22, Adrian Mariano via
Discuss < > >> discuss@lists.openscad.org> wrote: > >> >> > >> >> Thanks. The
possibility of rounding error exists in the computation. > >> Someone observed
in BOSL2 that offset behaved irregularly. The existing > >> calculation does
not match openscad but even with it fixed if I offset a > >> regular n gon
with $fn = n I get rounding errors and sometimes the ceil > >> rounds up
giving an extra facet. Openscad seems to avoid this somehow > and > >>
consistently produces just a single facet. > >> >> > >> >> On Thu, Aug 21,
2025 at 09:43 Cory Cross via Discuss < > >> discuss@lists.openscad.org
<mailto:discuss@lists.openscad.org>> wrote: > >> >>> At least in DxfData: > >>
>>> > >> >>> n = static_cast<int>(ceil(n * arc_angle / 360)); > >> >>> > >>
>>> where n comes from > >> >>> > >> >>> int n =
Calc::get_fragments_from_r(radius, fn, fs, fa); > >> >>> > >> >>> which
returns $fn so long as it's at least 3: < > >> >
https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47 >
>> > > >> >>> > >> >>> < > >> >
https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205 >
>> > > >> >>> > >> >>> Sorry for non-permalinks. > >> >>> > >> >>> > >> >>> On
August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss < > >>
discuss@lists.openscad.org <mailto:discuss@lists.openscad.org>> wrote: > >>
>>>> Does anybody know the calculation openscad uses for the number of > >>
segments on an arc of angle theta as a function of $fn? Exactly what > kind >
>> of rounding is used? > >> >>>
_______________________________________________ > >> >>> OpenSCAD mailing list
> >> >>> To unsubscribe send an email to discuss-leave@lists.openscad.org > >>
<mailto:discuss-leave@lists.openscad.org > >>
>_______________________________________________ > >> >> OpenSCAD mailing list
> >> >> To unsubscribe send an email to discuss-leave@lists.openscad.org > >>
> > >> _______________________________________________ > >> OpenSCAD mailing
list > >> To unsubscribe send an email to discuss-leave@lists.openscad.org >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Sun, Aug 24, 2025 9:57 PM

On 8/21/2025 2:18 PM, Adrian Mariano via Discuss wrote:

____

Does anybody know the calculation openscad uses for the number of  
segments on an arc of angle theta as a function of $fn? Exactly what  
kind of rounding is used?

I don't think anybody ever directly quoted the source:

<https://github.com/openscad/openscad/blob/7cf1c641e4dba4bac4ffe247b7a900029b8ae148/src/geometry/rotate_extrude.cc#L103>

const auto num_sections = (unsigned int)std::ceil(fmax(  
Calc::get_fragments_from_r(max_x - min_x, node.fn, node.fs, node.fa) *
std::abs(node.angle) / 360,  
1));

Calc:get_fragments_from_r() is the $fn/$fa/$fs/r calculation, which  
returns $fn if it is set and reasonable.

On 8/21/2025 2:18 PM, Adrian Mariano via Discuss wrote: > Does anybody know
the calculation openscad uses for the number of > segments on an arc of angle
theta as a function of $fn? Exactly what > kind of rounding is used? I don't
think anybody ever directly quoted the source:
https://github.com/openscad/openscad/blob/7cf1c641e4dba4bac4ffe247b7a900029b8ae148/src/geometry/rotate_extrude.cc#L103
const auto num_sections = (unsigned int)std::ceil(fmax(
Calc::get_fragments_from_r(max_x - min_x, node.fn, node.fs, node.fa) *
std::abs(node.angle) / 360, 1)); Calc:get_fragments_from_r() is the
$fn/$fa/$fs/r calculation, which returns $fn if it is set and reasonable.

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Sun, Aug 24, 2025 10:46 PM

On 8/22/25 3:28 PM, Adrian Mariano via Discuss wrote:

____

Why would it matter if n >360? I don't see that it makes a difference  
if you subtract epsilon from angle or from the whole expression. I  
did the latter because it was simpler.

So the error is in `angle`, and it's multiplied by n/360. We're assuming  
the error is as much as epsilon, so subtracting at the end:

n*(angle+epsilon)/360 - epsilon  
n _angle/360 + epsilon_ n/360 - epsilon

so if n=720 we're still epsilon too much, and if (n*angle/360) is an  
integer, the final result will round up to the next higher integer.

versus subtracting at angle:

n*(angle+epsilon-epsilon)/360  
n*angle/360

independent of n when error==epsilon (which we're assuming). If it's  
actually less than epsilon:

n _angle/360 - epsilon_ n/360

That will only cause a different result if n*angle/360 was slightly more  
than a whole number, which will never (for any sane measurements) be the  
case when you are choosing some fraction of $fn arc, and only arose in  
freak coincidences in existing code.

  * Cory Cross

____

On Fri, Aug 22, 2025 at 4:38 PM Cory Cross via Discuss  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

    
    
     On August 21, 2025 2:02:00 PM EDT, Adrian Mariano via Discuss
     <discuss@lists.openscad.org> wrote:
    

____

Representability as a double is not sufficient. You have to also

    
    
     compute
    

____

that representation. Since arccos is involved this is not

    
    
     guaranteed.  I
    

____

see issues with n of 5, 6 and 8 which have integer angles of 72,

    
    
     60 and
    

____

45\. It works for n of 3 and 12.

    
    
     Oops, I inverted the equation. (n * arc_angle / 360) of course.
     Okay, so a trigonometric function is calculating the angle and
     returning 72+epsilon (or more!? hope not), so just subtracting
     epsilon from the whole equation won't always work when n>360, so
     it should be taken from the angle.
    
     - Cory
    

____

Subtracting epsilon before the ceil seems ok and of course does

    
    
     fix it.
    

____

On Thu, Aug 21, 2025 at 13:30 Cory Cross via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

I think the cause is when either angle or 360/(n*arc_angle) isn't  
perfectly representable by a double.

I think the best solution is to subtract epsilon before calling

    
    
     ceil. I
    

____

____

haven't thought of any situation this is worse, especially

    
    
     given n is never
    

____

____

less than 3.

On August 21, 2025 10:45:52 AM EDT, Marius Kintel via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

In C++, OpenSCAD converts n to int first before doing the arc

    
    
     angle
    

____

____

calculation. That may introduce a tiny difference, as if you do

    
    
     the same
    

____

____

calculation in OpenSCAD, it’s kept as double all the way. Not

    
    
     sure if
    

____

____

that’s the root cause though..

If I'm remembering my numerical methods lessons correctly, I

    
    
     don't think
    

____

____

that's the reason, as the code correctly multiplies n*arc_angle

    
    
     first,
    

____

____

which will always be less than the maximum representable

    
    
     integer in a
    

____

____

double (for any reasonable n), so it will exact if the angle is  
representable as a double.

  * Cory Cross

____

-Marius

____

On Aug 21, 2025, at 10:22, Adrian Mariano via Discuss <

[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

____

Thanks. The possibility of rounding error exists in the

    
    
     computation.
    

____

____

Someone observed in BOSL2 that offset behaved irregularly. The

    
    
     existing
    

____

____

calculation does not match openscad but even with it fixed if I

    
    
     offset a
    

____

____

regular n gon with $fn = n I get rounding errors and sometimes

    
    
     the ceil
    

____

____

rounds up giving an extra facet. Openscad seems to avoid this

    
    
     somehow and
    

____

____

consistently produces just a single facet.

____

____

On Thu, Aug 21, 2025 at 09:43 Cory Cross via Discuss <

[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>

    
    
     wrote:
    

____

____

____

____

____

At least in DxfData:

n = static_cast<int>(ceil(n * arc_angle / 360));

where n comes from

int n = Calc::get_fragments_from_r(radius, fn,

    
    
     fs, fa);
    

____

____

____

____

____

which returns $fn so long as it's at least 3: <

    
    
     https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47
    

____

____

____

____

____

<

    
    
     https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205
    

____

____

____

____

____

Sorry for non-permalinks.

On August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss <

[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)>

    
    
     wrote:
    

____

____

____

____

____

____

Does anybody know the calculation openscad uses for the

    
    
     number of
    

____

____

segments on an arc of angle theta as a function of $fn?

    
    
     Exactly what kind
    

____

____

of rounding is used?

____

____

____

* * *

OpenSCAD mailing list  
To unsubscribe send an email to

    
    
     discuss-leave@lists.openscad.org
    

____

____

< mailto:[discuss-leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)

____

* * *

____

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

    
    
     _______________________________________________
     OpenSCAD mailing list
     To unsubscribe send an email to discuss-leave@lists.openscad.org
    

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

On 8/22/25 3:28 PM, Adrian Mariano via Discuss wrote: > Why would it matter if
n>360? I don't see that it makes a difference > if you subtract epsilon from
angle or from the whole expression. I > did the latter because it was simpler.
So the error is in `angle`, and it's multiplied by n/360. We're assuming the
error is as much as epsilon, so subtracting at the end: n*(angle+epsilon)/360
- epsilon n*angle/360 + epsilon*n/360 - epsilon so if n=720 we're still
epsilon too much, and if (n*angle/360) is an integer, the final result will
round up to the next higher integer. versus subtracting at angle:
n*(angle+epsilon-epsilon)/360 n*angle/360 independent of n when error==epsilon
(which we're assuming). If it's actually less than epsilon: n*angle/360 -
epsilon*n/360 That will only cause a different result if n*angle/360 was
slightly more than a whole number, which will never (for any sane
measurements) be the case when you are choosing some fraction of $fn arc, and
only arose in freak coincidences in existing code. \- Cory Cross > > On Fri,
Aug 22, 2025 at 4:38 PM Cory Cross via Discuss > <discuss@lists.openscad.org>
wrote: > > > > On August 21, 2025 2:02:00 PM EDT, Adrian Mariano via Discuss >
<discuss@lists.openscad.org> wrote: > >Representability as a double is not
sufficient. You have to also > compute > >that representation. Since arccos is
involved this is not > guaranteed. I > >see issues with n of 5, 6 and 8 which
have integer angles of 72, > 60 and > >45\. It works for n of 3 and 12. > >
Oops, I inverted the equation. (n * arc_angle / 360) of course. > Okay, so a
trigonometric function is calculating the angle and > returning 72+epsilon (or
more!? hope not), so just subtracting > epsilon from the whole equation won't
always work when n>360, so > it should be taken from the angle. > > \- Cory >
> > > > >Subtracting epsilon before the ceil seems ok and of course does > fix
it. > > > >On Thu, Aug 21, 2025 at 13:30 Cory Cross via Discuss < >
>discuss@lists.openscad.org> wrote: > > > >> I think the cause is when either
angle or 360/(n*arc_angle) isn't > >> perfectly representable by a double. >
>> > >> I think the best solution is to subtract epsilon before calling >
ceil. I > >> haven't thought of any situation this is worse, especially >
given n is never > >> less than 3. > >> > >> > >> > >> On August 21, 2025
10:45:52 AM EDT, Marius Kintel via Discuss < > >> discuss@lists.openscad.org>
wrote: > >> >In C++, OpenSCAD converts n to int first before doing the arc >
angle > >> calculation. That may introduce a tiny difference, as if you do >
the same > >> calculation in OpenSCAD, it’s kept as double all the way. Not >
sure if > >> that’s the root cause though.. > >> > >> If I'm remembering my
numerical methods lessons correctly, I > don't think > >> that's the reason,
as the code correctly multiplies n*arc_angle > first, > >> which will always
be less than the maximum representable > integer in a > >> double (for any
reasonable n), so it will exact if the angle is > >> representable as a
double. > >> > >> \- Cory Cross > >> > >> > >> > >> > >> > > >> > -Marius > >>
> > >> >> On Aug 21, 2025, at 10:22, Adrian Mariano via Discuss < > >>
discuss@lists.openscad.org> wrote: > >> >> > >> >> Thanks. The possibility of
rounding error exists in the > computation. > >> Someone observed in BOSL2
that offset behaved irregularly. The > existing > >> calculation does not
match openscad but even with it fixed if I > offset a > >> regular n gon with
$fn = n I get rounding errors and sometimes > the ceil > >> rounds up giving
an extra facet. Openscad seems to avoid this > somehow and > >> consistently
produces just a single facet. > >> >> > >> >> On Thu, Aug 21, 2025 at 09:43
Cory Cross via Discuss < > >> discuss@lists.openscad.org
<mailto:discuss@lists.openscad.org>> > wrote: > >> >>> At least in DxfData: >
>> >>> > >> >>> n = static_cast<int>(ceil(n * arc_angle / 360)); > >> >>> > >>
>>> where n comes from > >> >>> > >> >>> int n =
Calc::get_fragments_from_r(radius, fn, > fs, fa); > >> >>> > >> >>> which
returns $fn so long as it's at least 3: < > >> >
https://github.com/openscad/openscad/blob/master/src%2Futils%2Fcalc.cc#L47 >
>> > > >> >>> > >> >>> < > >> >
https://github.com/openscad/openscad/blob/master/src%2Fio%2FDxfData.cc#L205 >
>> > > >> >>> > >> >>> Sorry for non-permalinks. > >> >>> > >> >>> > >> >>> On
August 21, 2025 8:18:44 AM EDT, Adrian Mariano via Discuss < > >>
discuss@lists.openscad.org <mailto:discuss@lists.openscad.org>> > wrote: > >>
>>>> Does anybody know the calculation openscad uses for the > number of > >>
segments on an arc of angle theta as a function of $fn? > Exactly what kind >
>> of rounding is used? > >> >>>
_______________________________________________ > >> >>> OpenSCAD mailing list
> >> >>> To unsubscribe send an email to > discuss-leave@lists.openscad.org >
>> <mailto:discuss-leave@lists.openscad.org > >>
>_______________________________________________ > >> >> OpenSCAD mailing list
> >> >> To unsubscribe send an email to discuss-leave@lists.openscad.org > >>
> > >> _______________________________________________ > >> OpenSCAD mailing
list > >> To unsubscribe send an email to discuss-leave@lists.openscad.org >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email todiscuss-leave@lists.openscad.org

[Next
page](https://lists.openscad.org/empathy/thread/TONQPYB4H6IXP4E7YDTH22U7GGXPJTUX?page=2)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

