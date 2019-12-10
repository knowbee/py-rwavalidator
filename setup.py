#!/usr/bin/env python
from setuptools import setup                                      
from os import path                                               
here = path.abspath(path.dirname(__file__))                       
                                                                  
# Get the long description from the README file                   
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:  
    long_description = f.read()                                   

setup(
  name="rwavalidator",
  version='0.0.2',
  description="A fast minimal package to validate Rwandan National Ids and Phone Numbers(all carriers) using Regular Expressions.",
  long_description=long_description,
  py_modules=["rwavalidator"],
  package_dir={'.': 'rwavalidator'},
  keywords=['rwanda', 'validator', 'rwavalidator', 'validate', 'id'],
  python_requires=">=3.6",
  classifiers=[
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.7",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "License :: OSI Approved :: GNU General Public License (GPL)",
            "Operating System :: OS Independent",
      ],
      author='Igwaneza Bruce',
      author_email='knowbeeinc@gmail.com',
      license='MIT',
      zip_safe=False,

)
