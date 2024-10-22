from setuptools import setup, find_packages

setup(
    name='ee_automation',
    version='0.1',
    packages=find_packages(), # Automatically finds all packages
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
        'sympy',
    ],
)