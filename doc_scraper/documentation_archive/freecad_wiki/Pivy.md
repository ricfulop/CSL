---
url: https://wiki.freecad.org/Pivy
title: Pivy
scraped_at: 2025-09-08 16:41:45
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Introduction
  * 2 Scenegraph
  * 3 Callbacks
  * 4 Documentation Toggle Documentation subsection
    * 4.1 Older

# Pivy

  * [Page](/Pivy "View the content page \[ctrl-option-c\]")
  * [Discussion](/index.php?title=Talk:Pivy&action=edit&redlink=1 "Discussion about the content page \(page does not exist\) \[ctrl-option-t\]")

English

  * [Read](/Pivy)
  * [Edit](/index.php?title=Pivy&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Pivy&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Pivy.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Pivy&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Pivy)
  * [Edit](/index.php?title=Pivy&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Pivy&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Pivy&action=history)

General

  * [What links here](/Special:WhatLinksHere/Pivy "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Pivy "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Pivy&oldid=1605034 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Pivy&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Pivy&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Pivy&action=page&filter=&language=en)This is the approved revision of this
page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Pivy&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Pivy/id "Pivy \(3% translated\)")
  * [Deutsch](/Pivy/de "Pivy \(100% translated\)")
  * English
  * [Türkçe](/Pivy/tr "Pivy \(3% translated\)")
  * [español](/Pivy/es "Pivy \(19% translated\)")
  * [français](/Pivy/fr "Pivy \(100% translated\)")
  * [italiano](/Pivy/it "Pivy \(100% translated\)")
  * [polski](/Pivy/pl "Pivy \(100% translated\)")
  * [português do Brasil](/Pivy/pt-br "Pivy \(3% translated\)")
  * [română](/Pivy/ro "Pivy \(19% translated\)")
  * [svenska](/Pivy/sv "Pivy \(19% translated\)")
  * [čeština](/Pivy/cs "Pivy \(3% translated\)")
  * [русский](/Pivy/ru "Pivy \(74% translated\)")
  * [日本語](/Pivy/ja "Pivy/ja \(16% translated\)")

![](/images/6/6f/Arrow-left.svg) [Scenegraph](/Scenegraph "Scenegraph")

[PySide](/PySide "PySide") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Introduction

