---
url: https://cad.onshape.com/FsDoc/relational.html
scraped_at: 2025-09-08T14:26:10.333356
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

# Equality and ordering

There is a total order on FeatureScript values. Given any pair of values,
either one is less than the other or they are equal.

Any two values can be tested for equality with `==` and inequality with `!=`.
By definition, inequality is the opposite of equality.

FeatureScript does not have degrees of equality. There is no distinction like
JavaScript's `==` and `===` or Scheme's `eq?`, `eqv?`, and `equal?`.

Two values are equal if they have the same underlying type, same type tag (if
any), and satisfy the obvious equality relationship for the standard type.

  * Equal numbers are equal, and positive and negative zero are also equal.
  * Maps are equal if all the key-value pairs are equal.
  * Arrays are equal if they are the same length and corresponding values are equal.
  * Boxes are equal to themselves and not equal to other boxes that happen to hold the same value.
  * Lambda functions are equal if they were created by the same function definition and bound values (values captured from an enclosing block scope) are equal. Otherwise functions are not equal, even if their definitions are identical. (Top-level functions are not values and can not be tested for equality.)

Like all binary operators, `==` and `!=` evaluate their operands left to
right. (Exponentiation associates right to left, but evaluates left to right.)

Numbers may be compared with the `<` operator. Operator `<` may also be
overloaded for use with values with type tags.

Values also have an internal order. This order is visible when values are used
as map keys; iteration over a map proceeds in key order. This order does not
otherwise affect execution. Overloading operator `<` does not change this
order.

The internal order on values looks first at type tag, then at basic type, then
at value for two values with the same type.

Standard types sort in the order

  1. `undefined`
  2. `boolean`
  3. `number`
  4. `string`
  5. `array`
  6. `map`
  7. `box`
  8. `builtin`
  9. `function`

Type tags sort in the order they are declared, and after all predefined types.
Declaration order is a global property based on when a module is first seen in
the graph of imports. A module can not force a particular declaration order by
reordering its own imports. So type tag order is deterministic, but not
necessarily predictable except for two type tags defined in the same module.

If both values have the same type tag, the type comparison repeats with the
standard type. For example, given the type definition

    
    
    predicate anything(x) { true; }
    type Anything typecheck anything;
    

the value `0` comes before `true as Anything` but `true as Anything` comes
before `0 as Anything`.

If two objects of the same type are not equal, order is defined by these
rules.

  * `false` sorts before `true`
  * Numbers follow the obvious order, except `-0` and `0` are the same.
  * Strings sort by Unicode character values, not in any language-related collating sequence.
  * Arrays sort first by size, and then based on the first unequal element.
  * Maps sort as if they were arrays of [key,value] arrays sorted by key.
  * Boxes sort by order of creation.
  * Builtins sort by order of creation.
  * Functions sort first by an arbitrary order on all expression function declarations, and then by bound values compared in an arbitrary but deterministic order.

Enums can also be compared with comparison operators as long as the same enum
(same type, element, and version) is on both sides of the comparison. `EnumA.X
< EnumA.Y` will evaluate to `true` if `X` comes before `Y` in the definition
of `EnumA`, but `EnumA.X < EnumB.Y` will throw an error.

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

