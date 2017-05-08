cmake_minimum_required (VERSION 2.6)
project (Tutorial)

# The version number.
set (Tutorial_VERSION_MAJOR 1)
set (Tutorial_VERSION_MINOR 0)

# configure a header file to pass some of the CMake settings
# to the source code 
configure_file (
  "${PROJECT_SOURCE_DIR}/TutorialConfig.h.in"
  "${PROJECT_BINARY_DIR}/TutorialConfig.h"
)

include_directories ("${PROJECT_SOURCE_DIR}/MathFunction")
add_subdirectory (MathFunctions)

# add the binary tree to the search path for include files
# so that we will find TutorialConfig.h
include_directories("${PROJECT_BINARY_DIR}")

# should we use our own math function 
option (USE_MYMATH 
        "Use tutorial provided math implementation" ON)


# add MathFunction library ? 
# 
if (USE_MATH)
  include_directories ("${PROJECT_SOURCE_DIR}/MathFunctions")
  add_subdirectory (MathFunctions)
  set (EXTRA_LIBS ${EXTRA_LIBS} MathFunctions)
endif (USE_MATH)

# add the executable
add_executable(Tutorial tutorial.cxx)
target_link_libraries (Tutorial ${EXTRA_LIBS})
target_link_libraries (Tutorial MathFunctions)

# add to the top level (whatever the fuck that means) of this file
# add the install targets
install (TARGETS Tutorial DESTINATION bin)
install (FILES "${PROJECT_BINARY_DIR}/TutorialConfig.h"
        DESTINATION include)

include(CTest)

# does the application run
add_test (TutorialRuns Tutorial 25)

# does it sqrt of 25
add_test (TutorialComp25 Tutorial 25)
set_tests_properties (TutorialComp25 PROPERTIES PASS_REGULAR_EXPRESSION "25 is 5")

# does it handle negative numbers
add_test (TutorialNegative Tutorial -25)
set_tests_properties (TutorialNegative PROPERTIES PASS_REGULAR_EXPRESSION "-25 is 0")

# does it handle small numbers
add_test (TutorialSmall Tutorial 0.0001)
set_tests_properties (TutorialSmall PROPERTIES PASS_REGULAR_EXPRESSION "0.0001 is 0.01")

# does the usage message work?
add_test (TutorialUsage Tutorial)
set_tests_properties (TutorialUsage PROPERTIES PASS_REGULAR_EXPRESSION "Usage:.*number")


# .c++, .cc, .cxx. => .C & .c++

# Headers have used the corresponding 
# => .H, .h++, .hh, .hxx, .hpp

# Additionally, some use .ii, .ixx, .ipp, .inl 
# for headers providing inline definitions and  
# .txx, .tpp and .tpl for template definitions

#
#
#
#
#
#