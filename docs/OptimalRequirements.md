# OptimalRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_cores** | **float** | CPU Cores Requirement | [optional] 
**ram_mb** | **float** | Memory Requirement in MB | [optional] 
**disk_mb** | **float** | Storage Requirement in MB | [optional] 

## Example

```python
from pfruck_contabo.models.optimal_requirements import OptimalRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of OptimalRequirements from a JSON string
optimal_requirements_instance = OptimalRequirements.from_json(json)
# print the JSON string representation of the object
print(OptimalRequirements.to_json())

# convert the object into a dict
optimal_requirements_dict = optimal_requirements_instance.to_dict()
# create an instance of OptimalRequirements from a dict
optimal_requirements_from_dict = OptimalRequirements.from_dict(optimal_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


