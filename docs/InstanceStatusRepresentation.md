# InstanceStatusRepresentation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **int** | Instance id which is assigned to the firewall. | 
**status** | **str** | Instance status in firewall can be:&lt;br/&gt; &#x60;ok&#x60; - instance was successfully assigned &lt;br/&gt; &#x60;processing&#x60; -  creating firewall rules &lt;br/&gt; &#x60;deleting&#x60; - deleting firewall rules &lt;br/&gt; &#x60;error_processing&#x60; - error occurred while creating firewall rules &lt;br/&gt;  &#x60;error_deleting&#x60; - error occurred while deleting firewall rules | 
**error_message** | **str** | More detailed error message in case of error status. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


