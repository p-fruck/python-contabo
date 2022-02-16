# coding: utf-8

"""
    Contabo API


    OpenAPI spec version: 1.0.0
    Contact: support@contabo.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pfruck_contabo
from pfruck_contabo.api.internal_api import InternalApi  # noqa: E501
from pfruck_contabo.rest import ApiException


class TestInternalApi(unittest.TestCase):
    """InternalApi unit test stubs"""

    def setUp(self):
        self.api = InternalApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_object_storage_credentials(self):
        """Test case for get_object_storage_credentials

        Get S3 compatible object storage credentials  # noqa: E501
        """
        pass

    def test_regenerate_credentials(self):
        """Test case for regenerate_credentials

        Regenerates secret key of specified user for the S3 compatible object storages  # noqa: E501
        """
        pass

    def test_retrieve_user_is_password_set(self):
        """Test case for retrieve_user_is_password_set

        Get user is password set status  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
