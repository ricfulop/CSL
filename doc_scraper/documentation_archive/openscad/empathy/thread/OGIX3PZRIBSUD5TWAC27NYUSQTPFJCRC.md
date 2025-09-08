---
url: https://lists.openscad.org/empathy/thread/OGIX3PZRIBSUD5TWAC27NYUSQTPFJCRC
scraped_at: 2025-09-08T16:28:09.613694
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

###  BOSL skin does nott accept function polygon

![](https://www.gravatar.com/avatar/98685aada4cfe0b0ed8d339b8fd9e85f?d=blank&s=100)

JJ

Johan Jonker

Sun, Sep 7, 2025 8:03 PM

Dear forum,

I have a strange warning when combining BOSL2 and a polygon:

This warning caused execution to abort  
WARNING unknown function 'polygon' in file......

## This is the line that results in the warning:

skin([for (z = zz2)  
polygon(chamber_slice(-x_rooftop(z), w_rooftop(z), r_rooftop(z),  
r_side(z),  
x_bottom(z), w_bottom(z), r_bottom(z)))],  
z=zz2, slices = 3, refine=1);  
}

some help would be appreciated

kind regards,  
/Johan Jonker/

Dear forum, I have a strange warning when combining BOSL2 and a polygon: This
warning caused execution to abort WARNING unknown function 'polygon' in
file...... This is the line that results in the warning: \---------- skin([for
(z = zz2) polygon(chamber_slice(-x_rooftop(z), w_rooftop(z), r_rooftop(z),
r_side(z), x_bottom(z), w_bottom(z), r_bottom(z)))], z=zz2, slices = 3,
refine=1); } some help would be appreciated kind regards, /Johan Jonker/

![](https://www.gravatar.com/avatar/efffe97fbbe5ef43492550ef734147d9?d=blank&s=100)

TA

Todd Allen

Sun, Sep 7, 2025 11:31 PM

Despite the wiki doc stating polygon() is a function there is only a  
polygon() module so it doesn't return anything and can't be used as a  
parameter.

On Sun, Sep 7, 2025 at 3:04 PM Johan Jonker via Discuss <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

Dear forum,

I have a strange warning when combining BOSL2 and a polygon:

This warning caused execution to abort  
WARNING unknown function 'polygon' in file......

## This is the line that results in the warning:

    
    
     skin([for (z = zz2)
         polygon(chamber_slice(-x_rooftop(z), w_rooftop(z), r_rooftop(z),
                     r_side(z),
                     x_bottom(z), w_bottom(z), r_bottom(z)))],
         z=zz2, slices = 3, refine=1);
     }
    

some help would be appreciated

kind regards,  
_Johan Jonker_

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Despite the wiki doc stating polygon() is a function there is only a polygon()
module so it doesn't return anything and can't be used as a parameter. On Sun,
Sep 7, 2025 at 3:04 PM Johan Jonker via Discuss < discuss@lists.openscad.org>
wrote: > Dear forum, > > I have a strange warning when combining BOSL2 and a
polygon: > > This warning caused execution to abort > WARNING unknown function
'polygon' in file...... > > This is the line that results in the warning: >
\---------- > skin([for (z = zz2) > polygon(chamber_slice(-x_rooftop(z),
w_rooftop(z), r_rooftop(z), > r_side(z), > x_bottom(z), w_bottom(z),
r_bottom(z)))], > z=zz2, slices = 3, refine=1); > } > > some help would be
appreciated > > kind regards, > *Johan Jonker* >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/98685aada4cfe0b0ed8d339b8fd9e85f?d=blank&s=100)

I

info

Mon, Sep 8, 2025 5:45 AM

