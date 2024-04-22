# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.api.tags_api import TagsApi


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TagsApi()

    def tearDown(self) -> None:
        pass

    def test_create_tag(self) -> None:
        """Test case for create_tag

        Create a new tag
        """
        pass

    def test_delete_tag(self) -> None:
        """Test case for delete_tag

        Delete existing tag by id
        """
        pass

    def test_retrieve_tag(self) -> None:
        """Test case for retrieve_tag

        Get specific tag by id
        """
        pass

    def test_retrieve_tag_list(self) -> None:
        """Test case for retrieve_tag_list

        List tags
        """
        pass

    def test_update_tag(self) -> None:
        """Test case for update_tag

        Update specific tag by id
        """
        pass


if __name__ == '__main__':
    unittest.main()
