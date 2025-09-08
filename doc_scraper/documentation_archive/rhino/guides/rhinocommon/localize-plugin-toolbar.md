---
url: https://developer.rhino3d.com/guides/rhinocommon/localize-plugin-toolbar/#answer
scraped_at: 2025-09-08T16:09:15.954656
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

[Localizing Plugin
Toolbars](https://developer.rhino3d.com/guides/rhinocommon/localize-plugin-
toolbar/)

  * Question
  * Answer

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Localizing Plugin Toolbars

__

Windows only

by [Dale Fugier](https://discourse.mcneel.com/u/dale/) (Last updated:
Wednesday, December 5, 2018)

## Question

What is the best way to prepare a Rhino toolbar for multi-language support?

## Answer

If you want to create Rhino-style toolbars, then use Rhino’s `Toolbar`
command. You can save your custom toolbars in your own Rhino User Interface
(RUI) file. For details on creating toolbars, see the Rhino help file.

An RUI file is an XML file that can be viewed and edited in an ordinary text
editor.

If you open an RUI file, that contains a toolbar that contains a button, you
might see a block of XML that looks similar to the following:

    
    
    <macro_item guid="some_unique_guid" bitmap_id="some_unique_guid">
      <text>
        <locale_1033>RenderSettings</locale_1033>
      </text>
      <tooltip>
        <locale_1033>Render settings</locale_1033>
      </tooltip>
      <button_text>
        <locale_1033>Render</locale_1033>
      </button_text>
      <script>_DocumentPropertiesPage _Render</script>
    </macro_item>
    

Notice the `<locale_1033>` tag, which denotes the text used by Rhino when
configured for English (United States).

It is possible to add additional locale tags for supported language.

    
    
    <macro_item guid="some_unique_guid" bitmap_id="some_unique_guid">
      <text>
        <locale_1033>RenderSettings</locale_1033>
        <locale_1031>Rendereinstellungen</locale_1031>
        <locale_1034>RenderizadoOpciones</locale_1034>
        <locale_1036>ParamètresRendu</locale_1036>
        <locale_1040>RenderingImpostazioni</locale_1040>
        <locale_1042>렌더링_설정</locale_1042>
        <locale_2052>渲染设置</locale_2052>
        <locale_1028>彩現設定</locale_1028>
      </text>
      <tooltip>
        <locale_1033>Render settings</locale_1033>
        <locale_1031>Rendereinstellungen</locale_1031>
        <locale_1034>Opciones de renderizado</locale_1034>
        <locale_1036>Paramètres du rendu</locale_1036>
        <locale_1040>Impostazioni rendering</locale_1040>
        <locale_1041>ﾚﾝﾀﾞﾘﾝｸﾞ設定</locale_1041>
        <locale_1042>렌더링 설정</locale_1042>
        <locale_2052>渲染设置</locale_2052>
        <locale_1028>彩現設定</locale_1028>
      </tooltip>
      <button_text>
        <locale_1033>Render</locale_1033>
        <locale_1031>Rendern</locale_1031>
        <locale_1034>Renderizar</locale_1034>
        <locale_1036>Rendu</locale_1036>
        <locale_1040>Rendering</locale_1040>
        <locale_1041>ﾚﾝﾀﾞﾘﾝｸﾞ</locale_1041>
        <locale_1042>렌더링</locale_1042>
        <locale_2052>渲染</locale_2052>
        <locale_1028>彩現</locale_1028>
      </button_text>
      <script>_DocumentPropertiesPage _Render</script>
    </macro_item>
    

Note, it is not possible to localize toolbar bitmaps.

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/localize-
plugin-toolbar/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/localize-
plugin-toolbar/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

