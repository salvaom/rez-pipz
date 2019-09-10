import sys
name = "pipz"
version = "1.1.10"
requires = ["python>=2,<4"]

tools = [
    "install",
    "search",
]

# Upon a new release of pip, wheel or setuptools, this is what you edit
build_command = " ".join([
    sys.executable, "{root}/install.py ",
    "--pip=19.1.1",
    "--wheel=0.33.4",
    "--setuptools=41.0.1",
    "--packaging=19.0",
])


def commands():
    global env

    env.PATH.prepend("{root}/bin")
    env.PYTHONPATH.prepend("{root}/python")
