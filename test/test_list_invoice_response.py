"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.invoice_response import InvoiceResponse
from pfruck_contabo.model.list_invoice_response_links import ListInvoiceResponseLinks
from pfruck_contabo.model.list_user_response_pagination import ListUserResponsePagination
globals()['InvoiceResponse'] = InvoiceResponse
globals()['ListInvoiceResponseLinks'] = ListInvoiceResponseLinks
globals()['ListUserResponsePagination'] = ListUserResponsePagination
from pfruck_contabo.model.list_invoice_response import ListInvoiceResponse


class TestListInvoiceResponse(unittest.TestCase):
    """ListInvoiceResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListInvoiceResponse(self):
        """Test ListInvoiceResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListInvoiceResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
