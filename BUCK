python_library(
    name = "lib",
    srcs = ["lib.py"],
    deps = ["pip//:torch"],
)

python_binary(
    name = "main",
    main = "main.py",
    deps = [":lib"],
)