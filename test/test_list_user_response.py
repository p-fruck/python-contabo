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
from pfruck_contabo.model.pagination_meta import PaginationMeta
from pfruck_contabo.model.user_response import UserResponse
globals()['Links'] = Links
globals()['PaginationMeta'] = PaginationMeta
globals()['UserResponse'] = UserResponse
from pfruck_contabo.model.list_user_response import ListUserResponse


class TestListUserResponse(unittest.TestCase):
    """ListUserResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListUserResponse(self):
        """Test ListUserResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListUserResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
