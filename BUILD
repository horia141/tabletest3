py_library(
    name = "tabletest3",
    srcs = ["tabletest3/__init__.py"],
    srcs_version = "PY3",
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
      "tabletest3/__init__.py",
    ],
    size = "small",
    srcs_version = "PY3",
    default_python_version = "PY3",
)