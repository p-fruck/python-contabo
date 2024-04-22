# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.create_custom_image_request import CreateCustomImageRequest

class TestCreateCustomImageRequest(unittest.TestCase):
    """CreateCustomImageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateCustomImageRequest:
        """Test CreateCustomImageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateCustomImageRequest`
        """
        model = CreateCustomImageRequest()
        if include_optional:
            return CreateCustomImageRequest(
                name = 'Ubuntu Custom Image',
                description = 'Ubuntu Server 20.04.2 LTS',
                url = 'https://example.com/image.qcow2',
                os_type = 'Linux',
                version = '20.04.2'
            )
        else:
            return CreateCustomImageRequest(
                name = 'Ubuntu Custom Image',
                url = 'https://example.com/image.qcow2',
                os_type = 'Linux',
                version = '20.04.2',
        )
        """

    def testCreateCustomImageRequest(self):
        """Test CreateCustomImageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
