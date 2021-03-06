# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack import *


class PyMorphologyRepairWorkflow(PythonPackage):
    """Python library neuron morphology analysis"""

    homepage = "https://bbpcode.epfl.ch/code/#/admin/projects/nse/morphology-repair-workflow"
    git      = "ssh://bbpcode.epfl.ch/nse/morphology-repair-workflow"
    version('develop', branch='master')
    version('1.0.4', tag='morphology-repair-workflow-v1.0.4')
    version('1.0.3', tag='morphology-repair-workflow-v1.0.3')

    depends_on('py-setuptools', type=('build', 'run'))

    depends_on('py-neuroc', type='run')
    depends_on('py-morph-tool', type='run')
    depends_on('py-neuror', type='run')
