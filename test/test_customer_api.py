"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import pfruck_contabo
from pfruck_contabo.api.customer_api import CustomerApi  # noqa: E501


class TestCustomerApi(unittest.TestCase):
    """CustomerApi unit test stubs"""

    def setUp(self):
        self.api = CustomerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_retrieve_customer(self):
        """Test case for retrieve_customer

        Get customer info  # noqa: E501
        """
        pass

    def test_retrieve_payment_method(self):
        """Test case for retrieve_payment_method

        List current payment method  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
