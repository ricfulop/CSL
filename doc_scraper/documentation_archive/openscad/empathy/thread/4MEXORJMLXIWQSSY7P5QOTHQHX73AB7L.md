---
url: https://lists.openscad.org/empathy/thread/4MEXORJMLXIWQSSY7P5QOTHQHX73AB7L
scraped_at: 2025-09-08T16:28:19.644343
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

###  Namespaces support individual references in PR#6131

![](https://www.gravatar.com/avatar/5b8f418b34c9f0aba41426ab5c732a2c?d=blank&s=100)

CC

Cory Cross

Mon, Sep 1, 2025 10:45 PM

Namespaces have basic functionality for early testers to try out!

You'll need to build from my PR:  
<https://github.com/openscad/openscad/pull/6131>

Current remaining issues:

  * Namespaces defined in a `use<>` do not work.
  * use<> does not work inside namespaces
  * No top-level assert() or echo() allowed

So `namespace bosl2 { include<bosl2/std.scad> }` does not yet work. But  
you can do:

namespace explicit {  
module cuboid(s) {  
off = is_list(s) ? s[0] : s;  
translate([-off/2,0,0]) cube(s,center=true);  
}  
}

namespace implicit {  
favorite = "green";  
}

include<BOSL2/std.scad>  
using implicit;

color(favorite) right(5) cuboid(5);  
explicit::cuboid([8,25,30]);

The tests (serving as further examples) are available in this commit  
<https://github.com/openscad/openscad/tree/1b5200a10c32c151f02249565d6d77a6dc7421bd/tests/data/scad/namespaces>  
and are all passing!

-Cory

Namespaces have basic functionality for early testers to try out! You'll need
to build from my PR: https://github.com/openscad/openscad/pull/6131 Current
remaining issues: * Namespaces defined in a `use<>` do not work. * use<> does
not work inside namespaces * No top-level assert() or echo() allowed So
`namespace bosl2 { include<bosl2/std.scad> }` does not yet work. But you can
do: namespace explicit { module cuboid(s) { off = is_list(s) ? s[0] : s;
translate([-off/2,0,0]) cube(s,center=true); } } namespace implicit { favorite
= "green"; } include<BOSL2/std.scad> using implicit; color(favorite) right(5)
cuboid(5); explicit::cuboid([8,25,30]); The tests (serving as further
examples) are available in this commit
<https://github.com/openscad/openscad/tree/1b5200a10c32c151f02249565d6d77a6dc7421bd/tests/data/scad/namespaces>
and are all passing! -Cory

[ ![Attached image](https://lists.openscad.org/empathy/image/679102/200)
](https://lists.openscad.org/empathy/attachment/679102)

Replying to:  Quote

Send Cancel

Empathy v1.0 2025 ©[emwd.com](https://emwd.com/)

[Documentation](https://docs.harmonylists.io/view/Main_Page)

