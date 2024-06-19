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
#     spack install chemicalfun
#
# You can edit this file again by typing:
#
#     spack edit chemicalfun
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Chemicalfun(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/thermohub/chemicalfun/archive/refs/tags/v0.1.10.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.1.10", sha256="8948889cf3cce3f628eed04de9aa74ae8a0817ffa66d99ecb3867c644587e14f")
    version("0.1.9", sha256="3d5a7b22180a93b7fe566a10fa4cdaab47457193311c083aae4506079f6fe5c3")

    # FIXME: Add dependencies if required.
    # depends_on("foo")
    depends_on("python@3.11.9")
    depends_on("py-pybind11@2.12.0")
    depends_on("nlohmann-json@3.6:")
    depends_on("spdlog@1.11.0")
    depends_on("eigen@3.4.0")
    depends_on("py-pip")


    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
