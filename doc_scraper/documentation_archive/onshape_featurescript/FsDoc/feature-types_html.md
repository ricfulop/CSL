---
url: https://cad.onshape.com/FsDoc/feature-types.html
scraped_at: 2025-09-08T14:25:55.273104
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

# Defining feature types

Features are the fundamental unit of CAD, and they are also the fundamental
unit of FeatureScript. The FeatureScript inside a feature type can encompass
anything from attaching some commonly used geometry, to wrapping one of
Onshape's features in a more convenient interface, to generating a full part
in one feature.

A simple example of a feature type definition is below:

    
    
    annotation { "Feature Type Name" : "Fillet Everything" }
    export const filletEverything = defineFeature(function(context is Context, id is Id, definition is map)
        precondition
        {
            annotation { "Name" : "Fillet radius" }
            isLength(definition.filletRadius, BLEND_BOUNDS);
        }
        {
            opFillet(context, id + "fillet1", {
                    "entities" : qBodyType(qEverything(EntityType.EDGE), BodyType.SOLID),
                    "radius" : definition.filletRadius
            });
        });
    

The input to this feature type is defined in the `precondition` block of code,
which defines a one-dimensional length parameter named "Fillet radius".

The behavior of the feature is defined in the bottom block of code. The
statement inside that block calls the [`opFillet`](library.html#opFillet-
Context-Id-map) operation (the same one used in Onshape's fillet feature). The
`radius` of the fillet is set to the `filletRadius` provided by the user. The
`entities` to fillet are defined with a [`Query`](library.html#module-
query.fs) for every edge in the Part Studio.

![Fillet everything at end of feature tree](tutorials/images/fillet-
everything-1.png)

The FeatureScript inside a custom feature gets executed as part of the Part
Studio's regeneration. This means the code inside the feature type function
will run for every instance of the feature, every time its context or its
definition changes, including:

  * When the feature is first added.
  * When one of its definition's parameters (i.e. `filletRadius`) gets updated.
  * When any upstream feature is modified, deleted, or suppressed
  * When the rollback bar moves from before to after the feature

Moving the Fillet Everything feature up in the feature tree will cause it to
fillet only the edges which were defined when the Fillet Everything feature
was created: ![Fillet everything before hole](tutorials/images/fillet-
everything-2.png)

Suppressing an extrude above the Fillet Everything feature (and thus removing
edges) notably will NOT cause the Fillet Everything feature to break with an
error like "missing edges". This is because no explicit references to the
edges are passed into or stored by the feature. Rather, the feature
reevaluates the edge `Query` every time the feature is run.

![Fillet everything with extrude 3 suppressed](tutorials/images/fillet-
everything-3.png)

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

