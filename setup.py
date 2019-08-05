#!/usr/bin/env python
# Copyright 2019, Oath Inc.
# Licensed under the terms of the Apache 2.0 license.  See the LICENSE file in the project root for terms
"""
Package setup file for python module ouroath.screwdrivercd
"""
import setuptools
import sys


def setuptools_version_supported():
    major, minor, patch = setuptools.__version__.split('.')
    if int(major) > 38:
        return True
    return False
        

if __name__ == '__main__':
    # Check for a working version of setuptools here because earlier versions did not
    # support python_requires.
    if not setuptools_version_supported():
        print('Setuptools version 38.0.0 or higher is needed to install this package')
        sys.exit(1)

    # We're being run from the command line so call setup with our arguments
    setuptools.setup()
