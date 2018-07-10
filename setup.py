from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(name='necapy',
    version='0.1.3',
    description='Nested command-line arguments made easy.',
    long_description = long_description,
    url='https://github.com/dbadrian/necapy',
    author='David B. Adrian',
    author_email='dawidh.adrian@googlemail.com',
    license='MIT',
    packages=['necapy'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Console',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='nested command-line arguments',
    project_urls={
        'Documentation': 'https://github.com/dbadrian/necapy/blob/master/README.md',
        'Source': 'https://github.com/dbadrian/necapy',
        'Tracker': 'https://github.com/dbadrian/necapy/issues',
    },
    zip_safe=False,
    test_suite="tests",
    )
