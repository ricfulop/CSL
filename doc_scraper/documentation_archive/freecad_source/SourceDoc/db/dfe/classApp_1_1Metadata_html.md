---
url: https://freecad.github.io/SourceDoc/db/dfe/classApp_1_1Metadata.html
scraped_at: 2025-09-08T14:55:07.633251
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [Metadata](../../db/dfe/classApp_1_1Metadata.html)

[List of all members](../../da/d6d/classApp_1_1Metadata-members.html) | Public Member Functions

App::Metadata Class Reference

Reads data from a metadata file.
[More...](../../db/dfe/classApp_1_1Metadata.html#details)

`#include <Metadata.h>`

##  Public Member Functions  
  
---  
void | [addAuthor](../../db/dfe/classApp_1_1Metadata.html#a819eb31d898acd45ae4a7775279c07a7) (const [Meta::Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html) &[author](../../db/dfe/classApp_1_1Metadata.html#a664cf48813046e7b6a7c45f20fa1f0c3))  
void | [addConflict](../../db/dfe/classApp_1_1Metadata.html#afa2695fedb92a084728afeb2bb9c347f) (const [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) &dep)  
void | [addContentItem](../../db/dfe/classApp_1_1Metadata.html#abddcd05e07a2ffa29a37c264efb759c9) (const std::string &[tag](../../db/dfe/classApp_1_1Metadata.html#ad94f16a5ea0584d5a2e72b8b5ea6dea5), const [Metadata](../../db/dfe/classApp_1_1Metadata.html) &item)  
void | [addDepend](../../db/dfe/classApp_1_1Metadata.html#a57d1c0766df6acbd80ef8676ec6f5fe5) (const [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) &dep)  
void | [addFile](../../db/dfe/classApp_1_1Metadata.html#a584c82fe15c4f68fd0718033c4761b0c) (const boost::filesystem::path &path)  
void | [addGenericMetadata](../../db/dfe/classApp_1_1Metadata.html#a213c909572dae53be01d728d974a4137) (const std::string &[tag](../../db/dfe/classApp_1_1Metadata.html#ad94f16a5ea0584d5a2e72b8b5ea6dea5), const [Meta::GenericMetadata](../../d9/dc6/structApp_1_1Meta_1_1GenericMetadata.html) &genericMetadata)  
void | [addLicense](../../db/dfe/classApp_1_1Metadata.html#a209f2b65c9a208790d92cefb6f267974) (const [Meta::License](../../d0/d77/structApp_1_1Meta_1_1License.html) &[license](../../db/dfe/classApp_1_1Metadata.html#a5630aec416ec2e8e6678917e9950b516))  
void | [addMaintainer](../../db/dfe/classApp_1_1Metadata.html#a09515341f0fe12b989c9587098823e61) (const [Meta::Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html) &[maintainer](../../db/dfe/classApp_1_1Metadata.html#a21d780253a0197b1554ed61592400e0a))  
void | [addReplace](../../db/dfe/classApp_1_1Metadata.html#a4a648929277c053a4f64e781b8337225) (const [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) &dep)  
void | [addTag](../../db/dfe/classApp_1_1Metadata.html#a921b4baf13da0fea9f5a52e2ea737e34) (const std::string &[tag](../../db/dfe/classApp_1_1Metadata.html#ad94f16a5ea0584d5a2e72b8b5ea6dea5))  
void | [addUrl](../../db/dfe/classApp_1_1Metadata.html#ab0c41634e4d9dc6bf26609342b92cd00) (const [Meta::Url](../../d7/de5/structApp_1_1Meta_1_1Url.html) &[url](../../db/dfe/classApp_1_1Metadata.html#a947dab1b09c9c384f2151d183ed8703a))  
std::vector< [Meta::Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html) > | [author](../../db/dfe/classApp_1_1Metadata.html#a664cf48813046e7b6a7c45f20fa1f0c3) () const  
std::string | [classname](../../db/dfe/classApp_1_1Metadata.html#ab4eefe9b5d16c62e9b8533c2cf7d4493) () const  
std::vector< [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) > | [conflict](../../db/dfe/classApp_1_1Metadata.html#a97cb6b85044db96733d0881e010c55c7) () const  
std::multimap< std::string, [Metadata](../../db/dfe/classApp_1_1Metadata.html) > | [content](../../db/dfe/classApp_1_1Metadata.html#a6d71a54cf2e4b7ee189fd061f61f92b2) () const  
| Access the metadata for the content elements of this package.
[More...](../../db/dfe/classApp_1_1Metadata.html#a6d71a54cf2e4b7ee189fd061f61f92b2)  
  
std::vector< [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) > | [depend](../../db/dfe/classApp_1_1Metadata.html#a7d556fc7ae03edd6be8fdefab76d41ed) () const  
std::string | [description](../../db/dfe/classApp_1_1Metadata.html#a565c99c0358c52a56a41bd639743e075) () const  
XERCES_CPP_NAMESPACE::DOMElement * | [dom](../../db/dfe/classApp_1_1Metadata.html#a48981b2fcea61cefa10d182e2e50dfea) () const  
| Directly access the DOM tree to support unrecognized multi-level metadata.
[More...](../../db/dfe/classApp_1_1Metadata.html#a48981b2fcea61cefa10d182e2e50dfea)  
  
std::vector< boost::filesystem::path > | [file](../../db/dfe/classApp_1_1Metadata.html#af3ed8f8fb4b3c9389a4906d8661ae50b) () const  
[Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) | [freecadmax](../../db/dfe/classApp_1_1Metadata.html#a2fad950b46467606bdc368397f952a95) () const  
[Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) | [freecadmin](../../db/dfe/classApp_1_1Metadata.html#a8b334aeec8ba7d9e223bef84a07f68f3) () const  
boost::filesystem::path | [icon](../../db/dfe/classApp_1_1Metadata.html#a8e69b898f5efe5c7880302176c82e409) () const  
std::vector< [Meta::License](../../d0/d77/structApp_1_1Meta_1_1License.html) > | [license](../../db/dfe/classApp_1_1Metadata.html#a5630aec416ec2e8e6678917e9950b516) () const  
std::vector< [Meta::Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html) > | [maintainer](../../db/dfe/classApp_1_1Metadata.html#a21d780253a0197b1554ed61592400e0a) () const  
|
[Metadata](../../db/dfe/classApp_1_1Metadata.html#a21a1a8f0861128ad03cc8d31eeb1298a)
()  
|
[Metadata](../../db/dfe/classApp_1_1Metadata.html#a1ac8d5451b5001b5c22c2462c3ba7908)
(const boost::filesystem::path &metadataFile)  
| Read the data from a file on disk.
[More...](../../db/dfe/classApp_1_1Metadata.html#a1ac8d5451b5001b5c22c2462c3ba7908)  
  
|
[Metadata](../../db/dfe/classApp_1_1Metadata.html#a7f1a177bd4b8a87a3040e71567fc69ab)
(const XERCES_CPP_NAMESPACE::DOMNode *domNode,
[int](../../d1/da0/classint.html) format)  
| Construct a [Metadata](../../db/dfe/classApp_1_1Metadata.html "Reads data
from a metadata file.") object from a DOM node.
[More...](../../db/dfe/classApp_1_1Metadata.html#a7f1a177bd4b8a87a3040e71567fc69ab)  
  
std::string | [name](../../db/dfe/classApp_1_1Metadata.html#a75ac1e8c2967b464bfb0cf7436adbb7c) () const  
std::vector< [Meta::GenericMetadata](../../d9/dc6/structApp_1_1Meta_1_1GenericMetadata.html) > | [operator[]](../../db/dfe/classApp_1_1Metadata.html#af17bd4fd7200b90ba91ff0bb223930c0) (const std::string &[tag](../../db/dfe/classApp_1_1Metadata.html#ad94f16a5ea0584d5a2e72b8b5ea6dea5)) const  
| Convenience accessor for unrecognized simple metadata.
[More...](../../db/dfe/classApp_1_1Metadata.html#af17bd4fd7200b90ba91ff0bb223930c0)  
  
void | [removeContentItem](../../db/dfe/classApp_1_1Metadata.html#a645eb826a99299b8dca6c0a8f9ab63dc) (const std::string &[tag](../../db/dfe/classApp_1_1Metadata.html#ad94f16a5ea0584d5a2e72b8b5ea6dea5), const std::string &itemName)  
std::vector< [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) > | [replace](../../db/dfe/classApp_1_1Metadata.html#ac1774b28a6ad503c15cbb74ed581873e) () const  
[bool](../../d9/db9/classbool.html) | [satisfies](../../db/dfe/classApp_1_1Metadata.html#a022c52baf660a45a8870dd2e7042f13c) (const [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) &)  
| Determine whether this package satisfies the given dependency.
[More...](../../db/dfe/classApp_1_1Metadata.html#a022c52baf660a45a8870dd2e7042f13c)  
  
void | [setClassname](../../db/dfe/classApp_1_1Metadata.html#a0ee846a9ecddc10481a6cfda96c4c528) (const std::string &[name](../../db/dfe/classApp_1_1Metadata.html#a75ac1e8c2967b464bfb0cf7436adbb7c))  
void | [setDescription](../../db/dfe/classApp_1_1Metadata.html#a8eef82750f67142aff5f4acbbf5b445e) (const std::string &[description](../../db/dfe/classApp_1_1Metadata.html#a565c99c0358c52a56a41bd639743e075))  
void | [setFreeCADMax](../../db/dfe/classApp_1_1Metadata.html#a1a9656a28ec7c20026cd5aea0f88c703) (const [Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) &[version](../../db/dfe/classApp_1_1Metadata.html#abcb2493b0ed92b22d9c47980e5aaaf5d))  
void | [setFreeCADMin](../../db/dfe/classApp_1_1Metadata.html#aa301e7c41c99fceb11222d80cceb733a) (const [Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) &[version](../../db/dfe/classApp_1_1Metadata.html#abcb2493b0ed92b22d9c47980e5aaaf5d))  
void | [setIcon](../../db/dfe/classApp_1_1Metadata.html#a4bc6771bce32d276b8ef73171bae27ec) (const boost::filesystem::path &path)  
void | [setName](../../db/dfe/classApp_1_1Metadata.html#a6e06a7f6c75b618832b554e82959bf8c) (const std::string &[name](../../db/dfe/classApp_1_1Metadata.html#a75ac1e8c2967b464bfb0cf7436adbb7c))  
void | [setSubdirectory](../../db/dfe/classApp_1_1Metadata.html#a02e5983d2c69e498feb37728508419d3) (const boost::filesystem::path &path)  
void | [setVersion](../../db/dfe/classApp_1_1Metadata.html#a5951c39bfd764d689e7842c92b033496) (const [Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) &[version](../../db/dfe/classApp_1_1Metadata.html#abcb2493b0ed92b22d9c47980e5aaaf5d))  
boost::filesystem::path | [subdirectory](../../db/dfe/classApp_1_1Metadata.html#a639ebe9265788d00f6b0866b7189e936) () const  
[bool](../../d9/db9/classbool.html) | [supportsCurrentFreeCAD](../../db/dfe/classApp_1_1Metadata.html#a5a2340d71416e32211e1a6d1da938fcb) () const  
| Determine whether the current metadata specifies support for the currently-
running version of FreeCAD.
[More...](../../db/dfe/classApp_1_1Metadata.html#a5a2340d71416e32211e1a6d1da938fcb)  
  
std::vector< std::string > | [tag](../../db/dfe/classApp_1_1Metadata.html#ad94f16a5ea0584d5a2e72b8b5ea6dea5) () const  
std::vector< [Meta::Url](../../d7/de5/structApp_1_1Meta_1_1Url.html) > | [url](../../db/dfe/classApp_1_1Metadata.html#a947dab1b09c9c384f2151d183ed8703a) () const  
[Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) | [version](../../db/dfe/classApp_1_1Metadata.html#abcb2493b0ed92b22d9c47980e5aaaf5d) () const  
void | [write](../../db/dfe/classApp_1_1Metadata.html#ae9d5f5ecaccd6c347ca091978d5cca7a) (const boost::filesystem::path &[file](../../db/dfe/classApp_1_1Metadata.html#af3ed8f8fb4b3c9389a4906d8661ae50b)) const  
| Write the metadata to an XML file.
[More...](../../db/dfe/classApp_1_1Metadata.html#ae9d5f5ecaccd6c347ca091978d5cca7a)  
  
|
[~Metadata](../../db/dfe/classApp_1_1Metadata.html#a29845232ba882e6dba16311f2ae4c374)
()  
  
## Detailed Description

Reads data from a metadata file.

The metadata format is based on <https://ros.org/reps/rep-0149.html>, modified
for FreeCAD use. Full format documentation is available at the FreeCAD Wiki:
<https://wiki.freecadweb.org/Package_Metadata>

## Constructor & Destructor Documentation

## ◆ Metadata() [1/3]

Metadata::Metadata  | ( | | ) |   
---|---|---|---|---  
  
## ◆ Metadata() [2/3]

| App::Metadata::Metadata  | ( | const boost::filesystem::path & | _metadataFile_| ) |   
---|---|---|---|---|---  
explicit  
  
Read the data from a file on disk.

This constructor takes a path to an XML file and loads the XML from that file
as metadata.

## ◆ Metadata() [3/3]

App::Metadata::Metadata  | ( | const XERCES_CPP_NAMESPACE::DOMNode *  | _domNode_ ,   
---|---|---|---  
|  | [int](../../d1/da0/classint.html) | _format_  
| ) | |   
  
Construct a [Metadata](../../db/dfe/classApp_1_1Metadata.html "Reads data from
a metadata file.") object from a DOM node.

This node may have any tag name: it is only accessed via its children, which
are expected to follow the standard
[Metadata](../../db/dfe/classApp_1_1Metadata.html "Reads data from a metadata
file.") format for the contents of the <package> element.

## ◆ ~Metadata()

Metadata::~Metadata  | ( | | ) |   
---|---|---|---|---  
  
## Member Function Documentation

## ◆ addAuthor()

void Metadata::addAuthor  | ( | const [Meta::Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html) & | _author_| ) |   
---|---|---|---|---|---  
  
References
[author()](../../db/dfe/classApp_1_1Metadata.html#a664cf48813046e7b6a7c45f20fa1f0c3).

## ◆ addConflict()

void Metadata::addConflict  | ( | const [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) & | _dep_| ) |   
---|---|---|---|---|---  
  
## ◆ addContentItem()

void Metadata::addContentItem  | ( | const std::string & | _tag_ ,   
---|---|---|---  
|  | const [Metadata](../../db/dfe/classApp_1_1Metadata.html) & | _item_  
| ) | |   
  
References
[tag()](../../db/dfe/classApp_1_1Metadata.html#ad94f16a5ea0584d5a2e72b8b5ea6dea5).

## ◆ addDepend()

void Metadata::addDepend  | ( | const [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) & | _dep_| ) |   
---|---|---|---|---|---  
  
## ◆ addFile()

void Metadata::addFile  | ( | const boost::filesystem::path & | _path_| ) |   
---|---|---|---|---|---  
  
## ◆ addGenericMetadata()

void App::Metadata::addGenericMetadata  | ( | const std::string & | _tag_ ,   
---|---|---|---  
|  | const [Meta::GenericMetadata](../../d9/dc6/structApp_1_1Meta_1_1GenericMetadata.html) & | _genericMetadata_  
| ) | |   
  
## ◆ addLicense()

void Metadata::addLicense  | ( | const [Meta::License](../../d0/d77/structApp_1_1Meta_1_1License.html) & | _license_| ) |   
---|---|---|---|---|---  
  
References
[license()](../../db/dfe/classApp_1_1Metadata.html#a5630aec416ec2e8e6678917e9950b516).

## ◆ addMaintainer()

void Metadata::addMaintainer  | ( | const [Meta::Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html) & | _maintainer_| ) |   
---|---|---|---|---|---  
  
References
[maintainer()](../../db/dfe/classApp_1_1Metadata.html#a21d780253a0197b1554ed61592400e0a).

## ◆ addReplace()

void Metadata::addReplace  | ( | const [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) & | _dep_| ) |   
---|---|---|---|---|---  
  
## ◆ addTag()

void Metadata::addTag  | ( | const std::string & | _tag_| ) |   
---|---|---|---|---|---  
  
References
[tag()](../../db/dfe/classApp_1_1Metadata.html#ad94f16a5ea0584d5a2e72b8b5ea6dea5).

## ◆ addUrl()

void Metadata::addUrl  | ( | const [Meta::Url](../../d7/de5/structApp_1_1Meta_1_1Url.html) & | _url_| ) |   
---|---|---|---|---|---  
  
References
[url()](../../db/dfe/classApp_1_1Metadata.html#a947dab1b09c9c384f2151d183ed8703a).

## ◆ author()

std::vector< [Meta::Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html) > Metadata::author  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[addAuthor()](../../db/dfe/classApp_1_1Metadata.html#a819eb31d898acd45ae4a7775279c07a7),
and
[addonmanager_macro.Macro::fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac).

## ◆ classname()

std::string Metadata::classname  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ conflict()

std::vector< [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) > Metadata::conflict  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ content()

std::multimap< std::string, [Metadata](../../db/dfe/classApp_1_1Metadata.html) > Metadata::content  | ( | | ) |  const  
---|---|---|---|---  
  
Access the metadata for the content elements of this package.

In addition to the overall package metadata, this class reads in metadata
contained in a <content> element. Each entry in the content element is an
element representing some type of package content (e.g. add-on, macro, theme,
etc.). This class places no restriction on the types, it is up to client code
to place requirements on the metadata included here.

For example, themes might be specified: <content> <theme> <name>High
Contrast</name> </theme> </content>

## ◆ depend()

std::vector< [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) > Metadata::depend  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ description()

std::string Metadata::description  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[Addon.Addon::set_metadata()](../../d8/d91/classAddon_1_1Addon.html#a799523f4861c30f1516a59602d5b77cd),
[setDescription()](../../db/dfe/classApp_1_1Metadata.html#a8eef82750f67142aff5f4acbbf5b445e),
and
[Addon.Addon::to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5).

## ◆ dom()

XERCES_CPP_NAMESPACE::DOMElement * Metadata::dom  | ( | | ) |  const  
---|---|---|---|---  
  
Directly access the DOM tree to support unrecognized multi-level metadata.

## ◆ file()

std::vector< fs::path > Metadata::file  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[exportIFCHelper.ContextCreator::createAutomaticProject()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a148406623b830e96b625e4cc9ac25bd2),
[exportIFCHelper.ContextCreator::createCustomProject()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a34f97033698a98007b430b629d694626),
[exportIFCHelper.ContextCreator::createGeometricRepresentationContext()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a6a54d0b2f20650b6a7ce05d57d2ae8e3),
[exportIFCHelper.ContextCreator::createGeometricRepresentationSubContext()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a706ac46037632ab6fb9ea483bf3e4095),
[exportIFCHelper.ContextCreator::createMapConversion()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#aac779e6f884db286129eb07b8622645b),
[exportIFCHelper.ContextCreator::createTargetCRS()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#ab3bc2c1c6282b286bd93af440fda7afc),
[exportIFCHelper.ContextCreator::createTrueNorth()](../../da/d37/classexportIFCHelper_1_1ContextCreator.html#a8491dc7a339dce3412310dd42a65fd01),
[importIFClegacy.IfcFile::read()](../../d1/daa/classimportIFClegacy_1_1IfcFile.html#a9ad8d00537a61e0be429282c1c56fbdf),
and
[write()](../../db/dfe/classApp_1_1Metadata.html#ae9d5f5ecaccd6c347ca091978d5cca7a).

## ◆ freecadmax()

[Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) App::Metadata::freecadmax  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ freecadmin()

[Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) App::Metadata::freecadmin  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ icon()

fs::path Metadata::icon  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[addonmanager_macro.Macro::clean_icon()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a94e9c6586319d94b2ecd76c44e75601b),
[addonmanager_macro.Macro::fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[PathScripts.PathIconViewProvider.ViewProvider::getIcon()](../../d6/d55/classPathScripts_1_1PathIconViewProvider_1_1ViewProvider.html#ad1e3aaade62b820d052609905b752b99),
[PathScripts.PathOpGui.TaskPanelPage::getIcon()](../../d1/d18/classPathScripts_1_1PathOpGui_1_1TaskPanelPage.html#a354ad06f5f53f28d9fdae88eb6847181),
[addonmanager_macro.Macro::install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[addonmanager_macro.Macro::parse_wiki_page_for_icon()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#abf07ba9675bd3b47fcbca8e7ef0e37ad),
and
[addonmanager_macro.Macro::remove()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ad13245288f8beb62d92cb458a2d2ce05).

## ◆ license()

std::vector< [Meta::License](../../d0/d77/structApp_1_1Meta_1_1License.html) > Metadata::license  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[addLicense()](../../db/dfe/classApp_1_1Metadata.html#a209f2b65c9a208790d92cefb6f267974).

## ◆ maintainer()

std::vector< [Meta::Contact](../../dc/d04/structApp_1_1Meta_1_1Contact.html) > Metadata::maintainer  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[addMaintainer()](../../db/dfe/classApp_1_1Metadata.html#a09515341f0fe12b989c9587098823e61).

## ◆ name()

std::string Metadata::name  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[draftguitools.gui_groups.Ui_AddNamedGroup::accept()](../../d3/df7/classdraftguitools_1_1gui__groups_1_1Ui__AddNamedGroup.html#a9ea5973817eab7d74792f5b109a01466),
[prototype.Node::addtofreecad()](../../d2/d62/classprototype_1_1Node.html#adc095cc5636da029d1e0d9cef8859701),
[Addon.Addon::disable()](../../d8/d91/classAddon_1_1Addon.html#ae714705a38afe9f13cd2b17580178b31),
[Addon.Addon::enable()](../../d8/d91/classAddon_1_1Addon.html#a79d327ec9a0b4e85e9e96cfad4003ed6),
[addonmanager_macro.Macro::filename()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a5de4e6a1f3c41dce24066111955cd706),
[gzip_utf8.GzipFile::filename()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ab56fe84a4eb08c44e7a0026280c01229),
[addonmanager_macro.Macro::fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[addonmanager_macro.Macro::fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon::get_cached_icon_filename()](../../d8/d91/classAddon_1_1Addon.html#a7b026027a2904028032edbe3e99e2cbd),
[ifc4.ifcapproval::hasidentifierorname()](../../df/d91/classifc4_1_1ifcapproval.html#a54f558ba3b17fad5fc6579e9d5f50947),
[addonmanager_macro.Macro::install()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ae770ab07dcecebae2b7414f278b227fe),
[Addon.Addon::is_disabled()](../../d8/d91/classAddon_1_1Addon.html#a5752a95fcf0c51ed06f9841b381d3e50),
[femsolver.elmer.sifio.Section::keys()](../../db/dab/classfemsolver_1_1elmer_1_1sifio_1_1Section.html#ab5b099447f66f33743850697f0e20de4),
[automotive_design.si_unit::named_unit_dimensions()](../../d5/d77/classautomotive__design_1_1si__unit.html#a68eb7954eb09daa334bc8f2c2abbe5f9),
[Mod.PartDesign.WizardShaft.SegmentFunction.SegmentFunction::output()](../../de/d2e/classMod_1_1PartDesign_1_1WizardShaft_1_1SegmentFunction_1_1SegmentFunction.html#aeedd5f59969cc27432880d1916f3d7f9),
[prototype.Node::pprint()](../../d2/d62/classprototype_1_1Node.html#a5ae181c34e48238d2364b0ba4960c252),
[prototype.Node::pprint2()](../../d2/d62/classprototype_1_1Node.html#aaedcc4ba1fb305c7ddcc025235043cd5),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyGroup()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#a69cbbaadcb9cff7b526af2c743041d7b),
[PathScripts.PathSetupSheetGui.OpTaskPanel::propertyName()](../../df/dbe/classPathScripts_1_1PathSetupSheetGui_1_1OpTaskPanel.html#ad9bd0e0149d1bc42fc8e89a290de4910),
[PathScripts.PathJobGui.TaskPanel::reject()](../../dc/d2a/classPathScripts_1_1PathJobGui_1_1TaskPanel.html#a54fd97ba9b0060fa8fed8a43c360da0c),
[addonmanager_macro.Macro::remove()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#ad13245288f8beb62d92cb458a2d2ce05),
[setClassname()](../../db/dfe/classApp_1_1Metadata.html#a0ee846a9ecddc10481a6cfda96c4c528),
[setName()](../../db/dfe/classApp_1_1Metadata.html#a6e06a7f6c75b618832b554e82959bf8c),
[Addon.Addon::to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
[ifc2x3.ifcexternalreference::wr1()](../../dd/dec/classifc2x3_1_1ifcexternalreference.html#ae8dab59397d2468ff7fe0a10f42b75b2),
[ifc2x3.ifcdocumentreference::wr1()](../../df/dd6/classifc2x3_1_1ifcdocumentreference.html#a7d5fdb1cb0dee567c44834b868c5cdad),
[ifc4.ifcexternalreference::wr1()](../../d5/dd9/classifc4_1_1ifcexternalreference.html#a0e6ba5265c69b44700e8d9b179e9f240),
[ifc4.ifcdocumentreference::wr1()](../../d7/d2b/classifc4_1_1ifcdocumentreference.html#a8779d74c67e647441d1fb20c76f44f97),
and
[automotive_design.general_property_association::wr2()](../../d2/df3/classautomotive__design_1_1general__property__association.html#ae7f46462c59bc4e541a5d2511631eb65).

## ◆ operator[]()

std::vector< [Meta::GenericMetadata](../../d9/dc6/structApp_1_1Meta_1_1GenericMetadata.html) > Metadata::operator[]  | ( | const std::string & | _tag_| ) |  const  
---|---|---|---|---|---  
  
Convenience accessor for unrecognized simple metadata.

If the XML parser encounters tags that it does not recognize, and those tags
have no children, a GenericMetadata object is created. Those objects can be
accessed using operator[], which returns a (potentially empty) vector
containing all instances of the given tag. It cannot be used to _create_ a new
tag, however. See
[addGenericMetadata()](../../db/dfe/classApp_1_1Metadata.html#a213c909572dae53be01d728d974a4137).

References
[tag()](../../db/dfe/classApp_1_1Metadata.html#ad94f16a5ea0584d5a2e72b8b5ea6dea5).

## ◆ removeContentItem()

void App::Metadata::removeContentItem  | ( | const std::string & | _tag_ ,   
---|---|---|---  
|  | const std::string & | _itemName_  
| ) | |   
  
## ◆ replace()

std::vector< [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) > Metadata::replace  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ satisfies()

[bool](../../d9/db9/classbool.html) Metadata::satisfies  | ( | const [Meta::Dependency](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html) & | _dep_| ) |   
---|---|---|---|---|---  
  
Determine whether this package satisfies the given dependency.

References
[App::Meta::Dependency::condition](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html#a057417946fd29adb5cfd250ec3299a3f),
[App::Application::Config()](../../da/dbf/classApp_1_1Application.html#ae8e7accfb4fc5cda6a0cf9100c38d6fc),
[App::Meta::Dependency::package](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html#a48b5e9755962b4cf4567b6bd1146e421),
[App::Expression::parse()](../../dc/d5c/classApp_1_1Expression.html#a377c20925f92aab0265eb9e3e0b35c97),
[App::Meta::Dependency::version_eq](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html#a42f33142f792c496e0d665bcaf1fbc6b),
[App::Meta::Dependency::version_gt](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html#a8b1404b20fe218a8691e413276d7b8ac),
[App::Meta::Dependency::version_gte](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html#a9ff3b593de3a89bb4bacf71bd2b1eed2),
[App::Meta::Dependency::version_lt](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html#a58d5a9a2cc6150632c2735b3f058073e),
and
[App::Meta::Dependency::version_lte](../../d3/d3b/structApp_1_1Meta_1_1Dependency.html#af1eb75899f66a09831ec98e876283b3f).

## ◆ setClassname()

void Metadata::setClassname  | ( | const std::string & | _name_| ) |   
---|---|---|---|---|---  
  
References
[name()](../../db/dfe/classApp_1_1Metadata.html#a75ac1e8c2967b464bfb0cf7436adbb7c).

## ◆ setDescription()

void Metadata::setDescription  | ( | const std::string & | _description_| ) |   
---|---|---|---|---|---  
  
References
[description()](../../db/dfe/classApp_1_1Metadata.html#a565c99c0358c52a56a41bd639743e075).

## ◆ setFreeCADMax()

void App::Metadata::setFreeCADMax  | ( | const [Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) & | _version_| ) |   
---|---|---|---|---|---  
  
## ◆ setFreeCADMin()

void App::Metadata::setFreeCADMin  | ( | const [Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) & | _version_| ) |   
---|---|---|---|---|---  
  
## ◆ setIcon()

void Metadata::setIcon  | ( | const boost::filesystem::path & | _path_| ) |   
---|---|---|---|---|---  
  
## ◆ setName()

void Metadata::setName  | ( | const std::string & | _name_| ) |   
---|---|---|---|---|---  
  
References
[name()](../../db/dfe/classApp_1_1Metadata.html#a75ac1e8c2967b464bfb0cf7436adbb7c).

Referenced by
[Gui::PreferencePackManager::save()](../../d9/d11/classGui_1_1PreferencePackManager.html#aee5aeff2da8d329471da39b2741bffa8).

## ◆ setSubdirectory()

void App::Metadata::setSubdirectory  | ( | const boost::filesystem::path & | _path_| ) |   
---|---|---|---|---|---  
  
## ◆ setVersion()

void Metadata::setVersion  | ( | const [Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) & | _version_| ) |   
---|---|---|---|---|---  
  
References
[version()](../../db/dfe/classApp_1_1Metadata.html#abcb2493b0ed92b22d9c47980e5aaaf5d).

Referenced by
[Gui::PreferencePackManager::save()](../../d9/d11/classGui_1_1PreferencePackManager.html#aee5aeff2da8d329471da39b2741bffa8).

## ◆ subdirectory()

boost::filesystem::path App::Metadata::subdirectory  | ( | | ) |  const  
---|---|---|---|---  
  
## ◆ supportsCurrentFreeCAD()

[bool](../../d9/db9/classbool.html) App::Metadata::supportsCurrentFreeCAD  | ( | | ) |  const  
---|---|---|---|---  
  
Determine whether the current metadata specifies support for the currently-
running version of FreeCAD.

Does not interrogate content items, which must be querried individually.

References
[App::Application::Config()](../../da/dbf/classApp_1_1Application.html#ae8e7accfb4fc5cda6a0cf9100c38d6fc).

## ◆ tag()

std::vector< std::string > Metadata::tag  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[PathScripts.PathDressupHoldingTags.MapWireToTag::add()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#a635a31c3648c89f099d5fe6f97368237),
[addContentItem()](../../db/dfe/classApp_1_1Metadata.html#abddcd05e07a2ffa29a37c264efb759c9),
[addTag()](../../db/dfe/classApp_1_1Metadata.html#a921b4baf13da0fea9f5a52e2ea737e34),
[PathScripts.PathDressupHoldingTags.MapWireToTag::cleanupEdges()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#ad67774cf1b6aa1f4bb6bc52fa932df83),
[PathScripts.PathDressupHoldingTags.MapWireToTag::commandsForEdges()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#a198fbf1f749b551d10e292784e5921cf),
[Dice3DS.dom3ds.ChunkBase::document_html()](../../da/da5/classDice3DS_1_1dom3ds_1_1ChunkBase.html#abdc79325208ba093e3b508c646b3a4ba),
[Dice3DS.dom3ds.ChunkBase::dump_header()](../../da/da5/classDice3DS_1_1dom3ds_1_1ChunkBase.html#a64b07f8bfad61e851b2c2fb3c2974d9a),
[ArchPanel.PanelCut::getWires()](../../d6/dbd/classArchPanel_1_1PanelCut.html#a61534af5c2a0125dde05e08a22025195),
[operator[]()](../../db/dfe/classApp_1_1Metadata.html#af17bd4fd7200b90ba91ff0bb223930c0),
[PathScripts.PathDressupHoldingTags.MapWireToTag::shell()](../../dd/dd7/classPathScripts_1_1PathDressupHoldingTags_1_1MapWireToTag.html#a2f0df7770665a77dc3ec39aad49a7a58),
and
[FreeCADInit.FCADLogger::trace()](../../d2/d1e/classFreeCADInit_1_1FCADLogger.html#a9e5cc4f866ef7f6e4699ad1b481d7879).

## ◆ url()

std::vector< [Meta::Url](../../d7/de5/structApp_1_1Meta_1_1Url.html) > Metadata::url  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[addUrl()](../../db/dfe/classApp_1_1Metadata.html#ab0c41634e4d9dc6bf26609342b92cd00),
[addonmanager_macro.Macro::fill_details_from_wiki()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#afc7e62120da96fc1be9dd2b4bd28ddac),
[Addon.Addon::set_metadata()](../../d8/d91/classAddon_1_1Addon.html#a799523f4861c30f1516a59602d5b77cd),
[Addon.Addon::to_cache()](../../d8/d91/classAddon_1_1Addon.html#aba84dd320889a7cb37c99a8b8cdc87f5),
and
[Addon.Addon::verify_url_and_branch()](../../d8/d91/classAddon_1_1Addon.html#a920e70c1e01170868b69690eff7913e3).

## ◆ version()

[Meta::Version](../../dc/d5f/structApp_1_1Meta_1_1Version.html) Metadata::version  | ( | | ) |  const  
---|---|---|---|---  
  
Referenced by
[addonmanager_macro.Macro::fill_details_from_code()](../../d1/dca/classaddonmanager__macro_1_1Macro.html#a49b8d021a9b8255f8a490e880eb15489),
[Gui::Dialog::AboutDialog::on_copyButton_clicked()](../../d5/de0/classGui_1_1Dialog_1_1AboutDialog.html#a907ddd1537ac512ba4859ee2fb4575a6),
and
[setVersion()](../../db/dfe/classApp_1_1Metadata.html#a5951c39bfd764d689e7842c92b033496).

## ◆ write()

void Metadata::write  | ( | const boost::filesystem::path & | _file_| ) |  const  
---|---|---|---|---|---  
  
Write the metadata to an XML file.

References
[file()](../../db/dfe/classApp_1_1Metadata.html#af3ed8f8fb4b3c9389a4906d8661ae50b).

Referenced by
[gzip_utf8.GzipFile::seek()](../../d2/dbe/classgzip__utf8_1_1GzipFile.html#ac5b53848e16b6ba800ed9ac8d3f737c3).

* * *

The documentation for this class was generated from the following files:

  * FreeCAD/src/App/Metadata.h
  * FreeCAD/src/App/Metadata.cpp

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

