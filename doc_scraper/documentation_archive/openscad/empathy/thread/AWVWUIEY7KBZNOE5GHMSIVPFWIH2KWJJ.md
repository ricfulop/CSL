---
url: https://lists.openscad.org/empathy/thread/AWVWUIEY7KBZNOE5GHMSIVPFWIH2KWJJ
scraped_at: 2025-09-08T16:28:10.616345
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

###  Please try out namespaces! Binaries available.

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Sun, Sep 7, 2025 2:51 AM

From the most recent update of PR#6131  
<https://github.com/openscad/openscad/pull/6131> come these builds:

Windows Build  
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27151/artifacts>  
Linux Build  
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27152/artifacts>

Please try out namespaces for yourself and add feedback on the pull  
request. More syntax examples available at the pull request page.

namespace bosl2 {  
include <BOSL2/std.scad>  
} import_specials;  
using bosl2;

textured_tile("trunc_diamonds", 20, tex_reps=[5,5]);

module cuboid(s) {  
bosl2::cuboid(s/2);  
}

color("green") left(20) bosl2::cuboid(10);  
color("red") right(20) cuboid(10);

Thanks,  
Cory Cross

From the most recent update of PR#6131
<https://github.com/openscad/openscad/pull/6131> come these builds: Windows
Build
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27151/artifacts>
Linux Build
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27152/artifacts>
Please try out namespaces for yourself and add feedback on the pull request.
More syntax examples available at the pull request page. namespace bosl2 {
include <BOSL2/std.scad> } import_specials; using bosl2;
textured_tile("trunc_diamonds", 20, tex_reps=[5,5]); module cuboid(s) {
bosl2::cuboid(s/2); } color("green") left(20) bosl2::cuboid(10); color("red")
right(20) cuboid(10); Thanks, Cory Cross

