"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.customer_address import CustomerAddress
from pfruck_contabo.model.customer_email import CustomerEmail
from pfruck_contabo.model.customer_phone import CustomerPhone
from pfruck_contabo.model.customer_type_business import CustomerTypeBusiness
from pfruck_contabo.model.customer_type_private import CustomerTypePrivate
globals()['CustomerAddress'] = CustomerAddress
globals()['CustomerEmail'] = CustomerEmail
globals()['CustomerPhone'] = CustomerPhone
globals()['CustomerTypeBusiness'] = CustomerTypeBusiness
globals()['CustomerTypePrivate'] = CustomerTypePrivate
from pfruck_contabo.model.customer_response import CustomerResponse


class TestCustomerResponse(unittest.TestCase):
    """CustomerResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testCustomerResponse(self):
        """Test CustomerResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = CustomerResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()