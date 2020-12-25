# rwavalidator

[![Downloads](https://pepy.tech/badge/rwavalidator)](https://pepy.tech/project/rwavalidator)
[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)
[![Open Source Love](https://badges.frapsoft.com/os/mit/mit.svg?v=102)](https://github.com/ellerbrock/open-source-badge/)

A fast minimal package to validate Rwandan National Ids and Phone Numbers(all carriers) using Regular Expressions.

## Installation

The distribution is hosted on pypi at: https://pypi.org/project/rwavalidator/. To directly install the package from pypi, run from your terminal::

    $ pip install rwavalidator

Usage

---

# Validating Phone Numbers

```py

from rwavalidator import (isPhoneNumber, isNationalId)

isPhoneNumber("0788854444"); # true
isPhoneNumber("0778854444"); # false

```

# Validating National ID

```py

isNationalId("1199672222000040"); # true
isNationalId("1201772222000040"); # false
```