[ ![Attached image](https://lists.openscad.org/empathy/image/679610/200)
](https://lists.openscad.org/empathy/attachment/679610)

![](https://www.gravatar.com/avatar/d6de89c90e2e89a85dd10e6c3b5950e2?d=blank&s=100)

JB

Jon Bondy

Sun, Sep 7, 2025 9:18 AM

I can already write code that functions like this (I would call my  
cuboid() "MyCuboid()"), but is much less complex. Is this only  
compelling if I need to use two different libraries which have  
accidentally used the same name for different purposes? Is this solving  
problems for library creators or library users?

Jon

On 9/6/2025 10:51 PM, Cory Cross via Discuss wrote:

____

From the most recent update of PR#6131  
<https://github.com/openscad/openscad/pull/6131> come these builds:

Windows Build  
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27151/artifacts>  
Linux Build  
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27152/artifacts>

Please try out namespaces for yourself and add feedback on the pull  
request. More syntax examples available at the pull request page.

namespace bosl2 {  
include <BOSL2/std.scad>  
} import_specials;  
using bosl2;

textured_tile("trunc_diamonds", 20, tex_reps=[5,5]);

module cuboid(s) {  
bosl2::cuboid(s/2);  
}

color("green") left(20) bosl2::cuboid(10);  
color("red") right(20) cuboid(10);

Thanks,  
Cory Cross

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

\--  
This email has been checked for viruses by AVG antivirus software.  
[www.avg.com](http://www.avg.com)

I can already write code that functions like this (I would call my cuboid()
"MyCuboid()"), but is much less complex. Is this only compelling if I need to
use two different libraries which have accidentally used the same name for
different purposes? Is this solving problems for library creators or library
users? Jon On 9/6/2025 10:51 PM, Cory Cross via Discuss wrote: > From the most
recent update of PR#6131 > <https://github.com/openscad/openscad/pull/6131>
come these builds: > > Windows Build >
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27151/artifacts>
> Linux Build >
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27152/artifacts>
> > Please try out namespaces for yourself and add feedback on the pull >
request. More syntax examples available at the pull request page. > >
namespace bosl2 { > include <BOSL2/std.scad> > } import_specials; > using
bosl2; > > textured_tile("trunc_diamonds", 20, tex_reps=[5,5]); > > module
cuboid(s) { > bosl2::cuboid(s/2); > } > > color("green") left(20)
bosl2::cuboid(10); > color("red") right(20) cuboid(10); > > > > > Thanks, >
Cory Cross > > _______________________________________________ > OpenSCAD
mailing list > To unsubscribe send an email todiscuss-leave@lists.openscad.org
\-- This email has been checked for viruses by AVG antivirus software.
www.avg.com

[ ![Attached image](https://lists.openscad.org/empathy/image/679616/200)
](https://lists.openscad.org/empathy/attachment/679616)

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Sun, Sep 7, 2025 1:12 PM

On 9/7/25 2:18 AM, Jon Bondy via Discuss wrote:

____

Is this only compelling if I need to use two different libraries which  
have accidentally used the same name for different purposes?

It's certainly useful for that.

____

Is this solving problems for library creators or library users?

Every time you create something you want to reuse in another design, you  
are a library creator too!

-Cory

____

Jon

On 9/6/2025 10:51 PM, Cory Cross via Discuss wrote:

____

From the most recent update of PR#6131  
<https://github.com/openscad/openscad/pull/6131> come these builds:

Windows Build  
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27151/artifacts>  
Linux Build  
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27152/artifacts>

Please try out namespaces for yourself and add feedback on the pull  
request. More syntax examples available at the pull request page.

namespace bosl2 {  
include <BOSL2/std.scad>  
} import_specials;  
using bosl2;

textured_tile("trunc_diamonds", 20, tex_reps=[5,5]);

module cuboid(s) {  
bosl2::cuboid(s/2);  
}

color("green") left(20) bosl2::cuboid(10);  
color("red") right(20) cuboid(10);

Thanks,  
Cory Cross

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

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

<#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2>

* * *

OpenSCAD mailing list  
To unsubscribe send an email [todiscuss-
leave@lists.openscad.org](mailto:todiscuss-leave@lists.openscad.org)

On 9/7/25 2:18 AM, Jon Bondy via Discuss wrote: > > Is this only compelling if
I need to use two different libraries which > have accidentally used the same
name for different purposes? > It's certainly useful for that. > > Is this
solving problems for library creators or library users? > Every time you
create something you want to reuse in another design, you are a library
creator too! -Cory > Jon > > > On 9/6/2025 10:51 PM, Cory Cross via Discuss
wrote: >> From the most recent update of PR#6131 >>
<https://github.com/openscad/openscad/pull/6131> come these builds: >> >>
Windows Build >>
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27151/artifacts>
>> Linux Build >>
<https://app.circleci.com/pipelines/github/openscad/openscad/7166/workflows/d3d99684-c1da-45ec-9531-cc644eba3668/jobs/27152/artifacts>
>> >> Please try out namespaces for yourself and add feedback on the pull >>
request. More syntax examples available at the pull request page. >> >>
namespace bosl2 { >> include <BOSL2/std.scad> >> } import_specials; >> using
bosl2; >> >> textured_tile("trunc_diamonds", 20, tex_reps=[5,5]); >> >> module
cuboid(s) { >> bosl2::cuboid(s/2); >> } >> >> color("green") left(20)
bosl2::cuboid(10); >> color("red") right(20) cuboid(10); >> >> >> >> >>
Thanks, >> Cory Cross >> >> _______________________________________________ >>
OpenSCAD mailing list >> To unsubscribe send an email todiscuss-
leave@lists.openscad.org > > <http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> > Virus-free.www.avg.com >
<http://www.avg.com/email-
signature?utm_medium=email&utm_source=link&utm_campaign=sig-
email&utm_content=emailclient> > > > <#DAB4FAD8-2DD7-40BB-A1B8-4E2AA1F9FDF2> >
> _______________________________________________ > OpenSCAD mailing list > To
unsubscribe send an email todiscuss-leave@lists.openscad.org

[ ![Attached image](https://lists.openscad.org/empathy/image/679618/200)
](https://lists.openscad.org/empathy/attachment/679618)

![](https://www.gravatar.com/avatar/8373431929d88b3283f16eb4a4579039?d=blank&s=100)

JB

Jordan Brown

Sun, Sep 7, 2025 7:45 PM

On 9/7/2025 2:18 AM, Jon Bondy via Discuss wrote:

____

Is this solving problems for library creators or library users?

It's solving problems for library creators because when they add a new  
function they don't have to worry about it colliding with a function in  
some user's program.

It's solving problems for library users because when they add a new  
function they don't have to worry about it colliding with a library's  
function... including the function that the library adds in its next update.

("function" here really includes functions, modules, variables, and  
hopefully special variables.)

Indeed, namespacing is very similar to slapping a prefix on every name.  
The major differences are that inside the declaration you don't need to  
keep repeating the prefix, and if there's a "using" mechanism (as Cory  
proposes) then a caller can automatically add the prefix too.

BTW, while it's fairly unlikely that two libraries will use the same  
name for different purposes, it's not at all unlikely that they will use  
the same name for the _same_ purpose, but with slightly different  
arguments, return values, et cetera. Two libraries might well define  
regular_polygon(), but is it regular_polygon(size, sides) or  
regular_polygon(sides, size)? Or is it "vertexes" instead of "sides"?

On 9/7/2025 2:18 AM, Jon Bondy via Discuss wrote: > > Is this solving problems
for library creators or library users? > It's solving problems for library
creators because when they add a new function they don't have to worry about
it colliding with a function in some user's program. It's solving problems for
library users because when they add a new function they don't have to worry
about it colliding with a library's function... including the function that
the library adds in its next update. ("function" here really includes
functions, modules, variables, and hopefully special variables.) Indeed,
namespacing is very similar to slapping a prefix on every name. The major
differences are that inside the declaration you don't need to keep repeating
the prefix, and if there's a "using" mechanism (as Cory proposes) then a
caller can automatically add the prefix too. BTW, while it's fairly unlikely
that two libraries will use the same name for different purposes, it's not at
all unlikely that they will use the same name for the *same* purpose, but with
slightly different arguments, return values, et cetera. Two libraries might
well define regular_polygon(), but is it regular_polygon(size, sides) or
regular_polygon(sides, size)? Or is it "vertexes" instead of "sides"?

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

