# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.17

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Disable VCS-based implicit rules.
% : %,v


# Disable VCS-based implicit rules.
% : RCS/%


# Disable VCS-based implicit rules.
% : RCS/%,v


# Disable VCS-based implicit rules.
% : SCCS/s.%


# Disable VCS-based implicit rules.
% : s.%


.SUFFIXES: .hpux_make_needs_suffix_list


# Command-line flag to silence nested $(MAKE).
$(VERBOSE)MAKESILENT = -s

# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = "/Users/varunchitturi/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/202.6397.106/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/varunchitturi/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/202.6397.106/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/censoring.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/censoring.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/censoring.dir/flags.make

CMakeFiles/censoring.dir/censoring.cpp.o: CMakeFiles/censoring.dir/flags.make
CMakeFiles/censoring.dir/censoring.cpp.o: ../censoring.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/censoring.dir/censoring.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/censoring.dir/censoring.cpp.o -c /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/censoring.cpp

CMakeFiles/censoring.dir/censoring.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/censoring.dir/censoring.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/censoring.cpp > CMakeFiles/censoring.dir/censoring.cpp.i

CMakeFiles/censoring.dir/censoring.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/censoring.dir/censoring.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/censoring.cpp -o CMakeFiles/censoring.dir/censoring.cpp.s

# Object files for target censoring
censoring_OBJECTS = \
"CMakeFiles/censoring.dir/censoring.cpp.o"

# External object files for target censoring
censoring_EXTERNAL_OBJECTS =

censoring: CMakeFiles/censoring.dir/censoring.cpp.o
censoring: CMakeFiles/censoring.dir/build.make
censoring: CMakeFiles/censoring.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable censoring"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/censoring.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/censoring.dir/build: censoring

.PHONY : CMakeFiles/censoring.dir/build

CMakeFiles/censoring.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/censoring.dir/cmake_clean.cmake
.PHONY : CMakeFiles/censoring.dir/clean

CMakeFiles/censoring.dir/depend:
	cd /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug /Users/varunchitturi/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles/censoring.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/censoring.dir/depend

