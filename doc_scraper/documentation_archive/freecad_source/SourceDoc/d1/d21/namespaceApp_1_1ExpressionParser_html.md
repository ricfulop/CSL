---
url: https://freecad.github.io/SourceDoc/d1/d21/namespaceApp_1_1ExpressionParser.html
scraped_at: 2025-09-08T14:53:30.172247
title: Untitled
---

  * [ ![](https://www.freecad.org/svg/logo-freecad.svg) ](https://freecadweb.org "FreeCAD")
  * [Index](../../index.html "Index")
  * [Modules](../../modules.html "Modules list")
  * [Classes](../../annotated.html "Annotated list")

  * [App](../../dd/dc2/namespaceApp.html)
  * [ExpressionParser](../../d1/d21/namespaceApp_1_1ExpressionParser.html)

Classes | Functions | Variables

App::ExpressionParser Namespace Reference

##  Classes  
  
---  
class | [ExpressionImporter](../../db/df3/classApp_1_1ExpressionParser_1_1ExpressionImporter.html)  
| Convenient class to mark begin of importing.
[More...](../../db/df3/classApp_1_1ExpressionParser_1_1ExpressionImporter.html#details)  
  
class | [semantic_type](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html)  
| The
[semantic_type](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html
"The semantic_type class encapsulates the value in the parse tree during
parsing.") class encapsulates the value in the parse tree during parsing.
[More...](../../d6/dc0/classApp_1_1ExpressionParser_1_1semantic__type.html#details)  
  
  
##  Functions  
  
---  
void | [ExpressionParser_yyerror](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a7b70bab9fc3c6e95298d8daefe9f75d5) (const char *errorinfo)  
| Error function for parser.
[More...](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a7b70bab9fc3c6e95298d8daefe9f75d5)  
  
[int](../../d1/da0/classint.html) | [ExpressionParserlex](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a90b5ed1978b38bcd9f523cddd67f1d04) (void)  
static void | [initParser](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a0a4ac778266f88d5e0fe66cfbed76acf) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *owner)  
[bool](../../d9/db9/classbool.html) | [isModuleImported](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ac9298ffe56af3fc4a9feb9b60583ce21) ([PyObject](../../df/d1b/classPyObject.html) *module)  
[bool](../../d9/db9/classbool.html) | [isTokenAnIndentifier](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a755853498ef40d01139b6bf0fd57e70c) (const std::string &[str](../../d9/d36/classstr.html))  
[bool](../../d9/db9/classbool.html) | [isTokenAUnit](../../d1/d21/namespaceApp_1_1ExpressionParser.html#af51ff281865f7ec98e41913c5b985e85) (const std::string &[str](../../d9/d36/classstr.html))  
double | [num_change](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a46acbbebca6cb27882c1bc95427ea59b) (char *yytext, char dez_delim, char grp_delim)  
[Expression](../../dc/d5c/classApp_1_1Expression.html) * | [parse](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a9ce0a4421a2d7654d72187f76d5e8874) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *owner, const char *buffer)  
| Parse the expression given by _buffer_ , and use _owner_ as the owner of the
returned expression.
[More...](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a9ce0a4421a2d7654d72187f76d5e8874)  
  
[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) | [parsePath](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a36f6154c6f4f7e3a02fc421ad5722efd) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *owner, const char *buffer)  
[UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html) * | [parseUnit](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a5ce9e4984820d693ee32429e0f37db9c) (const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *owner, const char *buffer)  
std::vector< std::tuple< [int](../../d1/da0/classint.html), [int](../../d1/da0/classint.html), std::string > > | [tokenize](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a19b3ff248040ef5ac662f3cc6d756937) (const std::string &[str](../../d9/d36/classstr.html))  
  
##  Variables  
  
---  
static [int](../../d1/da0/classint.html) | [column](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a82858382d4506c0c4579af3f38400b43)  
static const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) * | [DocumentObject](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a342b52b23b15fb937ca5a983b97955d0) = nullptr  
| The [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base
class of all Classes handled in the Document.") that will own the expression.
[More...](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a342b52b23b15fb937ca5a983b97955d0)  
  
static std::stack< std::string > | [labels](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a48a8bdb5d8f15ac34c43ee46d0f46bfb)  
| Label string primitive.
[More...](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a48a8bdb5d8f15ac34c43ee46d0f46bfb)  
  
static [int](../../d1/da0/classint.html) | [last_column](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a7263efa71cf4c2ca761f966abad15597)  
static std::map< std::string, [FunctionExpression::Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658) > | [registered_functions](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ab7e873788206155b4b88d23b32b85c07)  
| Registered functions.
[More...](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ab7e873788206155b4b88d23b32b85c07)  
  
static [Expression](../../dc/d5c/classApp_1_1Expression.html) * | [ScanResult](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ae817ded935b1a13ed59af4aa8c778acb) = nullptr  
| The resulting expression after a successful parsing.
[More...](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ae817ded935b1a13ed59af4aa8c778acb)  
  
static [bool](../../d9/db9/classbool.html) | [unitExpression](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a7f553c629cb3c953a3e71a26bf2ea2be) = false  
| True if the parsed string is a unit only.
[More...](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a7f553c629cb3c953a3e71a26bf2ea2be)  
  
static [bool](../../d9/db9/classbool.html) | [valueExpression](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a60394070ea073e87bc0df4fd90976340) = false  
| True if the parsed string is a full expression.
[More...](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a60394070ea073e87bc0df4fd90976340)  
  
  
## Function Documentation

## ◆ ExpressionParser_yyerror()

void App::ExpressionParser::ExpressionParser_yyerror  | ( | const char *  | _errorinfo_| ) |   
---|---|---|---|---|---  
  
Error function for parser.

Throws a generic [Base::Exception](../../d8/df7/classBase_1_1Exception.html)
with the parser error.

## ◆ ExpressionParserlex()

[int](../../d1/da0/classint.html) App::ExpressionParser::ExpressionParserlex  | ( | void  | | ) |   
---|---|---|---|---|---  
  
Referenced by
[isTokenAnIndentifier()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a755853498ef40d01139b6bf0fd57e70c),
[isTokenAUnit()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#af51ff281865f7ec98e41913c5b985e85),
and
[tokenize()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a19b3ff248040ef5ac662f3cc6d756937).

## ◆ initParser()

| static void App::ExpressionParser::initParser  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _owner_| ) |   
---|---|---|---|---|---  
static  
  
References
[App::FunctionExpression::ABS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a6804d3fbcab38a404006d035cc4e1f4f),
[App::FunctionExpression::ACOS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a276e53bd5bc98ed43a56f5ca6b7964be),
[App::FunctionExpression::ASIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a0d51a64df26841bd69c1215df262843b),
[App::FunctionExpression::ATAN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a1fb71ce660de19d227304711d1d8866e),
[App::FunctionExpression::ATAN2](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658adf3ec31eb0b1129f2a3f8fc6ebb93730),
[App::FunctionExpression::AVERAGE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ad0be26e589bd55d1668ccbfb5e6f0f3b),
[App::FunctionExpression::CATH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ac2347403aa1e3ac6151b89e7b117f790),
[App::FunctionExpression::CEIL](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658af87d783d5a2d13c5fb343b11d7131864),
[App::FunctionExpression::COS](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a95716a81b64bb477b3112c6fb8ac6ddc),
[App::FunctionExpression::COSH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a7bccae7f391ed9c60f28644106ed1de7),
[App::FunctionExpression::COUNT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a288c5d4e96ea10990315720b7534bfd3),
[App::FunctionExpression::CREATE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a65e69aa96cb0b8a50daa77b5e7ead82c),
[DocumentObject](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a342b52b23b15fb937ca5a983b97955d0),
[App::FunctionExpression::EXP](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a98485d2edab862d50036742cf22c5e25),
[App::FunctionExpression::FLOOR](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a34299dd51d772f631fd115e5c88f631c),
[App::FunctionExpression::HIDDENREF](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aa8ffc9a30b770655e24289ed8d680c2c),
[App::FunctionExpression::HREF](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a1f8de8f0cc5297db89c1b14cc73c38d8),
[App::FunctionExpression::HYPOT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ae6d3982535c8eb6bc881e06e9e737ea1),
[labels](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a48a8bdb5d8f15ac34c43ee46d0f46bfb),
[App::FunctionExpression::LIST](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a59d141f026bec92e3bada80f92aa1185),
[App::FunctionExpression::LOG](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a584442cca2c253588e2919a6250cf8c4),
[App::FunctionExpression::LOG10](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a6645db0e4ed76f776fb0a2e90a5fa11f),
[App::FunctionExpression::MAX](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a24e9b1553580ddc2888c0033a5b3131d),
[App::FunctionExpression::MIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a485f8f4a9582feca008856cea0cf4cd4),
[App::FunctionExpression::MINVERT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658ab93f185810757ef04030b81fb271f7ce),
[App::FunctionExpression::MOD](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a189154be19979d1ed093ac38dbe6f04a),
[App::FunctionExpression::MSCALE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aed8970081f629373fcdb8bb07dffa1e8),
[App::FunctionExpression::POW](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a0d71bdf3ebcabe8f1be5342d80c2e8b7),
[registered_functions](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ab7e873788206155b4b88d23b32b85c07),
[App::FunctionExpression::ROUND](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aa1b17d8ff51ae98515e480ebb8f42a93),
[ScanResult](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ae817ded935b1a13ed59af4aa8c778acb),
[App::FunctionExpression::SIN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a8cb871e1b4297efc01a6c7bb8b91a1de),
[App::FunctionExpression::SINH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a4bf7a873227153a605236337c8306240),
[App::FunctionExpression::SQRT](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658af3f4842894f781437eb8fd562a4521cc),
[App::FunctionExpression::STDDEV](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a91dc31754bad8359d9bc294ba356fd0b),
[App::FunctionExpression::STR](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aff93140d7ec86ca9e5ad4a626a82ccd4),
[App::FunctionExpression::SUM](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a11a0e7bf8e83c21de7f87e694d164318),
[App::FunctionExpression::TAN](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a8642f76a8b6ba35cd1b4a20c615cf75f),
[App::FunctionExpression::TANH](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a99f98d2742d51c6391122e486d0f9999),
[App::FunctionExpression::TRUNC](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658a05a3b2ede4be6c42ced9cf08a3109bfe),
[App::FunctionExpression::TUPLE](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658aea83ba876162a835ecdca70d8ac90b3c),
[unitExpression](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a7f553c629cb3c953a3e71a26bf2ea2be),
and
[valueExpression](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a60394070ea073e87bc0df4fd90976340).

Referenced by
[parse()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a9ce0a4421a2d7654d72187f76d5e8874),
and
[parseUnit()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a5ce9e4984820d693ee32429e0f37db9c).

## ◆ isModuleImported()

[bool](../../d9/db9/classbool.html) App::ExpressionParser::isModuleImported  | ( | [PyObject](../../df/d1b/classPyObject.html) *  | _module_| ) |   
---|---|---|---|---|---  
  
Referenced by
[App::ObjectIdentifier::Component::get()](../../db/d9f/classApp_1_1ObjectIdentifier_1_1Component.html#ad99dffa416e065802811bcccd62bf0f7).

## ◆ isTokenAnIndentifier()

[bool](../../d9/db9/classbool.html) App::ExpressionParser::isTokenAnIndentifier  | ( | const std::string & | _str_| ) |   
---|---|---|---|---|---  
  
References
[ExpressionParserlex()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a90b5ed1978b38bcd9f523cddd67f1d04).

## ◆ isTokenAUnit()

[bool](../../d9/db9/classbool.html) App::ExpressionParser::isTokenAUnit  | ( | const std::string & | _str_| ) |   
---|---|---|---|---|---  
  
References
[ExpressionParserlex()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a90b5ed1978b38bcd9f523cddd67f1d04).

## ◆ num_change()

double App::ExpressionParser::num_change  | ( | char *  | _yytext_ ,   
---|---|---|---  
|  | char  | _dez_delim_ ,   
|  | char  | _grp_delim_  
| ) | |   
  
## ◆ parse()

[Expression](../../dc/d5c/classApp_1_1Expression.html) * App::ExpressionParser::parse  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _owner_ ,   
---|---|---|---  
|  | const char *  | _buffer_  
| ) | |   
  
Parse the expression given by _buffer_ , and use _owner_ as the owner of the
returned expression.

If the parser fails for some reason, and exception is thrown.

Parameters

     owner| The [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class of all Classes handled in the Document.") that will own the expression.   
---|---  
buffer| The string buffer to parse.  
  
Returns

    A pointer to an expression. 

References
[initParser()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a0a4ac778266f88d5e0fe66cfbed76acf),
[ScanResult](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ae817ded935b1a13ed59af4aa8c778acb),
and
[valueExpression](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a60394070ea073e87bc0df4fd90976340).

Referenced by
[App::ObjectIdentifier::parse()](../../dd/d13/classApp_1_1ObjectIdentifier.html#a067a142eca99580ead933730b95a075b),
[App::Expression::parse()](../../dc/d5c/classApp_1_1Expression.html#a377c20925f92aab0265eb9e3e0b35c97),
and
[Spreadsheet::Cell::setContent()](../../d5/d22/classSpreadsheet_1_1Cell.html#a4d07e67e0412f933cb7306ee3e6b962c).

## ◆ parsePath()

[ObjectIdentifier](../../dd/d13/classApp_1_1ObjectIdentifier.html) App::ExpressionParser::parsePath  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _owner_ ,   
---|---|---|---  
|  | const char *  | _buffer_  
| ) | |   
  
## ◆ parseUnit()

[UnitExpression](../../d2/d4a/classApp_1_1UnitExpression.html) * App::ExpressionParser::parseUnit  | ( | const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html) *  | _owner_ ,   
---|---|---|---  
|  | const char *  | _buffer_  
| ) | |   
  
References
[App::OperatorExpression::DIV](../../d1/d7d/classApp_1_1OperatorExpression.html#a92e03b90dd0860a4490288b6996b51c1a8ce9d53eec9fdefa45e0e48d6faa7e08),
[App::OperatorExpression::getLeft()](../../d1/d7d/classApp_1_1OperatorExpression.html#abddd60d75959a53810c1099c34fe382c),
[App::OperatorExpression::getOperator()](../../d1/d7d/classApp_1_1OperatorExpression.html#abf43aaec1641c7188a8a46fd1b0c9cef),
[App::OperatorExpression::getRight()](../../d1/d7d/classApp_1_1OperatorExpression.html#acddd8b9cf2a7622b5894a705bd9e1992),
[App::UnitExpression::getValue()](../../d2/d4a/classApp_1_1UnitExpression.html#ab2045fdff22bc6d6f23e9f3f0c3684ea),
[initParser()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a0a4ac778266f88d5e0fe66cfbed76acf),
[ScanResult](../../d1/d21/namespaceApp_1_1ExpressionParser.html#ae817ded935b1a13ed59af4aa8c778acb),
[App::Expression::simplify()](../../dc/d5c/classApp_1_1Expression.html#a1c84dd5e6ffe86c4f720e179859d5ca3),
and
[unitExpression](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a7f553c629cb3c953a3e71a26bf2ea2be).

## ◆ tokenize()

std::vector< std::tuple< [int](../../d1/da0/classint.html), [int](../../d1/da0/classint.html), std::string > > App::ExpressionParser::tokenize  | ( | const std::string & | _str_| ) |   
---|---|---|---|---|---  
  
References
[ExpressionParserlex()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a90b5ed1978b38bcd9f523cddd67f1d04),
and
[last_column](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a7263efa71cf4c2ca761f966abad15597).

## Variable Documentation

## ◆ column

| [int](../../d1/da0/classint.html) App::ExpressionParser::column  
---  
static  
  
## ◆ DocumentObject

| const [App::DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html)*
App::ExpressionParser::DocumentObject = nullptr  
---  
static  
  
The [DocumentObject](../../d2/de4/classApp_1_1DocumentObject.html "Base class
of all Classes handled in the Document.") that will own the expression.

Referenced by
[initParser()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a0a4ac778266f88d5e0fe66cfbed76acf).

## ◆ labels

| std::stack<std::string> App::ExpressionParser::labels  
---  
static  
  
Label string primitive.

Referenced by
[initParser()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a0a4ac778266f88d5e0fe66cfbed76acf).

## ◆ last_column

| [int](../../d1/da0/classint.html) App::ExpressionParser::last_column  
---  
static  
  
Referenced by
[tokenize()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a19b3ff248040ef5ac662f3cc6d756937).

## ◆ registered_functions

| std::map<std::string,
[FunctionExpression::Function](../../d6/da3/classApp_1_1FunctionExpression.html#acfab4b75abdb01737290843bcaa97658)>
App::ExpressionParser::registered_functions  
---  
static  
  
Registered functions.

Referenced by
[initParser()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a0a4ac778266f88d5e0fe66cfbed76acf).

## ◆ ScanResult

| [Expression](../../dc/d5c/classApp_1_1Expression.html)*
App::ExpressionParser::ScanResult = nullptr  
---  
static  
  
The resulting expression after a successful parsing.

Referenced by
[initParser()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a0a4ac778266f88d5e0fe66cfbed76acf),
[parse()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a9ce0a4421a2d7654d72187f76d5e8874),
and
[parseUnit()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a5ce9e4984820d693ee32429e0f37db9c).

## ◆ unitExpression

| [bool](../../d9/db9/classbool.html) App::ExpressionParser::unitExpression =
false  
---  
static  
  
True if the parsed string is a unit only.

Referenced by
[initParser()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a0a4ac778266f88d5e0fe66cfbed76acf),
and
[parseUnit()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a5ce9e4984820d693ee32429e0f37db9c).

## ◆ valueExpression

| [bool](../../d9/db9/classbool.html) App::ExpressionParser::valueExpression =
false  
---  
static  
  
True if the parsed string is a full expression.

Referenced by
[initParser()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a0a4ac778266f88d5e0fe66cfbed76acf),
and
[parse()](../../d1/d21/namespaceApp_1_1ExpressionParser.html#a9ce0a4421a2d7654d72187f76d5e8874).

* * *

Generated by
[![doxygen](../../doxygen.svg)](https://www.doxygen.org/index.html) 1.9.4

