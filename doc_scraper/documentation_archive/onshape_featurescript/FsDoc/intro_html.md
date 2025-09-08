---
url: https://cad.onshape.com/FsDoc/intro.html
scraped_at: 2025-09-08T14:25:54.273856
title: Untitled
---

[FeatureScript](index.html)  
  
[Welcome to FeatureScript](index.html)

  * [_Tutorials_](tutorials/create-a-slot-feature.html)
  * [ _Standard Library documentation_](library.html)
  * [ _Standard Library source_](/documents/12312312345abcabcabcdeff)

[FeatureScript guide](intro.html)

  * [Introduction](intro.html)
  * [Defining feature types](feature-types.html)
  * [Feature UI](uispec.html)
  * [Feature output](output.html)
  * [Values and types](variables.html)
  * [Modeling](modeling.html)
  * [Custom tables](tables.html)
  * [Computed part properties](computed-part-properties.html)
  * [Imports](imports.html)
  * [Debugging in Feature Studios](debugging-in-feature-studios.html)

[Language reference](tokens.html)

  * [Lexical conventions](tokens.html)
  * [Types and type tags](type-tags.html)
  * [Top-level constructs](top-level.html)
  * [Syntax and semantics](syntax.html)
  * [Annotations](annotations.html)
  * [Exception handling](exceptions.html)
  * [Equality and ordering](relational.html)

# Introduction

### FeatureScript in Onshape

Onshape's Part Studios are written in FeatureScript. User actions that modify
a Part Studio, under the hood, actually modify a representation of the Part
Studio consisting of FeatureScript code.

You can see the underlying FeatureScript of any Part Studio by right-clicking
its tab and clicking "Show code": ![FeatureScript in
Onshape](tutorials/images/part-studio-code.png)

The individual components of a Part Studio's FeatureScript are familiar
concepts for programmers of other languages:

  * A _feature type_ is a FeatureScript _function_.
    * The feature types in Onshape's default toolbar (like extrude and helix) are defined as functions in the [Onshape Standard Library](library.html).
    * Custom feature types are defined in Feature Studios.
  * A _feature_ in the feature tree is a _function call_.
  * Feature _parameters_ are contained in the function's _arguments_.
  * A _Part Studio_ defines a _build function_ , containing a function call for every feature.
  * The _geometry_ of a Part Studio is the _output_ of the build function.
  * Part Studio _regeneration_ , triggered when features are updated, is _execution_ of the build function.
  * The _rollback bar_ is a _return statement_ in the build function, causing subsequent features not to run.

In addition to custom features, FeatureScript can be used to define [custom
tables](tables.html) as functions that compute the data in the table by
executing once a Part Studio has finished regenerating.

### Feature Studios

Feature types (along with other user-defined functions, types, etc.) are
defined in Feature Studios within Onshape documents. Onshape's standard
features are defined in the Feature Studios of a [public
document](/documents/12312312345abcabcabcdeff), where their source code may be
viewed.

Feature Studios, Part Studios, and many types of data tabs in Onshape have a
FeatureScript representation. These tabs, called "modules", can be
[imported](imports.html) into Feature Studios, either in the same document or
from versions of linked documents. This consistent interface makes code and
data reuse simple and reliable.

One consequence of Feature Studios living inside Onshape documents is that
they share the version control and sharing systems used by the rest of
Onshape, complete with permissions, versions, branches, and a full history of
edits.

Feature Studios are implemented based on the [Ace](https://ace.c9.io/) editor
and many Ace [shortcuts](https://github.com/ajaxorg/ace/wiki/Default-Keyboard-
Shortcuts) work in a Feature Studio.

### Language fundamentals

FeatureScript's basic syntax is designed to look and feel familiar to
programmers of other C-family languages like C++, JavaScript, or Java. The
language is fully whitespace insensitive, and FeatureScript statements always
end in a semicolon. `/* block comments */` and `// end of line comments` can
be added in the standard way.

Determinism is a core principle of FeatureScript. At Onshape we believe that
models must regenerate the same way every time, everywhere. Thus,
FeatureScript has no concept of undefined behavior, and execution cannot be
influenced by external input, time, or randomness.

FeatureScript discourages hidden state and shared references. Value semantics
are used everywhere, and when references are needed, a distinctive syntax
(using [boxes](variables.html#box)) makes it obvious. Assignment, argument
passing, and function return values all behave as if making deep copies.

### Clean geometric calculation

FeatureScript is strongly typed and dynamically typed, and overloads for
functions and operators can be cleanly defined for each FeatureScript type.

The Standard Library defines natural overloads for operators (like `+` and
`*`) on geometric types (like `Vector` and `Transform`). This makes
calculations involving these types simple and readable:

    
    
    var v is Vector = vector(1, 2) + vector(3, 4);
    var transformedPoint = transform2 * transform1 * originalPoint;
    

FeatureScript is also a natural fit for working with units. Operator overloads
are defined to create a `ValueWithUnits`:

    
    
    const width is ValueWithUnits = 1.5 * inch;
    const angle is ValueWithUnits = 30 * degree;
    const area  is ValueWithUnits = 12 * centimeter^2;
    

These values know their own dimensionality (length, angle, etc.), but don't
differentiate unit systems (like meters vs. inches) making `1 * meter` equal
to and indistinguishable from `1000 * millimeter`.

Overloads on `ValueWithUnits` make math with units straightforward:

    
    
    var squareArea = (3 * meter + 3 * inch)^2;                              // Has area units
    
    var pendulumPeriod = 2 * PI * sqrt(armLength / (9.8 * meter/second^2)); // Has time units
    
    var numberOfBricks = floor(wallLength / brickLength);                   // Has no units
    
    var nonsense = (3 * meter) + (3 * degree);                              // Throws an error from unit mismatch
    

Values with units also play nicely with vectors and transforms. The code below
asserts that a point transformed by rotation around the z-axis is equal to the
same point constructed trigonometrically:

    
    
    const start is Vector = vector(2, 0, 0) * inch;
    const zAxis is Line   = line(vector(0, 0, 0) * inch, vector(0, 0, 1));
    const end   is Vector = rotationAround(zAxis, 30 * degree) * start;
    
    const goal  is Vector = vector(cos(30 * degree), sin(30 * degree), 0) * (2 * inch);
    
    println(tolerantEquals(end, goal)); // Prints "true"
    

For more on units, vectors, geometry, and other math in FeatureScript, see the
[math section](library.html#category-Math) of the Standard Library
documentation.

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

