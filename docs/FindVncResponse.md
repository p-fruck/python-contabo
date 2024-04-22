# FindVncResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[VncResponse]**](VncResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_vnc_response import FindVncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindVncResponse from a JSON string
find_vnc_response_instance = FindVncResponse.from_json(json)
# print the JSON string representation of the object
print(FindVncResponse.to_json())

# convert the object into a dict
find_vnc_response_dict = find_vnc_response_instance.to_dict()
# create an instance of FindVncResponse from a dict
find_vnc_response_from_dict = FindVncResponse.from_dict(find_vnc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


