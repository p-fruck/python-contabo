# ApplicationRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum** | [**MinimumRequirements**](MinimumRequirements.md) | Application minimum requirements | [optional] 
**optimal** | [**OptimalRequirements**](OptimalRequirements.md) | Application optimal requirements | [optional] 

## Example

```python
from pfruck_contabo.models.application_requirements import ApplicationRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationRequirements from a JSON string
application_requirements_instance = ApplicationRequirements.from_json(json)
# print the JSON string representation of the object
print(ApplicationRequirements.to_json())

# convert the object into a dict
application_requirements_dict = application_requirements_instance.to_dict()
# create an instance of ApplicationRequirements from a dict
application_requirements_from_dict = ApplicationRequirements.from_dict(application_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


