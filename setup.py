import os
from setuptools import setup, find_packages
from imp import load_source

version = load_source("version", os.path.join("stallion", "version.py"))

CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: Apache Software License',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Topic :: Internet',
    'Topic :: Utilities',
    'Topic :: Software Development :: Libraries :: Python Modules']

description = "Html Content / Article Extractor, web scrapping"

# read long description
try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as f:
        long_description = f.read()
except:
    long_description = description

setup(name='stallion-extractor',
      version=version.__version__,
      description=description,
      long_description=long_description,
      keywords='scrapping, extractor, web scrapping',
      classifiers=CLASSIFIERS,
      author='Galen Wang',
      url='https://git.rtbasia.com/galen/python_stallion',
      license='Apache',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=['lxml', 'request'],
      test_suite="tests"
      )
