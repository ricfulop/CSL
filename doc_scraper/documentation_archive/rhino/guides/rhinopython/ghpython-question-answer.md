---
url: https://developer.rhino3d.com/guides/rhinopython/ghpython-question-answer/
scraped_at: 2025-09-08T15:37:16.001764
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

[GhPython Common Questions and
Answers](https://developer.rhino3d.com/guides/rhinopython/ghpython-question-
answer/)

    * How can I use the rhinoscriptsyntax?
    * How can I use RhinoCommon?
    * What is “ghdoc” and how does it relate to the rhinoscriptsyntax?
    * Is RhinoScript use within GhPython less ideal than RhinoCommon?
    * Is the rhinoscriptsyntax target irrelevant if using solely RhinoCommon classes?
    * Are there RhinoScript and/or RhinoCommon objects which are not recognized as valid Grasshopper geometry?
    * How do I use DataTree’s?
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

GhPython Common Questions and Answers

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, December 5, 2018)

The GhPython component allows to use both RhinoCommon and RhinoScript from
within Grasshopper. Here some Q&As.

### How can I use the rhinoscriptsyntax?

By importing RhinoScript, for example by writing:

`import rhinoscriptsyntax as rs`

…and then calling some rhinoscript functions…

    
    
    import rhinoscriptsyntax as rs
    
    line = rs.AddLine((1, 2, 3), (10, 11, 12))
    a = line
    

### How can I use RhinoCommon?

By importing from the Rhino module, for example by writing:

`from Rhino.Geometry import Point3d, Line`

…and then assigning some new geometry to the results

    
    
    from Rhino.Geometry import Point3d, Line
    
    a = Line(Point3d(1, 2, 3), Point3d(10, 11, 12))
    

### What is “ghdoc” and how does it relate to the rhinoscriptsyntax?

The `ghdoc` variable is provided by the component for better RhinoScript
library support.

This library is imperative, and it is build from a set of functions that act
on geometrical types through one level of indirection: most of the time, the
user does not work with the geometry itself but with an identifier (Guid) of
geometry that is present in a document.

This is exactly what ghdoc is: it is a reference to the document that the
RhinoScript library implicitly targets with all Add__() calls (for example,
AddLine()).

The scriptcontext module has a doc variable with the currently active
document, that can be assigned by you to ghdoc, or RhinoDoc.ActiveDoc, the
Rhino document.

### Is RhinoScript use within GhPython less ideal than RhinoCommon?

While targeting the `ghdoc` variable, the special Grasshopper document is
used, therefore we can use Grasshopper while leaving the Rhino document
unchanged. This saves uncountable Undo’s, and makes it easy to structure ideas
through the Grasshopper definition.

This means that both RhinoCommon or RhinoScript are good in practice.

### Is the rhinoscriptsyntax target irrelevant if using solely RhinoCommon
classes?

Yes. If you create class instances (objects), you will need to create also
your own collection objects to store them (mostly lists, trees). You can
imagine the `ghdoc` as being an alternative to them, just that you do not
access data by index (number), but by Guid. So you can use the RhinoScript or
the RhinoCommon libraries independently or mix them. The RhinoScript
implementation in Rhino is open-source and is all written in RhinoCommon. Also
the `ghdoc` implementation is open-source, and is here.

### Are there RhinoScript and/or RhinoCommon objects which are not recognized
as valid Grasshopper geometry?

Yes, sure, Grasshopper handles only a portion of all available types.

Basically, unhandled types are all the types that do not exists in the
‘Params’ tab.

For example, there is no text dot and no leader. When/if Grasshopper one day
will support these types, these calls will be implemented.

### How do I use DataTree’s?

[Here](http://www.grasshopper3d.com/forum/topics/datatreelistitem-access-from)
is a small sample.

However, 80% of the times it is not necessary to program for DataTrees, as the
logic itself can be applied per-list and Grasshopper handles list-iteration.

**If you have more questions, please go to the[Rhino Developers
Forum](https://discourse.mcneel.com/c/rhino-developer)**

## Related Topics

  * [Your first script with Python in Grasshopper](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [What is Python and RhinoScript?](https://developer.rhino3d.com/guides/rhinopython/what-is-rhinopython/)
  * [Editing Python in Grasshopper](https://developer.rhino3d.com/guides/rhinopython/python-running-scripts/)
  * [Python Guide for Rhino](https://developer.rhino3d.com/guides/rhinopython/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/ghpython-
question-answer/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/ghpython-
question-answer/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

