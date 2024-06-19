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
#     spack install my-spdlog
#
# You can edit this file again by typing:
#
#     spack edit my-spdlog
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class MySpdlog(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/gabime/spdlog/archive/refs/tags/v1.14.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.14.1", sha256="1586508029a7d0670dfcb2d97575dcdc242d3868a259742b69f100801ab4e16b")
    version("1.14.0", sha256="429a6b73ade8285cb21f83bacf89e2821dd1720ea7faa3cb518ffe04b4e00efc")
    version("1.13.0", sha256="534f2ee1a4dcbeb22249856edfb2be76a1cf4f708a20b0ac2ed090ee24cfdbc9")
    version("1.12.0", sha256="4dccf2d10f410c1e2feaff89966bfc49a1abb29ef6f08246335b110e001e09a9")
    version("1.11.0", sha256="ca5cae8d6cac15dae0ec63b21d6ad3530070650f68076f3a4a862ca293a858bb")
    version("1.10.0", sha256="697f91700237dbae2326b90469be32b876b2b44888302afbc7aceb68bcfe8224")
    version("1.9.2", sha256="6fff9215f5cb81760be4cc16d033526d1080427d236e86d70bb02994f85e3d38")
    version("1.9.1", sha256="9a452cfa24408baccc9b2bc2d421d68172a7630c99e9504a14754be840d31a62")
    version("1.9.0", sha256="9ad181d75aaedbf47c8881e7b947a47cac3d306997e39de24dba60db633e70a7")
    version("1.8.5", sha256="944d0bd7c763ac721398dca2bb0f3b5ed16f67cef36810ede5061f35a543b4b8")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
