cmake_minimum_required(VERSION 2.8.3)
project(pyros_common)  # we need to follow ros package naming conventions here
# TODO : change name from lunar distro to match python naming (we are now using namespaces)

# Minimal Python module setup - catkin is assumed preinstalled along with ROS
# This assume catkin is installed along with a minimal ROS system.
find_package(catkin REQUIRED COMPONENTS
    catkin_pip
)

# defining current package as a package that should be managed by pip (not catkin - even though we make it usable with workspaces)
catkin_pip_package(pyros_common)

## Unit tests
if (CATKIN_ENABLE_TESTING)


    ##############################################################################
    # Nose Tests
    ##############################################################################

    # Careful this will not support parallel testing, due to multiprocess environment used in tests
    catkin_add_nosetests(pyros_interfaces_mock/tests)

    # TODO : run ROS tests with --no-skip to force them...

endif()



