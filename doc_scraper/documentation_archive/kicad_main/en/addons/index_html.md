---
url: https://dev-docs.kicad.org/en/addons/index.html
scraped_at: 2025-09-08T15:30:31.512985
title: KiCad Addons
---

# KiCad Addons

## Publishing KiCad Addons

This document is a guide for users and plugin developers who are interested in
creating addon packages that can be installed by the KiCad plugin and content
manager.

### The Plugin and Content Manager

The plugin and content manager (PCM) allows KiCad users to discover and
install addon packages from public or private repositories. These addon
packages may contain Python plugins, symbol or footprint libraries, color
themes, and other KiCad content. The KiCad team operates an official
repository of addon content that is available by default to KiCad users. Users
may also add other repositories, either hosted publicly by third parties or
privately (for example, an internal corporate repository).

### Packaging your content

A KiCad addon package consists of a compressed archive file containing a metadata file, the package content, and several optional files. The archive must be in ZIP format (compatible with the ISO 21320-1 standard). The contents of the archive file depend on the package type, but all packages must include a control file called `metadata.json` that is described in detail below. |  __ |  Addon archives must follow the exact folder structure listed below. Extra files that are not related to your addon are not permitted and must be stripped out of the archive.   
---|---  
  
#### Python plugins

The structure of a Python plugin archive must look like:

    
    
    Archive root
    |- plugins
       |- __init__.py
       |- ...
    |- resources
       |- icon.png
    |- metadata.json

`icon.png` is an optional 64x64-pixel icon that will be displayed alongside
your package in the PCM dialog. If no icon is supplied, the `resources`
subdirectory may be empty or omitted.

The contents of the `plugins` subdirectory should include any Python source
files and resources required by your plugin. Place your plugin directly inside
the `plugins` subdirectory, not inside a second level of subdirectory.

__ |  For action plugins that supply a toolbar button icon, this icon should be smaller (24x24) and located inside the `plugins` subdirectory. The action plugin toolbar icon will not be used by the PCM.   
---|---  
  
#### Content libraries

The structure of a content library package must look like:

    
    
    Archive root
    |- footprints
       |- first-library.pretty
          |- my-footprint.kicad_mod
          |- ...
       |- second-library.pretty
          |- another-footprint.kicad_mod
          |- ...
    |- 3dmodels
       |- 3d-library.3dshapes
          |- my-model.stp
          |- my-model.wrl
          |- ...
    |- symbols
          |- my-symbols.kicad_sym
          |- ...
    |- resources
       |- icon.png
    |- metadata.json

Each content library package must contain one or more of the `footprints`,
`3dmodels`, or `symbols` subdirectories. Each of these subdirectories may
contain one or more libraries of the corresponding type.

`icon.png` is an optional 64x64-pixel icon that will be displayed alongside
your package in the PCM dialog. If no icon is supplied, the `resources`
subdirectory may be empty or omitted.

#### Color themes

The structure of a color theme package must look like:

    
    
    Archive root
    |- colors
       |- my-theme.json
    |- resources
       |- icon.png
    |- metadata.json

`icon.png` is an optional 64x64-pixel icon that will be displayed alongside
your package in the PCM dialog. If no icon is supplied, the `resources`
subdirectory may be empty or omitted. For color themes, it is best if the icon
somehow represents the theme, for example by using the same primary colors and
background color as the theme.

#### Metadata file format

The metadata file, `metadata.json`, follows a JSON schema, currently published
at <https://go.kicad.org/pcm/schemas/v1>

Unless otherwise noted all fields are limited to valid UTF-8 code points and
1000 characters.

