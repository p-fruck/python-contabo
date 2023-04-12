"""
    Contabo API


    The version of the OpenAPI document: 1.0.0
    Contact: support@contabo.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import pfruck_contabo
from pfruck_contabo.api.subscriptions_api import SubscriptionsApi  # noqa: E501


class TestSubscriptionsApi(unittest.TestCase):
    """SubscriptionsApi unit test stubs"""

    def setUp(self):
        self.api = SubscriptionsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_windows(self):
        """Test case for activate_windows

        Activate the windows licence.  # noqa: E501
        """
        pass

    def test_cancel_subscription(self):
        """Test case for cancel_subscription

        Cancel the subscription.  # noqa: E501
        """
        pass

    def test_get_earliest_cancellation_date(self):
        """Test case for get_earliest_cancellation_date

        Get earliest cancellation date  # noqa: E501
        """
        pass

    def test_retrieve_subscription(self):
        """Test case for retrieve_subscription

        Retrieve specific subscription  # noqa: E501
        """
        pass

    def test_retrieve_subscriptions(self):
        """Test case for retrieve_subscriptions

        List all subscriptions by type  # noqa: E501
        """
        pass

    def test_revoke_subscription_cancellation(self):
        """Test case for revoke_subscription_cancellation

        Revoke cancellation  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()