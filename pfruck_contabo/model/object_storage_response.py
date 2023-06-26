"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from pfruck_contabo.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from pfruck_contabo.exceptions import ApiAttributeError


def lazy_import():
    from pfruck_contabo.model.object_storage_response_auto_scaling import ObjectStorageResponseAutoScaling
    globals()['ObjectStorageResponseAutoScaling'] = ObjectStorageResponseAutoScaling


class ObjectStorageResponse(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('status',): {
            'READY': "READY",
            'PROVISIONING': "PROVISIONING",
            'UPGRADING': "UPGRADING",
            'CANCELLED': "CANCELLED",
            'ERROR': "ERROR",
            'ENABLED': "ENABLED",
            'DISABLED': "DISABLED",
            'MANUAL_PROVISIONING': "MANUAL_PROVISIONING",
            'PRODUCT_NOT_AVAILABLE': "PRODUCT_NOT_AVAILABLE",
            'LIMIT_EXCEEDED': "LIMIT_EXCEEDED",
            'VERIFICATION_REQUIRED': "VERIFICATION_REQUIRED",
            'COMPLETED': "COMPLETED",
            'PENDING_PAYMENT': "PENDING_PAYMENT",
            'UNKNOWN': "UNKNOWN",
        },
    }

    validations = {
        ('tenant_id',): {
            'min_length': 1,
        },
        ('customer_id',): {
            'min_length': 1,
        },
        ('object_storage_id',): {
            'min_length': 1,
        },
        ('data_center',): {
            'min_length': 1,
        },
        ('display_name',): {
            'max_length': 255,
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'tenant_id': (str,),  # noqa: E501
            'customer_id': (str,),  # noqa: E501
            'object_storage_id': (str,),  # noqa: E501
            'created_date': (datetime,),  # noqa: E501
            'cancel_date': (date,),  # noqa: E501
            'auto_scaling': (ObjectStorageResponseAutoScaling,),  # noqa: E501
            'data_center': (str,),  # noqa: E501
            'total_purchased_space_tb': (float,),  # noqa: E501
            's3_url': (str,),  # noqa: E501
            's3_tenant_id': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'region': (str,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tenant_id': 'tenantId',  # noqa: E501
        'customer_id': 'customerId',  # noqa: E501
        'object_storage_id': 'objectStorageId',  # noqa: E501
        'created_date': 'createdDate',  # noqa: E501
        'cancel_date': 'cancelDate',  # noqa: E501
        'auto_scaling': 'autoScaling',  # noqa: E501
        'data_center': 'dataCenter',  # noqa: E501
        'total_purchased_space_tb': 'totalPurchasedSpaceTB',  # noqa: E501
        's3_url': 's3Url',  # noqa: E501
        's3_tenant_id': 's3TenantId',  # noqa: E501
        'status': 'status',  # noqa: E501
        'region': 'region',  # noqa: E501
        'display_name': 'displayName',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, tenant_id, customer_id, object_storage_id, created_date, cancel_date, auto_scaling, data_center, total_purchased_space_tb, s3_url, s3_tenant_id, status, region, display_name, *args, **kwargs):  # noqa: E501
        """ObjectStorageResponse - a model defined in OpenAPI

        Args:
            tenant_id (str): Your customer tenant id
            customer_id (str): Your customer number
            object_storage_id (str): Your object storage id
            created_date (datetime): Creation date for object storage.
            cancel_date (date): Cancellation date for object storage.
            auto_scaling (ObjectStorageResponseAutoScaling):
            data_center (str): Data center your object storage is located
            total_purchased_space_tb (float): Amount of purchased / requested object storage in TB.
            s3_url (str): S3 URL to connect to your S3 compatible object storage
            s3_tenant_id (str): Your S3 tenantId. Only required for public sharing.
            status (str): The object storage status
            region (str): The region where your object storage is located
            display_name (str): Display name for object storage.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', True)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.tenant_id = tenant_id
        self.customer_id = customer_id
        self.object_storage_id = object_storage_id
        self.created_date = created_date
        self.cancel_date = cancel_date
        self.auto_scaling = auto_scaling
        self.data_center = data_center
        self.total_purchased_space_tb = total_purchased_space_tb
        self.s3_url = s3_url
        self.s3_tenant_id = s3_tenant_id
        self.status = status
        self.region = region
        self.display_name = display_name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, tenant_id, customer_id, object_storage_id, created_date, cancel_date, auto_scaling, data_center, total_purchased_space_tb, s3_url, s3_tenant_id, status, region, display_name, *args, **kwargs):  # noqa: E501
        """ObjectStorageResponse - a model defined in OpenAPI

        Args:
            tenant_id (str): Your customer tenant id
            customer_id (str): Your customer number
            object_storage_id (str): Your object storage id
            created_date (datetime): Creation date for object storage.
            cancel_date (date): Cancellation date for object storage.
            auto_scaling (ObjectStorageResponseAutoScaling):
            data_center (str): Data center your object storage is located
            total_purchased_space_tb (float): Amount of purchased / requested object storage in TB.
            s3_url (str): S3 URL to connect to your S3 compatible object storage
            s3_tenant_id (str): Your S3 tenantId. Only required for public sharing.
            status (str): The object storage status
            region (str): The region where your object storage is located
            display_name (str): Display name for object storage.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            for arg in args:
                if isinstance(arg, dict):
                    kwargs.update(arg)
                else:
                    raise ApiTypeError(
                        "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                            args,
                            self.__class__.__name__,
                        ),
                        path_to_item=_path_to_item,
                        valid_classes=(self.__class__,),
                    )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.tenant_id = tenant_id
        self.customer_id = customer_id
        self.object_storage_id = object_storage_id
        self.created_date = created_date
        self.cancel_date = cancel_date
        self.auto_scaling = auto_scaling
        self.data_center = data_center
        self.total_purchased_space_tb = total_purchased_space_tb
        self.s3_url = s3_url
        self.s3_tenant_id = s3_tenant_id
        self.status = status
        self.region = region
        self.display_name = display_name
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
