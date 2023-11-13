python_library(
    name = "lib",
    srcs = ["lib.py"],
    deps = ["pip//:torch"],
)

python_test(
    name = "main",
    srcs = [
        "main.py",
        "test2.py",
    ],
    deps = [":lib"],
)