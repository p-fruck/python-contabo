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
from pfruck_contabo.model.tag_response import TagResponse
globals()['Links'] = Links
globals()['PaginationMeta'] = PaginationMeta
globals()['TagResponse'] = TagResponse
from pfruck_contabo.model.list_tag_response import ListTagResponse


class TestListTagResponse(unittest.TestCase):
    """ListTagResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListTagResponse(self):
        """Test ListTagResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListTagResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
