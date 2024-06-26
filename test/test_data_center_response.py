# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.data_center_response import DataCenterResponse

class TestDataCenterResponse(unittest.TestCase):
    """DataCenterResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DataCenterResponse:
        """Test DataCenterResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DataCenterResponse`
        """
        model = DataCenterResponse()
        if include_optional:
            return DataCenterResponse(
                name = 'European Union 1',
                slug = 'EU1',
                capabilities = ["VPS","Object-Storage"],
                s3_url = 'eu1-s3.contabo.com',
                region_name = 'European Union',
                region_slug = 'EU',
                tenant_id = 'DE',
                customer_id = '54321'
            )
        else:
            return DataCenterResponse(
                name = 'European Union 1',
                slug = 'EU1',
                capabilities = ["VPS","Object-Storage"],
                s3_url = 'eu1-s3.contabo.com',
                region_name = 'European Union',
                region_slug = 'EU',
                tenant_id = 'DE',
                customer_id = '54321',
        )
        """

    def testDataCenterResponse(self):
        """Test DataCenterResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
