from setuptools import setup

setup(
    name='cloudphoto',
    version='1.0',
    packages=['cloudphoto'],
    package_data={},
    install_requires=open('requirements.txt').read().splitlines(),
    entry_points={
        'console_scripts': ['cloudphoto = cloudphoto.cli:main']
    }
)
