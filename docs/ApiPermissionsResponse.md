# ApiPermissionsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_name** | **str** | API endpoint. In order to get a list availbale api enpoints please refer to the GET api-permissions endpoint. | 
**actions** | **List[str]** | Action allowed for the API endpoint. Basically &#x60;CREATE&#x60; corresponds to POST endpoints, &#x60;READ&#x60; to GET endpoints, &#x60;UPDATE&#x60; to PATCH / PUT endpoints and &#x60;DELETE&#x60; to DELETE endpoints. | 

## Example

```python
from pfruck_contabo.models.api_permissions_response import ApiPermissionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiPermissionsResponse from a JSON string
api_permissions_response_instance = ApiPermissionsResponse.from_json(json)
# print the JSON string representation of the object
print(ApiPermissionsResponse.to_json())

# convert the object into a dict
api_permissions_response_dict = api_permissions_response_instance.to_dict()
# create an instance of ApiPermissionsResponse from a dict
api_permissions_response_from_dict = ApiPermissionsResponse.from_dict(api_permissions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


