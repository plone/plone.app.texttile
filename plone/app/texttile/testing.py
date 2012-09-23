import doctest

from zope.configuration import xmlconfig

from plone.testing import z2

from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing.layers import FunctionalTesting
from plone.app.testing.layers import IntegrationTesting


class PloneAppTexttileLayer(PloneSandboxLayer):

    def setUpZope(self, app, configurationContext):
        import plone.app.texttile
        xmlconfig.file('configure.zcml', plone.app.texttile,
                       context=configurationContext)
        z2.installProduct(app, 'plone.app.texttile')

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plone.app.texttile:default')

PLONE_APP_TEXTTILE_FIXTURE = PloneAppTexttileLayer()

PLONE_APP_TEXTTILE_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONE_APP_TEXTTILE_FIXTURE,),
    name="PloneAppTexttileLayer:Integration")
PLONE_APP_TEXTTILE_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONE_APP_TEXTTILE_FIXTURE,),
    name="PloneAppTexttileLayer:Functional")
PLONE_APP_TEXTTILE_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(PLONE_APP_TEXTTILE_FIXTURE, z2.ZSERVER_FIXTURE),
    name="PloneAppTexttileLayer:Acceptance")

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
