# Copyright 2013-2019 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class Adlbx(AutotoolsPackage):
    """ADLB/X: Master-worker library + work stealing and data dependencies"""

    homepage = 'http://swift-lang.org/Swift-T'
    url      = 'http://swift-lang.github.io/swift-t-downloads/spack/adlbx-0.0.0.tar.gz'
    git      = "https://github.com/swift-lang/swift-t.git"

    version('master', branch='master')
    version('0.9.2', sha256='524902d648001b689a98492402d754a607b8c1d0734699154063c1a4f3410d4a')
    version('0.9.1', sha256='8913493fe0c097ff13c721ab057514e5bdb55f6318d4e3512692ab739c3190b3')

    depends_on('exmcutils@master', when='@master')
    depends_on('exmcutils@:0.5.3', when='@:0.8.0')
    depends_on('exmcutils', when='@0.9.1:')
    depends_on('autoconf', type='build', when='@master')
    depends_on('automake', type='build', when='@master')
    depends_on('libtool', type='build', when='@master')
    depends_on('m4', type='build', when='@master')
    depends_on('mpi')

    def setup_environment(self, spack_env, run_env):
        spec = self.spec
        spack_env.set('CC', spec['mpi'].mpicc)
        spack_env.set('CXX', spec['mpi'].mpicxx)
        spack_env.set('CXXLD', spec['mpi'].mpicxx)

    @property
    def configure_directory(self):
        if self.version == Version('master'):
            return 'lb/code'
        else:
            return '.'

    def configure_args(self):
        args = ['--with-c-utils=' + self.spec['exmcutils'].prefix]
        return args
