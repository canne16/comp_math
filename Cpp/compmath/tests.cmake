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
              )
target_compile_definitions(runDifferentiationTests PUBLIC TESTING)
target_include_directories(runDifferentiationTests PRIVATE
                            ${INCLUDE_DIR}
                            "${PROJECT_BINARY_DIR}"
                          )
target_link_libraries(runDifferentiationTests gtest gtest_main pthread)

# Integration test
add_executable(runIntegrationTests 
                        ${TEST_DIR}/test_integration.cc
                        ${SRC_DIR}/export_data.cc
              )
target_compile_definitions(runIntegrationTests PUBLIC TESTING)
target_include_directories(runIntegrationTests PRIVATE
                            ${INCLUDE_DIR}
                            "${PROJECT_BINARY_DIR}"
                          )
target_link_libraries(runIntegrationTests gtest gtest_main pthread)


# Interpolation test
add_executable(runInterpolationTests 
                        ${TEST_DIR}/test_interpolation.cc
                        ${SRC_DIR}/export_data.cc
              )
target_compile_definitions(runInterpolationTests PUBLIC TESTING)
target_include_directories(runInterpolationTests PRIVATE
                            ${INCLUDE_DIR}
                            "${PROJECT_BINARY_DIR}"
                          )
target_link_libraries(runInterpolationTests gtest gtest_main pthread)

enable_testing()
# Register the test
add_test(NAME BigTest COMMAND runTests)
add_test(NAME DifferentiationTest COMMAND runDifferentiationTests)
add_test(NAME IntegrationTest COMMAND runIntegrationTests)
add_test(NAME InterpolationTest COMMAND runInterpolationTests)