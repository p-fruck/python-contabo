# ApplicationMetaData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[str]** |  | 
**logo_url** | **str** |  | 
**initial_username** | **str** |  | 
**documentation_urls** | **List[str]** |  | 
**requires_password_for_install** | **bool** |  | 

## Example

```python
from pfruck_contabo.models.application_meta_data import ApplicationMetaData

# TODO update the JSON string below
json = "{}"
# create an instance of ApplicationMetaData from a JSON string
application_meta_data_instance = ApplicationMetaData.from_json(json)
# print the JSON string representation of the object
print(ApplicationMetaData.to_json())

# convert the object into a dict
application_meta_data_dict = application_meta_data_instance.to_dict()
# create an instance of ApplicationMetaData from a dict
application_meta_data_from_dict = ApplicationMetaData.from_dict(application_meta_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


