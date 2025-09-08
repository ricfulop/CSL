---
url: https://freecad.github.io/SourceDoc/d9/dea/namespaceCloud.html
scraped_at: 2025-09-08T15:19:22.622276
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

Classes | Functions

Cloud Namespace Reference

##  Classes  
  
---  
struct | [AmzData](../../d9/df1/structCloud_1_1AmzData.html)  
struct | [AmzDatav4](../../d0/d4c/structCloud_1_1AmzDatav4.html)  
class | [CloudReader](../../d2/de7/classCloud_1_1CloudReader.html)  
class | [CloudWriter](../../d0/d23/classCloud_1_1CloudWriter.html)  
class | [Module](../../d9/d80/classCloud_1_1Module.html)  
  
##  Functions  
  
---  
struct curl_slist * | [BuildHeaderAmzS3v2](../../d9/dea/namespaceCloud.html#a2537fd6ec769988ae3664f50a776fbbf) (const char *URL, const char *TCPPort, const char *PublicKey, struct [AmzData](../../d9/df1/structCloud_1_1AmzData.html) *Data)  
struct curl_slist * | [BuildHeaderAmzS3v4](../../d9/dea/namespaceCloud.html#a068954d887c1095aacd27be7c5bb35ed) (const char *URL, const char *PublicKey, struct [AmzDatav4](../../d0/d4c/structCloud_1_1AmzDatav4.html) *Data)  
struct [AmzData](../../d9/df1/structCloud_1_1AmzData.html) * | [ComputeDigestAmzS3v2](../../d9/dea/namespaceCloud.html#a7553aac877d630c37c9dc682752fca09) (char *operation, char *data_type, const char *target, const char *Secret, const char *ptr, long size)  
struct [AmzDatav4](../../d0/d4c/structCloud_1_1AmzDatav4.html) * | [ComputeDigestAmzS3v4](../../d9/dea/namespaceCloud.html#afd1710e5df1e7528000747301e6b5ceb) (char *operation, const char *server, char *data_type, const char *target, const char *Secret, const char *ptr, long size, char *parameters, std::string Region)  
size_t | [CurlWrite_CallbackFunc_StdString](../../d9/dea/namespaceCloud.html#a0706f2042a82b5e6a6375577359be029) (void *contents, size_t size, size_t nmemb, std::string *s)  
void | [eraseSubStr](../../d9/dea/namespaceCloud.html#a200581597cdfe01a88dfcc0b5d3f8529) (std::string &Str, const std::string &toErase)  
std::string | [getHexValue](../../d9/dea/namespaceCloud.html#a8a1c83d147967a1f9e449576ec546567) (unsigned char *input, unsigned [int](../../d1/da0/classint.html) HMACLength)  
[PyObject](../../df/d1b/classPyObject.html) * | [initModule](../../d9/dea/namespaceCloud.html#a6d1cb462191f7ba8e39cb9ec344dc538) ()  
char * | [MD5Sum](../../d9/dea/namespaceCloud.html#a3127628bea6978476d6b00ce98cd69f8) (const char *ptr, long size)  
char * | [SHA256Sum](../../d9/dea/namespaceCloud.html#aecb38e906648078f57af69f38c5adc8a) (const char *ptr, long size)  
  
## Function Documentation

## ◆ BuildHeaderAmzS3v2()

struct curl_slist * Cloud::BuildHeaderAmzS3v2  | ( | const char *  | _URL_ ,   
---|---|---|---  
|  | const char *  | _TCPPort_ ,   
|  | const char *  | _PublicKey_ ,   
|  | struct [AmzData](../../d9/df1/structCloud_1_1AmzData.html) *  | _Data_  
| ) | |   
  
Referenced by
[Cloud::CloudReader::CloudReader()](../../d2/de7/classCloud_1_1CloudReader.html#a35ce55bf83df7bb02c52ec91d3753c94),
[Cloud::CloudWriter::CloudWriter()](../../d0/d23/classCloud_1_1CloudWriter.html#a2f634c73bd3883066df762192e5ebb5f),
[Cloud::CloudWriter::createBucket()](../../d0/d23/classCloud_1_1CloudWriter.html#a32629112f9daf1c94c2ee29c66298b3c),
[Cloud::CloudReader::DownloadFile()](../../d2/de7/classCloud_1_1CloudReader.html#a0c28666c1d8f3c38adf9b7ea76ca8085),
and
[Cloud::CloudWriter::pushCloud()](../../d0/d23/classCloud_1_1CloudWriter.html#a2cde2d5d92835fcc17d47d7215445626).

## ◆ BuildHeaderAmzS3v4()

struct curl_slist * Cloud::BuildHeaderAmzS3v4  | ( | const char *  | _URL_ ,   
---|---|---|---  
|  | const char *  | _PublicKey_ ,   
|  | struct [AmzDatav4](../../d0/d4c/structCloud_1_1AmzDatav4.html) *  | _Data_  
| ) | |   
  
Referenced by
[Cloud::CloudReader::CloudReader()](../../d2/de7/classCloud_1_1CloudReader.html#a35ce55bf83df7bb02c52ec91d3753c94),
[Cloud::CloudWriter::CloudWriter()](../../d0/d23/classCloud_1_1CloudWriter.html#a2f634c73bd3883066df762192e5ebb5f),
[Cloud::CloudWriter::createBucket()](../../d0/d23/classCloud_1_1CloudWriter.html#a32629112f9daf1c94c2ee29c66298b3c),
[Cloud::CloudReader::DownloadFile()](../../d2/de7/classCloud_1_1CloudReader.html#a0c28666c1d8f3c38adf9b7ea76ca8085),
and
[Cloud::CloudWriter::pushCloud()](../../d0/d23/classCloud_1_1CloudWriter.html#a2cde2d5d92835fcc17d47d7215445626).

## ◆ ComputeDigestAmzS3v2()

struct [Cloud::AmzData](../../d9/df1/structCloud_1_1AmzData.html) * Cloud::ComputeDigestAmzS3v2  | ( | char *  | _operation_ ,   
---|---|---|---  
|  | char *  | _data_type_ ,   
|  | const char *  | _target_ ,   
|  | const char *  | _Secret_ ,   
|  | const char *  | _ptr_ ,   
|  | long  | _size_  
| ) | |   
  
References
[Base::base64_encode()](../../db/d07/namespaceBase.html#a3a68598115d554cfc1fd43f196e98adb),
[Cloud::AmzData::ContentType](../../d9/df1/structCloud_1_1AmzData.html#a6a7b9771c5353d16d0e1d6bf140190f5),
[Cloud::AmzData::dateFormatted](../../d9/df1/structCloud_1_1AmzData.html#ac61ed43d77e4646748da452785ef9e87),
[Cloud::AmzData::digest](../../d9/df1/structCloud_1_1AmzData.html#a671a8127b41e17e9e1746c4101b7bb17),
[Cloud::AmzData::MD5](../../d9/df1/structCloud_1_1AmzData.html#a1d6c442bcef4137b634d15a57cffb52a),
and
[MD5Sum()](../../d9/dea/namespaceCloud.html#a3127628bea6978476d6b00ce98cd69f8).

Referenced by
[Cloud::CloudReader::CloudReader()](../../d2/de7/classCloud_1_1CloudReader.html#a35ce55bf83df7bb02c52ec91d3753c94),
[Cloud::CloudWriter::CloudWriter()](../../d0/d23/classCloud_1_1CloudWriter.html#a2f634c73bd3883066df762192e5ebb5f),
[Cloud::CloudWriter::createBucket()](../../d0/d23/classCloud_1_1CloudWriter.html#a32629112f9daf1c94c2ee29c66298b3c),
[Cloud::CloudReader::DownloadFile()](../../d2/de7/classCloud_1_1CloudReader.html#a0c28666c1d8f3c38adf9b7ea76ca8085),
and
[Cloud::CloudWriter::pushCloud()](../../d0/d23/classCloud_1_1CloudWriter.html#a2cde2d5d92835fcc17d47d7215445626).

## ◆ ComputeDigestAmzS3v4()

struct [Cloud::AmzDatav4](../../d0/d4c/structCloud_1_1AmzDatav4.html) * Cloud::ComputeDigestAmzS3v4  | ( | char *  | _operation_ ,   
---|---|---|---  
|  | const char *  | _server_ ,   
|  | char *  | _data_type_ ,   
|  | const char *  | _target_ ,   
|  | const char *  | _Secret_ ,   
|  | const char *  | _ptr_ ,   
|  | long  | _size_ ,   
|  | char *  | _parameters_ ,   
|  | std::string  | _Region_  
| ) | |   
  
References
[Cloud::AmzDatav4::ContentType](../../d0/d4c/structCloud_1_1AmzDatav4.html#a8d95a3fa608737758b66fe1cb07f7dae),
[Cloud::AmzDatav4::dateFormattedD](../../d0/d4c/structCloud_1_1AmzDatav4.html#a73d36aaa94d365b8ff6a605ff9b8fff3),
[Cloud::AmzDatav4::dateFormattedS](../../d0/d4c/structCloud_1_1AmzDatav4.html#a8a3521fc65a1c35f58e637b8a26ef95a),
[Cloud::AmzDatav4::digest](../../d0/d4c/structCloud_1_1AmzDatav4.html#a19c8e11237057eaaa764296e607d41ac),
[getHexValue()](../../d9/dea/namespaceCloud.html#a8a1c83d147967a1f9e449576ec546567),
[Cloud::AmzDatav4::MD5](../../d0/d4c/structCloud_1_1AmzDatav4.html#ab7ac03ec92dbc7ade5b5e3faf1b1a38b),
[Cloud::AmzDatav4::Region](../../d0/d4c/structCloud_1_1AmzDatav4.html#a2e3346dbf668d8bf9307b75b9c654db0),
[Cloud::AmzDatav4::SHA256Sum](../../d0/d4c/structCloud_1_1AmzDatav4.html#aaa4431ef79fe6f9dd827ae8dc52a2170),
and
[SHA256Sum()](../../d9/dea/namespaceCloud.html#aecb38e906648078f57af69f38c5adc8a).

Referenced by
[Cloud::CloudReader::CloudReader()](../../d2/de7/classCloud_1_1CloudReader.html#a35ce55bf83df7bb02c52ec91d3753c94),
[Cloud::CloudWriter::CloudWriter()](../../d0/d23/classCloud_1_1CloudWriter.html#a2f634c73bd3883066df762192e5ebb5f),
[Cloud::CloudWriter::createBucket()](../../d0/d23/classCloud_1_1CloudWriter.html#a32629112f9daf1c94c2ee29c66298b3c),
[Cloud::CloudReader::DownloadFile()](../../d2/de7/classCloud_1_1CloudReader.html#a0c28666c1d8f3c38adf9b7ea76ca8085),
and
[Cloud::CloudWriter::pushCloud()](../../d0/d23/classCloud_1_1CloudWriter.html#a2cde2d5d92835fcc17d47d7215445626).

## ◆ CurlWrite_CallbackFunc_StdString()

size_t Cloud::CurlWrite_CallbackFunc_StdString  | ( | void *  | _contents_ ,   
---|---|---|---  
|  | size_t  | _size_ ,   
|  | size_t  | _nmemb_ ,   
|  | std::string *  | _s_  
| ) | |   
  
Referenced by
[Cloud::CloudReader::CloudReader()](../../d2/de7/classCloud_1_1CloudReader.html#a35ce55bf83df7bb02c52ec91d3753c94),
[Cloud::CloudWriter::CloudWriter()](../../d0/d23/classCloud_1_1CloudWriter.html#a2f634c73bd3883066df762192e5ebb5f),
and
[Cloud::CloudReader::DownloadFile()](../../d2/de7/classCloud_1_1CloudReader.html#a0c28666c1d8f3c38adf9b7ea76ca8085).

## ◆ eraseSubStr()

void Cloud::eraseSubStr  | ( | std::string & | _Str_ ,   
---|---|---|---  
|  | const std::string & | _toErase_  
| ) | |   
  
Referenced by
[Cloud::CloudReader::CloudReader()](../../d2/de7/classCloud_1_1CloudReader.html#a35ce55bf83df7bb02c52ec91d3753c94),
[Cloud::CloudWriter::CloudWriter()](../../d0/d23/classCloud_1_1CloudWriter.html#a2f634c73bd3883066df762192e5ebb5f),
[Cloud::CloudWriter::createBucket()](../../d0/d23/classCloud_1_1CloudWriter.html#a32629112f9daf1c94c2ee29c66298b3c),
[Cloud::CloudReader::DownloadFile()](../../d2/de7/classCloud_1_1CloudReader.html#a0c28666c1d8f3c38adf9b7ea76ca8085),
and
[Cloud::CloudWriter::pushCloud()](../../d0/d23/classCloud_1_1CloudWriter.html#a2cde2d5d92835fcc17d47d7215445626).

## ◆ getHexValue()

std::string Cloud::getHexValue  | ( | unsigned char *  | _input_ ,   
---|---|---|---  
|  | unsigned [int](../../d1/da0/classint.html) | _HMACLength_  
| ) | |   
  
Referenced by
[ComputeDigestAmzS3v4()](../../d9/dea/namespaceCloud.html#afd1710e5df1e7528000747301e6b5ceb),
and
[SHA256Sum()](../../d9/dea/namespaceCloud.html#aecb38e906648078f57af69f38c5adc8a).

## ◆ initModule()

[PyObject](../../df/d1b/classPyObject.html) * Cloud::initModule  | ( | | ) |   
---|---|---|---|---  
  
References
[Base::InterpreterSingleton::addModule()](../../d2/d9e/classBase_1_1InterpreterSingleton.html#af556d495376be43c3d93c9a44e6c15d3),
and
[Base::Interpreter()](../../db/d07/namespaceBase.html#a2ee9c987b769c5d1ed5f2fe69b21d2c9).

## ◆ MD5Sum()

char * Cloud::MD5Sum  | ( | const char *  | _ptr_ ,   
---|---|---|---  
|  | long  | _size_  
| ) | |   
  
References
[Base::base64_encode()](../../db/d07/namespaceBase.html#a3a68598115d554cfc1fd43f196e98adb).

Referenced by
[ComputeDigestAmzS3v2()](../../d9/dea/namespaceCloud.html#a7553aac877d630c37c9dc682752fca09).

## ◆ SHA256Sum()

char * Cloud::SHA256Sum  | ( | const char *  | _ptr_ ,   
---|---|---|---  
|  | long  | _size_  
| ) | |   
  
References
[getHexValue()](../../d9/dea/namespaceCloud.html#a8a1c83d147967a1f9e449576ec546567).

Referenced by
[ComputeDigestAmzS3v4()](../../d9/dea/namespaceCloud.html#afd1710e5df1e7528000747301e6b5ceb).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

