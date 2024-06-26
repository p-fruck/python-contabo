# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.vnc_response import VncResponse

class TestVncResponse(unittest.TestCase):
    """VncResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> VncResponse:
        """Test VncResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `VncResponse`
        """
        model = VncResponse()
        if include_optional:
            return VncResponse(
                tenant_id = 'DE',
                customer_id = '3f184ab8-a600-4e7c-8c9b-3413e21a3752',
                instance_id = 100,
                enabled = True,
                vnc_ip = '154.12.54.123',
                vnc_port = 8001
            )
        else:
            return VncResponse(
                tenant_id = 'DE',
                customer_id = '3f184ab8-a600-4e7c-8c9b-3413e21a3752',
                instance_id = 100,
                enabled = True,
                vnc_ip = '154.12.54.123',
                vnc_port = 8001,
        )
        """

    def testVncResponse(self):
        """Test VncResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
