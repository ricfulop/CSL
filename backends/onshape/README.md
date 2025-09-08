# Onshape Backend

## Overview
Cloud-based CAD platform with REST API and FeatureScript programming language. CSL integration via API calls and custom features.

## Quick Start

### Setup
1. Create Onshape account (free tier available)
2. Generate API keys:
   - Developer portal → API keys
   - Store Access Key and Secret Key
3. Configure environment:
   ```bash
   export ONSHAPE_ACCESS_KEY="your_access_key"
   export ONSHAPE_SECRET_KEY="your_secret_key"
   ```

### First API Test
```python
import requests
from onshape_client import OnshapeClient

client = OnshapeClient(
    access_key=os.environ['ONSHAPE_ACCESS_KEY'],
    secret_key=os.environ['ONSHAPE_SECRET_KEY']
)

# Create a new document
response = client.documents.create_document({
    "name": "CSL Test",
    "description": "Created via API"
})
```

## Architecture
- **Integration Method**: REST API + FeatureScript
- **API Types**: 
  - REST API for document/part management
  - FeatureScript for custom features
  - Webhook support for real-time updates
- **Communication**: HTTPS REST calls
- **Unit System**: Meters (API), configurable in UI

## Current Status
- [ ] Basic geometry creation
- [ ] Sketch support via FeatureScript
- [ ] Feature operations
- [ ] Assembly creation
- [ ] Export capabilities
- [ ] Real-time collaboration support

## API Endpoints Structure
```
https://cad.onshape.com/api/
├── documents/           # Document management
├── parts/              # Part studio operations
├── assemblies/         # Assembly operations
├── features/           # Feature creation
├── exports/            # Export to various formats
└── featurescripts/     # Custom FeatureScript execution
```

## FeatureScript Integration
```javascript
// Custom CSL feature in FeatureScript
annotation { "Feature Type Name" : "CSL Feature" }
export const cslFeature = defineFeature(function(context is Context, 
                                                  id is Id, 
                                                  definition is map)
{
    // Parse CSL input
    var cslData = definition.cslInput;
    
    // Create geometry
    if (cslData.type == "extrude") {
        opExtrude(context, id + "extrude", {
            "entities" : definition.sketch,
            "distance" : cslData.distance * millimeter
        });
    }
});
```

## Authentication
```python
import hmac
import base64
import hashlib
from datetime import datetime

def sign_request(method, url, access_key, secret_key):
    """Generate Onshape API signature"""
    date = datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
    signature = base64.b64encode(
        hmac.new(
            secret_key.encode('utf-8'),
            f"{method}\n{date}\n{url}".encode('utf-8'),
            hashlib.sha256
        ).digest()
    ).decode('utf-8')
    
    return {
        'Date': date,
        'Authorization': f'On {access_key}:HmacSHA256:{signature}'
    }
```

## Known Limitations
- API rate limits (varies by plan)
- FeatureScript execution timeout (30 seconds)
- Limited offline capability
- Version control differs from file-based CAD

## Advantages
- Cloud-native, no installation
- Real-time collaboration
- Version control built-in
- Cross-platform (browser-based)
- Powerful FeatureScript language

## Code Structure
```
onshape/
├── __init__.py
├── onshape_backend.py       # CSL to Onshape API translator
├── featurescript/
│   ├── csl_features.fs      # FeatureScript implementations
│   └── utils.fs
├── api_client.py            # REST API wrapper
└── examples/
    ├── create_part.py
    └── assembly_test.py
```

## Resources
- [Onshape API Documentation](https://onshape-public.github.io/docs/)
- [FeatureScript Documentation](https://cad.onshape.com/FsDoc/)
- [API Explorer](https://cad.onshape.com/glassworks/explorer/)
- [Python Client Library](https://github.com/onshape-public/onshape-clients)

## TODO
- [ ] Implement REST API client wrapper
- [ ] Create FeatureScript CSL interpreter
- [ ] Handle document/workspace management
- [ ] Add collaborative features support
- [ ] Implement webhook handlers
- [ ] Test performance with complex models

## Notes for Implementation
- Consider hybrid approach: REST for management, FeatureScript for geometry
- Use webhooks for real-time sync
- Cache API responses to avoid rate limits
- FeatureScript can be pre-compiled and stored
