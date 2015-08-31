from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='tabletest3',
    version='1.0.2',
    description='Unit testing module for table-like test, for Python 3.',
    long_description=readme(),
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords='unittest test table testing',
    url='http://github.com/horia141/tabletest3',
    author='Horia Coman',
    author_email='horia141@gmail.com',
    license='MIT',
    packages=[
        'tabletest3',
    ],
    zip_safe=False,
    test_suite='nose.collector',
    tests_require=['nose'],
)
