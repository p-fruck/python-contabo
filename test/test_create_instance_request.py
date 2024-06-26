# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.create_instance_request import CreateInstanceRequest

class TestCreateInstanceRequest(unittest.TestCase):
    """CreateInstanceRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateInstanceRequest:
        """Test CreateInstanceRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateInstanceRequest`
        """
        model = CreateInstanceRequest()
        if include_optional:
            return CreateInstanceRequest(
                image_id = 'afecbb85-e2fc-46f0-9684-b46b1faf00bb',
                product_id = 'V45',
                region = 'EU',
                ssh_keys = [123, 125],
                root_password = 1,
                user_data = '#cloud-config
user: admin
timezone: Europe/Berlin
chpasswd:
 expire: False',
                license = 'PleskHost',
                period = 6,
                display_name = 'VPS',
                default_user = 'admin',
                add_ons = pfruck_contabo.models.create_instance_addons.CreateInstanceAddons(
                    private_networking = {}, 
                    additional_ips = {}, 
                    extra_storage = {}, 
                    custom_image = {}, 
                    addons_ids = [
                        pfruck_contabo.models.add_on_request.AddOnRequest(
                            id = 1019, 
                            quantity = 4, )
                        ], ),
                application_id = '3f184ab8-a600-4e7c-8c9b-3413e21a3752'
            )
        else:
            return CreateInstanceRequest(
                period = 6,
        )
        """

    def testCreateInstanceRequest(self):
        """Test CreateInstanceRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
