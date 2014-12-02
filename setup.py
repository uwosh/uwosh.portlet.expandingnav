from setuptools import setup, find_packages
import os

version = '.0.1'

setup(name='uwosh.portlet.expandingnav',
      version=version,
      description="An expadning navigation that uses javascript animations",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='navigation expanding expand animate',
      author='Justin Fisher',
      author_email='webmaster@mio.uwosh.edu',
      url='http://mio.uwosh.edu',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['uwosh', 'uwosh.portlet'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
