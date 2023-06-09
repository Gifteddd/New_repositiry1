from setuptools import find_packages, setup

setup(
    name= 'mylibrary',
    packages= find_packages(include='mylibrary'),
    version='0.0.1',
    description= 'My python library',
    author='Me',
    license='MTI',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require= ['pytest==4.4.1'],
    test_suite= 'tests',
)