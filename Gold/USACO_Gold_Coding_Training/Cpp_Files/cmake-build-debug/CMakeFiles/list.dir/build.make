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
include CMakeFiles/list.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/list.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/list.dir/flags.make

CMakeFiles/list.dir/list.cpp.o: CMakeFiles/list.dir/flags.make
CMakeFiles/list.dir/list.cpp.o: ../list.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir="/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/list.dir/list.cpp.o"
	/usr/bin/g++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/list.dir/list.cpp.o -c "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/list.cpp"

CMakeFiles/list.dir/list.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/list.dir/list.cpp.i"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/list.cpp" > CMakeFiles/list.dir/list.cpp.i

CMakeFiles/list.dir/list.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/list.dir/list.cpp.s"
	/usr/bin/g++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/list.cpp" -o CMakeFiles/list.dir/list.cpp.s

# Object files for target list
list_OBJECTS = \
"CMakeFiles/list.dir/list.cpp.o"

# External object files for target list
list_EXTERNAL_OBJECTS =

list: CMakeFiles/list.dir/list.cpp.o
list: CMakeFiles/list.dir/build.make
list: CMakeFiles/list.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir="/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles" --progress-num=$(CMAKE_PROGRESS_2) "Linking CXX executable list"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/list.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/list.dir/build: list

.PHONY : CMakeFiles/list.dir/build

CMakeFiles/list.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/list.dir/cmake_clean.cmake
.PHONY : CMakeFiles/list.dir/clean

CMakeFiles/list.dir/depend:
	cd "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug" && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug" "/Users/varunchitturi/Library/Mobile Documents/com~apple~CloudDocs/Documents/Coding/USACO_Gold_Coding_Training/Cpp_Files/cmake-build-debug/CMakeFiles/list.dir/DependInfo.cmake" --color=$(COLOR)
.PHONY : CMakeFiles/list.dir/depend
