# ListFirewallResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**firewall_id** | **str** | Your firewall id. | 
**name** | **str** | The name of the firewall. | 
**description** | **str** | The description of the firewall. | 
**status** | **str** | Inactive status means no rules of this firewall are set for all assigned instances. | 
**instance_status** | [**[InstanceStatusRepresentation]**](InstanceStatusRepresentation.md) |  | 
**instances** | [**[InstanceDetails]**](InstanceDetails.md) |  | 
**rules** | [**Rules**](Rules.md) |  | 
**is_default** | **bool** | The default firewall rules are assigned by default to newly created instances with Firewall Add-On if not specified otherwise. Exactly one firewall can be set as default. | 
**created_date** | **datetime** | The creation date time for the firewall | 
**updated_date** | **datetime** | The update date time for the firewall | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


