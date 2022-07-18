from conans.model import Generator
from conans import ConanFile, tools
try:
    from pprintpp import pformat as pp
except:
    from pprint import pformat as pp

required_conan_version = '>= 1.50'

class dummy(Generator):
    @property
    def filename(self):
        return 'conanbuildinfo.dummy'

    @property
    def content(self):
        self.conanfile.output.info('Generating content for {} arch: {}'.format(self.conanfile.settings.get_safe('build_type'), self.conanfile.settings.get_safe('arch')))
        out = []
        for _, dependency in self.conanfile.dependencies.items():
            name = dependency.ref.name
            self.conanfile.output.info(f'{name} has components: {dependency.cpp_info.has_components}, which is ignored since all info is all in components field regardless')
            for comp_name, comp in dependency.cpp_info.components.items():
                out.extend(self.processSingleDependency(comp_name or name, comp))
        return '\n'.join(out)

    def processSingleDependency(self, name, info):
        output = []
        output.append(f'processing {name}: {pp(vars(info))}')

        # Sometimes present, sometimes not... :shrug:
        if hasattr(info, 'name'):
            output.append(f'  Overriding {name} with {info.name}')
            name = info.name

        if info.includedirs:
            output.append(f'  Include Dirs: {info.includedirs}')
        if info.libdirs:
            output.append(f'  Lib Dirs: {info.libdirs}')
        if info.requires:
            output.append(f'  Required: {info.requires}')
        if info.system_libs:
            output.append(f'  Required System Libs: {info.system_libs}')
        if info.libs:
            output.append(f'  Provided Libs: {info.libs}')
        if info.defines:
            output.append(f'  Defines: {info.defines}')
        if info.cflags:
            output.append(f'  CFlags: {info.cflags}')
        if info.cxxflags:
            output.append(f'  CXXFlags: {info.cxxflags}')

        output.extend(['', '===========================================', ''])
        return output



class DummyGeneratorConan(ConanFile):
    name = 'dummy-generator'
    description = 'Just a dummy generator for debugging'
    version = '0.1.0'
    author = 'Sil3ntStorm'
    license = 'MS-RL'
    settings = ''
    url = 'https://github.com/Sil3ntStorm'
    homepage = 'https://github.com/Sil3ntStorm'
