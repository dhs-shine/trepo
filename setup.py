#!/usr/bin/env python3
# Copyright 2017 Samsung Electronics Co., Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages

PROJECT_NAME = 'trepo'

setup(name=PROJECT_NAME,
      description='Tizen repo',
      long_description='Tizen repo is a wrapper of git-repo'
                       ' for tizen platform source management',
      version='0.1',
      author="Donghoon Shin",
      author_email="dhs.shin@samsung.com",
      url="http://www.tizen.org",
      package_dir={PROJECT_NAME: 'trepo'},
      packages=find_packages(exclude=['trepo/git-repo.git, \
                                       trepo/gbs.conf.template,\
                                       trepo/repo']),
      include_package_data=True,
      license="Apache",
      platforms='any',
      scripts=['bin/trepo'],
      )
