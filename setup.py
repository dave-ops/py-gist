from setuptools import setup, find_packages

setup(
    name='py-gist',
    version='0.1',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'py-gist=src.main:main',
        ],
    },
    author='Your Name',
    description='Upload files to GitHub Gist',
    long_description=open('docs/README.md').read(),
    long_description_content_type="text/markdown",
)
