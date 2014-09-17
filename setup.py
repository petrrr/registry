# Copyright (c) The University of Edinburgh 2014
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "dispel4py_registry",
    version = "0.0.1",
    author = "The University of Edinburgh",
    author_email = "a.krause@epcc.ed.ac.uk",
    description = ("The dispel4py_registry client provides commandline tools and helper methods to access a Dispel4Py registry."),
    license = "Apache 2",
    keywords = "dispel4py registry processing elements",
    url = "https://github.com/akrause2014/registry",
    packages=['dispel4py.registry'],
    entry_points={
        'console_scripts': ['idispel4py = dispel4py.registry.client:main']
    },
    install_requires=['requests'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2 License",
    ],
)
