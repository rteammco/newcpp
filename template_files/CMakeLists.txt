cmake_minimum_required(VERSION 3.1)

project(@project_name)

@find_packages

@include_directories

# Default to Release mode.
IF(NOT DEFINED CMAKE_BUILD_TYPE)
  SET(${CMAKE_BUILD_TYPE} Release ... FORCE)
ENDIF()

# Release mode makes the code run faster.
IF(NOT ${CMAKE_BUILD_TYPE} MATCHES Debug)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -m64 -Ofast")
ENDIF()

@require_cpp11

# Libraries will be stored in the "lib" directory, and binaries in "bin".
SET(CMAKE_ARCHIVE_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/@lib_dir)
SET(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/@lib_dir)
SET(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/@bin_dir)

# Grab all files in the source directory.
file(GLOB SRC "${CMAKE_CURRENT_SOURCE_DIR}/@src_dir/*")


@add_executables
