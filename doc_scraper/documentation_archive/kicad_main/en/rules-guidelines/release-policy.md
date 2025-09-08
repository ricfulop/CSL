---
url: https://dev-docs.kicad.org/en/rules-guidelines/release-policy/
scraped_at: 2025-09-08T15:29:27.458677
title: Stable Release Policy
---

# Stable Release Policy

## 1 Introduction

The purpose of this document is to provide the guidelines for creating releases for the KiCad project. |  __ |  This document is applicable to all stable releases after version 6.0.0.   
---|---  
  
__ |  Do not modify this document without the consent of the project leader. All changes to this document require approval.   
---|---  
  
### 1.1 Versioning Scheme

KiCad uses a typical [major].[minor].[bug fix] versioning scheme. Each new
version is a simple incremental integer of the previous version. New major
releases will reset the minor and bug fix version back to 0.

### 1.2 Restrictions

No board, schematic, footprint library, symbol library, or project file format
changes are allowed during a major release cycle except to fix known bugs.
Changes to configuration files are acceptable.

Minor and bug fix releases are only valid for the current stable major
release. Once a new stable major version is released, the previous stable
version is considered a no longer supported (dead) branch.

## 2 Major Release Policy

Major releases will occur annually by January 31st of a given calendar year.
This corresponds with the annual [FOSDEM](https://fosdem.org/) conference. The
following table outlines the release schedule dates.

Table 1. Major Release Schedule Date | Milestone  
---|---  
February 1st | New feature merge window opens.  
September 30th | New feature merge window closes. Bug fixing only period begins.  
December 1st | String freeze begins.  
December 15th | Release candidate 1 tagged.  
January 14th | Library, documentation, and, translation repository freeze. Bug fix freeze.  
January 15th | Source code repository tagged with next major version and branched. Begin package build and upload to website.  
January 31st | New version release announcement.  
  
* * *

__ |  Features not ready by the merge window close will have to wait until the next merge window. **No exceptions.**  
---|---  
  
__ |  Only the source code repository branch is mandatory. All other repositories are branched if the development team determines it is necessary.   
---|---  
  
## 3 Minor Release Policy

Features from the current development branch of KiCad can be back ported to
the current stable branch provided the following criteria is met:

  * The the last feature commit was pushed to the development branch at least 60 days prior to merging into the current stable branch.

  * The the last known issue filed against the feature occurred at least 30 days prior to merging into the current stable branch.

  * The cherry pick to current stable can be performed without pulling any other dependent code that does meets the file format change criteria above.

A new minor release will include all of the bug fixes included in the current
bug fix release so the bug fix version will be reset to 0 for new minor
version releases.

__ |  Back ports from the development branch can only be applied to the current stable branch. Back porting to older stable versions is not allowed.   
---|---  
  
## 4 Bug Fix Release Policy

Bug fix releases are at the discretion of the lead development team.

Bug fix releases will be announced 14 days in advance of the release by the
project manager to allow time for all required release actions to be
completed.

A release candidate `-rc1` tag will be created a minimum of three days before
the final release. The release candidate will be announced by the project
leader on the [KiCad blog](https://www.kicad.org/blog/) along with the usual
KiCad social media sites.

During the release candidate period, only regression fixes since the last bug
fix release are allowed. All other bug fixes must wait until after the bug fix
release period and release announcement are completed.

If a regression is fixed in the release candidate before the three day minimum
testing period ends, a new incremental release candidate will be created and
the three day minimum testing period begins from the date of the new release
candidate. This process repeats until no new regressions are found in a
release candidate. Multiple regressions may be fixed between release
candidates.

The final bug fix release will be tagged if no new regressions occur within
three days of the last release candidate.

__ |  Bug fixes cannot contain translatable string changes except for spelling and grammar errors. New strings are allowed assuming they do not clash with any existing strings.   
---|---  
  
__ |  Bug fixes can only applied to the current stable release.   
---|---  
  
__Last Modified 2024-04-30

