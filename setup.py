import distutils.core
import os
import sys

with open('README.md') as file:
    readme = file.read()

if os.getenv("WITH_CYTHON") is not None:
    import Cython.Build
    extension_modules = Cython.Build.cythonize('chu_liu_edmonds_module.pyx')
else:
    extra_link_args = []
    extra_compile_args = ['-std=c++11', '-fvisibility=hidden', '-w']
    if sys.platform == "darwin":
        extra_compile_args += ['-stdlib=libc++']
        extra_link_args += ['-stdlib=libc++']

    extension_modules = [distutils.core.Extension(
        'ufal.chu_liu_edmonds',
        ['chu_liu_edmonds.cpp', 'chu_liu_edmonds_module.cpp'],
        language = 'c++',
        extra_compile_args = extra_compile_args,
        extra_link_args = extra_link_args
    )]

distutils.core.setup(
    name             = 'ufal.chu_liu_edmonds',
    version          = '0.9.0',
    description      = 'Bindings to Chu-Liu-Edmonds algorithm from TurboParser',
    long_description = readme,
    author           = 'Milan Straka',
    author_email     = 'straka@ufal.mff.cuni.cz',
    license          = 'GPLv3',
    ext_modules      = extension_modules,
    classifiers      = [
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: C++',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries'
    ]
)