Example `metadata.json` for a color theme:

    
    
    {
        "$schema": "https://go.kicad.org/pcm/schemas/v1",
        "name": "My Beautiful Theme",
        "description": "A theme that makes KiCad truly beautiful",
        "description_full": "I came up with this theme in a dream one night.",
        "identifier": "com.github.kicad-user.kicad-beautiful-theme",
        "type": "colortheme",
        "author": {
            "name": "KiCad User",
            "contact": {
                "web": "https://mywebsite.com"
            }
        },
        "maintainer": {
            "name": "KiCad User",
            "contact": {
                "web": "https://mywebsite.com"
            }
        },
        "license": "CC0-1.0",
        "resources": {
            "homepage": "https://github.com/kicad-user/kicad-beautiful-theme"
        },
        "versions": [
            {
                "version": "1.0",
                "status": "stable",
                "kicad_version": "5.99",
                "download_sha256": "YOUR_SHA256_HERE",
                "download_size": 1234,
                "download_url": "https://github.com/YOUR/DOWNLOAD/URL/kicad-beautiful-theme.zip",
                "install_size": 5678
            }
        ]
    }

##### Fields

`$schema`: **(optional)** Must contain the URL to the current KiCad package
JSON schema (<https://go.kicad.org/pcm/schemas/v1>)

`name`: **(required)** The human-readable name of the package (may contain any
valid UTF-8 characters)

`description`: **(required)** A short free-form description of the package
that will be shown in the PCM alongside the package name. May contain a
maximum of 150 characters.

`description_full`: **(required)** A long free-form description of the package
that will be shown in the PCM when the package is selected by the user. May
include line breaks.

`identifier`: **(required)** The unique identifier for the package. May
contain only alphanumeric characters and the dash (`-`) symbol. Must be
between 2 and 50 characters in length. Must start with a latin character and
end with a latin character or a numeral. See instructions below on namespaces
for guidelines for selecting an identifier.

`type`: **(required)** The type of the package; one of `plugin`, `library`, or
`colortheme`.

`author`: **(required)** Object containing one mandatory field, `name`,
containing the name of the package creator. An optional `contact` field may be
present, containing free-form fields with contact information.

`maintainer`: **(optional)** Semantics same as `author`, but containing
information about the maintainer of the package. Can be omitted if same as
author.

`license`: **(required)** A string containing the license under which the
package is distributed.

The license must be a valid string under [Debian license
rules](https://www.debian.org/doc/packaging-manuals/copyright-
format/1.0/#license-specification) with the following modifications:

  * The MIT license is always taken to mean the [Expat license](https://www.debian.org/legal/licenses/mit).

  * The Creative Commons licenses are permitted without a version number, indicating the author did not specify which version applies.

  * Stripping of trailing zeroes is not recognized.

  * `CERN-OHL` is recognized as a valid license.

  * `WTFPL` is recognized as a valid license.

  * `Unlicense` is recognized as a valid license.

The following license strings are also valid and indicate other licensing not
described above:

  * `open-source`: Other Open Source Initiative (OSI) approved license.

  * `unrestricted`: Not an OSI approved license, but not restricted.

`resources`: **(optional)** Additional resource links for the package. Place
your website, github, documentation and other links here.

`keep_on_update`: **(optional)** **(since KiCad 7.0)** List of regular
expressions describing which files should be kept on package update. Each file
from the extracted package is tested against all regex with the
`$KICADX_3RD_PARTY` component removed. If it matches any expression then it
will not be deleted.

If your plugin type package archive has `keepme.txt` file directly in
`plugins` directory, then path `/plugins/your_package_id/keepme.txt` will be
tested against all regex in the list.

__ | 

  * For consistency, directory delimiter will always be forward slash (`/`) even on windows. Tested path will have a leading forward slash.
  * Dots in package identifier are replaced with underscore (`_`) when extracted.
  * When updating the package `keep_on_update` field is used as it is in the repository at the moment of update, not at the moment of previous version installation.
  * [Extended POSIX](https://en.wikibooks.org/wiki/Regular_Expressions/POSIX-Extended_Regular_Expressions) flavour of regular expressions is used.

  
---|---  
  
__ |  If you want to keep all ini and bkp files on update, this regex will work: `.*(\.ini|\.bkp)$`. If you want to keep all .step files from 3d models directory: `^/3dmodels/.*\.step$`  
---|---  
  
`versions`: **(required)** A list of objects describing package versions. Each
version object can contain the following keys:

`version`: **(required)** A string containing the version of the package
(format of this is up to you).

`status`: **(required)** A string containing one of the following:

  * `stable`: This package is stable for general use.

  * `testing`: This package is in a testing phase, users should be cautious and report issues.

  * `development`: This package is in a development phase and should not be expected to work fully.

  * `deprecated`: This package is no longer maintained.

`kicad_version`: **(required)** The minimum required KiCad version for this
package (major.minor).

`kicad_version_max`: **(optional)** The latest KiCad version this package is
compatible with (major.minor).

`download_sha256`: **(optional)** A string containing a SHA-256 hash of the
package archive.

`download_url`: **(optional)** A string containing a direct download URL for
the package archive.

`download_size`: **(optional)** The size of the package archive, in bytes.

`install_size`: **(optional)** The size of the package (uncompressed), in
bytes.

`keep_on_update`: **(optional)** **(since KiCad 7.0)** Same semantics as
corresponding field in package struct but specific to this version. Field of
the package version user is updating **to** is used, not the package user is
updating **from**.

`runtime`: **(optional)** **(since KiCad 9.0.1)** For plugin packages, this
field may be set to either "ipc" or "swig" to indicate which runtime the
plugin requires. If not set, the plugin will be assumed to require the SWIG
(legacy) runtime.

__ |  The `download_*` keys must only be present in the version of the `metadata.json` that you submit to the package metadata repository, not in the version of the file that is actually present in the package archive. It is not possible to put a valid `download_sha256` value in the `metadata.json` file inside the archive.   
---|---  
  
### Submission to the official repository

KiCad hosts an official addons repository that is available by default to all
KiCad users. To be included in the official repository, your package must meet
several requirements beyond the technical requirements described above.

#### Namespacing and naming

  * Your package identifier **must** be namespaced using reverse-DNS format. For example, official KiCad addons use the namespace `org.kicad.packagename`.

  * If your addon content is hosted on a publicly-visible code-hosting service such as GitHub or GitLab, your namespace should be based on this service. For example, `com.github.username.packagename`. The package identifier should generally match the repository name if there is a 1-to-1 correspondence between the package and the repository.

  * Your package namespace may also be based on a domain name that you control. If there is no obvious link between the domain name you submit and the download location of your package, or if it is not otherwise clear that you control the domain name, the KiCad team may request further information before approving your submission.

  * Your package identifier **must** be unique. The namespacing requirements above should make this easy.

  * If you are not clearly a maintainer of the project, we must have written confirmation from a maintainer that you are permitted to submit the project to the KiCad repository on their behalf.

  * Your package must not be a fork or copy of an existing package in the KiCad repository, unless your fork is significantly different in scope from the original work and has a clearly unique name, or unless you are proposing to replace an abandoned project (see below).

#### Licensing

  * Packages **must** be licensed under a valid open-source license. Closed-source packages may be used with KiCad under a third-party repository, but all packages in the official KiCad repository must be open-source to allow for code review, issue reporting, and to maintain license compatibility with KiCad itself.

  * Packages containing code (Python plugins) **must** be licensed under an open-source license [compatible with the GNU GPL](https://www.gnu.org/licenses/license-list.en.html#GPLCompatibleLicenses).

  * Packages containing data (color themes, libraries, etc) should be licensed under a Creative Commons or similar license.

#### Technical requirements

  * Metadata files submitted to the official repository **must** include the `download_sha256` key in the metadata, containing a valid SHA-256 hash of the archive file.

  * The `download_url` **must** point to a publicly-accessible URL.

  * Package metadata **must** be in English. Package contents (for example, the language used inside a dialog created by a Python plugin) may be in any language, but the package description should clearly state if the contents are in a language other than English. At this time, KiCad does not have a built-in mechanism to allow for plugins to offer multiple language translations.

  * The package source **must** be hosted in a location that allows issue reporting and tracking. Examples that meet this requirement include GitHub, GitLab, Bitbucket and Sourceforge.

#### Content policy

  * Packages added to the official KiCad addon repository **must** follow our community [Code of Conduct](https://www.kicad.org/contribute/code-of-conduct/). The KiCad team reserves the right to review package content and metadata and reject submissions that violate this code of conduct.

  * The KiCad team makes no guarantees about the quality, security, or safety of any addon content, but will strive to maintain a general standard of security and safety. If a security, safety, or privacy issue related to a package is brought to our attention, we reserve the right to take corrective actions up to and including removing a package from the repository without advance notice. In this case, the package can be submitted to the repository again once the issue has been resolved to the satisfaction of the KiCad team.

  * The KiCad team reserves the right to modify or expand on this policy in the future in order to best meet the needs of the KiCad user community. Publishers of existing packages that become in violation of new or updated content policies will receive advance notice and have the opportunity to make changes to meet the updated policies.

#### Abandoned content policy

  * The KiCad team may consider a package published to the official repository abandoned if we are unable to contact the maintainer, or if it has bugs preventing its use on a stable version of KiCad that remain open with no feedback for longer than 90 days. In order to prevent the situation of users installing broken packages from the official repository, the KiCad team may edit (for example, by changing the `kicad_version_max` field) or remove packages from the repository if they have been abandoned.

  * Anyone wishing to "revive" an abandoned project can do so either by taking over maintenance of it from the original submitter (with their permission) or by forking it and submitting it under a new name. The standard requirements for all packages will apply to the newly-forked project.

#### Commercial Services

  * Packages that link to or provide commercial services, including but not limited to PCB fabrication, component lookup and order management, **must** first contact the KiCad team at [[email protected]](/cdn-cgi/l/email-protection#74041801131d1a07341f1d1715105a1b0613) to discuss commercial plugin options.

##### Commercial Service FAQ

Why do we need to e-mail the KiCad Team?

We need to have a simple contract on file with the commercial service
provider. This protects both the KiCad project and the commercial service
provider.

I wrote a plugin that only uses public APIs of a service provider. Do I need
to e-mail the KiCad Team?

In general, we will only deal with the service provider. They may be
interested in contracting with you to build a plugin or in allowing third-
party plugins generally. Either way, we need to discuss this directly with the
service provider.

What if the API terms of service already allow my plugin?

We are not lawyers. We pay lawyers to review our contracts and make sure that
the KiCad project and, by extension, our users are legally safe. We do not
have the resources to review other entities' terms of service or to watch them
for changes. This is one reason why we need a direct contract with the
commercial service provider.

Doesn’t this process go against the spirit of Open Source?

No. We place no restrictions on users publishing and publicising their own
plugins. Open Source does not require us to distribute or publish others'
content.

My plugin formats KiCad data for easier use by a commercial service provider.
Do I need to e-mail the KiCad Team?

No. As long as your plugin doesn’t connect to the commercial service provider,
we do not need a contract with the provider.

I represent a commercial service provider. Can we provide a blanket allowance
for developers to use our API?

Yes! We love it when we can make the process of PCB creation easier for our
users. Please e-mail the KiCad team at [[email protected]](/cdn-cgi/l/email-
protection#6b1b071e0c0205182b0002080a0f4504190c) and we’ll help to make this
happen.

### Submitting your package

Once you have created a package following the guidelines above, and confirmed
that your package is available for download using the URL listed in the
metadata file, you can submit your package to the official KiCad addon
repository.

To do so, you must have an account at GitLab, and submit your metadata file as
a merge request to the Package Metadata repository at
<https://gitlab.com/kicad/addons/metadata>. Create a directory inside the
packages directory named the same as your package identifier, and containing
the `metadata.json` file and any additional optional metadata files (for
example, an icon) as described above. You may submit more than one new package
in a single merge request as long as the packages share a namespace.

__ |  Do not submit merge requests to the public-facing repository at <https://gitlab.com/kicad/addons/repository> \- changes to this repository are made automatically based on changes to the metadata repository.   
---|---  
  
### Updating your package

Updates should be submitted as additional merge requests that change the
`metadata.json` file (and any other package files that need updating). You may
submit updates to more than one package in a single merge request as long as
the packages share a namespace.

__Last Modified 2025-02-23

