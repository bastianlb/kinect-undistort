cmake_minimum_required(VERSION 3.4)
set(CMAKE_BUILD_TYPE Debug)

project(undistort CXX)

if (EXISTS ${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo_multi.cmake)
    include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo_multi.cmake)
    conan_set_find_paths()
elseif (EXISTS ${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
    include(${CMAKE_CURRENT_BINARY_DIR}/conanbuildinfo.cmake)
else ()
    message(WARNING "The file conanbuildinfo.cmake doesn't exist, you have to run conan install first")
endif ()

# list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_BINARY_DIR}")
conan_basic_setup(TARGETS)

add_executable(undistort main.cpp)

target_link_libraries(undistort PUBLIC
    CONAN_PKG::kinect-azure-sensor-sdk)
