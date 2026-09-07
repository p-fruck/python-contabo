# HandleAddress


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**street** | **str** | Street | 
**street_number** | **str** | Street Number | 
**city** | **str** | City | 
**country** | **str** | Country | 
**zip_code** | **str** | ZipCode | 
**siret** | **str** | Siret | [optional] 
**region** | **str** | Region | [optional] 

## Example

```python
from pfruck_contabo.models.handle_address import HandleAddress

# TODO update the JSON string below
json = "{}"
# create an instance of HandleAddress from a JSON string
handle_address_instance = HandleAddress.from_json(json)
# print the JSON string representation of the object
print(HandleAddress.to_json())

# convert the object into a dict
handle_address_dict = handle_address_instance.to_dict()
# create an instance of HandleAddress from a dict
handle_address_from_dict = HandleAddress.from_dict(handle_address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


