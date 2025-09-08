---
url: https://docs.blender.org/api/current/bpy.ops.console.html
scraped_at: 2025-09-08T14:18:00.444508
title: Console Operators¶
---

# Console Operators¶

bpy.ops.console.autocomplete()¶

    

Evaluate the namespace up until the cursor and give a list of options or
complete the name if there is only one

File:

    

[startup/bl_operators/console.py:61](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L61)

bpy.ops.console.banner()¶

    

Print a message when the terminal initializes

File:

    

[startup/bl_operators/console.py:104](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L104)

bpy.ops.console.clear(_*_ , _scrollback =True_, _history =False_)¶

    

Clear text by type

Parameters:

    

  * **scrollback** (_boolean_ _,__(__optional_ _)_) – Scrollback, Clear the scrollback history

  * **history** (_boolean_ _,__(__optional_ _)_) – History, Clear the command history

bpy.ops.console.clear_line()¶

    

Clear the line and store in history

bpy.ops.console.copy(_*_ , _delete =False_)¶

    

Copy selected text to clipboard

Parameters:

    

**delete** (_boolean_ _,__(__optional_ _)_) – Delete Selection, Whether to
delete the selection after copying

bpy.ops.console.copy_as_script()¶

    

Copy the console contents for use in a script

File:

    

[startup/bl_operators/console.py:82](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L82)

bpy.ops.console.delete(_*_ , _type =NEXT_CHARACTER_)¶

    

Delete text by cursor position

Parameters:

    

**type** (enum in [`NEXT_CHARACTER`, `PREVIOUS_CHARACTER`, `NEXT_WORD`,
`PREVIOUS_WORD`], (optional)) – Type, Which part of the text to delete

bpy.ops.console.execute(_*_ , _interactive =False_)¶

    

Execute the current console line as a Python expression

Parameters:

    

**interactive** (_boolean_ _,__(__optional_ _)_) – interactive

File:

    

[startup/bl_operators/console.py:38](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L38)

bpy.ops.console.history_append(_*_ , _text =''_, _current_character =0_,
_remove_duplicates =False_)¶

    

Append history at cursor position

Parameters:

    

  * **text** (_string_ _,__(__optional_ _,__never None_ _)_) – Text, Text to insert at the cursor position

  * **current_character** (_int in_ _[__0_ _,__inf_ _]__,__(__optional_ _)_) – Cursor, The index of the cursor

  * **remove_duplicates** (_boolean_ _,__(__optional_ _)_) – Remove Duplicates, Remove duplicate items in the history

bpy.ops.console.history_cycle(_*_ , _reverse =False_)¶

    

Cycle through history

Parameters:

    

**reverse** (_boolean_ _,__(__optional_ _)_) – Reverse, Reverse cycle history

bpy.ops.console.indent()¶

    

Add 4 spaces at line beginning

bpy.ops.console.indent_or_autocomplete()¶

    

Indent selected text or autocomplete

bpy.ops.console.insert(_*_ , _text =''_)¶

    

Insert text at cursor position

Parameters:

    

**text** (_string_ _,__(__optional_ _,__never None_ _)_) – Text, Text to
insert at the cursor position

bpy.ops.console.language(_*_ , _language =''_)¶

    

Set the current language for this console

Parameters:

    

**language** (_string_ _,__(__optional_ _,__never None_ _)_) – Language

File:

    

[startup/bl_operators/console.py:136](https://projects.blender.org/blender/blender/src/branch/main/scripts/startup/bl_operators/console.py#L136)

bpy.ops.console.move(_*_ , _type =LINE_BEGIN_, _select =False_)¶

    

Move cursor position

Parameters:

    

  * **type** (enum in [`LINE_BEGIN`, `LINE_END`, `PREVIOUS_CHARACTER`, `NEXT_CHARACTER`, `PREVIOUS_WORD`, `NEXT_WORD`], (optional)) – Type, Where to move cursor to

  * **select** (_boolean_ _,__(__optional_ _)_) – Select, Whether to select while moving

bpy.ops.console.paste(_*_ , _selection =False_)¶

    

Paste text from clipboard

Parameters:

    

**selection** (_boolean_ _,__(__optional_ _)_) – Selection, Paste text
selected elsewhere rather than copied (X11/Wayland only)

bpy.ops.console.scrollback_append(_*_ , _text =''_, _type =OUTPUT_)¶

    

Append scrollback text by type

Parameters:

    

  * **text** (_string_ _,__(__optional_ _,__never None_ _)_) – Text, Text to insert at the cursor position

  * **type** (enum in [`OUTPUT`, `INPUT`, `INFO`, `ERROR`], (optional)) – Type, Console output type

bpy.ops.console.select_all()¶

    

Select all the text

bpy.ops.console.select_set()¶

    

Set the console selection

bpy.ops.console.select_word()¶

    

Select word at cursor position

bpy.ops.console.unindent()¶

    

Delete 4 spaces from line beginning

  *[API]: Application Programming Interface
  *[TL;DR]: Too long; didn't read.