Pivy is a [Python](/Python "Python") binding library for
[Coin](https://github.com/coin3d), the 3D-rendering library used in FreeCAD to
display things in a [3D view](/3D_view "3D view"). Coin is an open source
implementation of the "Open Inventor" specification to handle graphics.
Therefore, in FreeCAD, the terms "Pivy", "Coin" or "Open Inventor" refer to
the same thing essentially.

When imported in a running Python interpreter, Pivy allows us to communicate
directly with any running Coin [scenegraph](/Scenegraph "Scenegraph"), such as
the [3D view](/3D_view "3D view"), or even to create new ones. Pivy is not
required to compile FreeCAD, but it is required at runtime when running
Python-based workbenches that create shapes on screen, like
[Draft](/Draft_Workbench "Draft Workbench") and [BIM](/BIM_Workbench "BIM
Workbench"). Because of this, Pivy is normally installed when installing a
distribution of FreeCAD.

The Coin library is divided into several pieces, Coin itself for manipulating
scenegraphs, and bindings for several GUI systems, such as Windows and Qt. If
present on the system, those modules are available to Pivy as well. The Coin
module is always present, and it is what we will use anyway, since we won't
need to care about anchoring our 3D display in any interface, that is already
done by FreeCAD. All we need to do is this:

    
    
    from pivy import coin
    

## Scenegraph

We saw on the [Scenegraph](/Scenegraph "Scenegraph") page how a typical Coin
scene is organized. Everything that appears in a [3D view](/3D_view "3D view")
is a Coin scenegraph, organized in the same way. We have one root node, and
all objects on the screen are its children.

FreeCAD has an easy way to access the root node of a 3D view scenegraph:

    
    
    sg = FreeCADGui.ActiveDocument.ActiveView.getSceneGraph()
    print(sg)
    

This will return the root node:

    
    
    <pivy.coin.SoSelection; proxy of <Swig Object of type 'SoSelection *' at 0x360cb60> >
    

We can inspect the immediate children of our scene:

    
    
    for node in sg.getChildren():
        print(node)
    

Some of those nodes, such as `SoSeparator` or `SoGroup` nodes, can have
children themselves. The complete list of the available Coin objects can be
found in the official Coin documentation.

Let's try to add something to our scenegraph now. We'll add a nice red cube:

    
    
    col = coin.SoBaseColor()
    col.rgb = (1, 0, 0)
    cub = coin.SoCube()
    myCustomNode = coin.SoSeparator()
    myCustomNode.addChild(col)
    myCustomNode.addChild(cub)
    sg.addChild(myCustomNode)
    

Now, let's try this:

    
    
    col.rgb = (1, 1, 0)
    

As you can see everything is still accessible and modifiable on-the-fly. No
need to recompute or redraw anything, Coin takes care of everything. You can
add stuff to your scenegraph, change properties, hide stuff, show temporary
objects, anything. Of course, this only concerns the display in the 3D view.
That display gets recomputed by FreeCAD on file open, and when an object needs
recomputing. So, if you change the aspect of an existing FreeCAD object, those
changes will be lost if the object gets recomputed or when you reopen the
file.

As already mentioned, in an openInventor scenegraph the order is important. A
node affects what comes next. For example, if we want to have the ability to
move our cube we will need to add a `SoTranslation` node _before_ the cube:

    
    
    col = coin.SoBaseColor()
    col.rgb = (1, 0, 0)
    trans = coin.SoTranslation()
    trans.translation.setValue([0, 0, 0])
    cub = coin.SoCube()
    myCustomNode = coin.SoSeparator()
    myCustomNode.addChild(col)
    myCustomNode.addChild(trans)
    myCustomNode.addChild(cub)
    sg.addChild(myCustomNode)
    

To move our cube we can now do:

    
    
    trans.translation.setValue([2, 0, 0])
    

Finally, removing something is done with:

    
    
    sg.removeChild(myCustomNode)
    

Top

## Callbacks

A [callback
mechanism](https://en.wikipedia.org/wiki/Callback_%28computer_science%29) is a
system that permits a library, such as our Coin library, to call you back,
that is, to call a certain function from your currently running Python object.
That way Coin can notify you that some specific event occurred in the scene.
Coin can watch very different things, such as mouse position, mouse button
clicks, keyboard keys being pressed, and many more.

FreeCAD features an easy way to use such callbacks:

    
    
    from pivy import coin
    
    class ButtonTest:
        def __init__(self):
            self.view = FreeCADGui.ActiveDocument.ActiveView
            self.callback = self.view.addEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.getMouseClick) 
    
        def getMouseClick(self, event_cb):
            event = event_cb.getEvent()
            if event.getState() == coin.SoMouseButtonEvent.DOWN:
                print("Alert!!! A mouse button has been improperly clicked!!!")
                self.view.removeEventCallbackPivy(coin.SoMouseButtonEvent.getClassTypeId(), self.callback)
    
    ButtonTest()
    

The callback has to be initiated from an object, because that object must
still be running when the callback occurs. See also a [complete
list](/Code_snippets#Observe_mouse_events_in_the_3D_viewer_via_Python "Code
snippets") of possible events and their parameters, or the official Coin
documentation.

Top

## Documentation

Unfortunately, Pivy doesn't have its own documentation. However, since it is
an accurate wrapper of the Coin library, you can read the C++ reference for
information. In this case, you need to translate the C++ class naming style to
Python style.

In C++:

    
    
    SoFile::getClassTypeId()
    

In Pivy:

    
    
    SoFile.getClassId()
    

  * [Coin3D](https://github.com/coin3d) homepage.
  * [Pivy](https://github.com/coin3d/pivy) homepage.
  * [Coin3D wiki](https://github.com/coin3d/coin/wiki), at GitHub.
  * [Coin3D wiki documentation](https://github.com/coin3d/coin/wiki/Documentation), at GitHub.
  * [Coin3D Documentation](https://coin3d.github.io/Coin/html/), latest automatically generated Doxygen documentation.
  * [(Open)Inventor Mentor](https://webdocs.cs.ualberta.ca/~graphics/books/mentor.pdf) \- recommended.

### Older

These links provide reference documentation for Coin v3.x. The differences
with v4.x are minimal, so they may still be useful.

  * [Coin3D Documentation](https://coin3d.bitbucket.io/Coin/index.html), at BitBucket.
  * [Coin3D Documentation](https://grey.colorado.edu/coin3d/index.html), at University of Colorado.
  * [Open Inventor Reference Documentation](https://mevislabdownloads.mevis.de/docs/current/MeVis/ThirdParty/Documentation/Publish/OpenInventorReference/index.html), by MeVisLab.

Top

![](/images/6/6f/Arrow-left.svg) [Scenegraph](/Scenegraph "Scenegraph")

[PySide](/PySide "PySide") ![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/8/8f/Power_user_hub.png/24px-
Power_user_hub.png)](/index.php?title=File:Power_user_hub.png&filetimestamp=20200511213015&)
[Power user documentation](/Power_users_hub "Power users hub")

  * **FreeCAD scripting:** [Python](/Python "Python"), [Introduction to Python](/Introduction_to_Python "Introduction to Python"), [Python scripting tutorial](/Python_scripting_tutorial "Python scripting tutorial"), [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD Scripting Basics")

* * *

  * **Modules:** [Builtin modules](/Builtin_modules "Builtin modules"), [Units](/Units "Units"), [Quantity](/Quantity "Quantity")
  * **Workbenches:** [Workbench creation](/Workbench_creation "Workbench creation"), [Gui Commands](/Gui_Command "Gui Command"), [Commands](/Command "Command"), [Installing more workbenches](/Installing_more_workbenches "Installing more workbenches")
  * **Meshes and Parts:** [Mesh Scripting](/Mesh_Scripting "Mesh Scripting"), [Topological data scripting](/Topological_data_scripting "Topological data scripting"), [Mesh to Part](/Mesh_to_Part "Mesh to Part"), [PythonOCC](/PythonOCC "PythonOCC")

* * *

  * **Parametric objects:** [Scripted objects](/Scripted_objects "Scripted objects"), [Viewproviders](/Viewprovider "Viewprovider") ([Custom icon in tree view](/Custom_icon_in_tree_view "Custom icon in tree view"))
  * **Scenegraph:** [Coin (Inventor) scenegraph](/Scenegraph "Scenegraph"), Pivy
  * **Graphical interface:** [Interface creation](/Interface_creation "Interface creation"), [Interface creation completely in Python](/Dialog_creation "Dialog creation") ([1](/Dialog_creation_with_various_widgets "Dialog creation with various widgets"), [2](/Dialog_creation_reading_and_writing_files "Dialog creation reading and writing files"), [3](/Dialog_creation_setting_colors "Dialog creation setting colors"), [4](/Dialog_creation_image_and_animated_GIF "Dialog creation image and animated GIF"), [5](/PySide_usage_snippets "PySide usage snippets")), [PySide](/PySide "PySide"), PySide examples [beginner](/PySide_Beginner_Examples "PySide Beginner Examples"), [intermediate](/PySide_Intermediate_Examples "PySide Intermediate Examples"), [advanced](/PySide_Advanced_Examples "PySide Advanced Examples")
  * **Macros:** [Macros](/Macros "Macros"), [How to install macros](/How_to_install_macros "How to install macros")
  * **Embedding:** [Embedding FreeCAD](/Embedding_FreeCAD "Embedding FreeCAD"), [Embedding FreeCADGui](/Embedding_FreeCADGui "Embedding FreeCADGui")

* * *

  * **Other:** [Expressions](/Expressions "Expressions"), [Code snippets](/Code_snippets "Code snippets"), [Line drawing function](/Line_drawing_function "Line drawing function"), [FreeCAD vector math library](/FreeCAD_vector_math_library "FreeCAD vector math library") (deprecated)

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

