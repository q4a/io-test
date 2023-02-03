from conans import ConanFile, tools
from os import getenv
from random import getrandbits
from distutils.dir_util import copy_tree

class SdlPure(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    # dependencies used in deploy binaries
    requires = ["libsafec/3.6.0"] # conan-center

    generators = "cmake_multi"
