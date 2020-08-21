import setuptools
import os

pkg_vars = {}
pkg_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(pkg_dir, "stream_repeater", "_version.py"), "r") as fh:
    exec(fh.read(), pkg_vars)

with open(os.path.join(pkg_dir, "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stream_repeater",
    version=pkg_vars['__version__'],
    author="FrozenFOXX",
    author_email="frozenfoxx@churchoffoxx.net",
    description="Converts and uploads saved streams to remote platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frozenfoxx/stream_repeater",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Apache License v2",
        "Operating System :: OS Independent",
    ],
    install_requires=[],
    scripts=[
        "scripts/stream_repeater",
    ],
    entry_points = {
        "console_scripts": ["stream_repeater=stream_repeater.stream_repeater:main"],
    },
    data_files=[
        ('/etc/stream_repeater', ['conf/stream_repeater.yaml'])
    ],
    include_package_data=True,
)

