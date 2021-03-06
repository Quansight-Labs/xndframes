#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import versioneer

with open("README.md", encoding="utf-8") as readme_file:
    readme = readme_file.read()


requirements = ["pandas>=0.23.0", "xnd"]

setup_requirements = ["pytest-runner"]

test_requirements = ["pytest"]

setup(
    maintainer="Anderson Banihirwe",
    maintainer_email="axbanihirwe@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description="Pandas ExtensionDType/Array backed by xnd",
    install_requires=requirements,
    license="BSD license",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords="xndframes",
    name="xndframes",
    packages=find_packages(include=["xndframes"]),
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/Quansight/xndframes",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    zip_safe=False,
)
