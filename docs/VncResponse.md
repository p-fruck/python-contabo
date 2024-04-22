# VncResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Customer ID | 
**instance_id** | **int** | Instance ID | 
**enabled** | **bool** | VNC Status for the instance. | 
**vnc_ip** | **str** | VNC IP for the instance. | 
**vnc_port** | **float** | VNC Port for the instance. | 

## Example

```python
from pfruck_contabo.models.vnc_response import VncResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VncResponse from a JSON string
vnc_response_instance = VncResponse.from_json(json)
# print the JSON string representation of the object
print(VncResponse.to_json())

# convert the object into a dict
vnc_response_dict = vnc_response_instance.to_dict()
# create an instance of VncResponse from a dict
vnc_response_from_dict = VncResponse.from_dict(vnc_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


