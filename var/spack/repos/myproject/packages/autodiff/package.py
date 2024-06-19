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
#     spack install autodiff
#
# You can edit this file again by typing:
#
#     spack edit autodiff
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class Autodiff(CMakePackage):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "https://www.example.com"
    url = "https://github.com/autodiff/autodiff/archive/refs/tags/v1.1.2.tar.gz"

    # FIXME: Add a list of GitHub accounts to
    # notify when the package is updated.
    # maintainers("github_user1", "github_user2")

    # FIXME: Add the SPDX identifier of the project's license below.
    # See https://spdx.org/licenses/ for a list. Upon manually verifying
    # the license, set checked_by to your Github username.
    license("UNKNOWN", checked_by="github_user1")

    version("1.1.2", sha256="86f68aabdae1eed214bfbf0ddaa182c78ea1bb99e4df404efb7b94d30e06b744")
    version("1.1.1", sha256="05aa2a432c83db079efeca1c407166a3f3d190645bd3202da3b6357fb30fc9e1")
    version("1.1.0", sha256="a5489bb546c460af52de8ead447439b3c97429184df28b4d142ce7dcfd62b82c")
    version("1.0.3", sha256="21b57ce60864857913cacb856c3973ae10f7539b6bb00bcc04f85b2f00db0ce2")
    version("1.0.2", sha256="a3289aed937a39a817f76e6befa0d071a3e70a5b0b125ec62d1acf1d389e2197")
    version("1.0.1", sha256="63f2c8aaf940fbb1d1e7098b1d6c08794da0194eec3faf773f3123dc7233838c")
    version("1.0.0", sha256="112c6f5740071786b3f212c96896abc2089a74bca16b57bb46ebf4cec79dca43")
    version("0.6.12", sha256="3e9d667b81bba8e43bbe240a0321e25f4be248d1761097718664445306882dcc")
    version("0.6.11", sha256="ac7a52387a10ecb8ba77ce5385ffb23893ff9a623467b4392bd204422a3b5c09")
    version("0.6.10", sha256="d6bc2f44cab5fd132deabdcb2a9e914b4959660c80a40a2c3f20dde79fc113d9")

    # FIXME: Add dependencies if required.
    depends_on("catch2@3.0:")
    depends_on("eigen@3.4:")
    depends_on("py-pybind11")

    patch('python_executable_file.patch', when='@1.0:')


    def cmake_args(self):
        # FIXME: Add arguments other than
        # FIXME: CMAKE_INSTALL_PREFIX and CMAKE_BUILD_TYPE
        # FIXME: If not needed delete this function
        args = []
        return args
