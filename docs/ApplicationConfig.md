# ApplicationConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_id** | **str** | Image ID | 
**user_data_id** | **str** | User Data ID | 
**user_data** | **str** | [Cloud-Init](https://cloud-init.io/) Config in order to customize during start of compute instance. | 

## Example

```python
from pfruck_contabo.models.application_config import ApplicationConfig

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationConfig from a JSON string
application_config_instance = ApplicationConfig.from_json(json)
# print the JSON string representation of the object
print(ApplicationConfig.to_json())

# convert the object into a dict
application_config_dict = application_config_instance.to_dict()
# create an instance of ApplicationConfig from a dict
application_config_from_dict = ApplicationConfig.from_dict(application_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


