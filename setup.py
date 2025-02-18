# setup.py
from setuptools import setup, find_packages

setup(
    name='py-gist',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'py-gist=main:main',
        ],
    },
    install_requires=[],
    author='dave-ops',
    author_email='daveops@codeforge.cc',
    description='A tool to convert a private GitHub repo into a secret Gist repo',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dave-ops/py-gist',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)