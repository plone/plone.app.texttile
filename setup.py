from setuptools import setup, find_packages

version = '1.0'
tests_require = [
    'plone.app.testing',
]

setup(
    name='plone.app.texttile',
    version=version,
    description="Text tile for Deco UI",
    long_description=open('README.rst').read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
    keywords='plone deco tile',
    author='Rok Garbas',
    author_email='rok@garbas.si',
    url='https://github.com/plone/plone.app.texttile',
    license='GPL',
    packages=find_packages(),
    namespace_packages=['plone', 'plone.app'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
        'zope.schema',
        'zope.i18nmessageid',
        'plone.directives.form',
        'plone.tiles',
        'plone.app.z3cform',
        'plone.app.deco',
    ],
    tests_require=tests_require,
    extras_require=dict(test=tests_require),
    entry_points="""
        [z3c.autoinclude.plugin]
        target = plone
        """,
    )
