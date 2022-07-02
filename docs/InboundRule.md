# InboundRule


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** | Protocol for defining the connection type. | 
**src_ports** | **[str]** | Ports for which the rules will be applied | 
**src_cidr** | [**SrcCidr**](SrcCidr.md) |  | 
**status** | **str** | Status of the inbound rule. | 
**action** | **str** | Actions to be applied to the incoming connections. | defaults to "accept"
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

