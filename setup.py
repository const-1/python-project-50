from setuptools import setup, find_packages

setup(
    name='gendiff',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'gendiff = gendiff.scripts.gendiff:main',
        ],
    },
)
