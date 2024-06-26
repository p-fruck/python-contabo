# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.assignment_audit_response import AssignmentAuditResponse

class TestAssignmentAuditResponse(unittest.TestCase):
    """AssignmentAuditResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AssignmentAuditResponse:
        """Test AssignmentAuditResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AssignmentAuditResponse`
        """
        model = AssignmentAuditResponse()
        if include_optional:
            return AssignmentAuditResponse(
                tenant_id = 'DE',
                customer_id = '54321',
                id = 12345,
                resource_id = 'a1b2c3',
                resource_type = 'instance',
                tag_id = 12345,
                action = 'CREATED | DELETED',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                changed_by = '54321',
                username = 'John Doe',
                request_id = '04E0F898-37B4-48BC-A794-1A57ABE6AA31',
                trace_id = '78E9A428-94E9-4A2A-92F5-26038C6884F5',
                changes = None
            )
        else:
            return AssignmentAuditResponse(
                tenant_id = 'DE',
                customer_id = '54321',
                id = 12345,
                resource_id = 'a1b2c3',
                resource_type = 'instance',
                tag_id = 12345,
                action = 'CREATED | DELETED',
                timestamp = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                changed_by = '54321',
                username = 'John Doe',
                request_id = '04E0F898-37B4-48BC-A794-1A57ABE6AA31',
                trace_id = '78E9A428-94E9-4A2A-92F5-26038C6884F5',
        )
        """

    def testAssignmentAuditResponse(self):
        """Test AssignmentAuditResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
