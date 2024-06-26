# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.upgrade_object_storage_response_data import UpgradeObjectStorageResponseData

class TestUpgradeObjectStorageResponseData(unittest.TestCase):
    """UpgradeObjectStorageResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UpgradeObjectStorageResponseData:
        """Test UpgradeObjectStorageResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UpgradeObjectStorageResponseData`
        """
        model = UpgradeObjectStorageResponseData()
        if include_optional:
            return UpgradeObjectStorageResponseData(
                tenant_id = 'DE',
                customer_id = '54321',
                object_storage_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
                created_date = '2021-06-02T12:32:03.363Z',
                data_center = 'EU',
                auto_scaling = pfruck_contabo.models.auto_scaling_type_response.AutoScalingTypeResponse(
                    state = 'enabled', 
                    size_limit_tb = 1, 
                    error_message = '', ),
                s3_url = 'eu1-s3.contabo.com',
                status = 'READY',
                total_purchased_space_tb = 6,
                region = 'European Union',
                display_name = 'Object storage 1'
            )
        else:
            return UpgradeObjectStorageResponseData(
                tenant_id = 'DE',
                customer_id = '54321',
                object_storage_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
                created_date = '2021-06-02T12:32:03.363Z',
                data_center = 'EU',
                auto_scaling = pfruck_contabo.models.auto_scaling_type_response.AutoScalingTypeResponse(
                    state = 'enabled', 
                    size_limit_tb = 1, 
                    error_message = '', ),
                s3_url = 'eu1-s3.contabo.com',
                status = 'READY',
                total_purchased_space_tb = 6,
                region = 'European Union',
                display_name = 'Object storage 1',
        )
        """

    def testUpgradeObjectStorageResponseData(self):
        """Test UpgradeObjectStorageResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
