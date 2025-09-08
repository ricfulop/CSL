---
url: https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints/
scraped_at: 2025-09-08T15:37:01.808228
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

[Optional Cloud Zoo endpoints for License
Management](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-
optional-endpoints/)

  * Endpoint Conventions
    * Endpoint Location
    * JSON
    * Authentication
    * Non-successful responses
  * Endpoints
    * DELETE /license
    * PUT /license

[Guides](https://developer.rhino3d.com/en/guides/) / [RhinoCommon
Guides](https://developer.rhino3d.com/en/guides/rhinocommon/) /

Optional Cloud Zoo endpoints for License Management

by [Andrés Jacobo (AJ) González](https://discourse.mcneel.com/u/aj1/) (Last
updated: Wednesday, June 2, 2021)

## Endpoint Conventions

Unless noted, the following conventions apply to _all_ endpoints available to
registered issuers in Cloud Zoo.

### Endpoint Location

The base URL for all requests is `https://cloudzoo.rhino3d.com/v1`.

### JSON

All payload to and from endpoints happens in [JSON
format](https://www.json.org). To make this explicit, every response to an
endpoint will have the header `Content-Type: application/json` present in the
HTTPS response.

### Authentication

All endpoints in Cloud Zoo or on the issuer use [Basic
Authentication](https://en.wikipedia.org/wiki/Basic_access_authentication). To
receive a successful response from an endpoint, you must include an
`Authorization` header like so:

    
    
    Authorization: Basic BASE64ENCODEDSTRING
    

where `BASE64ENCODEDSTRING` is a
[base64](https://en.wikipedia.org/wiki/Base64) encoded string containing your
issuer id and your issuer secret:

    
    
    	BASE64ENCODEDSTRING = b64.encode(issuer_id + ":" + issuer_secret)
    

### Non-successful responses

All unsuccessful responses from endpoints will have an HTTP status code
greater or equal to `400`. If the status code is also less than `500`, the
payload will include the following JSON:

    
    
    {
        "Error": "SomeErrorCode"
    	"Description": "A description about the error message",
    	"Details": "More details about the error"
    }
    

  * The `Error` field contains a specific error code that can be used by the issuer to recognize a specific error, such as incorrect credentials.
  * The `Description` field contains a description of the error.
  * The `Details` field contains details of the error, possibly suggesting how to fix it.

If the status code is greater or equal to `500`, the response may not be in
JSON format and may be empty.

## Endpoints

### DELETE /license

Removes a license from Cloud Zoo. This method deletes the entire [License
Cluster
object](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-
licensecluster/) the license is in. If the License Cluster the license belongs
to contains additional licenses, they will be removed as well.

__Heads up!__

This endpoint expects the arguments to be passed as a [query
string](https://en.wikipedia.org/wiki/Query_string).

#### Example Request

    
    
    DELETE /license?licenseId=LICENSE_ID&productId=PRODUCT_ID&entityId=ENTITY_ID
    

  * `entityId`: The id of the entity the license belongs to.
  * `productId`: The id of the product the license represents. This is a GUID.
  * `licenseId`: The license id that identifies a unique license within the product id domain.

#### Response

A successful response (The license was removed):

  * HTTP Status Code: `200 (OK)`
  * Response Payload: Empty.

A non-successful (error) response (The license cannot be removed):

  * HTTP Status Code: A code greater or equal to `400 (Bad Request)`
  * Response Payload: [A non-successful response](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints/#non-successful-responses)

### PUT /license

Adds or replaces a License Cluster in Cloud Zoo. If any of the licenses in the
[License Cluster
object](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-
licensecluster/) passed already exist in the given entity, their license
cluster will be overwritten with the License Cluster passed. If there is more
than one cluster in the entity containing the licenses in the cluster passed,
an error will be returned and the operation will be aborted.

#### Example Request

    
    
    PUT /license
    
    {
        "entityId": "9034901491490-|-Group",
        "licenseCluster": LICENSE_CLUSTER_OBJECT
    }
    

The `entityId` should be the entity where the License Cluster will be added or
updated. The `licenseCluster` should be a [License Cluster
object](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-
licensecluster/) representing the license(s) to be added or updated.

#### Response

A successful response (The license was removed):

  * HTTP Status Code: `200 (OK)`
  * Response Payload: Empty.

A non-successful (error) response (The license cannot be added/updated):

  * HTTP Status Code: A code greater or equal to `400 (Bad Request)`
  * Response Payload: [A non-successful response](https://developer.rhino3d.com/guides/rhinocommon/cloudzoo/cloudzoo-optional-endpoints/#non-successful-responses)

Edit this page

[ Edit on
GitHub](https://github.com/mcneel/developer.rhino3d.com/edit/master/content/en/guides/rhinocommon/cloudzoo/cloudzoo-
optional-endpoints/index.md) [
History](https://github.com/mcneel/developer.rhino3d.com/commits/master/content/en/guides/rhinocommon/cloudzoo/cloudzoo-
optional-endpoints/index.md) [ Admin](https://developer.rhino3d.com/admin)

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

