# CmsErrorsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[str]** | Machine-readable error codes from CMS | 

## Example

```python
from pfruck_contabo.models.cms_errors_response import CmsErrorsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CmsErrorsResponse from a JSON string
cms_errors_response_instance = CmsErrorsResponse.from_json(json)
# print the JSON string representation of the object
print(CmsErrorsResponse.to_json())

# convert the object into a dict
cms_errors_response_dict = cms_errors_response_instance.to_dict()
# create an instance of CmsErrorsResponse from a dict
cms_errors_response_from_dict = CmsErrorsResponse.from_dict(cms_errors_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


