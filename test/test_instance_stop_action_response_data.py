# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.instance_stop_action_response_data import InstanceStopActionResponseData

class TestInstanceStopActionResponseData(unittest.TestCase):
    """InstanceStopActionResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> InstanceStopActionResponseData:
        """Test InstanceStopActionResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `InstanceStopActionResponseData`
        """
        model = InstanceStopActionResponseData()
        if include_optional:
            return InstanceStopActionResponseData(
                tenant_id = 'DE',
                customer_id = '54321',
                instance_id = 12345,
                action = 'start'
            )
        else:
            return InstanceStopActionResponseData(
                tenant_id = 'DE',
                customer_id = '54321',
                instance_id = 12345,
                action = 'start',
        )
        """

    def testInstanceStopActionResponseData(self):
        """Test InstanceStopActionResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
