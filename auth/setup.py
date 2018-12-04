import io

from setuptools import find_packages, setup

with io.open('README.md', 'rt', encoding='utf8') as f:
    readme = f.read()

setup(
    name='notes',
    version='0.0.1',
    url='http://www.example.com',
    license='MIT',
    maintainer='Leonardo Fleury',
    maintainer_email='fleuryleomoraes@gmail.com',
    description='Do auth',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pymongo',
        'nameko',
        'pyjwt',
        'bcrypt',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
            'pylint',
            'autopep8',
        ],
    },
)
