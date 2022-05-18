# CustomerResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** | Your customer tenant id | 
**customer_id** | **str** | Your customer number | 
**salutation** | **str** | Customer salutation | 
**type** | **str** | Customer type | 
**private** | [**CustomerTypePrivate**](CustomerTypePrivate.md) |  | 
**business** | [**CustomerTypeBusiness**](CustomerTypeBusiness.md) |  | 
**tax_percentage** | **float** | Customer tax percentage | 
**currency** | **str** | Customer currency | 
**balance** | **float** | Customer balance | 
**locale** | **str** | Customer locale | 
**addresses** | [**[CustomerAddress]**](CustomerAddress.md) |  | 
**emails** | [**[CustomerEmail]**](CustomerEmail.md) |  | 
**phones** | [**[CustomerPhone]**](CustomerPhone.md) |  | 
**status** | **str** | Customer status | 
**created_date** | **datetime** | The creation date of the customer | 
**monthly_recurring_revenue** | **float** | The monthly revenue of the customer (How much the customer has to pay recurring each month) | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


