from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'DESCRIPTION.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='jobber',
    version='0.0.1',
    description='misc tools',
    long_description=long_description,
    url='https://github.com/immanetize/jobber',
    author='Pete Travis',
    author_email='me@petetravis.com',
    license='GPLv3+',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Documentation',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
 #       'Programming Language :: Python :: 3',
 #       'Programming Language :: Python :: 3.2',
 #       'Programming Language :: Python :: 3.3',
 #       'Programming Language :: Python :: 3.4',
    ],
    keywords='documentation, buildbot',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    install_requires=[
#            'buildbot',
            ],
    entry_points={
        'console_scripts': [
            'jobber = jobber.cli:main',
        ],
    },
)
