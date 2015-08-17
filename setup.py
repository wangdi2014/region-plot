#!/usr/bin/env python

# How to build source distribution
# python setup.py sdist --format bztar
# python setup.py sdist --format gztar
# python setup.py sdist --format zip


import os
from setuptools import setup


MAJOR = 0
MINOR = 1
MICRO = 0
VERSION = "{}.{}.{}".format(MAJOR, MINOR, MICRO)


def write_version_file(fn=None):
    if fn is None:
        fn = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            os.path.join("region_plot", "version.py"),
        )

    content = ("\n# THIS FILE WAS AUTOMATICALLY GENERATED BY POST_GWAS SETUP\n"
               'region_plot_version = "{version}"\n')

    a = open(fn, "w")
    try:
        a.write(content.format(version=VERSION))
    finally:
        a.close()


def setup_package():
    # Saving the version into a file
    write_version_file()

    setup(
        name="region-plot",
        version=VERSION,
        description="Plots significant regions of GWAS.",
        author="Louis-Philippe Lemieux Perreault",
        author_email="louis-philippe.lemieux.perreault@statgen.org",
        url="http://www.statgen.org",
        license="CC BY-NC 4.0",
        entry_points={
            "console_scripts": [
                "launch-region-plot=region_plot.cli:main",
            ],
        },
        packages=["region_plot"],
        install_requires=["numpy >= 1.9.1", "pandas >= 0.15.0", "six >= 1.9.0",
                          "matplotlib >= 1.4.3", "gepyto >= 0.9.2"],
        classifiers=[
            "Intended Audience :: Science/Research",
            "License :: Free for non-commercial use",
            "Operating System :: Unix",
            "Operating System :: POSIX :: Linux",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Programming Language :: Python",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Topic :: Scientific/Engineering :: Bio-Informatics",
        ],
    )

    return


if __name__ == "__main__":
    setup_package()
