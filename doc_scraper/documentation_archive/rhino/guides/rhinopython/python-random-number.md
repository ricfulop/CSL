---
url: https://developer.rhino3d.com/guides/rhinopython/python-random-number/
scraped_at: 2025-09-08T15:37:57.172965
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

[Generating Random Numbers in
Python](https://developer.rhino3d.com/guides/rhinopython/python-random-
number/)

  * Overview
  * Simple Random numbers
  * Advanced Random numbers
  * Choosing Randomly
  * Os and System Random
  * Related Links

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Generating Random Numbers in Python

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, December 5, 2018)

## Overview

Python comes with a random number generator which can be used to generate
various distributions of numbers. These random number generators are suitable
for generating numbers for spacial and graphical distributions. To access the
random number generators, the `random` module must be imported.

IMPORTANT NOTE: The pseudo-random generators of this module should not be used
for security purposes. Use `os.urandom()` or `SystemRandom` if you require a
cryptographically secure pseudo-random number generator.

## Simple Random numbers

The basic method to create a random number from the imported `random` module
is with `random.random()`

    
    
    import random
    
    ran_number = random.random()
    print ran_number
    

The output from the above code is a random number between 0 and 1, say
0.280268102083 The number can be used directly or to arrive at some other
number:

    
    
    import random
    import rhinoscriptsyntax as  rs
    
    ran_number = random.random()
    degrees =  ran_number*360
    id = rs.GetObject("Select an object to rotate randomly around the CPlane origin")
    if id:
        rs.RotateObject(id,[0,0,0], degrees)
    

Use `random.uniform()` to generate a random number between two numbers other
than zero and 1:

    
    
    import random
    
    low = 4; high = 8
    ran_number = random.uniform(low, high)
    print ran_number
    

The above would generate a random number between 4 and 8. Note for
random.uniform low and high numbers must be specified.

## Advanced Random numbers

For graphic and special random distributions, many times better distributions
can be generated using one of the advanced distributions. These random numbers
can generate cumulative distribution functions. There are functions to compute
[uniform](https://en.wikipedia.org/wiki/Uniform_distribution_%28continuous%29),
[normal (Gaussian)](https://en.wikipedia.org/wiki/Normal_distribution),
[lognormal](https://en.wikipedia.org/wiki/Log-normal_distribution), [negative
exponential](https://en.wikipedia.org/wiki/Exponential_distribution),
[gamma](https://en.wikipedia.org/wiki/Gamma_distribution), and
[beta](https://en.wikipedia.org/wiki/Beta_distribution) distributions. For
generating distributions of angles, the [von Mises
distribution](https://en.wikipedia.org/wiki/Von_Mises_distribution) is also
available.

For more detailed information on these advanced number generators go to the
[Generate pseudo-random numbers
documentation](https://docs.python.org/2/library/random.html)

The random module contains functions for finding random integers, selection of
a random element from a list, a function to generate a random permutation of a
list in-place, for random sampling with and without replacement, etc.

The Random number generator may also be started with a seed number.
`random.seed(seed_number)` When a seed is used, the generator can create a
repeatable set of pseudo-random numbers. If repeatability is important, this
may be worth using. Normally the current system time is used which leads to a
different solution each time.

## Choosing Randomly

The random functions also have the ability to choose a random element from a
list. The following code will print a random selection from the string
containing the alphabet. Note that processing a string of characters is
equivalent to processing a list of the characters in the string.

    
    
    import random
    
    print random.choice('abcdefghijklmnopqrstuvmxyz')  
    ​```
    
    `random` can also generate a set of samples from a larger list of values. The following code will return 3 randomly chosen samples from the list of numbers.
    
    ​```python
    import random
    my_list = [1, 2, 3, 4, 5]
    my_samp = 3
    print random.sample(my_list,  my_samp)
    

For more detailed information on these advanced methods go to the [Generate
pseudo-random numbers
documentation](https://docs.python.org/2/library/random.html)

## Os and System Random

For a random number generator that does not rely on the software state and for
which the sequences are not reproducible, use the SystemRandom method. This
function returns random bytes from an OS-specific randomness source.

    
    
    import sys
    import random
    
    key_num = random.SystemRandom()
    print key_num.random() #produces a number between 0 and 1
    print key_num.randint(0, sys.maxint) # produces a integer between 0 and the highest allowed by the OS.
    

## Related Links

  * [Generate pseudo-random numbers documentation](https://docs.python.org/2/library/random.html)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
random-number/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
random-number/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

