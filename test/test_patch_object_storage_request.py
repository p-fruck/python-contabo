# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.patch_object_storage_request import PatchObjectStorageRequest

class TestPatchObjectStorageRequest(unittest.TestCase):
    """PatchObjectStorageRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PatchObjectStorageRequest:
        """Test PatchObjectStorageRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PatchObjectStorageRequest`
        """
        model = PatchObjectStorageRequest()
        if include_optional:
            return PatchObjectStorageRequest(
                display_name = 'Object storage 1'
            )
        else:
            return PatchObjectStorageRequest(
                display_name = 'Object storage 1',
        )
        """

    def testPatchObjectStorageRequest(self):
        """Test PatchObjectStorageRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
