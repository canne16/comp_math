cmake_minimum_required(VERSION 3.25)

# Project name and version
project(compMath VERSION 1.0 LANGUAGES CXX)

# Set C++ standard
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

configure_file(Config.hh.in Config.hh)

set(SRC_DIR "${CMAKE_SOURCE_DIR}/src")
set(INCLUDE_DIR "${CMAKE_SOURCE_DIR}/include")
set(TEST_DIR "${CMAKE_SOURCE_DIR}/test")


# Add the library, source files, include directories
add_library(compMath STATIC)
target_sources(compMath
    PRIVATE
        ${SRC_DIR}/main.cc
        ${SRC_DIR}/export_data.cc
        # ${SRC_DIR}/Analyzer.cpp
        # ${SRC_DIR}/Visualize.cpp
)
target_include_directories(compMath
    PUBLIC
        ${CMAKE_CURRENT_SOURCE_DIR}/include
        "${PROJECT_BINARY_DIR}"
)

# Set library properties
set_target_properties(compMath PROPERTIES
    VERSION ${PROJECT_VERSION}
    SOVERSION 1
    OUTPUT_NAME "compMath"
)


# Testing

include(${CMAKE_SOURCE_DIR}/tests.cmake)

# Add a test application
add_executable(TestApplication ${TEST_DIR}/test_app.cc)
target_include_directories(TestApplication PRIVATE
                                ${CMAKE_SOURCE_DIR}/include
                                "${PROJECT_BINARY_DIR}"
                            )

target_link_libraries(TestApplication PRIVATE 
                        compMath
                     )