---
url: https://freecad.github.io/SourceDoc/d7/db6/group__ZIPIOS.html
scraped_at: 2025-09-08T14:52:31.936007
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Zipios++

[Embedded 3rd party libraries](../../d0/dd8/group__EMBEDDED.html)

C++ library for reading and writing Zip file.

C++ library for reading and writing Zip file.

#  Introduction

Zipios++ is a java.util.zip-like C++ library for reading and writing Zip
files. Access to individual entries is provided through standard C++
iostreams. A simple read-only virtual file system that mounts regular
directories and zip files is also provided.

The source code is released under the [GNU Lesser General Public
License](http://www.gnu.org/copyleft/lesser.html).

#  Status

Spanned archives are not supported, and support is not planned.

The library has been tested and appears to be working with

  * [FreeBSD stable and current / gcc 2.95.3](http://www.freebsd.org/ports/archivers.html#zipios++-0.1.5)
  * Red Hat Linux release 7.0 / gcc 2.96 
  * Red Hat Linux release 6.2 (Zoot) / egcs-2.91.66 
  * Linux Mandrake release 7.0 (Air) / gcc 2.95.2 
  * SGI IRIX64 6.5 / gcc 2.95.2 
  * SGI IRIX64 6.5 / MIPSpro Compilers: Version 7.30 

If you are aware of any other platforms that Zipios++ works on, please let me
know (thoma.nosp@m.ss@d.nosp@m.eltad.nosp@m.ata..nosp@m.dk).

##  Zip file access

The two most important classes are
[ZipFile](../../d7/da4/classzipios_1_1ZipFile.html#zipfile_anchor) and
[ZipInputStream](../../d0/d1f/classzipios_1_1ZipInputStream.html#ZipInputStream_anchor).
ZipInputStream is an istream for reading zipfiles. It can be instantiated
directly, without the use of ZipFile. A new ZipInputStream reads from the
first entry, and the user can skip to the next entry by calling
[ZipInputStream::getNextEntry()](../../d0/d1f/classzipios_1_1ZipInputStream.html#ZipInputStream_getnextentry_anchor).

ZipFile scans the central directory of a zipfile and provides an interface to
access that directory. The user may search for entries with a particular
filename using
[ZipFile::getEntry()](../../d1/d24/classzipios_1_1FileCollection.html#fcoll_getentry_anchor),
or simply get the complete list of entries with
[ZipFile::entries()](../../d1/d24/classzipios_1_1FileCollection.html#fcoll_entries_anchor).
To get an istream (ZipInputStream) to a particular entry simply use
[ZipFile::getInputStream()](../../d7/da4/classzipios_1_1ZipFile.html#fcoll_getinputstream).

"example_zip.cpp" demonstrates the central elements of Zipios++.

A Zip file appended to another file, e.g. a binary program, with the program
"appendzip", can be read with
[ZipFile::openEmbeddedZipFile()](../../d7/da4/classzipios_1_1ZipFile.html#zipfile_openembeddedzipfile).

##  FileCollections

A ZipFile is actually just a special kind of
[FileCollection](../../d1/d24/classzipios_1_1FileCollection.html#fcoll_anchor)
that obtains its entries from a .zip Zip archive. Zipios++ also implements a
[DirectoryCollection](../../d7/dbb/classzipios_1_1DirectoryCollection.html#dircol_anchor)
that obtains its entries from a specified directory, and a
[CollectionCollection](../../da/d40/classzipios_1_1CollectionCollection.html#collcoll_anchor)
that obtains its entries from other collections. Using a single
CollectionCollection any number of other FileCollections can be placed under
its control and accessed through the same single interface that is used to
access a ZipFile or a DirectoryCollection. A singleton (a unique global
instance) CollectionCollection can be obtained through

[CollectionCollection::inst()](../../da/d40/classzipios_1_1CollectionCollection.html#collcoll_inst_anchor)
;

To save typing CollectionCollection has been typedef'ed to CColl. In the
initialization part of an application FileCollections can be created, and
placed under CColll::inst()'s control using

[CColl::inst().addCollection()](../../da/d40/classzipios_1_1CollectionCollection.html#collcoll_addcoll_anchor)

and later an istream can be obtained using

[CColl::inst().getInputStream()](../../d7/da4/classzipios_1_1ZipFile.html#fcoll_getinputstream).

#  Download

Go to Zipios++ project page on SourceForge for tar balls and ChangeLog.
<http://sourceforge.net/project/?group_id=5418>

#  Links

[zlib](ftp://ftp.freesoftware.com/pub/infozip/zlib/zlib.html). The compression
library that Zipios++ uses to perform the actual decompression.

[Java 2 Platform, Standard Edition, v 1.3 API Specification
](http://java.sun.com/products/jdk/1.3/docs/api/index.html). Zipios++ is
heavily inspired by the java.util.zip package.

[PKWARE zip format
](http://www.geocities.com/SiliconValley/Lakes/2160/fformats/files/zip.txt). A
description of the zip file format.

#  Bugs

Submit bug reports and patches to
thoma.nosp@m.ss@d.nosp@m.eltad.nosp@m.ata..nosp@m.dk

Project hosted by [ SourceForge ](http://sourceforge.net)

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

