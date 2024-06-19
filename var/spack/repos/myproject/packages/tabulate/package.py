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
#     spack install tabulate
#
# You can edit this file again by typing:
#
#     spack edit tabulate
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Tabulate(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/p-ranav/tabulate/archive/refs/tags/v1.5.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.5", sha256="16b289f46306283544bb593f4601e80d6ea51248fde52e910cc569ef08eba3fb")
    version("1.4", sha256="c20cdc3175526a069e932136a7cbdf6f27b137bdb4fc5f574eb5a497228c8e11")
    version("1.3", sha256="d1739e82f9f5acab084a5166a78714fde5198ce6b9448ec8ae8e403085048f7e")
    version("1.2", sha256="c1e1407f9cc7639ba4b6c2906c64ea35c5a9ee6d6bd71afcfb8aa44e7468a2f7")
    version("1.1", sha256="95b1e68e6e3e4300437bf239d407f81afd2ccf7c88383f789962ad7e88c4db53")
    version("1.0", sha256="34eda3605e2ce0c7ca339fa2af6a0c77a5e49321b2f549ff5313f955273c8ac8")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
