---
url: https://developer.rhino3d.com/guides/rhinocommon/procedurally-generate-toolbars/
scraped_at: 2025-09-08T15:36:49.887989
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

[Procedurally Generate
Toolbars](https://developer.rhino3d.com/guides/rhinocommon/procedurally-
generate-toolbars/)

  * Question
  * Answer
  * Related Topics

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Procedurally Generate Toolbars

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Question

I am trying to generate a toolbar without using Rhino. Having a toolbar with
correct macros is done and working, but the bitmap (icons) part is still
problematic

I’m not sure if the issue is with the image generation or the GUID system of
Rhino.

For each icon size, the script takes all the icons needed and makes a big one,
resulting in a column of icons. Then the image is translated to `Base64`
format.

Rhino does not recognize these images. They are not displayed. And upon saving
the toolbar, all the previous icon data is replaced with a blank image.

## Answer

Toolbar bitmaps are stored in a grid with 250 columns and enough rows to
accommodate the total item count. New items are added to then end of the last
row until the row fills up at which time a new row is added to the bitmap.
Rhino writes the bitmap as a PNG file to a stream and then writes the raw
bitmap to the RUI file.

Here is some sample code for writing:

    
    
    const string NODE_BITMAPITEM = "bitmap_item";
    const string NODE_BITMAP = "bitmap";
    ...
    public void Write(System.Xml.XmlWriter writer, string elementName)
    {
      writer.WriteStartElement(elementName);
      {
        writer.WriteAttributeString("item_width", m_item_size.Width.ToString());
        writer.WriteAttributeString("item_height", m_item_size.Height.ToString());
        foreach (KeyValuePair<Guid, BitmapItem> kvp in m_id_list)
        {
          writer.WriteStartElement(NODE_BITMAPITEM);
          {
            writer.WriteAttributeString("guid", kvp.Key.ToString());
            writer.WriteAttributeString("index", kvp.Value.m_index.ToString());
          }
          writer.WriteEndElement();
        }
        writer.WriteStartElement(NODE_BITMAP);
        {
          if (null != FullBitmap)
          {
            try
            {
              using (var stream = new MemoryStream())
              {
                FullBitmap.Save(stream, System.Drawing.Imaging.ImageFormat.Png);
                byte[] bytes = stream.GetBuffer();
                if (null != bytes && bytes.Length > 0)
                  writer.WriteString(Convert.ToBase64String(bytes, Base64FormattingOptions.InsertLineBreaks));
              }
            }
            catch (Exception ex)
            {
              Rhino.Runtime.HostUtils.ExceptionReport(ex);
            }
          }
        }
        writer.WriteEndElement();
      }
      writer.WriteEndElement();
    }
    

## Related Topics

  * [Creating and Deploying Plugin Toolbars](https://developer.rhino3d.com/guides/rhinocommon/create-deploy-plugin-toolbar/)

  * [Localizing Plugin Toolbars](https://developer.rhino3d.com/guides/rhinocommon/localize-plugin-toolbar/)

​

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/procedurally-
generate-toolbars/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/procedurally-
generate-toolbars/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

