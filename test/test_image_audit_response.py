# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.image_audit_response import ImageAuditResponse

class TestImageAuditResponse(unittest.TestCase):
    """ImageAuditResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ImageAuditResponse:
        """Test ImageAuditResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ImageAuditResponse`
        """
        model = ImageAuditResponse()
        if include_optional:
            return ImageAuditResponse(
                pagination = pfruck_contabo.models.pagination_meta.PaginationMeta(
                    size = 10, 
                    total_elements = 100, 
                    total_pages = 10, 
                    page = 1, ),
                data = [
                    pfruck_contabo.models.image_audit_response_data.ImageAuditResponseData(
                        id = 12345, 
                        action = 'CREATED', 
                        timestamp = '2021-03-30T11:35:06.177Z', 
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        changed_by = 'c4c800ff-e524-47dd-9543-71dfc8b91113', 
                        username = 'John.Doe', 
                        request_id = 'A2F56FAF-18N0-4893-11HG-R312M1E4FEC5', 
                        trace_id = '78E9A428-94E9-4A2A-92F5-26038C6884F', 
                        image_id = 'e443eab5-647a-4bc3-b4f9-16f5a281224d', 
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
            return ImageAuditResponse(
                pagination = pfruck_contabo.models.pagination_meta.PaginationMeta(
                    size = 10, 
                    total_elements = 100, 
                    total_pages = 10, 
                    page = 1, ),
                data = [
                    pfruck_contabo.models.image_audit_response_data.ImageAuditResponseData(
                        id = 12345, 
                        action = 'CREATED', 
                        timestamp = '2021-03-30T11:35:06.177Z', 
                        tenant_id = 'DE', 
                        customer_id = '54321', 
                        changed_by = 'c4c800ff-e524-47dd-9543-71dfc8b91113', 
                        username = 'John.Doe', 
                        request_id = 'A2F56FAF-18N0-4893-11HG-R312M1E4FEC5', 
                        trace_id = '78E9A428-94E9-4A2A-92F5-26038C6884F', 
                        image_id = 'e443eab5-647a-4bc3-b4f9-16f5a281224d', 
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

    def testImageAuditResponse(self):
        """Test ImageAuditResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
