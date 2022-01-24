import setuptools
import os

pkg_vars = {}
pkg_dir = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(pkg_dir, "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="stream_repeater",
    version='0.1.0',
    author="FrozenFOXX",
    author_email="frozenfoxx@churchoffoxx.net",
    description="Converts and uploads saved streams to remote platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/frozenfoxx/stream_repeater",
    download_url = 'https://github.com/frozenfoxx/stream_repeater/archive/refs/tags/0.1.0.tar.gz',
    packages=["stream_repeater"],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'flask'
    ],
    entry_points = {
        "console_scripts": ["stream_repeater=stream_repeater.stream_repeater:main"],
    },
    data_files=[
        ('/etc/stream_repeater', ['conf/stream_repeater.yaml'])
    ],
)

