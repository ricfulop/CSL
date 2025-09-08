---
url: https://developer.rhino3d.com/guides/rhinopython/python-xml-json/
scraped_at: 2025-09-08T15:37:49.027440
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

[How to use JSON](https://developer.rhino3d.com/guides/rhinopython/python-xml-
json/)

  * JSON in Python
  * Writing a JSON file
  * Reading JSON

[Guides](https://developer.rhino3d.com/en/guides/) / [Rhino.Python
Guides](https://developer.rhino3d.com/en/guides/rhinopython/) /

How to use JSON

by [Scott Davidson](https://discourse.mcneel.com/u/scottd/) (Last updated:
Wednesday, January 15, 2020)

[JSON (JavaScript Object Notation)](http://www.json.org/) is an easy to read,
flexible text based format that can be used to store and communicate
information to other products. It is mainly based on key:value pairs and is
web and .NET friendly. There are many libraries and products that support
JSON.

One of the reasons JSON might be used is to collect data from the Rhino model
to be used in other places. Use JSON to store information for a door schedule,
or a parts list. A report can be created on the name, size and location of all
the bitmaps in a model. A JSON file can have the endpoints of all the lines in
a model representing column or beam connection points. JSON files are used in
several other places and products. JSON is also easy to display on dynamic
webpages.

Here is an example of a JSON structure describing a medical office, taken from
a set of polylines off a Rhino floorplan. As you will see in the example, the
medical space includes 5 rooms and parking, with square footage and pricing
for each dedicated space.

    
    
    { "office": 
        {"medical": [
          { "room-number": 100,
            "use": "reception",
            "sq-ft": 50,
            "price": 75
          },
          { "room-number": 101,
            "use": "waiting",
            "sq-ft": 250,
            "price": 75
          },
          { "room-number": 102,
            "use": "examination",
            "sq-ft": 125,
            "price": 150
          },
          { "room-number": 103,
            "use": "examination",
            "sq-ft": 125,
            "price": 150
          },
          { "room-number": 104,
            "use": "office",
            "sq-ft": 150,
            "price": 100
          }
        ],
        "parking": {
          "location": "premium",
          "style": "covered",
          "price": 750
        }
      }
    } 
    

It is this dictionary setup that works best for Json.

For more information on creating and manipulating this type of information in
Python see the [Dictionary as a Database
Guide](https://developer.rhino3d.com/guides/rhinopython/python-dictionary-
database/)

## JSON in Python

JSON can store Lists, bools, numbers, tuples and dictionaries. But to be saved
into a file, all these structures must be reduced to strings. It is the string
version that can be read or written to a file. Python has a JSON module that
will help converting the datastructures to JSON strings. Use the `import`
function to import the JSON module.

    
    
    import json
    

The JSON module is mainly used to convert the python dictionary above into a
JSON string that can be written into a file.

    
    
    json_string = json.dumps(datastore)
    

The JSON module can also take a JSON string and convert it back to a
dictionary structure:

    
    
    datastore = json.loads(json_string)
    

While the JSON module will convert strings to Python datatypes, normally the
JSON functions are used to read and write directly from JSON files.

## Writing a JSON file

Not only can the `json.dumps()` function convert a Python datastructure to a
JSON string, but it can also dump a JSON string directly into a file. Here is
an example of writing a structure above to a JSON file:

    
    
    #Get the file name for the new file to write
    filter = "JSON File (*.json)|*.json|All Files (*.*)|*.*||"
    filename = rs.SaveFileName("Save JSON file as", filter)
    
    # If the file name exists, write a JSON string into the file.
    if filename:
        # Writing JSON data
        with open(filename, 'w') as f:
            json.dump(datastore, f)
    

Remember only a JSON formatted string can be written to the file. For more
information about using Rhino.Python to read and write files see the [How to
read and write a simple
file](https://developer.rhino3d.com/guides/rhinopython/python-reading-
writing/)

## Reading JSON

Reading in a JSON file uses the `json.load()` function.

    
    
    import rhinoscriptsyntax as rs
    import json
    
    #prompt the user for a file to import
    filter = "JSON file (*.json)|*.json|All Files (*.*)|*.*||"
    filename = rs.OpenFileName("Open JSON File", filter)
    
    #Read JSON data into the datastore variable
    if filename:
        with open(filename, 'r') as f:
            datastore = json.load(f)
    
    #Use the new datastore datastructure
    print datastore["office"]["parking"]["style"]
    

The result of the code above will result in the same data structure at the top
of this guide.

For more information about using Rhino.Python to read and write files see the
[How to read and write a simple
file](https://developer.rhino3d.com/guides/rhinopython/python-reading-
writing/)

For more details on accessing the information in the dictionary datastructure
see, [Dictionary as a Database
Guide](https://developer.rhino3d.com/guides/rhinopython/python-dictionary-
database/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinopython/python-
xml-json/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinopython/python-
xml-json/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

