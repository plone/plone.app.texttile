# -*- coding: utf-8 -*-
from zope.component import queryUtility
from zope.component import getMultiAdapter

import unittest2 as unittest

from plone.tiles.interfaces import ITileType

from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, \
    setRoles, login

from plone.app.texttile.tile import ITextTile

from plone.app.texttile.testing import \
    PLONE_APP_TEXTTILE_INTEGRATION_TESTING


class PloneAppTexttileIntegrationTest(unittest.TestCase):

    layer = PLONE_APP_TEXTTILE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        login(self.portal, TEST_USER_NAME)
        self.portal.invokeFactory('Document', 'doc')
        self.doc = self.portal.doc

    def test_tile_registration(self):
        tile = queryUtility(ITileType, name='plone.app.texttile')
        self.assertEqual(tile.title, u"Text tile")
        self.assertEqual(tile.schema, ITextTile)

    def test_add_tile(self):
        #view = getMultiAdapter(
        #    (self.portal, self.portal.REQUEST),
        #    name='plone.app.texttile')
        view = self.doc.restrictedTraverse('@@add-tile/plone.app.texttile')
        self.assertEqual(view())
        #browser.open(pageURL + '/@@plone.app.texttile.text')
        #browser.getControl('Save').click()

    def test_view_registration(self):
        view = self.doc.restrictedTraverse('@@edit-tile/plone.app.texttile/1')
        self.assertEqual(view())
        # This works:
        #http://localhost:8080/Plone/@@edit-tile/plone.app.texttile/1

    def test_edit_view_registration(self):
        pass

    def test_view(self):
        view = getMultiAdapter(
            (self.portal, self.portal.REQUEST),
            name='plone.app.texttile')
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_edit_view(self):
        pass


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
