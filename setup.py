#!/usr/bin/env python

# Author: Hubert Kario
# Released under Gnu GPL v2.0, see LICENSE file for details

from setuptools import setup

setup(name="tlsfuzzer",
      version="0.0.1",
      author="Hubert Kario",
      author_email="hkario@redhat.com",
      url="https://github.com/tlsfuzzer/tlsfuzzer",
      description="TLS test suite and fuzzer.",
      license="GPLv2",
      install_requires=["tlslite-ng==0.8.0-beta5"],
      extras_require={"fastcrypto": ["m2crypto", "gmpy"]},
      packages=["tlsfuzzer", "tlsfuzzer.utils"])
