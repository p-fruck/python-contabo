"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.credential_data import CredentialData
from pfruck_contabo.model.list_credential_response_links import ListCredentialResponseLinks
from pfruck_contabo.model.list_instances_actions_audit_response_pagination import ListInstancesActionsAuditResponsePagination
globals()['CredentialData'] = CredentialData
globals()['ListCredentialResponseLinks'] = ListCredentialResponseLinks
globals()['ListInstancesActionsAuditResponsePagination'] = ListInstancesActionsAuditResponsePagination
from pfruck_contabo.model.list_credential_response import ListCredentialResponse


class TestListCredentialResponse(unittest.TestCase):
    """ListCredentialResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testListCredentialResponse(self):
        """Test ListCredentialResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ListCredentialResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
