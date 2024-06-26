# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.list_role_audit_response import ListRoleAuditResponse

class TestListRoleAuditResponse(unittest.TestCase):
    """ListRoleAuditResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListRoleAuditResponse:
        """Test ListRoleAuditResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListRoleAuditResponse`
        """
        model = ListRoleAuditResponse()
        if include_optional:
            return ListRoleAuditResponse(
                data = [
                    pfruck_contabo.models.role_audit_response.RoleAuditResponse(
                        id = 12345, 
                        action = 'CREATED', 
                        timestamp = '2021-03-30T11:35:06.177Z', 
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        changed_by = '54321', 
                        username = 'John.Doe', 
                        request_id = 'A2F56FAF-18N0-4893-11HG-R312M1E4FEC5', 
                        trace_id = '78E9A428-94E9-4A2A-92F5-26038C6884F', 
                        role_id = 12345, 
                        changes = {"prev":{"name":"test"},"new":{"name":"test1"}}, )
                    ],
                links = pfruck_contabo.models.links.Links(
                    self = '', 
                    first = '', 
                    previous = '', 
                    next = '', 
                    last = '', )
            )
        else:
            return ListRoleAuditResponse(
                data = [
                    pfruck_contabo.models.role_audit_response.RoleAuditResponse(
                        id = 12345, 
                        action = 'CREATED', 
                        timestamp = '2021-03-30T11:35:06.177Z', 
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        changed_by = '54321', 
                        username = 'John.Doe', 
                        request_id = 'A2F56FAF-18N0-4893-11HG-R312M1E4FEC5', 
                        trace_id = '78E9A428-94E9-4A2A-92F5-26038C6884F', 
                        role_id = 12345, 
                        changes = {"prev":{"name":"test"},"new":{"name":"test1"}}, )
                    ],
                links = pfruck_contabo.models.links.Links(
                    self = '', 
                    first = '', 
                    previous = '', 
                    next = '', 
                    last = '', ),
        )
        """

    def testListRoleAuditResponse(self):
        """Test ListRoleAuditResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
