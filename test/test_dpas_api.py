"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import pfruck_contabo
from pfruck_contabo.api.dpas_api import DPASApi  # noqa: E501


class TestDPASApi(unittest.TestCase):
    """DPASApi unit test stubs"""

    def setUp(self):
        self.api = DPASApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_conclude_dpa(self):
        """Test case for conclude_dpa

        Concludes a data processing agreement  # noqa: E501
        """
        pass

    def test_create_dpa(self):
        """Test case for create_dpa

        Create a new data processing agreement  # noqa: E501
        """
        pass

    def test_download_dpa_file(self):
        """Test case for download_dpa_file

        Download concluded DPA PDF file  # noqa: E501
        """
        pass

    def test_download_preview_dpa(self):
        """Test case for download_preview_dpa

        Download preview version of DPA  # noqa: E501
        """
        pass

    def test_list_dpa_services(self):
        """Test case for list_dpa_services

        List services  # noqa: E501
        """
        pass

    def test_retrieve_dpa(self):
        """Test case for retrieve_dpa

        Get specific Dpa by it's dpaId  # noqa: E501
        """
        pass

    def test_retrieve_dpa_list(self):
        """Test case for retrieve_dpa_list

        List all Dpas  # noqa: E501
        """
        pass

    def test_terminate_dpa(self):
        """Test case for terminate_dpa

        Terminate an existing DPA by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()