---
url: https://wiki.freecad.org/Localisation
title: Localisation
scraped_at: 2025-09-08 16:44:55
---

Toggle the table of contents

## Contents

move to sidebar hide

  * Beginning
  * 1 Overview
  * 2 Helping to translate FreeCAD
  * 3 Translate the FreeCAD source code
  * 4 Translating external workbenches
  * 5 FreeCAD Preferences for Translators
  * 6 Translate the FreeCAD wiki Toggle Translate the FreeCAD wiki subsection
    * 6.1 Mediawiki Translation Extension
    * 6.2 Important notes
    * 6.3 Translate the FreeCAD documentation
    * 6.4 Old translation instructions
  * 7 Translate the FreeCAD website
  * 8 Development - How to Add Localisation Toggle Development - How to Add Localisation subsection
    * 8.1 Preparing your FreeCAD/master modules for translation
    * 8.2 Preparing your 3rd party module or macro for translation
  * 9 Automating Crowdin Translation Updates
  * 10 Related Pages
  * 11 Scripting

# Localisation

  * [Page](/Localisation "View the content page \[ctrl-option-c\]")
  * [Discussion](/Talk:Localisation "Discussion about the content page \[ctrl-option-t\]")

English

  * [Read](/Localisation)
  * [Edit](/index.php?title=Localisation&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Localisation&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [Edit on GitHub](https://github.com/Reqrefusion/FreeCAD-Documentation-Project/blob/main/wiki/Localisation.wikitext "Edit this page on GitHub")
  * [View history](/index.php?title=Localisation&action=history "Past revisions of this page \[ctrl-option-h\]")

Tools

Tools

move to sidebar hide

Actions

  * [Read](/Localisation)
  * [Edit](/index.php?title=Localisation&veaction=edit "Edit this page \[ctrl-option-v\]")
  * [Edit source](/index.php?title=Localisation&action=edit "Edit the source code of this page \[ctrl-option-e\]")
  * [View history](/index.php?title=Localisation&action=history)

General

  * [What links here](/Special:WhatLinksHere/Localisation "A list of all wiki pages that link here \[ctrl-option-j\]")
  * [Related changes](/Special:RecentChangesLinked/Localisation "Recent changes in pages linked from this page \[ctrl-option-k\]")
  * [Special pages](/Special:SpecialPages "A list of all special pages \[ctrl-option-q\]")
  * [Permanent link](https://wiki.freecad.org/index.php?title=Localisation&oldid=1604472 "Permanent link to this revision of this page")
  * [Page information](/index.php?title=Localisation&action=info "More information about this page")
  * Expand all

Print/export

  * [Download as PDF](/index.php?title=Special:DownloadAsPdf&page=Localisation&action=show-download-screen)
  * [Printable version](javascript:print\(\); "Printable version of this page \[ctrl-option-p\]")

From FreeCAD Documentation

[Translate this page](/Special:Translate?group=page-
Localisation&action=page&filter=&language=en)This is the approved revision of
this page, as well as being the most recent.

Other languages:

  * [](/index.php?title=Special:Translate&group=page-Localisation&language=&task=view "Start translation for this language")
  * [Bahasa Indonesia](/Localisation/id "Localisation \(1% translated\)")
  * [Deutsch](/Localisation/de "Lokalisierung \(100% translated\)")
  * English
  * [Türkçe](/Localisation/tr "Yerelleştirme \(19% translated\)")
  * [español](/Localisation/es "Localización \(91% translated\)")
  * [français](/Localisation/fr "Localisation ou traduction de l'interface et de la documentation \(100% translated\)")
  * [hrvatski](/Localisation/hr "Lokalizacija \(12% translated\)")
  * [italiano](/Localisation/it "Localizzazione \(100% translated\)")
  * [polski](/Localisation/pl "Lokalizacja - tłumaczenie interfejsu i dokumentacji \(100% translated\)")
  * [português](/Localisation/pt "Localização \(1% translated\)")
  * [português do Brasil](/Localisation/pt-br "Localização \(91% translated\)")
  * [română](/Localisation/ro "Localisation/Traducere, Adaptare, Localizare \(19% translated\)")
  * [svenska](/Localisation/sv "Localisation \(3% translated\)")
  * [čeština](/Localisation/cs "Localisation/cs \(0% translated\)")
  * [български](/Localisation/bg "Localisation/bg \(0% translated\)")
  * [русский](/Localisation/ru "Локализация \(65% translated\)")
  * [українська](/Localisation/uk "Localisation/uk \(0% translated\)")
  * [中文（中国大陆）](/Localisation/zh-cn "本地化 \(34% translated\)")
  * [中文（臺灣）](/Localisation/zh-tw "Localisation/zh-tw \(0% translated\)")
  * [日本語](/Localisation/ja "ローカライゼーション \(47% translated\)")
  * [한국어](/Localisation/ko "현지화 \(37% translated\)")

![](/images/6/6f/Arrow-left.svg) [Branding](/Branding "Branding")

[Workbench creation](/Workbench_creation "Workbench creation")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

## Overview

**Localisation** is in general the process of providing a Software with a
multiple language user interface. In FreeCAD you can set the language of the
user interface under **Edit → Preferences → General**. FreeCAD uses
[Qt](http://en.wikipedia.org/wiki/Qt_\(toolkit\) "wikipedia:Qt \(toolkit\)")
to enable multiple language support. On Unix/Linux systems, FreeCAD uses the
current locale settings of your system by default.

## Helping to translate FreeCAD

One of the very important things users can contribute to FreeCAD (if for
example they don't have programming skills) is to help translate its different
aspects (source code, wiki, website, documentation etc...) in to another
language. Here are the ways to do that.

## Translate the FreeCAD source code

FreeCAD utilizes a third party collaborative on-line translation system called
[Crowdin](https://crowdin.net).

[![](/images/thumb/0/0d/Logo-crowdin.png/320px-Logo-
crowdin.png)](/index.php?title=File:Logo-
crowdin.png&filetimestamp=20191211121846&)

It is proprietary software but free to
[FOSS](https://en.wikipedia.org/wiki/Free_and_open-source_software) projects.
Below are instructions on how to use it:

  * Go to the [FreeCAD translation project page on Crowdin](http://crowdin.net/project/freecad)
  * Login by creating a new profile, or using a third-party account (GitHub, GitLab, GMail etc...)
  * Click on the language you wish to translate
  * Start translating by clicking on the Translate button next to one of the files. For example, FreeCAD.ts contains the text strings for the FreeCAD main GUI.
  * You can vote for existing translations, or you can create your own.

If you are actively taking part in translating FreeCAD and want to be informed
before next release is ready to be launched, so there is time to review your
translation, please subscribe to one of the Crowdin FreeCAD translation teams.

  
_Note:_ Details on how to use crowdin can be found on the [Crowdin
Administration](/Crowdin_Administration "Crowdin Administration") page.

## Translating external workbenches

Visit [Translating an external workbench](/Translating_an_external_workbench
"Translating an external workbench").

## FreeCAD Preferences for Translators

Starting with FreeCAD 0.20, the following variables can be manually added to
the BaseApp/Preferences/General section of the user.cfg file to assist with
the development of new translations:

**AdditionalLanguageDomainEntries** \- to add entirely new languages to
FreeCAD that are not currently supported by the source code, you can use this
user preference to add to the list of available languages. The format of the
languages is "Language Name"="code"; for example:

    
    
    <FCText Name="AdditionalLanguageDomainEntries">"Esperanto"="eo";"French"="fr";</FCText>
    

**AdditionalTranslationsDirectory** \- add an additional directory for FreeCAD
to search for *.qm files. This location will take precedence over
$userAppDataDir/translations and $resourceDir/translations. For example:

    
    
    <FCText Name="AdditionalTranslationsDirectory">C:/Users/FreeCADUser/TestTranslations</FCText>
    

## Translate the FreeCAD wiki

This wiki hosts a lot of contents, the majority of which build up the manual.
You can browse the documentation starting from the [Main Page](/Main_Page
"Main Page"), or have a look at the user's manual [Online Help
Toc](/Online_Help_Toc "Online Help Toc").

To translate the wiki, you must have wiki edit permissions; see [How can I get
edit permission on the
wiki?](/Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki?
"Frequently asked questions").

You should also have enough knowledge of wiki markup and follow the general
styling guidelines described on [WikiPages](/WikiPages "WikiPages").

### Mediawiki Translation Extension

When the wiki moved away from SourceForge, [Yorik](/User:Yorik "User:Yorik")
installed [MediaWiki's Translation
extension](http://www.mediawiki.org/wiki/Help:Extension:Translate) which
facilitates translating pages. Advantages of the translation extension are
that the page title can now be translated, it keeps track of translations, it
notifies if the original page has been updated, and it maintains translations
in sync with the original English page.

The tool is documented in
[Help:Extension:Translate](http://www.mediawiki.org/wiki/Help:Extension:Translate),
and is part of [MediaWiki Language Extension
Bundle](http://www.mediawiki.org/wiki/MediaWiki_Language_Extension_Bundle).

To quickly get started on preparing a page for translation, please read the
[Page translation
example](http://www.mediawiki.org/wiki/Help:Extension:Translate/Page_translation_example).
A pair of tags need to surround the entire page to activate the translation
system:

    
    
    <translate> ... </translate>
    

The page also needs to be marked for translation.

To see an example of how the translation tool works, visit the [Main
Page](/Main_Page "Main Page"). You will see an automatically generated
language bar at the top. Click on [Deutsch](/Main_Page/de "Main Page/de")
(German), it will get you to [Main Page/de](/Main_Page/de "Main Page/de").
Right under the title, "Hauptseite" (in English "Main Page"), you can read
_This page is a translated version of the page Main Page and the translation
is XX% complete_ , XX being the current percentage of translation. Click on
"Translate" at the top of the page to start the translation utility to update,
correct and review the existing translation.

If you go to [Main Page](/Main_Page "Main Page"), you will notice that you
cannot edit the page directly anymore by clicking the [Edit] tags, and the top
link "Edit" has been substituted by the "Translate" link that opens the
translation utility.

When adding new content, the English page should be created first, then
translated into another language. If someone wants to change or add content in
a page, the English page should be modified first.

If you are unsure on how to proceed with the translations, don't hesitate to
ask for help in the [Development → Wiki
subforum](https://forum.freecad.org/viewforum.php?f=21) or in the [specific
language subforum](https://forum.freecad.org/viewforum.php?f=11) in the
[FreeCAD forum](https://forum.freecad.org).

### Important notes

Every wiki user that has "Editor" permissions is able to launch the translate
utility to write, save and review translations.

However, only users with "Administrator" permissions are able to mark pages
for translation. A page that is not marked for translation won't make use of
the translation extension and won't be correctly synchronized to the English
information.

The left sidebar is also translatable, but only Administrators can modify this
element of the site. Please follow the dedicated instructions on [Localisation
Sidebar](/Localisation_Sidebar "Localisation Sidebar").

The first time you switch a page to the new translation system, it loses all
its old "manual" translations. To recover a translation, you should save an
offline copy of the old text before the switch. Then you can use this old
translated text to fill in the translation units in the new system. You can
also open an earlier version from the history, and get the old text in this
way. This has to be done for every language that had a translated page.

### Translate the FreeCAD documentation

As per general consensus, the reference page in the wiki is the English page,
which should be created first. If you want to change or add content to a page,
you should do it to the English page first, and only once the update is
completed, port the modification to the translated page.

### Old translation instructions

ExpandThese instructions are for historical background only. Translations
should use the new system with the #Mediawiki Translation Extension described
above.  
---  
So the first step is to **check if the manual translation has already been
started for your language** (look in the left sidebar, under "manual").  
If not, head to the [forum](https://forum.freecad.org) and say that you want
to start a new translation, we'll create the basic setup for the language you
want to work on.  
You must then [gain wiki edit
permission](/Frequently_asked_questions#How_can_I_get_edit_permission_on_the_wiki.3F
"Frequently asked questions").  
If your language is already listed, see what pages are still missing a
translation (they will be listed in red). The technique is simple: **go into a
red page, and copy/paste the contents of the corresponding English page, and
start translating**.  
Do not forget to include all the tags and templates from the original English
page. Some of those templates will have an equivalent in your language (for
example, there is a French Docnav template called Docnav/fr). You should use
**a slash and your language code** in almost all the links. Look at other
already translated pages to see how they did it.  
Add a slash and your language code in the categories, like
[[Category:Developer Documentation/fr]]  
And if you are unsure, head to the forums and ask people to check what you did
and tell you if it's right or not.  
Four templates are commonly used in manual pages. These 4 templates have
localized versions (Template:Docnav/fr, Template:fr, etc...)

  * [Template:GuiCommand](/Template:GuiCommand "Template:GuiCommand") : is the Gui Command information block in upper-right of command documentation.
  * [Template:Docnav](/Template:Docnav "Template:Docnav") : it is the navigation bar at the bottom of the pages, showing previous and next pages.
  * [Template:Userdocnavi](/Template:Userdocnavi "Template:Userdocnavi") : gives direct links to the main base pages  

**Page Naming Convention**  
Please take note that, due to limitations in the Sourceforge implementation of
the MediaWiki engine, we require that your pages all keep their original
English counterpart's name, appending a slash and your language code. For
example, the translated page for About FreeCAD should be About Freecad/es for
Spanish, About FreeCAD/pl for polish, etc. The reason is simple: so that if
translators go away, the wiki's administrators, who do not speak all
languages, will know what these pages are for. This will facilitate
maintenance and avoid lost pages.  
If you want the Docnav template to show linked pages in your language, you can
use **redirect pages**. They are basically shortcut links to the actual page.
Here is an example with the French page for About FreeCAD.  

  * The page About FreeCAD/fr is the page with content
  * The page À propos de FreeCAD contains this code:

    
    
    #REDIRECT [[About_FreeCAD/fr]]
    

  * In the About FreeCAD/fr page, the Docnav code will look like this:

    
    
    {{docnav/fr|[[Online_Help_Startpage/fr|Bienvenue dans l'aide en ligne de FreeCAD]]|[[Feature_list/fr|Fonctionnalités]]}}
    

The page "Bienvenue dans l'aide en ligne de FreeCAD" redirects to
Online_Help_Startpage/fr, and the page "Fonctionnalités" redirects to
Feature_list/fr.  
  
## Translate the FreeCAD website

Translation of the FreeCAD website is now done through
[Crowdin](https://crowdin.com/translate/freecad/561/en-en). The file is named
homepage.po.

## Development - How to Add Localisation

This section is for developers who want to add localisation to their code.

### Preparing your FreeCAD/master modules for translation

These are the parts to the FreeCAD translation process:

  * extract text strings from source code into *.ts files
  * load *.ts files into [FreeCAD Crowdin](http://crowdin.net/project/freecad).
  * translation of strings within Crowdin
  * extract modified/new *.ts files from Crowdin
  * convert *.ts files into *.qm files and update each module's *.qrc file
  * update FreeCAD master

All of the above steps are performed by the "translation scripts" which are
run by an administrator periodically.

Preparing your module for translation is quite easy. First, you need to ensure
that you have a "translations" directory in myModule/Gui/Resources. Then open
a terminal window (or Windows/OSX equivalent) in your "translations" directory
and enter the following command:

    
    
    lupdate -ts myModule.ts
    

This creates an empty translation file. Once this is done, you need to ensure
that the translation scripts are updated as in this [pull
request](https://github.com/FreeCAD/FreeCAD/pull/810).

Everything after this is automatic as far as a developer is concerned. The
administrator will extract the text strings, the translators will translate
them, then the administrator will extract the translations and update
FreeCAD/master.

### Preparing your 3rd party module or macro for translation

3rd party modules or macros are translated in much the same fashion, except
that you must do some of the work yourself. This [forum
discussion](https://forum.freecad.org/viewtopic.php?f=3&t=25180) describes the
details.

Update: see [Translating an external
workbench](/Translating_an_external_workbench "Translating an external
workbench")

## Automating Crowdin Translation Updates

Currently FreeCAD maintainers use the Crowdin API via [Crowdin
Scripts](/Crowdin_Scripts "Crowdin Scripts") to pull and push translations in
to Crowdin and back in to the Github repo. The Crowdin API gives FreeCAD
maintainers the ability to automate aspects of the project's translation
workflow, for more info refer to the [Crowdin API
documentation](https://support.crowdin.com/api/api-integration-setup/).

## Related Pages

  * [Crowdin Administration](/Crowdin_Administration "Crowdin Administration")
  * [Crowdin Scripts](/Crowdin_Scripts "Crowdin Scripts")

## Scripting

_See also:_ [FreeCAD Scripting Basics](/FreeCAD_Scripting_Basics "FreeCAD
Scripting Basics").

To get a dictionary with the languages the FreeCAD interface supports, use the
`supportedLocales` method of the `FreeCADGui` module.

    
    
    locales = FreeCADGui.supportedLocales()
    

After execution `locales` will contain:

    
    
    {'English': 'en', 'Afrikaans': 'af', 'Arabic': 'ar', 'Basque': 'eu', 'Catalan': 'ca', 'Chinese Simplified': 'zh-CN', 'Chinese Traditional': 'zh-TW', 'Croatian': 'hr', 'Czech': 'cs', 'Dutch': 'nl', 'Filipino': 'fil', 'Finnish': 'fi', 'French': 'fr', 'Galician': 'gl', 'German': 'de', 'Hungarian': 'hu', 'Indonesian': 'id', 'Italian': 'it', 'Japanese': 'ja', 'Kabyle': 'kab', 'Korean': 'ko', 'Lithuanian': 'lt', 'Norwegian': 'no', 'Polish': 'pl', 'Portuguese': 'pt-PT', 'Portuguese, Brazilian': 'pt-BR', 'Romanian': 'ro', 'Russian': 'ru', 'Slovak': 'sk', 'Slovenian': 'sl', 'Spanish': 'es-ES', 'Swedish': 'sv-SE', 'Turkish': 'tr', 'Ukrainian': 'uk', 'Valencian': 'val-ES', 'Vietnamese': 'vi'}
    

To get the current interface language use the `getLocale` method of the same
module:

    
    
    locale = FreeCADGui.getLocale()
    

If the current language is English `locale` will contain:

    
    
    'English'
    

To get the corresponding [language
code](https://support.crowdin.com/api/language-codes/) you can use use:

    
    
    locale = FreeCADGui.supportedLocales()[Gui.getLocale()]
    

If the current language is English the result will be:

    
    
    'en'
    

To set the current interface language use the `setLocale` method of the same
module. You can specify the language or the language code:

    
    
    FreeCADGui.setLocale('Russian')
    FreeCADGui.setLocale('ru')
    

  

![](/images/6/6f/Arrow-left.svg) [Branding](/Branding "Branding")

[Workbench creation](/Workbench_creation "Workbench creation")
![](/images/a/af/Arrow-right.svg)

[Index](/Online_Help_Toc "Online Help Toc")
![](/images/7/76/Online_Help_Toc.svg)

Expand[![](/images/thumb/9/94/User_hub.png/24px-
User_hub.png)](/index.php?title=File:User_hub.png&filetimestamp=20190221145008&)
[User documentation](/User_hub "User hub")

  * **[Getting started](/Getting_started "Getting started")**
  * **Installation:** [Download](/Download "Download"), [Windows](/Installing_on_Windows "Installing on Windows"), [Linux](/Installing_on_Linux "Installing on Linux"), [Mac](/Installing_on_Mac "Installing on Mac"), [Additional components](/Installing_additional_components "Installing additional components"), [Docker](/Compile_on_Docker "Compile on Docker"), [AppImage](/AppImage "AppImage"), [Ubuntu Snap](/Ubuntu_Snap "Ubuntu Snap")
  * **Basics:** [About FreeCAD](/About_FreeCAD "About FreeCAD"), [Interface](/Interface "Interface"), [Mouse navigation](/Mouse_navigation "Mouse navigation"), [Selection methods](/Selection_methods "Selection methods"), [Object name](/Object_name "Object name"), [Preferences](/Preferences_Editor "Preferences Editor"), [Workbenches](/Workbenches "Workbenches"), [Document structure](/Document_structure "Document structure"), [Properties](/Property "Property"), [Help FreeCAD](/Help_FreeCAD "Help FreeCAD"), [Donate](/Donate "Donate")

* * *

  * **Help:** [Tutorials](/Tutorials "Tutorials"), [Video tutorials](/Video_tutorials "Video tutorials")
  * **[Workbenches](/Workbenches "Workbenches"):** [Std Base](/Std_Base "Std Base"), [Assembly](/Assembly_Workbench "Assembly Workbench"), [BIM](/BIM_Workbench "BIM Workbench"), [CAM](/CAM_Workbench "CAM Workbench"), [Draft](/Draft_Workbench "Draft Workbench"), [FEM](/FEM_Workbench "FEM Workbench"), [Inspection](/Inspection_Workbench "Inspection Workbench"), [Material](/Material_Workbench "Material Workbench"), [Mesh](/Mesh_Workbench "Mesh Workbench"), [OpenSCAD](/OpenSCAD_Workbench "OpenSCAD Workbench"), [Part](/Part_Workbench "Part Workbench"), [PartDesign](/PartDesign_Workbench "PartDesign Workbench"), [Points](/Points_Workbench "Points Workbench"), [Reverse Engineering](/Reverse_Engineering_Workbench "Reverse Engineering Workbench"), [Robot](/Robot_Workbench "Robot Workbench"), [Sketcher](/Sketcher_Workbench "Sketcher Workbench"), [Spreadsheet](/Spreadsheet_Workbench "Spreadsheet Workbench"), [Surface](/Surface_Workbench "Surface Workbench"), [TechDraw](/TechDraw_Workbench "TechDraw Workbench"), [Test Framework](/Testing "Testing")

* * *

  * **[Addons](/Addon "Addon"):** [Addon Manager](/Std_AddonMgr "Std AddonMgr"), [External workbenches](/External_workbenches "External workbenches"), [Scripting and macros](/Scripting_and_macros "Scripting and macros")

* * *

  * **Hubs:** [User hub](/User_hub "User hub"), [Power users hub](/Power_users_hub "Power users hub"), [Developer hub](/Developer_hub "Developer hub")

