# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install optima
#
# You can edit this file again by typing:
#
#     spack edit optima
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Optima(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/reaktoro/optima/archive/refs/tags/v0.5.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.5.0", sha256="7a93cb9fc98ed6a9c4a841c80579c03f7c1e773944ff5e765dbb7c486c85cc99")
    version("0.4.0", sha256="10e7e5130b4cbbbe78bb1f9bcfae38a31190b14706061284c58b0464bd0e0bd1")
    version("0.3.3", sha256="54124acaab897aa6a546697126f213f7edfc42e0248cc08f812fff8d42e3f42f")
    version("0.3.2", sha256="18ee17bbf44226cf9fa0fca2be8e9b497a61ba56cf9380df80aa47d7b43c87b0")
    version("0.3.1", sha256="52d32620090d9aeacb4a31ad1ce620d93df0ac54024905999c9876d29112aa0b")
    version("0.3.0", sha256="de9d1f7a1585ea5a870f8a610f40dec77e4646c6335851c9481deff44b3d88a8")
    version("0.2.15", sha256="aa866ac5424e038cdc1ad41ccaa1c61a58651d453aeeade6ebd371d2815cf1c9")
    version("0.2.14", sha256="aea8eb69181c43523ab0ef4823f52a1b23f33aa59a40b2168e2b11a9e794af95")
    version("0.2.13", sha256="aa4bb3eeb3ef2ed32e147d3d627ca3b4398663bf66e445bd59c8834d1cbba51a")
    version("0.2.12", sha256="19d016aabee363bcdbaa9fd974b23e603b9c12090091e7431a234679e0810213")

    # FIXME: Add dependencies if required.
    depends_on("catch2@3.0:")
    depends_on("eigen@3.4:")
    depends_on("py-pybind11")

    patch("python_executable.patch")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
