# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.api.object_storages_audits_api import ObjectStoragesAuditsApi


class TestObjectStoragesAuditsApi(unittest.TestCase):
    """ObjectStoragesAuditsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ObjectStoragesAuditsApi()

    def tearDown(self) -> None:
        pass

    def test_retrieve_object_storage_audits_list(self) -> None:
        """Test case for retrieve_object_storage_audits_list

        List history about your object storages (audit)
        """
        pass


if __name__ == '__main__':
    unittest.main()
