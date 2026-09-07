# InstanceStatusRepresentation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **int** | Instance id which is assigned to the firewall. | 
**status** | **str** | Instance status in firewall can be:&lt;br/&gt; &#x60;ok&#x60; - instance was successfully assigned &lt;br/&gt; &#x60;processing&#x60; -  creating firewall rules &lt;br/&gt; &#x60;deleting&#x60; - deleting firewall rules &lt;br/&gt; &#x60;error_processing&#x60; - error occurred while creating firewall rules &lt;br/&gt;  &#x60;error_deleting&#x60; - error occurred while deleting firewall rules | 
**error_message** | **str** | More detailed error message in case of error status. | [optional] 

## Example

```python
from pfruck_contabo.models.instance_status_representation import InstanceStatusRepresentation

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceStatusRepresentation from a JSON string
instance_status_representation_instance = InstanceStatusRepresentation.from_json(json)
# print the JSON string representation of the object
print(InstanceStatusRepresentation.to_json())

# convert the object into a dict
instance_status_representation_dict = instance_status_representation_instance.to_dict()
# create an instance of InstanceStatusRepresentation from a dict
instance_status_representation_from_dict = InstanceStatusRepresentation.from_dict(instance_status_representation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


