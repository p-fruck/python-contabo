"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import pfruck_contabo
from pfruck_contabo.api.images_audits_api import ImagesAuditsApi  # noqa: E501


class TestImagesAuditsApi(unittest.TestCase):
    """ImagesAuditsApi unit test stubs"""

    def setUp(self):
        self.api = ImagesAuditsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_image_audits_list(self):
        """Test case for retrieve_image_audits_list

        List history about your custom images (audit)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
