"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.application_config import ApplicationConfig
from pfruck_contabo.model.application_response_requirements import ApplicationResponseRequirements
globals()['ApplicationConfig'] = ApplicationConfig
globals()['ApplicationResponseRequirements'] = ApplicationResponseRequirements
from pfruck_contabo.model.application_response import ApplicationResponse


class TestApplicationResponse(unittest.TestCase):
    """ApplicationResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationResponse(self):
        """Test ApplicationResponse"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationResponse()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()