# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.rfd16.testing import PLONETHEME_RFD16_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.rfd16 is properly installed."""

    layer = PLONETHEME_RFD16_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.rfd16 is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.rfd16'))

    def test_browserlayer(self):
        """Test that IPlonethemeRfd16Layer is registered."""
        from plonetheme.rfd16.interfaces import (
            IPlonethemeRfd16Layer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeRfd16Layer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_RFD16_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.rfd16'])

    def test_product_uninstalled(self):
        """Test if plonetheme.rfd16 is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.rfd16'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeRfd16Layer is removed."""
        from plonetheme.rfd16.interfaces import IPlonethemeRfd16Layer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeRfd16Layer, utils.registered_layers())
