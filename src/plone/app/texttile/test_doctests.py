import doctest
from plone.testing import layered
import unittest2 as unittest
from plone.app.texttile.tests.base import PASTANDARDTILES_FUNCTIONAL_TESTING, \
    PASTANDARDTILES_TESTTYPE_FUNCTIONAL_TESTING
import pprint
import interlude

optionflags = (doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE)
normal_testfiles = [
    '../text.txt',
]
testtype_testfiles = []


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite(test,
                                     optionflags=optionflags,
                                     globs={'interact': interlude.interact,
                                            'pprint': pprint.pprint,
                                            },
                                     ),
                layer=PASTANDARDTILES_FUNCTIONAL_TESTING)
        for test in normal_testfiles])
    suite.addTests([
        layered(doctest.DocFileSuite(test,
                                     optionflags=optionflags,
                                     globs={'interact': interlude.interact,
                                            'pprint': pprint.pprint,
                                            },
                                     ),
                layer=PASTANDARDTILES_TESTTYPE_FUNCTIONAL_TESTING)
        for test in testtype_testfiles])
    return suite