thanks, that explains a lot. Then the question is how to convert a series of
points into a 2d object.Verzonden vanaf mijn Galaxy  
\-------- Oorspronkelijk bericht --------Van: Todd Allen via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) Datum:
08-09-2025 01:31 (GMT+01:00) Aan: OpenSCAD general discussion Mailing-list
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) Cc: Johan
Jonker [info@johanjonker.net](mailto:info@johanjonker.net), Todd Allen
[speedebikes@gmail.com](mailto:speedebikes@gmail.com) Onderwerp: [OpenSCAD]
Re: BOSL skin does nott accept function polygon Despite the wiki doc stating
polygon() is a function there is only a polygon() module so it doesn't return
anything and can't be used as a parameter. On Sun, Sep 7, 2025 at 3:04 PM
Johan Jonker via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

    
    
    Dear forum,
    
    I have a strange warning when combining BOSL2 and a polygon:
    
    This warning caused execution to abort
    WARNING unknown function 'polygon' in
      file......
      
      This is the line that results in the warning:
      ----------
          skin([for (z = zz2) 
              polygon(chamber_slice(-x_rooftop(z), w_rooftop(z),
      r_rooftop(z),
                          r_side(z),
                          x_bottom(z), w_bottom(z), r_bottom(z)))],
              z=zz2, slices = 3, refine=1);
          }
      
      some help would be appreciated
      
      kind regards,
      Johan Jonker
    

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

thanks, that explains a lot. Then the question is how to convert a series of
points into a 2d object.Verzonden vanaf mijn Galaxy \-------- Oorspronkelijk
bericht --------Van: Todd Allen via Discuss <discuss@lists.openscad.org>
Datum: 08-09-2025 01:31 (GMT+01:00) Aan: OpenSCAD general discussion Mailing-
list <discuss@lists.openscad.org> Cc: Johan Jonker <info@johanjonker.net>,
Todd Allen <speedebikes@gmail.com> Onderwerp: [OpenSCAD] Re: BOSL skin does
nott accept function polygon Despite the wiki doc stating polygon() is a
function there is only a polygon() module so it doesn't return anything and
can't be used as a parameter. On Sun, Sep 7, 2025 at 3:04 PM Johan Jonker via
Discuss <discuss@lists.openscad.org> wrote: Dear forum, I have a strange
warning when combining BOSL2 and a polygon: This warning caused execution to
abort WARNING unknown function 'polygon' in file...... This is the line that
results in the warning: \---------- skin([for (z = zz2)
polygon(chamber_slice(-x_rooftop(z), w_rooftop(z), r_rooftop(z), r_side(z),
x_bottom(z), w_bottom(z), r_bottom(z)))], z=zz2, slices = 3, refine=1); } some
help would be appreciated kind regards, Johan Jonker
_______________________________________________ OpenSCAD mailing list To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Mon, Sep 8, 2025 6:32 AM

On 9/7/2025 4:31 PM, Todd Allen via Discuss wrote:

____

Despite the wiki doc stating polygon() is a function there is only a  
polygon() module so it doesn't return anything and can't be used as a  
parameter.

Indeed the doc page says that; it misuses the word "function" a number  
of times on that page. (Probably a C/C++ habit leaking through.) I  
think I've fixed it on that page, but there are probably similar errors  
throughout.

On 9/7/2025 10:45 PM, info via Discuss wrote:

____

Then the question is how to convert a series of points into a 2d object.

No, that's not the question. That's what polygon() does.

The question is how to turn a series of points into a data structure  
that skin() can accept.

I suspect that the answer to that is... nothing, that skin wants to see  
a list of points. Indeed, dumping the results from BOSL2's square()  
function shows that it returns exactly that.

Perhaps Adrian or Revar can confirm.

On 9/7/2025 4:31 PM, Todd Allen via Discuss wrote: > Despite the wiki doc
stating polygon() is a function there is only a > polygon() module so it
doesn't return anything and can't be used as a > parameter. Indeed the doc
page says that; it misuses the word "function" a number of times on that page.
(Probably a C/C++ habit leaking through.) I think I've fixed it on that page,
but there are probably similar errors throughout. On 9/7/2025 10:45 PM, info
via Discuss wrote: > Then the question is how to convert a series of points
into a 2d object. No, that's not the question. That's what polygon() does. The
question is how to turn a series of points into a data structure that skin()
can accept. I suspect that the answer to that is... nothing, that skin wants
to see a list of points. Indeed, dumping the results from BOSL2's square()
function shows that it returns exactly that. Perhaps Adrian or Revar can
confirm.

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

