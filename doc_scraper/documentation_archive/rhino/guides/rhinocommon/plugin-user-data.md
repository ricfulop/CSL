---
url: https://developer.rhino3d.com/guides/rhinocommon/plugin-user-data/#related-topics
scraped_at: 2025-09-08T16:07:30.861372
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

[Plugin User Data](https://developer.rhino3d.com/guides/rhinocommon/plugin-
user-data/)

  * Document User Data
  * Object User Data
  * Related topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Plugin User Data

by [Steve Baer](https://discourse.mcneel.com/u/stevebaer/) (Last updated:
Wednesday, December 5, 2018)

There are two basic ways plugins can store information in Rhino .3dm files:

  1. [Document User Data](https://developer.rhino3d.com/guides/rhinocommon/plugin-user-data/#document-user-data)
  2. [Object User Data](https://developer.rhino3d.com/guides/rhinocommon/plugin-user-data/#object-user-data)

For example, a rendering plugin might save a scene descriptions as document
user data and use object user data to attach rendering material information to
individual surfaces.

## Document User Data

To save document user data your plugin must override three PlugIn base class
functions:

    
    
    PlugIn.ShouldCallWriteDocument
    PlugIn.WriteDocument
    PlugIn.ReadDocument
    

SDK references for these functions can be found
[here](https://developer.rhino3d.com/api/RhinoCommon/html/Methods_T_Rhino_PlugIns_PlugIn.htm).

When Rhino writes a .3dm file, it goes through all the plugins that are
currently loaded. First Rhino calls `ShouldCallWriteDocument()` to see if the
plugin wants to save document user data. If `ShouldWriteDocument()` returns
true, Rhino saves information that identifies the plugin and then calls
`WriteDocument()` when it is time for the plugin to save its “document” user
data.

When Rhino reads a .3dm file and it encounters document user data, it uses the
plugin identification information to load the plugin and then calls the
plugin’s `ReadDocument()` to read the plugin’s “document” user data.

## Object User Data

Object user data can be attached to things like layers, materials, geometry
objects, and object attributes. In fact object user data can be attached to
any class derived from CommonObject. This user data is stored in a linked list
on CommonObject and can be copied, transformed and saved along with the parent
object. For example, you could attach object user data to a mesh. When the
mesh is copied the object user data would be copied and attached to the copy.
When the mesh is transformed, the transformation would be recored by the
object user data. When the mesh is saved in a .3dm file, the object user data
will be saved too.

There are three forms of object user data:

  1. User strings
  2. UserDictionary
  3. Custom UserData

It is _recommended to typically use the User Strings or the UserDictionary on
an object_ since the data is automatically serialized for you and it is easily
shared between plugins and scripts.

In the case that you want to write your own private custom user data, you
would derive a class from `Rhino.DocObjects.Custom.UserData`. Here’s a sample:

    
    
    using System;
    using Rhino;
    using System.Runtime.InteropServices;
    
    namespace examples_cs
    {
      // You must define a Guid attribute for your user data derived class
      // in order to support serialization. Every custom user data class
      // needs a custom Guid
      [Guid("DAAA9791-01DB-4F5F-B89B-4AE46767C783")]
      public class PhysicalData : Rhino.DocObjects.Custom.UserData
      {
        public int Weight{ get; set; }
        public double Density {get; set;}
    
    
        // Your UserData class must have a public parameterless constructor
        public PhysicalData(){}
    
        public PhysicalData(int weight, double density)
        {
          Weight = weight;
          Density = density;
        }
    
        public override string Description
        {
          get { return "Physical Properties"; }
        }
    
        public override string ToString()
        {
          return String.Format("weight={0}, density={1}", Weight, Density);
        }
    
        protected override void OnDuplicate(Rhino.DocObjects.Custom.UserData source)
        {
          PhysicalData src = source as PhysicalData;
          if (src != null)
          {
            Weight = src.Weight;
            Density = src.Density;
          }
        }
    
        // return true if you have information to save
        public override bool ShouldWrite
        {
          get
          {
            if (Weight > 0 && Density > 0)
              return true;
            return false;
          }
        }
    
        protected override bool Read(Rhino.FileIO.BinaryArchiveReader archive)
        {
          Rhino.Collections.ArchivableDictionary dict = archive.ReadDictionary();
          if (dict.ContainsKey("Weight") && dict.ContainsKey("Density"))
          {
            Weight = (int)dict["Weight"];
            Density = (double)dict["Density"];
          }
          return true;
        }
        protected override bool Write(Rhino.FileIO.BinaryArchiveWriter archive)
        {
          // you can implement File IO however you want... but the dictionary class makes
          // issues like versioning in the 3dm file a bit easier.  If you didn't want to use
          // the dictionary for writing, your code would look something like.
          //
          //  archive.Write3dmChunkVersion(1, 0);
          //  archive.WriteInt(Weight);
          //  archive.WriteDouble(Density);
          var dict = new Rhino.Collections.ArchivableDictionary(1, "Physical");
          dict.Set("Weight", Weight);
          dict.Set("Density", Density);
          archive.WriteDictionary(dict);
          return true;
        }
      }
    
    
      [Guid("ca9a110e-3969-49ec-9d59-a7c2ee0b85bd")]
      public class ex_userdataCommand : Rhino.Commands.Command
      {
        public override string EnglishName { get { return "cs_userdataCommand"; } }
    
        protected override Rhino.Commands.Result RunCommand(RhinoDoc doc, Rhino.Commands.RunMode mode)
        {
          Rhino.DocObjects.ObjRef objref;
          var rc = Rhino.Input.RhinoGet.GetOneObject("Select Object", false, Rhino.DocObjects.ObjectType.AnyObject, out objref);
          if (rc != Rhino.Commands.Result.Success)
            return rc;
    
          // See if user data of my custom type is attached to the geomtry
          var ud = objref.Geometry().UserData.Find(typeof(PhysicalData)) as PhysicalData;
          if (ud == null)
          {
            // No user data found; create one and add it
            int weight = 0;
            rc = Rhino.Input.RhinoGet.GetInteger("Weight", false, ref weight);
            if (rc != Rhino.Commands.Result.Success)
              return rc;
    
            ud = new PhysicalData(weight, 12.34);
            objref.Geometry().UserData.Add(ud);
          }
          else
          {
            RhinoApp.WriteLine("{0} = {1}", ud.Description, ud);
          }
          return Rhino.Commands.Result.Success;
        }
      }
    }
    

## Related topics

  * [Rhino.PlugIns.PlugIn Methods (API Reference)](https://developer.rhino3d.com/api/RhinoCommon/html/Methods_T_Rhino_PlugIns_PlugIn.htm)
  * [RhinoCommon object plugin user data](https://developer.rhino3d.com/samples/rhinocommon/user-data/)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/plugin-
user-data/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/plugin-
user-data/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

