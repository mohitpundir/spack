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
#     spack install ordered-map
#
# You can edit this file again by typing:
#
#     spack edit ordered-map
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class OrderedMap(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/Tessil/ordered-map/archive/refs/tags/v1.1.0.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.1.0", sha256="d6070502351646d68f2bbe6078c0da361bc1db733ee8a392e33cfb8b31183e28")
    version("1.0.0", sha256="49cd436b8bdacb01d5f4afd7aab0c0d6fa57433dfc29d65f08a5f1ed1e2af26b")
    version("0.8.1", sha256="620772eed53e54ca2c5fdaf3e7653d79d9531df39696790146679a1e1ce80452")
    version("0.8.0", sha256="a7c721b84029f1fdbbaf1b5c9647c58765886a7b39db0e4b1c61b1ef075bde43")
    version("0.7.1", sha256="8ca0979a6063c36976dfb9abf308a1402ce59fe52574f553b59e2a1337cb9447")
    version("0.7.0", sha256="e98ff5afde7ab0b505c514d4bb00e8fcade8a3f2b866112204403015bc8d54a0")
    version("0.6.0", sha256="53e50d7f9d9ba55614bac3921013ada3f9fde531482874923bef23b2c6eb7c54")
    version("0.5.0", sha256="aa459f3ce9be94c129cfabc56b8215a76c267689803a6627eb44c99d5ad6897d")
    version("0.4.0", sha256="7a170f1fe56db0ac7be6148147eae4363b2367bd8a8e8aaead170e15719d5a12")
    version("0.3.0", sha256="aac08d309ac8bf262a5edf2bff2789b970640633998c1113dbc70a07d9ad923e")

    # FIXME: Add dependencies if required.
    # depends_on("foo")

    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
