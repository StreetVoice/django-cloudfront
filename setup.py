from setuptools import setup

setup(
    name='django_cloudfront',
    version='0.1.1',
    description='cloudfront private content signing for django',
    url='http://github.com/tzangms/django_cloudfront',
    author='tzangms',
    author_email='tzangms@gmail.com',
    keywords='django cloudfront',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    license='MIT',
    packages=['cloudfront'],
    install_requires=[
        'pycrypto==2.6',
    ],
    zip_safe=False
)
