"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pfruck_contabo
from pfruck_contabo.model.application_requirements_minimum import ApplicationRequirementsMinimum
from pfruck_contabo.model.application_requirements_optimal import ApplicationRequirementsOptimal
globals()['ApplicationRequirementsMinimum'] = ApplicationRequirementsMinimum
globals()['ApplicationRequirementsOptimal'] = ApplicationRequirementsOptimal
from pfruck_contabo.model.application_requirements import ApplicationRequirements


class TestApplicationRequirements(unittest.TestCase):
    """ApplicationRequirements unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testApplicationRequirements(self):
        """Test ApplicationRequirements"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ApplicationRequirements()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
