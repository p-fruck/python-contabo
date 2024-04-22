# CreateInstanceResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CreateInstanceResponseData]**](CreateInstanceResponseData.md) |  | 
**links** | [**SelfLinks**](SelfLinks.md) |  | 

## Example

```python
from pfruck_contabo.models.create_instance_response import CreateInstanceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateInstanceResponse from a JSON string
create_instance_response_instance = CreateInstanceResponse.from_json(json)
# print the JSON string representation of the object
print(CreateInstanceResponse.to_json())

# convert the object into a dict
create_instance_response_dict = create_instance_response_instance.to_dict()
# create an instance of CreateInstanceResponse from a dict
create_instance_response_from_dict = CreateInstanceResponse.from_dict(create_instance_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


