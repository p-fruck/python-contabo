"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.list_firewall_response_data import ListFirewallResponseData
from pfruck_contabo.model.list_firewall_response_links import ListFirewallResponseLinks
from pfruck_contabo.model.list_user_response_pagination import ListUserResponsePagination
globals()['ListFirewallResponseData'] = ListFirewallResponseData
globals()['ListFirewallResponseLinks'] = ListFirewallResponseLinks
globals()['ListUserResponsePagination'] = ListUserResponsePagination
from pfruck_contabo.model.list_firewall_response import ListFirewallResponse


class TestListFirewallResponse(unittest.TestCase):
    """ListFirewallResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListFirewallResponse(self):
        """Test ListFirewallResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListFirewallResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
