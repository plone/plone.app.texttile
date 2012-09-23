# -*- coding: utf-8 -*-
from zope.component import queryUtility
import unittest2 as unittest

from plone.tiles.interfaces import ITileType

from plone.app.texttile.testing import \
    PLONE_APP_TEXTTILE_INTEGRATION_TESTING

from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, \
    setRoles, login


class PloneAppTexttileIntegrationTest(unittest.TestCase):

    layer = PLONE_APP_TEXTTILE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)

    def test_view_registration(self):
        pass

    def test_edit_view_registration(self):
        pass

    def test_view(self):
        pass

    def test_edit_view(self):
        pass

    def test_tile_registration(self):
        import pdb; pdb.set_trace()
        tile_info = queryUtility(ITileType, name='plone.app.texttile')

    def test_add_tile(self):
        #browser.open(pageURL + '/@@plone.app.texttile.text')
        #browser.getControl('Save').click()
        pass

    def test_view(self):
        #unprivileged_browser.open(pageURL + '/@@plone.app.standardtiles.text')
        pass

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
