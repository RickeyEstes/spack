# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class PyMorphio(PythonPackage):
    """Python library for reading / writing morphology files"""

    homepage = "https://github.com/BlueBrain/MorphIO/"
    git      = "git@github.com:BlueBrain/MorphIO.git"

    version('develop', branch='master', submodules=True)
    version('2.0.5', commit='4275313b723d1207918a160896bf3ab6cfb9b7ce', submodules=True, preferred=True)

    depends_on('py-setuptools', type='build')

    depends_on('cmake@3.2:', type='build')
    depends_on('py-numpy', type='run')
    depends_on('hdf5~mpi', type=('build', 'run'))
