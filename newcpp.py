CMAKE_LISTS_FILE = 'CMakeLists.txt'

class Config(object):
  """Contains config options"""

  def __init__(self):
    """??"""
    self.project_name = 'MyProject'
    self.src_dir = 'src'
    self.lib_dir = 'lib'
    self.bin_dir = 'bin'
    self.find_packages = []
    self.include_directories = []
    self.debug_flags = []
    self.add_executables = []
    self.source_files = {}

  def get_find_packages(self):
    return ''

  def get_include_directories(self):
    return ''

  def get_add_executables(self):
    return ''

def get_config(rc_file_paths):
  config = Config()
  for rc_file_path in rc_file_paths:
    pass
  return config

def make_cmake_file(template_path, config):
  cmake_file_template = open(template_path, 'r')
  cmake_string = cmake_file_template.read()
  cmake_file_template.close()
  cmake_string = cmake_string.replace('@project_name', config.project_name)
  cmake_string = cmake_string.replace(
      '@find_packages', config.get_find_packages())
  cmake_string = cmake_string.replace(
      '@include_directories', config.get_include_directories())
  cmake_string = cmake_string.replace('@lib_dir', config.lib_dir)
  cmake_string = cmake_string.replace('@bin_dir', config.bin_dir)
  cmake_string = cmake_string.replace('@src_dir', config.src_dir)
  cmake_string = cmake_string.replace(
      '@add_executables', config.get_add_executables())
  cmake_file = open(CMAKE_LISTS_FILE, 'w')
  cmake_file.write(cmake_string)
  cmake_file.close()
  print 'Generated {}'.format(CMAKE_LISTS_FILE)

def make_source_files(config):
  for fname, file_contents in config.source_files:
    source_file = open('{}/{}'.format(config.src_dir, fname), 'w')
    source_file.write(file_contents)
    source_file.close()
    print 'Generated source file: {}'.format(source_file)

# mkdir directory
# cd directory
# make_cmake_file(template, packages, dirs, executables)
# mkdir @src_dir
# cp template_file @src_dir
# mkdir build
# cd build
# cmake ..
# make

if __name__ == '__main__':
  config = get_config([])
  make_cmake_file('template_files/CMakeLists.txt', config)
