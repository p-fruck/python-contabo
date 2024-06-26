# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.upgrade_object_storage_request import UpgradeObjectStorageRequest

class TestUpgradeObjectStorageRequest(unittest.TestCase):
    """UpgradeObjectStorageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpgradeObjectStorageRequest:
        """Test UpgradeObjectStorageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpgradeObjectStorageRequest`
        """
        model = UpgradeObjectStorageRequest()
        if include_optional:
            return UpgradeObjectStorageRequest(
                auto_scaling = pfruck_contabo.models.upgrade_auto_scaling_type.UpgradeAutoScalingType(
                    state = 'enabled', 
                    size_limit_tb = 6, ),
                total_purchased_space_tb = 8
            )
        else:
            return UpgradeObjectStorageRequest(
        )
        """

    def testUpgradeObjectStorageRequest(self):
        """Test UpgradeObjectStorageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
