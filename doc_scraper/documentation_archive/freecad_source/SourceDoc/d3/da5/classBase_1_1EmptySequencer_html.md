---
url: https://freecad.github.io/SourceDoc/d3/da5/classBase_1_1EmptySequencer.html
scraped_at: 2025-09-08T15:16:03.771825
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [Base](../../db/d07/namespaceBase.html)
  * [EmptySequencer](../../d3/da5/classBase_1_1EmptySequencer.html)

[List of all members](../../da/d58/classBase_1_1EmptySequencer-members.html) | Public Member Functions

Base::EmptySequencer Class Reference

This special sequencer might be useful if you want to suppress any indication
of the progress to the user.
[More...](../../d3/da5/classBase_1_1EmptySequencer.html#details)

`#include <Sequencer.h>`

##  Public Member Functions  
  
---  
|
[EmptySequencer](../../d3/da5/classBase_1_1EmptySequencer.html#a94eb09f36aaa4790564a927cd692689f)
()=default  
| construction
[More...](../../d3/da5/classBase_1_1EmptySequencer.html#a94eb09f36aaa4790564a927cd692689f)  
  
![-](../../closed.png) Public Member Functions inherited from
[Base::SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html)  
virtual void | [checkAbort](../../d5/d0d/classBase_1_1SequencerBase.html#aa0341031675242aa6aff2a17b4325539) ()  
| Check if the operation is aborted by user.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#aa0341031675242aa6aff2a17b4325539)  
  
virtual [bool](../../d9/db9/classbool.html) | [isBlocking](../../d5/d0d/classBase_1_1SequencerBase.html#a0f260bdce91cdd1854dd9a448550ab9c) () const  
| Returns true if the running sequencer is blocking any user input.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a0f260bdce91cdd1854dd9a448550ab9c)  
  
[bool](../../d9/db9/classbool.html) | [isLocked](../../d5/d0d/classBase_1_1SequencerBase.html#a84588b6e9b8924d463aecfc3ab088283) () const  
| Returns true if the sequencer was locked, false otherwise.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a84588b6e9b8924d463aecfc3ab088283)  
  
[bool](../../d9/db9/classbool.html) | [isRunning](../../d5/d0d/classBase_1_1SequencerBase.html#a06f770a5ba78c654f4d132b235bccd28) () const  
| Returns true if the sequencer is running, otherwise returns false.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a06f770a5ba78c654f4d132b235bccd28)  
  
[bool](../../d9/db9/classbool.html) | [setLocked](../../d5/d0d/classBase_1_1SequencerBase.html#a137ca2a91b990d8053be9f3ca6add1ff) ([bool](../../d9/db9/classbool.html) bLock)  
| If _bLock_ is true then the sequencer gets locked.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a137ca2a91b990d8053be9f3ca6add1ff)  
  
[bool](../../d9/db9/classbool.html) | [wasCanceled](../../d5/d0d/classBase_1_1SequencerBase.html#a3e0668144ea48ef7cd9040513bcc4b3c) () const  
| Returns true if the pending operation was canceled.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a3e0668144ea48ef7cd9040513bcc4b3c)  
  
  
##  Additional Inherited Members  
  
---  
![-](../../closed.png) Static Public Member Functions inherited from
[Base::SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html)  
static [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) & | [Instance](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d) ()  
| Returns the last created sequencer instance.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#aa05bb36f60b72f0bdde3ee8bdea0490d)  
  
![-](../../closed.png) Protected Member Functions inherited from
[Base::SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html)  
[bool](../../d9/db9/classbool.html) | [next](../../d5/d0d/classBase_1_1SequencerBase.html#a708d36d490fcfb8ef3e5a65c68b692ac) ([bool](../../d9/db9/classbool.html) canAbort=false)  
| Performs the next step and returns true if the operation is not yet
finished.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a708d36d490fcfb8ef3e5a65c68b692ac)  
  
virtual void | [nextStep](../../d5/d0d/classBase_1_1SequencerBase.html#a65ca8eb627a8bf4c9f91274637867f48) ([bool](../../d9/db9/classbool.html) canAbort)  
| This method can be reimplemented in sub-classes to give the user a feedback
when the next is performed.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a65ca8eb627a8bf4c9f91274637867f48)  
  
size_t | [numberOfSteps](../../d5/d0d/classBase_1_1SequencerBase.html#ae72645f88f8f398096187bb6877e6e34) () const  
| Returns the number of steps.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#ae72645f88f8f398096187bb6877e6e34)  
  
[SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) & | [operator=](../../d5/d0d/classBase_1_1SequencerBase.html#af30a06e06c0f87d55e716b7d0aec7519) (const [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html) &)=default  
virtual void | [pause](../../d5/d0d/classBase_1_1SequencerBase.html#a804a91939fc20301356a1fa4cbd306b6) ()  
| Breaks the sequencer if needed.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a804a91939fc20301356a1fa4cbd306b6)  
  
[int](../../d1/da0/classint.html) | [progressInPercent](../../d5/d0d/classBase_1_1SequencerBase.html#ad8f695625153088ee4dd478c0830f72c) () const  
| Returns the current state of progress in percent.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#ad8f695625153088ee4dd478c0830f72c)  
  
void | [rejectCancel](../../d5/d0d/classBase_1_1SequencerBase.html#abf3ee0dbca29f0361881fb8c767d58ae) ()  
| If you tried to cancel but then decided to continue the operation.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#abf3ee0dbca29f0361881fb8c767d58ae)  
  
virtual void | [resetData](../../d5/d0d/classBase_1_1SequencerBase.html#a8c7af5d20b184eb577c09ce3f02782c8) ()  
| Resets internal data.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a8c7af5d20b184eb577c09ce3f02782c8)  
  
virtual void | [resume](../../d5/d0d/classBase_1_1SequencerBase.html#aea81b4efe906649564fd9b32e43484c3) ()  
| Continues with progress.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#aea81b4efe906649564fd9b32e43484c3)  
  
|
[SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html#a2e3a2199b335137138937c9ef7fc326f)
()  
| construction
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a2e3a2199b335137138937c9ef7fc326f)  
  
|
[SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html#ae4fa3bbfd02762f65b4dc01aab9e6326)
(const [SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html)
&)=default  
virtual void | [setProgress](../../d5/d0d/classBase_1_1SequencerBase.html#a20ca12713d51a8435bca90ce7cfa3ba7) (size_t)  
| Sets the progress indicator to a certain position.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a20ca12713d51a8435bca90ce7cfa3ba7)  
  
virtual void | [setText](../../d5/d0d/classBase_1_1SequencerBase.html#ab666acb27961c1927c77a1a82a19879f) (const char *pszTxt)  
| Sets a text what the pending operation is doing.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#ab666acb27961c1927c77a1a82a19879f)  
  
[bool](../../d9/db9/classbool.html) | [start](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b) (const char *pszStr, size_t steps)  
| Starts a new operation, returns false if there is already a pending
operation, otherwise it returns true.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a9e388dd22618a5f8c04f5128e888929b)  
  
virtual void | [startStep](../../d5/d0d/classBase_1_1SequencerBase.html#a45d8df4cace8ae2b5c5b70a0c432a8f7) ()  
| This method can be reimplemented in sub-classes to give the user a feedback
when a new sequence starts.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a45d8df4cace8ae2b5c5b70a0c432a8f7)  
  
[bool](../../d9/db9/classbool.html) | [stop](../../d5/d0d/classBase_1_1SequencerBase.html#af7abe491fae28be30f1f1fae10511303) ()  
| Stops the sequencer if all operations are finished.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#af7abe491fae28be30f1f1fae10511303)  
  
void | [tryToCancel](../../d5/d0d/classBase_1_1SequencerBase.html#afe4af6fa0632db72c75c533477526fb5) ()  
| Try to cancel the pending operation(s).
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#afe4af6fa0632db72c75c533477526fb5)  
  
virtual | [~SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html#a33bef6ebde4a0cf72fa5c542e519a8d2) ()  
| Destruction.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a33bef6ebde4a0cf72fa5c542e519a8d2)  
  
![-](../../closed.png) Protected Attributes inherited from
[Base::SequencerBase](../../d5/d0d/classBase_1_1SequencerBase.html)  
size_t | [nProgress](../../d5/d0d/classBase_1_1SequencerBase.html#a8f546309a7f6ab043a757e79d5d5409e)  
| Stores the current amount of progress.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a8f546309a7f6ab043a757e79d5d5409e)  
  
size_t | [nTotalSteps](../../d5/d0d/classBase_1_1SequencerBase.html#a34e1fc4574b504b22098ac12305a85a6)  
| Stores the total number of steps.
[More...](../../d5/d0d/classBase_1_1SequencerBase.html#a34e1fc4574b504b22098ac12305a85a6)  
  
  
## Detailed Description

This special sequencer might be useful if you want to suppress any indication
of the progress to the user.

## Constructor & Destructor Documentation

## ◆ EmptySequencer()

| Base::EmptySequencer::EmptySequencer  | ( | | ) |   
---|---|---|---|---  
default  
  
construction

* * *

The documentation for this class was generated from the following file:

  * FreeCAD/src/Base/Sequencer.h

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

