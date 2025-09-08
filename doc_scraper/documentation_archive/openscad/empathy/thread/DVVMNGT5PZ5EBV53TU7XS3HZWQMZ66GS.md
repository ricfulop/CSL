---
url: https://lists.openscad.org/empathy/thread/DVVMNGT5PZ5EBV53TU7XS3HZWQMZ66GS
scraped_at: 2025-09-08T16:28:16.744262
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

###  rounding and fillets with python in openSCAD

![](https://www.gravatar.com/avatar/e52db4b9dc6c9ada14dd09e2e1b27825?d=blank&s=100)

SP

Sanjeev Prabhakar

Fri, Aug 22, 2025 6:12 PM

I have been working with python to find some solution on fillets and  
rounding in openSCAD.

Although I could not find any specific solution, there could be a few  
strategies which can be followed to create rounding and fillets.

sharing a few pictures here to show what is possible. What is required is  
to find a way to work with points in 3d space, instead of openSCAD  
primitives.  
[image: Screenshot 2025-08-22 at 10.43.34 PM.png]  
[image: Screenshot 2025-08-22 at 9.44.25 PM.png]  
[image: Screenshot 2025-08-22 at 11.14.20 PM.png]  
[image: Screenshot 2025-08-22 at 11.18.54 PM.png][image: Screenshot  
2025-08-22 at 11.21.39 PM.png][image: Screenshot 2025-08-22 at  
11.41.27 PM.png]

I have been working with python to find some solution on fillets and rounding
in openSCAD. Although I could not find any specific solution, there could be a
few strategies which can be followed to create rounding and fillets. sharing a
few pictures here to show what is possible. What is required is to find a way
to work with points in 3d space, instead of openSCAD primitives. [image:
Screenshot 2025-08-22 at 10.43.34 PM.png] [image: Screenshot 2025-08-22 at
9.44.25 PM.png] [image: Screenshot 2025-08-22 at 11.14.20 PM.png] [image:
Screenshot 2025-08-22 at 11.18.54 PM.png][image: Screenshot 2025-08-22 at
11.21.39 PM.png][image: Screenshot 2025-08-22 at 11.41.27 PM.png]

[ ![Attached image](https://lists.openscad.org/empathy/image/678378/200)
](https://lists.openscad.org/empathy/attachment/678378) [ ![Attached
image](https://lists.openscad.org/empathy/image/678377/200)
](https://lists.openscad.org/empathy/attachment/678377) [ ![Attached
image](https://lists.openscad.org/empathy/image/678376/200)
](https://lists.openscad.org/empathy/attachment/678376) [ ![Attached
image](https://lists.openscad.org/empathy/image/678375/200)
](https://lists.openscad.org/empathy/attachment/678375) [ ![Attached
image](https://lists.openscad.org/empathy/image/678374/200)
](https://lists.openscad.org/empathy/attachment/678374) [ ![Attached
image](https://lists.openscad.org/empathy/image/678373/200)
](https://lists.openscad.org/empathy/attachment/678373)

![](https://www.gravatar.com/avatar/d6de89c90e2e89a85dd10e6c3b5950e2?d=blank&s=100)

JB

Jon Bondy

Fri, Aug 22, 2025 6:55 PM

Sorry if you think this is pedantic, but you are NOT trying "to find  
some solution on fillets and rounding in openSCAD". You are trying to  
find a solution in Python and OpenSCAD.

And that is a huge difference.

BOSL attempts to solve these problems in OpenSCAD. To date, I do not  
recall your trying to do this at all.

I get frustrated with these kinds of mis-statements.

Jon

On 8/22/2025 2:12 PM, Sanjeev Prabhakar via Discuss wrote:

____

I have been working with python to find some solution on fillets and  
rounding in openSCAD.

Although I could not find any specific solution, there could be a few  
strategies which can be followed to create rounding and fillets.

sharing a few pictures here to show what is possible. What is required  
is to find a way to work with points in 3d space, instead of openSCAD  
primitives.  
Screenshot 2025-08-22 at 10.43.34 PM.png  
Screenshot 2025-08-22 at 9.44.25 PM.png  
Screenshot 2025-08-22 at 11.14.20 PM.png  
Screenshot 2025-08-22 at 11.18.54 PM.pngScreenshot 2025-08-22 at  
11.21.39 PM.pngScreenshot 2025-08-22 at 11.41.27 PM.png

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

\--  
This email has been checked for viruses by AVG antivirus software.  
[www.avg.com](http://www.avg.com)

Sorry if you think this is pedantic, but you are NOT trying "to find some
solution on fillets and rounding in openSCAD". You are trying to find a
solution in Python and OpenSCAD. And that is a huge difference. BOSL attempts
to solve these problems in OpenSCAD. To date, I do not recall your trying to
do this at all. I get frustrated with these kinds of mis-statements. Jon On
8/22/2025 2:12 PM, Sanjeev Prabhakar via Discuss wrote: > I have been working
with python to find some solution on fillets and > rounding in openSCAD. > >
Although I could not find any specific solution, there could be a few >
strategies which can be followed to create rounding and fillets. > > sharing a
few pictures here to show what is possible. What is required > is to find a
way to work with points in 3d space, instead of openSCAD > primitives. >
Screenshot 2025-08-22 at 10.43.34 PM.png > Screenshot 2025-08-22 at 9.44.25
PM.png > Screenshot 2025-08-22 at 11.14.20 PM.png > Screenshot 2025-08-22 at
11.18.54 PM.pngScreenshot 2025-08-22 at > 11.21.39 PM.pngScreenshot 2025-08-22
at 11.41.27 PM.png > > _______________________________________________ >
OpenSCAD mailing list > To unsubscribe send an email todiscuss-
leave@lists.openscad.org \-- This email has been checked for viruses by AVG
antivirus software. www.avg.com

[ ![Attached image](https://lists.openscad.org/empathy/image/678388/200)
](https://lists.openscad.org/empathy/attachment/678388) [ ![Attached
image](https://lists.openscad.org/empathy/image/678387/200)
](https://lists.openscad.org/empathy/attachment/678387) [ ![Attached
image](https://lists.openscad.org/empathy/image/678386/200)
](https://lists.openscad.org/empathy/attachment/678386) [ ![Attached
image](https://lists.openscad.org/empathy/image/678385/200)
](https://lists.openscad.org/empathy/attachment/678385) [ ![Attached
image](https://lists.openscad.org/empathy/image/678384/200)
](https://lists.openscad.org/empathy/attachment/678384) [ ![Attached
image](https://lists.openscad.org/empathy/image/678383/200)
](https://lists.openscad.org/empathy/attachment/678383)

![](https://www.gravatar.com/avatar/e52db4b9dc6c9ada14dd09e2e1b27825?d=blank&s=100)

SP

Sanjeev Prabhakar

Sat, Aug 23, 2025 2:15 AM

Please don't feel frustrated, have a bucket of cold water and relax.

On Sat, 23 Aug 2025 at 00:26, Jon Bondy
[jon@jonbondy.com](mailto:jon@jonbondy.com) wrote:

____

Sorry if you think this is pedantic, but you are NOT trying "to find some  
solution on fillets and rounding in openSCAD". You are trying to find a  
solution in Python and OpenSCAD.

And that is a huge difference.

BOSL attempts to solve these problems in OpenSCAD. To date, I do not  
recall your trying to do this at all.

I get frustrated with these kinds of mis-statements.

Jon

On 8/22/2025 2:12 PM, Sanjeev Prabhakar via Discuss wrote:

I have been working with python to find some solution on fillets and  
rounding in openSCAD.

Although I could not find any specific solution, there could be a few  
strategies which can be followed to create rounding and fillets.

sharing a few pictures here to show what is possible. What is required is  
to find a way to work with points in 3d space, instead of openSCAD  
primitives.  
[image: Screenshot 2025-08-22 at 10.43.34 PM.png]  
[image: Screenshot 2025-08-22 at 9.44.25 PM.png]  
[image: Screenshot 2025-08-22 at 11.14.20 PM.png]  
[image: Screenshot 2025-08-22 at 11.18.54 PM.png][image: Screenshot  
2025-08-22 at 11.21.39 PM.png][image: Screenshot 2025-08-22 at  
11.41.27 PM.png]

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

[http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient](http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient)  
Virus-free.www.avg.com  
[http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient](http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient)  
<#m_-1398042392476013121_DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2>

Please don't feel frustrated, have a bucket of cold water and relax. On Sat,
23 Aug 2025 at 00:26, Jon Bondy <jon@jonbondy.com> wrote: > Sorry if you think
this is pedantic, but you are NOT trying "to find some > solution on fillets
and rounding in openSCAD". You are trying to find a > solution in Python and
OpenSCAD. > > And that is a huge difference. > > BOSL attempts to solve these
problems in OpenSCAD. To date, I do not > recall your trying to do this at
all. > > I get frustrated with these kinds of mis-statements. > > Jon > > > On
8/22/2025 2:12 PM, Sanjeev Prabhakar via Discuss wrote: > > I have been
working with python to find some solution on fillets and > rounding in
openSCAD. > > Although I could not find any specific solution, there could be
a few > strategies which can be followed to create rounding and fillets. > >
sharing a few pictures here to show what is possible. What is required is > to
find a way to work with points in 3d space, instead of openSCAD > primitives.
> [image: Screenshot 2025-08-22 at 10.43.34 PM.png] > [image: Screenshot
2025-08-22 at 9.44.25 PM.png] > [image: Screenshot 2025-08-22 at 11.14.20
PM.png] > [image: Screenshot 2025-08-22 at 11.18.54 PM.png][image: Screenshot
> 2025-08-22 at 11.21.39 PM.png][image: Screenshot 2025-08-22 at > 11.41.27
PM.png] > > _______________________________________________ > OpenSCAD mailing
list > To unsubscribe send an email to discuss-leave@lists.openscad.org > > >
> <http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> > Virus-free.www.avg.com >
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> >
<#m_-1398042392476013121_DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2> >

[ ![Attached image](https://lists.openscad.org/empathy/image/678425/200)
](https://lists.openscad.org/empathy/attachment/678425) [ ![Attached
image](https://lists.openscad.org/empathy/image/678424/200)
](https://lists.openscad.org/empathy/attachment/678424) [ ![Attached
image](https://lists.openscad.org/empathy/image/678423/200)
](https://lists.openscad.org/empathy/attachment/678423) [ ![Attached
image](https://lists.openscad.org/empathy/image/678422/200)
](https://lists.openscad.org/empathy/attachment/678422) [ ![Attached
image](https://lists.openscad.org/empathy/image/678421/200)
](https://lists.openscad.org/empathy/attachment/678421) [ ![Attached
image](https://lists.openscad.org/empathy/image/678420/200)
](https://lists.openscad.org/empathy/attachment/678420)

![](https://www.gravatar.com/avatar/901519ec4216a54cde3ac2d5a018b082?d=blank&s=100)

P

pca006132

Sat, Aug 23, 2025 2:25 AM

@Jon: For me, I don't care if the method is in "pure" openscad or not.  
If it is good and general, we can implement it in C++ and expose it as a  
call. If it is not general enough, there is still a chance it can be  
implemented in userspace when we expose geometry data to users.

@Sanjeev: I have several questions.

  1. What are your strategies?

  2. Are your fillets real fillets (constant radius or something), or just   
something that looks good enough? For the third figure (2 tubes), it  
doesn't look like a constant radius result to me as the transition  
doesn't look as smooth.

On 8/23/25 10:15, Sanjeev Prabhakar via Discuss wrote:

____

Please don't feel frustrated, have a bucket of cold water and relax.

On Sat, 23 Aug 2025 at 00:26, Jon Bondy
[jon@jonbondy.com](mailto:jon@jonbondy.com) wrote:

    
    
     Sorry if you think this is pedantic, but you are NOT trying "to
     find some solution on fillets and rounding in openSCAD".  You are
     trying to find a solution in Python and OpenSCAD.
    
     And that is a huge difference.
    
     BOSL attempts to solve these problems in OpenSCAD.  To date, I do
     not recall your trying to do this at all.
    
     I get frustrated with these kinds of mis-statements.
    
     Jon
    
    
     On 8/22/2025 2:12 PM, Sanjeev Prabhakar via Discuss wrote:
    

____

    
    
    I have been working with python to find some solution on fillets
     and rounding in openSCAD.
    
     Although I could not find any specific solution, there could be a
     few strategies which can be followed to create rounding and fillets.
    
     sharing a few pictures here to show what is possible. What is
     required is to find a way to work with points in 3d space,
     instead of openSCAD primitives.
     Screenshot 2025-08-22 at 10.43.34 PM.png
     Screenshot 2025-08-22 at 9.44.25 PM.png
     Screenshot 2025-08-22 at 11.14.20 PM.png
     Screenshot 2025-08-22 at 11.18.54 PM.pngScreenshot 2025-08-22 at
     11.21.39 PM.pngScreenshot 2025-08-22 at 11.41.27 PM.png
    
     _______________________________________________
     OpenSCAD mailing list
     To unsubscribe send an email todiscuss-leave@lists.openscad.org
    
    
     <http://www.avg.com/email-signature?utm_medium=email&utm_source=link&utm_campaign=sig-email&utm_content=emailclient>
     	Virus-free.www.avg.com
     <http://www.avg.com/email-signature?utm_medium=email&utm_source=link&utm_campaign=sig-email&utm_content=emailclient>
    
    
     <#m_-1398042392476013121_DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2>
    

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

@Jon: For me, I don't care if the method is in "pure" openscad or not. If it
is good and general, we can implement it in C++ and expose it as a call. If it
is not general enough, there is still a chance it can be implemented in
userspace when we expose geometry data to users. @Sanjeev: I have several
questions. 1\. What are your strategies? 2\. Are your fillets real fillets
(constant radius or something), or just something that looks good enough? For
the third figure (2 tubes), it doesn't look like a constant radius result to
me as the transition doesn't look as smooth. On 8/23/25 10:15, Sanjeev
Prabhakar via Discuss wrote: > Please don't feel frustrated, have a bucket of
cold water and relax. > > On Sat, 23 Aug 2025 at 00:26, Jon Bondy
<jon@jonbondy.com> wrote: > > Sorry if you think this is pedantic, but you are
NOT trying "to > find some solution on fillets and rounding in openSCAD". You
are > trying to find a solution in Python and OpenSCAD. > > And that is a huge
difference. > > BOSL attempts to solve these problems in OpenSCAD. To date, I
do > not recall your trying to do this at all. > > I get frustrated with these
kinds of mis-statements. > > Jon > > > On 8/22/2025 2:12 PM, Sanjeev Prabhakar
via Discuss wrote: >> I have been working with python to find some solution on
fillets >> and rounding in openSCAD. >> >> Although I could not find any
specific solution, there could be a >> few strategies which can be followed to
create rounding and fillets. >> >> sharing a few pictures here to show what is
possible. What is >> required is to find a way to work with points in 3d
space, >> instead of openSCAD primitives. >> Screenshot 2025-08-22 at 10.43.34
PM.png >> Screenshot 2025-08-22 at 9.44.25 PM.png >> Screenshot 2025-08-22 at
11.14.20 PM.png >> Screenshot 2025-08-22 at 11.18.54 PM.pngScreenshot
2025-08-22 at >> 11.21.39 PM.pngScreenshot 2025-08-22 at 11.41.27 PM.png >> >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email todiscuss-leave@lists.openscad.org > >
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> > Virus-free.www.avg.com >
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> > > >
<#m_-1398042392476013121_DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2> > > >
_______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email todiscuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/678432/200)
](https://lists.openscad.org/empathy/attachment/678432) [ ![Attached
image](https://lists.openscad.org/empathy/image/678431/200)
](https://lists.openscad.org/empathy/attachment/678431) [ ![Attached
image](https://lists.openscad.org/empathy/image/678430/200)
](https://lists.openscad.org/empathy/attachment/678430) [ ![Attached
image](https://lists.openscad.org/empathy/image/678429/200)
](https://lists.openscad.org/empathy/attachment/678429) [ ![Attached
image](https://lists.openscad.org/empathy/image/678428/200)
](https://lists.openscad.org/empathy/attachment/678428) [ ![Attached
image](https://lists.openscad.org/empathy/image/678427/200)
](https://lists.openscad.org/empathy/attachment/678427)

![](https://www.gravatar.com/avatar/e52db4b9dc6c9ada14dd09e2e1b27825?d=blank&s=100)

SP

Sanjeev Prabhakar

Sat, Aug 23, 2025 5:22 AM

Both are possible  
perfect radius fillets and visually appealing one  
I am attaching 2 files with very simple example, due to file size  
constraints

Will explain the strategies later in evening once I have some time

Both are possible perfect radius fillets and visually appealing one I am
attaching 2 files with very simple example, due to file size constraints Will
explain the strategies later in evening once I have some time

[ __visually_appealing_fillet.scad(100.77 KB)
](https://lists.openscad.org/empathy/attachment/678438 "application/octet-
stream")

[ __perfect_fillet_radius.scad(175.12 KB)
](https://lists.openscad.org/empathy/attachment/678437 "application/octet-
stream")

![](https://www.gravatar.com/avatar/e52db4b9dc6c9ada14dd09e2e1b27825?d=blank&s=100)

SP

Sanjeev Prabhakar

Sat, Aug 23, 2025 2:14 PM

There are mainly 2 simpler ways which works for creating fillets

strategy 1 is explained in attached file.

Let me know, in case you have any questions

On Sat, 23 Aug 2025 at 10:52, Sanjeev Prabhakar
[sprabhakar2006@gmail.com](mailto:sprabhakar2006@gmail.com)  
wrote:

____

Both are possible  
perfect radius fillets and visually appealing one  
I am attaching 2 files with very simple example, due to file size  
constraints

Will explain the strategies later in evening once I have some time

There are mainly 2 simpler ways which works for creating fillets strategy 1 is
explained in attached file. Let me know, in case you have any questions On
Sat, 23 Aug 2025 at 10:52, Sanjeev Prabhakar <sprabhakar2006@gmail.com> wrote:
> Both are possible > perfect radius fillets and visually appealing one > I am
attaching 2 files with very simple example, due to file size > constraints > >
Will explain the strategies later in evening once I have some time > >

[ __filleting_strategy_1.pdf(424.91 KB)
](https://lists.openscad.org/empathy/attachment/678447 "application/pdf")

![](https://www.gravatar.com/avatar/901519ec4216a54cde3ac2d5a018b082?d=blank&s=100)

P

pca006132

Sun, Aug 24, 2025 12:20 AM

OK, the method you are talking about doesn't seem new, and is not that  
general.

Another question is, if we want to support this, we will need a way to  
specify which edges the user wants (apart from being able to compute the  
points in openscad).

On 8/23/25 22:14, Sanjeev Prabhakar wrote:

____

There are mainly 2 simpler ways which works for creating fillets

strategy 1 is explained in attached file.

Let me know, in case you have any questions

On Sat, 23 Aug 2025 at 10:52, Sanjeev Prabhakar  
[sprabhakar2006@gmail.com](mailto:sprabhakar2006@gmail.com) wrote:

    
    
     Both are possible
     perfect radius fillets and visually appealing one
     I am attaching 2 files with very simple example, due to file size
     constraints
    
     Will explain the strategies later in evening once I have some time
    

OK, the method you are talking about doesn't seem new, and is not that
general. Another question is, if we want to support this, we will need a way
to specify which edges the user wants (apart from being able to compute the
points in openscad). On 8/23/25 22:14, Sanjeev Prabhakar wrote: > There are
mainly 2 simpler ways which works for creating fillets > > strategy 1 is
explained in attached file. > > Let me know, in case you have any questions >
> > On Sat, 23 Aug 2025 at 10:52, Sanjeev Prabhakar >
<sprabhakar2006@gmail.com> wrote: > > Both are possible > perfect radius
fillets and visually appealing one > I am attaching 2 files with very simple
example, due to file size > constraints > > Will explain the strategies later
in evening once I have some time >

![](https://www.gravatar.com/avatar/e52db4b9dc6c9ada14dd09e2e1b27825?d=blank&s=100)

SP

Sanjeev Prabhakar

Sun, Aug 24, 2025 2:05 AM

Your question is not completely clear to me. Are you saying some portion of  
the intersection line to convert to fillet?

That can be done by selecting those few points in the intersection line. So  
openscad should have a way to select a portion of a list.

On Sun, 24 Aug, 2025, 5:50 am pca006132,
[john.lck40@gmail.com](mailto:john.lck40@gmail.com) wrote:

____

OK, the method you are talking about doesn't seem new, and is not that  
general.

Another question is, if we want to support this, we will need a way to  
specify which edges the user wants (apart from being able to compute the  
points in openscad).  
On 8/23/25 22:14, Sanjeev Prabhakar wrote:

There are mainly 2 simpler ways which works for creating fillets

strategy 1 is explained in attached file.

Let me know, in case you have any questions

On Sat, 23 Aug 2025 at 10:52, Sanjeev Prabhakar
[sprabhakar2006@gmail.com](mailto:sprabhakar2006@gmail.com)  
wrote:

____

Both are possible  
perfect radius fillets and visually appealing one  
I am attaching 2 files with very simple example, due to file size  
constraints

Will explain the strategies later in evening once I have some time

Your question is not completely clear to me. Are you saying some portion of
the intersection line to convert to fillet? That can be done by selecting
those few points in the intersection line. So openscad should have a way to
select a portion of a list. On Sun, 24 Aug, 2025, 5:50 am pca006132,
<john.lck40@gmail.com> wrote: > OK, the method you are talking about doesn't
seem new, and is not that > general. > > Another question is, if we want to
support this, we will need a way to > specify which edges the user wants
(apart from being able to compute the > points in openscad). > On 8/23/25
22:14, Sanjeev Prabhakar wrote: > > There are mainly 2 simpler ways which
works for creating fillets > > strategy 1 is explained in attached file. > >
Let me know, in case you have any questions > > > On Sat, 23 Aug 2025 at
10:52, Sanjeev Prabhakar <sprabhakar2006@gmail.com> > wrote: > >> Both are
possible >> perfect radius fillets and visually appealing one >> I am
attaching 2 files with very simple example, due to file size >> constraints >>
>> Will explain the strategies later in evening once I have some time >> >>

![](https://www.gravatar.com/avatar/901519ec4216a54cde3ac2d5a018b082?d=blank&s=100)

P

pca006132

Sun, Aug 24, 2025 2:34 AM

Yes you can select sublist, but doing this is annoying. Ideally we should  
provide APIs to select edges formed due to intersection, or around certain  
features, for example.

On Sun, Aug 24, 2025, 10:05 Sanjeev Prabhakar
[sprabhakar2006@gmail.com](mailto:sprabhakar2006@gmail.com)  
wrote:

____

Your question is not completely clear to me. Are you saying some portion  
of the intersection line to convert to fillet?

That can be done by selecting those few points in the intersection line.  
So openscad should have a way to select a portion of a list.

On Sun, 24 Aug, 2025, 5:50 am pca006132,
[john.lck40@gmail.com](mailto:john.lck40@gmail.com) wrote:

____

OK, the method you are talking about doesn't seem new, and is not that  
general.

Another question is, if we want to support this, we will need a way to  
specify which edges the user wants (apart from being able to compute the  
points in openscad).  
On 8/23/25 22:14, Sanjeev Prabhakar wrote:

There are mainly 2 simpler ways which works for creating fillets

strategy 1 is explained in attached file.

Let me know, in case you have any questions

On Sat, 23 Aug 2025 at 10:52, Sanjeev Prabhakar
[sprabhakar2006@gmail.com](mailto:sprabhakar2006@gmail.com)  
wrote:

____

Both are possible  
perfect radius fillets and visually appealing one  
I am attaching 2 files with very simple example, due to file size  
constraints

Will explain the strategies later in evening once I have some time

Yes you can select sublist, but doing this is annoying. Ideally we should
provide APIs to select edges formed due to intersection, or around certain
features, for example. On Sun, Aug 24, 2025, 10:05 Sanjeev Prabhakar
<sprabhakar2006@gmail.com> wrote: > Your question is not completely clear to
me. Are you saying some portion > of the intersection line to convert to
fillet? > > That can be done by selecting those few points in the intersection
line. > So openscad should have a way to select a portion of a list. > > On
Sun, 24 Aug, 2025, 5:50 am pca006132, <john.lck40@gmail.com> wrote: > >> OK,
the method you are talking about doesn't seem new, and is not that >> general.
>> >> Another question is, if we want to support this, we will need a way to
>> specify which edges the user wants (apart from being able to compute the >>
points in openscad). >> On 8/23/25 22:14, Sanjeev Prabhakar wrote: >> >> There
are mainly 2 simpler ways which works for creating fillets >> >> strategy 1 is
explained in attached file. >> >> Let me know, in case you have any questions
>> >> >> On Sat, 23 Aug 2025 at 10:52, Sanjeev Prabhakar
<sprabhakar2006@gmail.com> >> wrote: >> >>> Both are possible >>> perfect
radius fillets and visually appealing one >>> I am attaching 2 files with very
simple example, due to file size >>> constraints >>> >>> Will explain the
strategies later in evening once I have some time >>> >>>

![](https://www.gravatar.com/avatar/e52db4b9dc6c9ada14dd09e2e1b27825?d=blank&s=100)

SP

Sanjeev Prabhakar

Sun, Aug 24, 2025 2:51 AM

Yes, you can do that for sure.

Here is strategy 2 for filleting.

On Sun, 24 Aug 2025 at 08:04, pca006132
[john.lck40@gmail.com](mailto:john.lck40@gmail.com) wrote:

____

Yes you can select sublist, but doing this is annoying. Ideally we should  
provide APIs to select edges formed due to intersection, or around certain  
features, for example.

On Sun, Aug 24, 2025, 10:05 Sanjeev Prabhakar
[sprabhakar2006@gmail.com](mailto:sprabhakar2006@gmail.com)  
wrote:

____

Your question is not completely clear to me. Are you saying some portion  
of the intersection line to convert to fillet?

That can be done by selecting those few points in the intersection line.  
So openscad should have a way to select a portion of a list.

On Sun, 24 Aug, 2025, 5:50 am pca006132,
[john.lck40@gmail.com](mailto:john.lck40@gmail.com) wrote:

____

OK, the method you are talking about doesn't seem new, and is not that  
general.

Another question is, if we want to support this, we will need a way to  
specify which edges the user wants (apart from being able to compute the  
points in openscad).  
On 8/23/25 22:14, Sanjeev Prabhakar wrote:

There are mainly 2 simpler ways which works for creating fillets

strategy 1 is explained in attached file.

Let me know, in case you have any questions

On Sat, 23 Aug 2025 at 10:52, Sanjeev Prabhakar <  
[sprabhakar2006@gmail.com](mailto:sprabhakar2006@gmail.com)> wrote:

____

Both are possible  
perfect radius fillets and visually appealing one  
I am attaching 2 files with very simple example, due to file size  
constraints

Will explain the strategies later in evening once I have some time

Yes, you can do that for sure. Here is strategy 2 for filleting. On Sun, 24
Aug 2025 at 08:04, pca006132 <john.lck40@gmail.com> wrote: > Yes you can
select sublist, but doing this is annoying. Ideally we should > provide APIs
to select edges formed due to intersection, or around certain > features, for
example. > > On Sun, Aug 24, 2025, 10:05 Sanjeev Prabhakar
<sprabhakar2006@gmail.com> > wrote: > >> Your question is not completely clear
to me. Are you saying some portion >> of the intersection line to convert to
fillet? >> >> That can be done by selecting those few points in the
intersection line. >> So openscad should have a way to select a portion of a
list. >> >> On Sun, 24 Aug, 2025, 5:50 am pca006132, <john.lck40@gmail.com>
wrote: >> >>> OK, the method you are talking about doesn't seem new, and is
not that >>> general. >>> >>> Another question is, if we want to support this,
we will need a way to >>> specify which edges the user wants (apart from being
able to compute the >>> points in openscad). >>> On 8/23/25 22:14, Sanjeev
Prabhakar wrote: >>> >>> There are mainly 2 simpler ways which works for
creating fillets >>> >>> strategy 1 is explained in attached file. >>> >>> Let
me know, in case you have any questions >>> >>> >>> On Sat, 23 Aug 2025 at
10:52, Sanjeev Prabhakar < >>> sprabhakar2006@gmail.com> wrote: >>> >>>> Both
are possible >>>> perfect radius fillets and visually appealing one >>>> I am
attaching 2 files with very simple example, due to file size >>>> constraints
>>>> >>>> Will explain the strategies later in evening once I have some time
>>>> >>>>

[ __filletin_strategy_2.pdf(215.62 KB)
](https://lists.openscad.org/empathy/attachment/678470 "application/pdf")

[Next
page](https://lists.openscad.org/empathy/thread/DVVMNGT5PZ5EBV53TU7XS3HZWQMZ66GS?page=2)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

