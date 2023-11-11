# A simple prebuilt_python_library with no external dependencies.
remote_file(
    name = "requests-download",
    url = "https://files.pythonhosted.org/packages/51/bd/23c926cd341ea6b7dd0b2a00aba99ae0f828be89d72b2190f27c11d4b7fb/requests-2.22.0-py2.py3-none-any.whl",
    sha1 = "e1fc28120002395fe1f2da9aacea4e15a449d9ee",
    out = "requests-2.22.0-py2.py3-none-any.whl",
)

remote_file(
    name = "chardet-download",
    url = "https://files.pythonhosted.org/packages/38/6f/f5fbc992a329ee4e0f288c1fe0e2ad9485ed064cac731ed2fe47dcc38cbf/chardet-5.2.0-py3-none-any.whl",
    sha1 = "e1fc28120002395fe1f2da9aacea4e15a449d9e1",
    out = "chardet-5.2.0-py3-none-any.whl",
)

prebuilt_python_library(
    name = "requests",
    binary_src = ":requests-download",
    # deps = [":chardet"],
)

prebuilt_python_library(
    name = "chardet",
    binary_src = ":requests-download",
)

python_library(
    name = "lib",
    srcs = ["lib.py"],
    deps = [":requests"],
)

python_binary(
    name = "main",
    main = "main.py",
    deps = [":lib"],
)