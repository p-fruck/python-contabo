"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import pfruck_contabo
from pfruck_contabo.api.roles_api import RolesApi  # noqa: E501


class TestRolesApi(unittest.TestCase):
    """RolesApi unit test stubs"""

    def setUp(self):
        self.api = RolesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_role(self):
        """Test case for create_role

        Create a new role  # noqa: E501
        """
        pass

    def test_delete_role(self):
        """Test case for delete_role

        Delete existing role by id  # noqa: E501
        """
        pass

    def test_retrieve_api_permissions_list(self):
        """Test case for retrieve_api_permissions_list

        List of API permissions  # noqa: E501
        """
        pass

    def test_retrieve_role(self):
        """Test case for retrieve_role

        Get specific role by id  # noqa: E501
        """
        pass

    def test_retrieve_role_list(self):
        """Test case for retrieve_role_list

        List roles  # noqa: E501
        """
        pass

    def test_update_role(self):
        """Test case for update_role

        Update specific role by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
