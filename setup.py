#!/usr/bin/env python

from setuptools import setup

setup(
    name='django-affect',
    version='1.5.0',
    description='Request flagging engine inspired by django-waffle',
    author='Jeremy Sattefield',
    author_email='jsatt@jsatt.com',
    url='https://github.com/jsatt/django-affect',
    #license='',
    packages=[
        'affect', 'affect.migrations'],
    install_requires=[
        'Django>=1.8',
        'django-extensions'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Site Management'],
)
