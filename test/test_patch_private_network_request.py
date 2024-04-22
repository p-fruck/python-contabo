# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.patch_private_network_request import PatchPrivateNetworkRequest

class TestPatchPrivateNetworkRequest(unittest.TestCase):
    """PatchPrivateNetworkRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchPrivateNetworkRequest:
        """Test PatchPrivateNetworkRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchPrivateNetworkRequest`
        """
        model = PatchPrivateNetworkRequest()
        if include_optional:
            return PatchPrivateNetworkRequest(
                name = 'myPrivateNetwork',
                description = 'myPrivateNetwork Description'
            )
        else:
            return PatchPrivateNetworkRequest(
        )
        """

    def testPatchPrivateNetworkRequest(self):
        """Test PatchPrivateNetworkRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
