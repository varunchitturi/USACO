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
CMAKE_COMMAND = "/Users/varunchitturi/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/203.5981.166/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/varunchitturi/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/203.5981.166/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/scales.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/scales.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/scales.dir/flags.make

CMakeFiles/scales.dir/scales.cpp.o: CMakeFiles/scales.dir/flags.make
CMakeFiles/scales.dir/scales.cpp.o: ../scales.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/scales.dir/scales.cpp.o"
	/usr/bin/g++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/scales.dir/scales.cpp.o -c "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/scales.cpp"

CMakeFiles/scales.dir/scales.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/scales.dir/scales.cpp.i"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/scales.cpp" > CMakeFiles/scales.dir/scales.cpp.i

CMakeFiles/scales.dir/scales.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/scales.dir/scales.cpp.s"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/scales.cpp" -o CMakeFiles/scales.dir/scales.cpp.s

# Object files for target scales
scales_OBJECTS = \
"CMakeFiles/scales.dir/scales.cpp.o"

# External object files for target scales
scales_EXTERNAL_OBJECTS =

scales: CMakeFiles/scales.dir/scales.cpp.o
scales: CMakeFiles/scales.dir/build.make
scales: CMakeFiles/scales.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable scales"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/scales.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/scales.dir/build: scales

.PHONY : CMakeFiles/scales.dir/build

CMakeFiles/scales.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/scales.dir/cmake_clean.cmake
.PHONY : CMakeFiles/scales.dir/clean

CMakeFiles/scales.dir/depend:
	cd "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles/scales.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/scales.dir/depend
