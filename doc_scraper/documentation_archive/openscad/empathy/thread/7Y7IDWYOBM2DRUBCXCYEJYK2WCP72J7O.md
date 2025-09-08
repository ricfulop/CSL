---
url: https://lists.openscad.org/empathy/thread/7Y7IDWYOBM2DRUBCXCYEJYK2WCP72J7O
scraped_at: 2025-09-08T16:28:27.682786
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

###  Should lambda functions be found in use<d> files?

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Mon, Aug 25, 2025 9:51 PM

xlib.scad:

x=function () "from_xlib";

my source file:

use<xlib.scad>  
echo(x());

WARNING: Ignoring unknown function 'x' in file test.scad, line 2

ECHO: undef

I think this is a bug, as variables from use files are available and  
functions are as well, so shouldn't variables which are lambda functions?

  * Cory

xlib.scad: x=function () "from_xlib"; my source file: use<xlib.scad>
echo(x()); WARNING: Ignoring unknown function 'x' in file test.scad, line 2
ECHO: undef I think this is a bug, as variables from use files are available
and functions are as well, so shouldn't variables which are lambda functions?
\- Cory

![](https://www.gravatar.com/avatar/095124c1792024c67a3336fc575ec4a6?d=blank&s=100)

NH

nop head

Mon, Aug 25, 2025 9:53 PM

No variables are not available from used files.

On Mon, 25 Aug 2025, 22:51 Cory Cross via Discuss, <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

xlib.scad:

x=function () "from_xlib";

my source file:

use<xlib.scad>  
echo(x());

WARNING: Ignoring unknown function 'x' in file test.scad, line 2

ECHO: undef

I think this is a bug, as variables from use files are available and  
functions are as well, so shouldn't variables which are lambda functions?

  * Cory

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

No variables are not available from used files. On Mon, 25 Aug 2025, 22:51
Cory Cross via Discuss, < discuss@lists.openscad.org> wrote: > xlib.scad: > >
x=function () "from_xlib"; > > my source file: > > use<xlib.scad> > echo(x());
> > WARNING: Ignoring unknown function 'x' in file test.scad, line 2 > > ECHO:
undef > > I think this is a bug, as variables from use files are available and
> functions are as well, so shouldn't variables which are lambda functions? >
> \- Cory > _______________________________________________ > OpenSCAD mailing
list > To unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Mon, Aug 25, 2025 10:34 PM

Ugh I'm always confused because bosl2 uses include and we're discussing why
more-or-less in the other threads. Thanks.

On August 25, 2025 5:53:26 PM EDT, nop head via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

No variables are not available from used files.

On Mon, 25 Aug 2025, 22:51 Cory Cross via Discuss, <  
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

xlib.scad:

x=function () "from_xlib";

my source file:

use<xlib.scad>  
echo(x());

WARNING: Ignoring unknown function 'x' in file test.scad, line 2

ECHO: undef

I think this is a bug, as variables from use files are available and  
functions are as well, so shouldn't variables which are lambda functions?

  * Cory

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Ugh I'm always confused because bosl2 uses include and we're discussing why
more-or-less in the other threads. Thanks. On August 25, 2025 5:53:26 PM EDT,
nop head via Discuss <discuss@lists.openscad.org> wrote: >No variables are not
available from used files. > >On Mon, 25 Aug 2025, 22:51 Cory Cross via
Discuss, < >discuss@lists.openscad.org> wrote: > >> xlib.scad: >> >>
x=function () "from_xlib"; >> >> my source file: >> >> use<xlib.scad> >>
echo(x()); >> >> WARNING: Ignoring unknown function 'x' in file test.scad,
line 2 >> >> ECHO: undef >> >> I think this is a bug, as variables from use
files are available and >> functions are as well, so shouldn't variables which
are lambda functions? >> >> \- Cory >>
_______________________________________________ >> OpenSCAD mailing list >> To
unsubscribe send an email to discuss-leave@lists.openscad.org

![](https://www.gravatar.com/avatar/4ae585652404eee099c2b2e079e0c817?d=blank&s=100)

BC

Bob Carlson

Mon, Aug 25, 2025 11:28 PM

Yes, includes allow you to reference variables. Use does not.

____

On Aug 25, 2025, at 15:34, Cory Cross via
Discuss[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

Ugh I'm always confused because bosl2 uses include and we're discussing why
more-or-less in the other threads. Thanks.

On August 25, 2025 5:53:26 PM EDT, nop head via Discuss
[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org) wrote:

____

No variables are not available from used files.

On Mon, 25 Aug 2025, 22:51 Cory Cross via Discuss,
<[discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)
[mailto:discuss@lists.openscad.org](mailto:discuss@lists.openscad.org)> wrote:

____

xlib.scad:

x=function () "from_xlib";

my source file:

use<xlib.scad>  
echo(x());

WARNING: Ignoring unknown function 'x' in file test.scad, line 2 <>  
ECHO: undef

I think this is a bug, as variables from use files are available and functions
are as well, so shouldn't variables which are lambda functions?

  * Cory

* * *

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)
[mailto:discuss-leave@lists.openscad.org](mailto:discuss-
leave@lists.openscad.org)_______________________________________________

OpenSCAD mailing list  
To unsubscribe send an email to [discuss-
leave@lists.openscad.org](mailto:discuss-leave@lists.openscad.org)

Yes, includes allow you to reference variables. Use does not. > On Aug 25,
2025, at 15:34, Cory Cross via Discuss <discuss@lists.openscad.org> wrote: > >
Ugh I'm always confused because bosl2 uses include and we're discussing why
more-or-less in the other threads. Thanks. > > > > On August 25, 2025 5:53:26
PM EDT, nop head via Discuss <discuss@lists.openscad.org> wrote: >> No
variables are not available from used files. >> >> On Mon, 25 Aug 2025, 22:51
Cory Cross via Discuss, <discuss@lists.openscad.org
<mailto:discuss@lists.openscad.org>> wrote: >>> xlib.scad: >>> >>> x=function
() "from_xlib"; >>> >>> my source file: >>> >>> use<xlib.scad> >>> echo(x());
>>> >>> WARNING: Ignoring unknown function 'x' in file test.scad, line 2 <>
>>> ECHO: undef >>> >>> >>> I think this is a bug, as variables from use files
are available and functions are as well, so shouldn't variables which are
lambda functions? >>> >>> >>> \- Cory >>> >>>
_______________________________________________ >>> OpenSCAD mailing list >>>
To unsubscribe send an email to discuss-leave@lists.openscad.org
<mailto:discuss-
leave@lists.openscad.org>_______________________________________________ >
OpenSCAD mailing list > To unsubscribe send an email to discuss-
leave@lists.openscad.org

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

