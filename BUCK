python_library(
    name = "lib",
    srcs = ["lib.py"],
    deps = ["pip//:requests"],
)

python_binary(
    name = "main",
    main = "main.py",
    deps = [":lib"],
)