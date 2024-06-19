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
#     spack install thermofun
#
# You can edit this file again by typing:
#
#     spack edit thermofun
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Thermofun(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/thermohub/thermofun/archive/refs/tags/v0.4.5.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("0.4.5", sha256="90519474d54ff91de61172cab0169c8a26a3dc7e2b0b6345237ed0d4e9787b30")
    version("0.4.4", sha256="d5ca71461eeeb7e2343bad15131d7d5c0a271d495f869243b28677f82386ee6d")
    version("0.4.3", sha256="76c02ba5c0f417e14153ffa98004190d20bc1c526f7b5c43e2237fb649940e3c")
    version("0.4.2", sha256="977990f17fa1b54b7acfa3e4bc0d084b7b2f6b0598d0fb58a68b7ab5fffa74b2")
    version("0.4.1", sha256="4f0cf27876a18e9be1c0d882b1ec0a031c41c29d6b6cb541f058ea9be958c2a0")
    version("0.4.0", sha256="a94946338a86e76eda91877631bcf4c23d42ba2b58c18821a86aeb7339564106")
    version("0.3.9", sha256="49995b3a139e7ed93d2bf6ab09a316459bca809cf3f612878c9fa017befaf913")
    version("0.3.8", sha256="1daffed5ca3b6187548729da9884f63c76c02af4dd6cb7e649a898b016353c6f")
    version("0.3.7", sha256="0cf7c9c09e83f56d6d0b43e1c57bc1e1595a6002e87cd2ccf3ec519f2be5323c")
    version("0.3.6", sha256="083e55f1c142344870de9fe9638e5d14e541f33cf0968b681f1ee857ea2e17a0")

    # FIXME: Add dependencies if required.
    depends_on("chemicalfun")
    depends_on("nlohmann-json@3.6:")
    depends_on("spdlog@1.11.0")
    depends_on("eigen@3.4.0")
    depends_on("py-pybind11@2.12.0")


    
    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
