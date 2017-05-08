# our own implementation for computing sqrt 
add_library(MathFunctions mysqrt.cxx)

# setup the library & header fiels to be installed:
# add the install targets 
# apparently: CMake Error at MathFunctions/CMakeLists.txt:6 (install):
# install TARGETS given target "Tutorial" which does not exist in this
install (TARGETS Tutorial DESTINATION bin)
# this is telling cmake to install our binary file into the bin 
# directory? of the install dir.
install (FILES MathFunctions.h DESTINATION includes)