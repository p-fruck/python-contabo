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
    from pfruck_contabo.model.other_data import OtherData
    globals()['OtherData'] = OtherData


class ProcessedDataType(ModelNormal):
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
    }

    validations = {
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
            'billing_data': (bool,),  # noqa: E501
            'address_data': (bool,),  # noqa: E501
            'offer_data': (bool,),  # noqa: E501
            'authentication_data': (bool,),  # noqa: E501
            'bank_details': (bool,),  # noqa: E501
            'order_data': (bool,),  # noqa: E501
            'image_files': (bool,),  # noqa: E501
            'emails': (bool,),  # noqa: E501
            'financial_data': (bool,),  # noqa: E501
            'communication_data': (bool,),  # noqa: E501
            'employee_data': (bool,),  # noqa: E501
            'usage_data': (bool,),  # noqa: E501
            'password_data': (bool,),  # noqa: E501
            'personnel_data': (bool,),  # noqa: E501
            'personnel_master_data': (bool,),  # noqa: E501
            'program_code': (bool,),  # noqa: E501
            'profile_data': (bool,),  # noqa: E501
            'transaction_data': (bool,),  # noqa: E501
            'contract_data': (bool,),  # noqa: E501
            'contract_billing_data': (bool,),  # noqa: E501
            'video_files': (bool,),  # noqa: E501
            'payment_data': (bool,),  # noqa: E501
            'ip_addresses': (bool,),  # noqa: E501
            'other': (OtherData,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'billing_data': 'billingData',  # noqa: E501
        'address_data': 'addressData',  # noqa: E501
        'offer_data': 'offerData',  # noqa: E501
        'authentication_data': 'authenticationData',  # noqa: E501
        'bank_details': 'bankDetails',  # noqa: E501
        'order_data': 'orderData',  # noqa: E501
        'image_files': 'imageFiles',  # noqa: E501
        'emails': 'emails',  # noqa: E501
        'financial_data': 'financialData',  # noqa: E501
        'communication_data': 'communicationData',  # noqa: E501
        'employee_data': 'employeeData',  # noqa: E501
        'usage_data': 'usageData',  # noqa: E501
        'password_data': 'passwordData',  # noqa: E501
        'personnel_data': 'personnelData',  # noqa: E501
        'personnel_master_data': 'personnelMasterData',  # noqa: E501
        'program_code': 'programCode',  # noqa: E501
        'profile_data': 'profileData',  # noqa: E501
        'transaction_data': 'transactionData',  # noqa: E501
        'contract_data': 'contractData',  # noqa: E501
        'contract_billing_data': 'contractBillingData',  # noqa: E501
        'video_files': 'videoFiles',  # noqa: E501
        'payment_data': 'paymentData',  # noqa: E501
        'ip_addresses': 'ipAddresses',  # noqa: E501
        'other': 'other',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, billing_data, address_data, offer_data, authentication_data, bank_details, order_data, image_files, emails, financial_data, communication_data, employee_data, usage_data, password_data, personnel_data, personnel_master_data, program_code, profile_data, transaction_data, contract_data, contract_billing_data, video_files, payment_data, ip_addresses, other, *args, **kwargs):  # noqa: E501
        """ProcessedDataType - a model defined in OpenAPI

        Args:
            billing_data (bool): Billing Data
            address_data (bool): Address Data
            offer_data (bool): Offer Data
            authentication_data (bool): Authentication Data
            bank_details (bool): Bank Details
            order_data (bool): Order Data
            image_files (bool): Image Files
            emails (bool): Emails
            financial_data (bool): Financial Data
            communication_data (bool): Communication Data
            employee_data (bool): Employee Data
            usage_data (bool): Usage Data
            password_data (bool): Password Data
            personnel_data (bool): Personnel Data
            personnel_master_data (bool): Personnel Master Data
            program_code (bool): Program Code
            profile_data (bool): Profile Data
            transaction_data (bool): Transaction Data
            contract_data (bool): Contract Data
            contract_billing_data (bool): Contract Billing Data
            video_files (bool): Video Files
            payment_data (bool): Payment Data
            ip_addresses (bool): Ip Addresses
            other (OtherData):

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

        self.billing_data = billing_data
        self.address_data = address_data
        self.offer_data = offer_data
        self.authentication_data = authentication_data
        self.bank_details = bank_details
        self.order_data = order_data
        self.image_files = image_files
        self.emails = emails
        self.financial_data = financial_data
        self.communication_data = communication_data
        self.employee_data = employee_data
        self.usage_data = usage_data
        self.password_data = password_data
        self.personnel_data = personnel_data
        self.personnel_master_data = personnel_master_data
        self.program_code = program_code
        self.profile_data = profile_data
        self.transaction_data = transaction_data
        self.contract_data = contract_data
        self.contract_billing_data = contract_billing_data
        self.video_files = video_files
        self.payment_data = payment_data
        self.ip_addresses = ip_addresses
        self.other = other
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
    def __init__(self, billing_data, address_data, offer_data, authentication_data, bank_details, order_data, image_files, emails, financial_data, communication_data, employee_data, usage_data, password_data, personnel_data, personnel_master_data, program_code, profile_data, transaction_data, contract_data, contract_billing_data, video_files, payment_data, ip_addresses, other, *args, **kwargs):  # noqa: E501
        """ProcessedDataType - a model defined in OpenAPI

        Args:
            billing_data (bool): Billing Data
            address_data (bool): Address Data
            offer_data (bool): Offer Data
            authentication_data (bool): Authentication Data
            bank_details (bool): Bank Details
            order_data (bool): Order Data
            image_files (bool): Image Files
            emails (bool): Emails
            financial_data (bool): Financial Data
            communication_data (bool): Communication Data
            employee_data (bool): Employee Data
            usage_data (bool): Usage Data
            password_data (bool): Password Data
            personnel_data (bool): Personnel Data
            personnel_master_data (bool): Personnel Master Data
            program_code (bool): Program Code
            profile_data (bool): Profile Data
            transaction_data (bool): Transaction Data
            contract_data (bool): Contract Data
            contract_billing_data (bool): Contract Billing Data
            video_files (bool): Video Files
            payment_data (bool): Payment Data
            ip_addresses (bool): Ip Addresses
            other (OtherData):

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

        self.billing_data = billing_data
        self.address_data = address_data
        self.offer_data = offer_data
        self.authentication_data = authentication_data
        self.bank_details = bank_details
        self.order_data = order_data
        self.image_files = image_files
        self.emails = emails
        self.financial_data = financial_data
        self.communication_data = communication_data
        self.employee_data = employee_data
        self.usage_data = usage_data
        self.password_data = password_data
        self.personnel_data = personnel_data
        self.personnel_master_data = personnel_master_data
        self.program_code = program_code
        self.profile_data = profile_data
        self.transaction_data = transaction_data
        self.contract_data = contract_data
        self.contract_billing_data = contract_billing_data
        self.video_files = video_files
        self.payment_data = payment_data
        self.ip_addresses = ip_addresses
        self.other = other
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
