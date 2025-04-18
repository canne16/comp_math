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

# Fetch Google Test
include(FetchContent)
FetchContent_Declare(
    googletest
    GIT_REPOSITORY https://github.com/google/googletest.git
    GIT_TAG v1.16.0
)
FetchContent_MakeAvailable(googletest)

# Main test
add_executable(runTests 
                        ${TEST_DIR}/test_main.cc
                        ${TEST_DIR}/test_differentiation.cc
                        ${SRC_DIR}/export_data.cc
                        ${SRC_DIR}/norm.cc
              )
target_compile_definitions(runTests PUBLIC TESTING)
target_include_directories(runTests PRIVATE
                            ${INCLUDE_DIR}
                            "${PROJECT_BINARY_DIR}"
                          )
target_link_libraries(runTests gtest gtest_main pthread)

# Differentiation test
add_executable(runDifferentiationTests 
                        ${TEST_DIR}/test_differentiation.cc
                        ${SRC_DIR}/export_data.cc
                        ${SRC_DIR}/norm.cc
              )
target_compile_definitions(runDifferentiationTests PUBLIC TESTING)
target_include_directories(runDifferentiationTests PRIVATE
                            ${INCLUDE_DIR}
                            "${PROJECT_BINARY_DIR}"
                          )
target_link_libraries(runDifferentiationTests gtest gtest_main pthread)


enable_testing()
# Register the test
add_test(NAME BigTest COMMAND runTests)
add_test(NAME DifferentiationTest COMMAND runDifferentiationTests)




# Add a test application
add_executable(TestApplication ${TEST_DIR}/test_app.cc)
target_include_directories(TestApplication PRIVATE
                                ${CMAKE_SOURCE_DIR}/include
                                "${PROJECT_BINARY_DIR}"
                            )

target_link_libraries(TestApplication PRIVATE 
                        compMath
                     )