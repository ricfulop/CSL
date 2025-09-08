---
url: https://lists.openscad.org/empathy/thread/BRYO7Y5ZUBWHBSP6OQOB5DKMUX7VOVQ2
scraped_at: 2025-09-08T16:28:23.652441
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

###  Why namespace keyword

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Wed, Aug 27, 2025 9:53 PM

Programming is communicating with a machine and communicating with  
others (including your future self) who reuse, adapt, and extend your  
program.

This proposed namespace keyword and functionality clearly communicates  
to the machine that library names should not be shared with the user's  
names.

To the human, it clearly communicates the author's intention to have  
separate names. It reuses the existing syntax and layout, making  
adoption trivial for existing libraries:

namespace bosl2_threading {  
using bosl2_utility;  
using bosl2_skin;  
using bosl2_attachable;  
using bosl2_lists;  
using bosl2_shapes3d;  
module generic_nut() {...} // Exact same code as before indented once  
}

With object() as namespaces, the namespace names share the  
assignment/variable environment, still causing collisions. The syntax  
requires rewriting the code to function literals instead of `function`  
keyword definition and wait for module literals to be implemented before  
then rewriting all `method` definitions and every reference to other  
libraries must be individually updated:

bosl2_threading = object(  
generic_nut = module() {  
// Make assignments for every single module and function declared  
in bosl2_threading:  
all_positive = bosl2.utility.all_positive;  
first_defined = bosl2.utility.first_defined;  
linear_sweep = bosl2.skin.linear_sweep;  
attachable = bosl2.attachable.attachable;  
in_list = bosl2.lists.in_list;  
cyl = bosl2.shapes3d.cyl;

// Rest of the existing code  
}  
}

A draft PR is under way  
<https://github.com/openscad/openscad/pull/6131>. I expect to have it  
working in 1.5 weeks or sooner. In the next couple days I should have  
`using` working; at that point others can start playing with it if desired.

Technical discussion is happening on the original Namespace Issue  
<https://github.com/openscad/openscad/issues/522>.

This isn't exclusive with whether to treat `object` as a limited form of  
OO with `this`.

  * Cory Cross

Programming is communicating with a machine and communicating with others
(including your future self) who reuse, adapt, and extend your program. This
proposed namespace keyword and functionality clearly communicates to the
machine that library names should not be shared with the user's names. To the
human, it clearly communicates the author's intention to have separate names.
It reuses the existing syntax and layout, making adoption trivial for existing
libraries: namespace bosl2_threading { using bosl2_utility; using bosl2_skin;
using bosl2_attachable; using bosl2_lists; using bosl2_shapes3d; module
generic_nut() {...} // Exact same code as before indented once } With object()
as namespaces, the namespace names share the assignment/variable environment,
still causing collisions. The syntax requires rewriting the code to function
literals instead of `function` keyword definition and wait for module literals
to be implemented before then rewriting all `method` definitions and every
reference to other libraries must be individually updated: bosl2_threading =
object( generic_nut = module() { // Make assignments for every single module
and function declared in bosl2_threading: all_positive =
bosl2.utility.all_positive; first_defined = bosl2.utility.first_defined;
linear_sweep = bosl2.skin.linear_sweep; attachable =
bosl2.attachable.attachable; in_list = bosl2.lists.in_list; cyl =
bosl2.shapes3d.cyl; // Rest of the existing code } } A draft PR is under way
<https://github.com/openscad/openscad/pull/6131>. I expect to have it working
in 1.5 weeks or sooner. In the next couple days I should have `using` working;
at that point others can start playing with it if desired. Technical
discussion is happening on the original Namespace Issue
<https://github.com/openscad/openscad/issues/522>. This isn't exclusive with
whether to treat `object` as a limited form of OO with `this`. \- Cory Cross

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

