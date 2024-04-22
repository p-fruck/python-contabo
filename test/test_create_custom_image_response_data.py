# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.create_custom_image_response_data import CreateCustomImageResponseData

class TestCreateCustomImageResponseData(unittest.TestCase):
    """CreateCustomImageResponseData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCustomImageResponseData:
        """Test CreateCustomImageResponseData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCustomImageResponseData`
        """
        model = CreateCustomImageResponseData()
        if include_optional:
            return CreateCustomImageResponseData(
                tenant_id = 'DE',
                customer_id = '54321',
                image_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d'
            )
        else:
            return CreateCustomImageResponseData(
                tenant_id = 'DE',
                customer_id = '54321',
                image_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d',
        )
        """

    def testCreateCustomImageResponseData(self):
        """Test CreateCustomImageResponseData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
