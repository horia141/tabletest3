load("/tools/pypi_package", "pypi_package")

py_library(
    name = "tabletest3",
    srcs = ["tabletest3/__init__.py"],
)

# TODO(horia141): This rule is badly written. It references "tabletest3/__init__.py" directly,
# instead of through the "tabletest3" dependency. There seems to be a bug in Bazel, where it
# doesn't properly pick up the fact that both rules are for Python 3 and should work without
# inovking 2to3.
py_test(
    name = "tabletest3_test",
    main = "tests/test_tabletest3.py",
    srcs = [
      "tests/__init__.py",
      "tests/test_tabletest3.py",
    ],
    deps = [":tabletest3"],
    size = "small",
    srcs_version = "PY3",
    default_python_version = "PY3",
)

pypi_package(
    name = "tabletest3_pkg",
    version = "1.0.3",
    description = "Unit testing module for table-like test, for Python 3.",
    long_description = "README.md",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    keywords = "unittest test table testing",
    url = "http://github.com/horia141/tabletest3",
    author = "Horia Coman",
    author_email = "horia141@gmail.com",
    license = "MIT",
    packages = [":tabletest3"],
    test_suite = "nose.collector",
    tests_require = ["nose"],
)
