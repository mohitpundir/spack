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
#     spack install phreeqc4rkt
#
# You can edit this file again by typing:
#
#     spack edit phreeqc4rkt
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Phreeqc4rkt(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/reaktoro/phreeqc4rkt/archive/refs/tags/v3.6.2.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("3.6.2.2", sha256="b1b81b030d051f796e82754ba979443e601a063f4b94a743b00ef4352404fa85")
    version("3.6.2.1", sha256="bbb86381bc01ec4376757b5c020134845de60012183906303de0b94db8427683")
    version("3.6.2.0", sha256="7ff98566664952d531c9eaf48cdd2271af62aa7590bb94497fedcffb92fb2378")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
