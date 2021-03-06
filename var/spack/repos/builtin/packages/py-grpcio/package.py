# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyGrpcio(PythonPackage):
    """Package for gRPC Python"""

    homepage = "https://pypi.org/project/grpcio/"
    url      = "https://github.com/grpc/grpc/archive/v1.16.0.tar.gz"

    version('1.16.0', sha256='d99db0b39b490d2469a8ef74197d5f211fa740fc9581dccecbb76c56d080fce1')

    depends_on('cares', type=('build', 'run'))
    depends_on('zlib', type=('build', 'run'))
    depends_on('openssl@1.0.2:', type=('build', 'run'))
    depends_on('py-setuptools', type='build')
    depends_on('py-six@1.10:', type=('build', 'run'))
    depends_on('py-futures@2.2.0:', type=('build', 'run'), when='^python@2.7.0:2.7.999')
    depends_on('py-enum34@1.0.4:', type=('build', 'run'), when='^python@:3.1')
    depends_on('py-sphinx@1.3:', type=('build', 'run'))
    depends_on('py-sphinx-rtd-theme@0.1.8:', type=('build', 'run'))
    depends_on('py-cython@0.23:', type=('build', 'run'))

    def setup_build_environment(self, env):
        env.set('GRPC_PYTHON_BUILD_WITH_CYTHON', '1')
        env.set('GRPC_PYTHON_BUILD_SYSTEM_OPENSSL', '1')
        env.set('GRPC_PYTHON_BUILD_SYSTEM_ZLIB', '1')
        env.set('GRPC_PYTHON_BUILD_SYSTEM_CARES', '1')
        env.append_flags('LDFLAGS', self.spec['cares'].libs.search_flags)
        env.append_flags(
            'CFLAGS',
            '-I{0}'.format(self.spec['cares'].prefix.include)
        )
        env.append_flags('LDFLAGS', self.spec['zlib'].libs.search_flags)
