# ImageAuditResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**PaginationMeta**](PaginationMeta.md) | Data about pagination like how many results, pages, page size. | 
**data** | [**List[ImageAuditResponseData]**](ImageAuditResponseData.md) |  | 
**links** | [**Links**](Links.md) |  | 

## Example

```python
from pfruck_contabo.models.image_audit_response import ImageAuditResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ImageAuditResponse from a JSON string
image_audit_response_instance = ImageAuditResponse.from_json(json)
# print the JSON string representation of the object
print(ImageAuditResponse.to_json())

# convert the object into a dict
image_audit_response_dict = image_audit_response_instance.to_dict()
# create an instance of ImageAuditResponse from a dict
image_audit_response_from_dict = ImageAuditResponse.from_dict(image_audit_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


