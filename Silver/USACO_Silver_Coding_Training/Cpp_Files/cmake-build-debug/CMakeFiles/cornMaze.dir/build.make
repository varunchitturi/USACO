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
CMAKE_COMMAND = "/Users/varunchitturi/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/202.6948.80/CLion.app/Contents/bin/cmake/mac/bin/cmake"

# The command to remove a file.
RM = "/Users/varunchitturi/Library/Application Support/JetBrains/Toolbox/apps/CLion/ch-0/202.6948.80/CLion.app/Contents/bin/cmake/mac/bin/cmake" -E rm -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files"

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug"

# Include any dependencies generated for this target.
include CMakeFiles/cornMaze.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/cornMaze.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/cornMaze.dir/flags.make

CMakeFiles/cornMaze.dir/cornMaze.cpp.o: CMakeFiles/cornMaze.dir/flags.make
CMakeFiles/cornMaze.dir/cornMaze.cpp.o: ../cornMaze.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/cornMaze.dir/cornMaze.cpp.o"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/cornMaze.dir/cornMaze.cpp.o -c "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cornMaze.cpp"

CMakeFiles/cornMaze.dir/cornMaze.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/cornMaze.dir/cornMaze.cpp.i"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cornMaze.cpp" > CMakeFiles/cornMaze.dir/cornMaze.cpp.i

CMakeFiles/cornMaze.dir/cornMaze.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/cornMaze.dir/cornMaze.cpp.s"
	/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cornMaze.cpp" -o CMakeFiles/cornMaze.dir/cornMaze.cpp.s

# Object files for target cornMaze
cornMaze_OBJECTS = \
"CMakeFiles/cornMaze.dir/cornMaze.cpp.o"

# External object files for target cornMaze
cornMaze_EXTERNAL_OBJECTS =

cornMaze: CMakeFiles/cornMaze.dir/cornMaze.cpp.o
cornMaze: CMakeFiles/cornMaze.dir/build.make
cornMaze: CMakeFiles/cornMaze.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable cornMaze"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/cornMaze.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/cornMaze.dir/build: cornMaze

.PHONY : CMakeFiles/cornMaze.dir/build

CMakeFiles/cornMaze.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/cornMaze.dir/cmake_clean.cmake
.PHONY : CMakeFiles/cornMaze.dir/clean

CMakeFiles/cornMaze.dir/depend:
	cd "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Silver_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles/cornMaze.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/cornMaze.dir/depend
