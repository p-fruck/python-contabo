# FindClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ClientResponse]**](ClientResponse.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.find_client_response import FindClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FindClientResponse from a JSON string
find_client_response_instance = FindClientResponse.from_json(json)
# print the JSON string representation of the object
print(FindClientResponse.to_json())

# convert the object into a dict
find_client_response_dict = find_client_response_instance.to_dict()
# create an instance of FindClientResponse from a dict
find_client_response_from_dict = FindClientResponse.from_dict(find_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


