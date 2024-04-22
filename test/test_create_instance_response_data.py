# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.create_instance_response_data import CreateInstanceResponseData

class TestCreateInstanceResponseData(unittest.TestCase):
    """CreateInstanceResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInstanceResponseData:
        """Test CreateInstanceResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInstanceResponseData`
        """
        model = CreateInstanceResponseData()
        if include_optional:
            return CreateInstanceResponseData(
                tenant_id = 'DE',
                customer_id = '54321',
                instance_id = 12345,
                created_date = '2021-06-02T12:32:03.363Z',
                image_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
                product_id = 'V45',
                region = 'EU',
                add_ons = [
                    pfruck_contabo.models.add_on_response.AddOnResponse(
                        id = 1431, 
                        quantity = 4, )
                    ],
                os_type = 'Linux',
                status = 'provisioning',
                ssh_keys = [123,125]
            )
        else:
            return CreateInstanceResponseData(
                tenant_id = 'DE',
                customer_id = '54321',
                instance_id = 12345,
                created_date = '2021-06-02T12:32:03.363Z',
                image_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
                product_id = 'V45',
                region = 'EU',
                add_ons = [
                    pfruck_contabo.models.add_on_response.AddOnResponse(
                        id = 1431, 
                        quantity = 4, )
                    ],
                os_type = 'Linux',
                status = 'provisioning',
                ssh_keys = [123,125],
        )
        """

    def testCreateInstanceResponseData(self):
        """Test CreateInstanceResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
