---
url: https://cad.onshape.com/FsDoc/annotations.html
scraped_at: 2025-09-08T14:26:08.320202
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

# Annotations

Top level declarations, enumeration values, and statements may have
_annotations_. An annotation is a set of key+value pairs written as a map
literal. Annotations are interpreted by system software and are not visible to
programs.

Annotation keys should be strings.

Annotation values are usually strings or enumerations, but other valid
expressions may be used. However, these expressions do not have access to
function local variables even if they appear inside a function. The system may
ignore erroneous values.

Annotations are used to define the user interface for features. For example,
consider the definition

    
    
    export enum BooleanOperationType
    {
        annotation {"Name" : "Union"}
        UNION,
        annotation {"Name" : "Subtract"}
        SUBTRACTION,
        annotation {"Name" : "Intersect"}
        INTERSECTION,
        annotation {"Hidden" : true}
        SUBTRACT_COMPLEMENT
    }
    

The annotations take effect when `BooleanOperationType` is used as a feature
parameter. Then the names appear in the feature menu except for the hidden
value which is not available to users. (In this case the hidden value is meant
for use in FeatureScript code.)

A feature has an annotation like

    
    
    annotation { "Feature Type Name" : "Fillet" }
    

The "Feature Type Name" is required on all features.

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

