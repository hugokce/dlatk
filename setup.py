try:
  from setuptools import setup
except ImportError:
  sys.exit("Need setuptools to install DLATK for Python 3.x")

DESCRIPTION = "DLATK is an end to end text analysis package developed by the World Well-Being Project at the University of Pennsylvania."
LONG_DESCRIPTION = """
DLATK v1.0
----------

This package offers end to end text analysis: feature extraction, correlation, 
mediation and prediction / classification. For more information please visit:

  * http://wwbp.org
  * http://dlatk.wwbp.org

CONTACT
-------

Please send bug reports, patches, and other feedback to

  Andy Schwartz (hansens@sas.upenn.edu) or Salvatore Giorgi (sgiorgi@sas.upenn.edu)

"""
DISTNAME = 'dlatk'
PACKAGES = ['dlatk',
  'dlatk.lib',
  'dlatk.LexicaInterface',
  'dlatk.mysqlMethods',
]
LICENSE = 'Creative Commons Attribution-NonCommercial-ShareAlike 3.0 United States License'
AUTHOR = "H. Andrew Schwartz, Salvatore Giorgi, Maarten Sap, Patrick Crutchley, Lukasz Dziurzynski and Megha Agrawal"
EMAIL = "hansens@sas.upenn.edu, sgiorgi@sas.upenn.edu"
MAINTAINER = "Salvatore Giorgi, Andy Schwartz, Patrick Crutchley"
MAINTAINER_EMAIL = "sgiorgi@sas.upenn.edu, hansens@sas.upenn.edu, pcrutchl@psych.upenn.edu"
URL = "http://dlatk.wwbp.org"
DOWNLOAD_URL = 'https://github.com/wwbp/dlatk'
CLASSIFIERS = [
  'Environment :: Console',
  'Natural Language :: English',
  'Intended Audience :: End Users/Desktop',
  'Intended Audience :: Developers',
  'Intended Audience :: Science/Research',
  'Programming Language :: Python',
  'Programming Language :: Python :: 2',
  'Programming Language :: Python :: 2.7',
  'Programming Language :: Python :: 3',
  'Programming Language :: Python :: 3.5',
  'Topic :: Scientific/Engineering',
]
VERSION = '1.0.dev4'
PACKAGE_DATA = {'dlatk': ['data/*.sql',
            'data/*.csv',],
}
INSTALL_REQUIRES = [
  'image',
  'matplotlib>=1.3.1', 
  'mysqlclient', 
  'nltk>=3.1', 
  'numpy', 
  'pandas>=0.17.1', 
  'patsy>=0.2.1', 
  'python-dateutil>=2.5.0', 
  'rpy2',
  'scikit-learn>=0.17.1', 
  'scipy>=0.13.3', 
  'SQLAlchemy>=0.9.9', 
  'statsmodels>=0.5.0', 
  'wordcloud>1.1.3', 
]

setup(name=DISTNAME,
      author=AUTHOR,
      author_email=EMAIL, 
      maintainer=MAINTAINER,
      maintainer_email=MAINTAINER_EMAIL,
      version=VERSION,
      packages=PACKAGES,
      package_data=PACKAGE_DATA,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      license=LICENSE,
      url=URL,
      download_url=DOWNLOAD_URL,
      classifiers=CLASSIFIERS,
      install_requires=INSTALL_REQUIRES,
)