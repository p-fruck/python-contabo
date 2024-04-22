# MinimumRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu_cores** | **float** | CPU Cores Requirement | [optional] 
**ram_mb** | **float** | Memory Requirement in MB | [optional] 
**disk_mb** | **float** | Storage Requirement in MB | [optional] 

## Example

```python
from pfruck_contabo.models.minimum_requirements import MinimumRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of MinimumRequirements from a JSON string
minimum_requirements_instance = MinimumRequirements.from_json(json)
# print the JSON string representation of the object
print(MinimumRequirements.to_json())

# convert the object into a dict
minimum_requirements_dict = minimum_requirements_instance.to_dict()
# create an instance of MinimumRequirements from a dict
minimum_requirements_from_dict = MinimumRequirements.from_dict(minimum_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


