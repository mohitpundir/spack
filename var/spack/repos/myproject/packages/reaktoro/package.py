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
#     spack install reaktoro
#
# You can edit this file again by typing:
#
#     spack edit reaktoro
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Reaktoro(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/reaktoro/reaktoro/archive/refs/tags/v2.12.1.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("2.12.1", sha256="0fccdfdec8f1d76682ec61ab21347c33349ae9c20acac5ca74f019ce6e16350b")
    version("2.12.0", sha256="ad3a1549a4c63790e1b483db914c3ef4474bf215f9f332a03f1a0a0fb342b747")
    version("2.11.0", sha256="5d92b30ceabcea1fda3cd34ce5bb12b70105dbbeb3b9c2048471dec9c8aa0d7b")
    version("2.10.0", sha256="bf114be1c75c2254fcd66336f81c8d8f02b3f38d450fb74e27ce1f0837dd3afd")
    version("2.9.4", sha256="8125e4c165458a433c47325451c605ad12b74c362d88d1bc8c20e4ba7769d31d")
    version("2.9.3", sha256="047468c26b4fb97951a881b10850636ff2e013c7efa49f534d405b5136337fed")
    version("2.9.2", sha256="970b59fc55440f7688192dc2486e66fab50c7af7547ad3f921272e783ffcd19c")
    version("2.9.1", sha256="cfc2f9b8fd901116ddf853298166d84cd599526ee9eb1b124d1a143bdea8bae6")
    version("2.9.0", sha256="d7af8182d02aa490f04fd5a239c41bfee37035bd70741c57e44a0dccd65a3a38")
    version("2.8.2", sha256="095901497ef640d136f9f0f42b8ac2b4889ae488050eeebd22f1e2ccd9fa6e35")

    # FIXME: Add dependencies if required.
    depends_on("autodiff@1.1:", when="@2.12:")
    depends_on("catch2@2.0:")
    depends_on("eigen@3.4:")
    depends_on("py-pybind11")
    depends_on("nlohmann-json@3.11:")
    depends_on("tabulate@1.0:")
    depends_on("optima@0.5.0", when="@2.11:")
    depends_on("phreeqc4rkt")
    depends_on("thermofun@0.4.5")
    depends_on("ordered-map@1.0.0")

    patch("python_executable.patch")
    
    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
