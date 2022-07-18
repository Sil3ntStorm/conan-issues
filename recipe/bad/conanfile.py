from conans import ConanFile, tools

class conanBug(ConanFile):
    python_requires = 'dummy-generator/0.1.0@local/testing'
    settings = 'os', 'compiler', 'build_type', 'arch'
    generators = 'dummy'
    requires = (
        'sqlitecpp/3.1.1',
    )
