"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.links import Links
from pfruck_contabo.model.object_storage_audit_response import ObjectStorageAuditResponse
from pfruck_contabo.model.pagination_meta import PaginationMeta
globals()['Links'] = Links
globals()['ObjectStorageAuditResponse'] = ObjectStorageAuditResponse
globals()['PaginationMeta'] = PaginationMeta
from pfruck_contabo.model.list_object_storage_audit_response import ListObjectStorageAuditResponse


class TestListObjectStorageAuditResponse(unittest.TestCase):
    """ListObjectStorageAuditResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListObjectStorageAuditResponse(self):
        """Test ListObjectStorageAuditResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListObjectStorageAuditResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
