import os
from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()

PACKAGE_NAME = 'ha-beoplay'
HERE = os.path.abspath(os.path.dirname(__file__))
VERSION = '0.0.7'

PACKAGES = find_packages(exclude=['tests', 'tests.*', 'dist', 'ccu', 'build'])

REQUIRES = []

setup(
        name=PACKAGE_NAME,
        version=VERSION,
        license='MIT License',
        url='https://github.com/martonborzak/ha-beoplay',
        download_url='https://github.com/martonborzak/ha-beoplay/tarball/'+VERSION,
        author='Marton Borzak',
        author_email='hello@martonborzak.com',
        description='BeoPlay API for Home-Assistant',
        packages=PACKAGES,
        include_package_data=True,
        zip_safe=False,
        platforms='any',
        install_requires=REQUIRES,
        keywords=['beoplay'],
        classifiers=[
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python :: 3.4'
        ],
)
