"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import pfruck_contabo
from pfruck_contabo.api.tags_audits_api import TagsAuditsApi  # noqa: E501


class TestTagsAuditsApi(unittest.TestCase):
    """TagsAuditsApi unit test stubs"""

    def setUp(self):
        self.api = TagsAuditsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_tag_audits_list(self):
        """Test case for retrieve_tag_audits_list

        List history about your assignments (audit)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
