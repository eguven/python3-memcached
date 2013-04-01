#!/usr/bin/env python

from setuptools import setup
import memcache

setup(name="python3-memcached",
      version=memcache.__version__,
      description="Pure python memcached client",
      long_description=open("README").read(),
      author="Evan Martin",
      author_email="martine@danga.com",
      maintainer="Eren Guven",
      maintainer_email="erenguven0@gmail.com",
      url="https://github.com/eguven/python3-memcached",
      py_modules=["memcache"],
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Python Software Foundation License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.1",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ])

