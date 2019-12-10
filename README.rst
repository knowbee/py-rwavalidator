rwavalidator
=======================

A fast minimal package to validate Rwandan National Ids and Phone Numbers(all carriers) using Regular Expressions.

Installation
------------

The distribution is hosted on pypi at: https://pypi.org/project/rwavalidator/. To directly install the package from pypi, run from your terminal::

    $ pip install rwavalidator

Usage
----------- 

Validating Phone Numbers
=========================

.. code-block :: python

   from rwavalidator import (isPhoneNumber, isNationalId)
   
   isPhoneNumber("0788854444"); # true
   isPhoneNumber("0778854444"); # false

Validating National ID
=======================

.. code-block :: python
   
   isNationalId("1199672222000040"); # true
   isNationalId("1201772222000040"); # false

