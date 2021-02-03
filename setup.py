#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
try:
    from pipenv.project import Project
    from pipenv.utils import convert_deps_to_pip

    pfile = Project().parsed_pipfile
    requirements = convert_deps_to_pip(pfile['packages'], r=False)
    test_requirements = convert_deps_to_pip(pfile['dev-packages'], r=False)
except ImportError:
    # get the requirements from the requirements.txt
    requirements = [line.strip()
                    for line in open('requirements.txt').readlines()
                    if line.strip() and not line.startswith('#')]
    # get the test requirements from the test_requirements.txt
    test_requirements = [line.strip()
                         for line in
                         open('dev-requirements.txt').readlines()
                         if line.strip() and not line.startswith('#')]

readme = open('README.rst').read()
history = open('HISTORY.rst').read().replace('.. :changelog:', '')
version = open('.VERSION').read()


setup(
    name='''outpost24hiabclient''',
    version=version,
    description='''Client for interacting with Outpost24 HIAB''',
    long_description=readme + '\n\n' + history,
    #long_description=readme + '\n\n' + history,
    author='''Theodoor Scholte''',
    author_email='''tscholte@schubergphilis.com''',
    url='''https://github.com/schubergphilis/outpost24hiabclient''',
    packages=find_packages(where='.', exclude=('tests', 'hooks')),
    package_dir={'''outpost24hiabclient_python''':
                 '''outpost24hiabclient_python'''},
    setup_requires=['nose>=1.0'],
    include_package_data=True,
    install_requires=requirements,
    license='MIT',
    zip_safe=False,
    keywords='''outpost24 HIAB API XML python''',
    entry_points={
                   'console_scripts': [
                       # enable this to automatically generate a script in /usr/local/bin called myscript that points to your
                       #  okta_python.okta_python:main method
                       # 'myscript = okta_python.okta_python:main'
                   ]},
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        ],
    test_suite='tests',
    tests_require=test_requirements,
    data_files=[('', ['.VERSION',
                      'LICENSE',
                      'AUTHORS.rst',
                      'CONTRIBUTING.rst',
                      'HISTORY.rst',
                      'README.rst',
                      'USAGE.rst',
                      'Pipfile',
                      'requirements.txt',
                      'dev-requirements.txt']),
                ]
)
