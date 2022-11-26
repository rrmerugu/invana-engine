#!/usr/bin/env python

from setuptools import setup, find_packages
from invana_engine.settings import __VERSION__


setup(
    name='invana-engine',
    version=__VERSION__,
    description='GraphQL API and Insights engine for Apache TinkerPop supported graph databases.',
    author='Ravi Raja Merugu',
    author_email='ravi@invana.io',
    url='https://github.com/invanalabs/invana-engine',
    packages=find_packages(
        exclude=("dist", "docs", "tests", "scripts", "experiments")
    ),
    install_requires=[
        'gremlinpython==3.4.6',
        'starlette==0.13.8',
        'graphene==2.1.8',
        'uvicorn==0.12.2',
        'jinja2==2.11.2',
        'aiofiles==0.6.0'
    ],
    entry_points={
        'console_scripts': [
            'invana-engine-start = invana_engine.server.server:server_start',
        ]
    },
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 3 - Alpha',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
