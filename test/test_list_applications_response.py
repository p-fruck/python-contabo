# coding: utf-8

"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from pfruck_contabo.models.list_applications_response import ListApplicationsResponse

class TestListApplicationsResponse(unittest.TestCase):
    """ListApplicationsResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ListApplicationsResponse:
        """Test ListApplicationsResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ListApplicationsResponse`
        """
        model = ListApplicationsResponse()
        if include_optional:
            return ListApplicationsResponse(
                pagination = pfruck_contabo.models.pagination_meta.PaginationMeta(
                    size = 10, 
                    total_elements = 100, 
                    total_pages = 10, 
                    page = 1, ),
                data = [
                    pfruck_contabo.models.application_response.ApplicationResponse(
                        application_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d', 
                        tenant_id = 'DE', 
                        customer_id = '12345', 
                        name = 'Webmin', 
                        description = 'Webmin cloud init', 
                        type = 'standard', 
                        application_config = [
                            pfruck_contabo.models.application_config.ApplicationConfig(
                                image_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d', 
                                user_data_id = '8b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d', 
                                user_data = '#cloud-config
user: admin
timezone: Europe/Berlin
chpasswd:
 expire: False', )
                            ], 
                        requirements = null, )
                    ],
                links = pfruck_contabo.models.links.Links(
                    self = '', 
                    first = '', 
                    previous = '', 
                    next = '', 
                    last = '', )
            )
        else:
            return ListApplicationsResponse(
                pagination = pfruck_contabo.models.pagination_meta.PaginationMeta(
                    size = 10, 
                    total_elements = 100, 
                    total_pages = 10, 
                    page = 1, ),
                data = [
                    pfruck_contabo.models.application_response.ApplicationResponse(
                        application_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d', 
                        tenant_id = 'DE', 
                        customer_id = '12345', 
                        name = 'Webmin', 
                        description = 'Webmin cloud init', 
                        type = 'standard', 
                        application_config = [
                            pfruck_contabo.models.application_config.ApplicationConfig(
                                image_id = '9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d', 
                                user_data_id = '8b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d', 
                                user_data = '#cloud-config
user: admin
timezone: Europe/Berlin
chpasswd:
 expire: False', )
                            ], 
                        requirements = null, )
                    ],
                links = pfruck_contabo.models.links.Links(
                    self = '', 
                    first = '', 
                    previous = '', 
                    next = '', 
                    last = '', ),
        )
        """

    def testListApplicationsResponse(self):
        """Test ListApplicationsResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
