---
url: https://developer.rhino3d.com/guides/rhinopython/python-operators/
scraped_at: 2025-09-08T15:37:23.016039
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

[Python Operators](https://developer.rhino3d.com/guides/rhinopython/python-
operators/)

  * Overview
  * Operator Precedence
    * Arithmetic
    * Comparison
    * Logical
  * Considerations
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

Python Operators

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated: Friday,
March 6, 2020)

## Overview

Python has a full range of operators, including arithmetic operators,
comparison operators, concatenation operators, and logical operators.

## Operator Precedence

When several operations occur in an expression, each part is evaluated and
resolved in a predetermined order called operator precedence. You can use
parentheses to override the order of precedence and force some parts of an
expression to be evaluated before others. Operations within parentheses are
always performed before those outside. Within parentheses, however, standard
operator precedence is maintained.

When expressions contain operators from more than one category, arithmetic
operators are evaluated first, comparison operators are evaluated next, and
logical operators are evaluated last. Comparison operators all have equal
precedence; that is, they are evaluated in the left-to-right order in which
they appear. Arithmetic and logical operators are evaluated in the following
order of precedence.

### Arithmetic

Description |  | Symbol  
---|---|---  
Exponentiation |  | `**`  
Unary negation |  | `-`  
Multiplication |  | `*`  
Division |  | `/`  
Integer Division |  | `//`  
Modulus arithmetic |  | `%`  
Addition |  | `+`  
Subtraction |  | `-`  
String concatenation |  | `+`  
  
### Comparison

Description |  | Symbol  
---|---|---  
Less than |  | `<`  
Greater than |  | `>`  
Less than or equal to |  | `<=`  
Greater than or equal to |  | `>=`  
Equality |  | `==`  
Inequality |  | `!=`  
Object equivalence |  | `is`  
  
### Logical

Description |  | Symbol  
---|---|---  
Logical negation |  | `not`  
Logical conjunction |  | `and`  
Logical disjunction |  | `or`  
  
## Considerations

When multiplication and division occur together in an expression, each
operation is evaluated as it occurs from left to right. Likewise, when
addition and subtraction occur together in an expression, each operation is
evaluated in order of appearance from left to right.

The string concatenation (`+`) operator is not an arithmetic operator, but in
precedence it falls after all arithmetic operators and before all comparison
operators. The `is` operator is an object reference comparison operator. It
does not compare objects or their values; it checks only to determine if two
object references refer to the same object.

## Related Topics

  * [What are VBScript and RhinoScript?](https://developer.rhino3d.com/guides/rhinoscript/what-are-vbscript-rhinoscript/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
operators/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
operators/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

