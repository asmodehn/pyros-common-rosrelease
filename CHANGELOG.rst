Changelog
=========


0.5.1 (2018-04-16)
------------------
- Adding common package to hold crossprocess exceptions. [AlexV]


0.5.0 (2018-04-13)
------------------
- V0.5.0. [AlexV]
- Cosmetics and comments for future API upgrade. [AlexV]
- Adding tests for configuration after init. [AlexV]
- Now handling args and config in child context. [AlexV]
- Now handling interface setup as part of context to guarantee
  availability after start() call. now using pytest. [AlexV]
- Added badges. [AlexV]
- Removing pyros requirements. not needed anymore. [AlexV]
- Not using pyros_setup anymore here, since we do not depend on ROS
  environment for common or mock. [AlexV]
- Remove ROS build files, now useless here since this is just a python
  package. [AlexV]
- Fixing cmakelists.txt after reverting to normal package. [AlexV]


0.4.2 (2017-04-19)
------------------
- Updating changelog. [AlexV]
- Fixing setup.py to point to normal pyros-common package. [AlexV]
- V0.4.2. [AlexV]
- Fixing setup.py commands after pacakge structure change. [AlexV]
- Dropping the namespace idea, since we cant make a working deb pkg out
  of it. [AlexV]
- Preparing ros release... [AlexV]


0.4.1 (2017-04-19)
------------------
- V0.4.1. [AlexV]
- Some setup.py commands fixes for release. [AlexV]
- Changing tox tester to nose. [AlexV]
- Moving ctx_server back to pyros to keep dependencies one-way. [AlexV]
- Renaming test_pyros_mock for pytest to detect it. [AlexV]
- Removing the pkgutil way to only use one way to do namespace packages.
  [AlexV]
- Adding tox and travis files. adding dependency on pyros repo for
  tests... [AlexV]
- Setup.py publish command description change. [AlexV]
- Adding null logging handler by default. [AlexV]
- Keep using the same ros package name for now. [AlexV]
- Reorganizing to nest everything under pyros_interfaces namespace.
  [AlexV]
- Now relying on catkin_pip >0.2. [AlexV]
- Fix for cmakelists. added dependencies in package.xml. [alexv]
- Added git changelog configuration. some setup.py fixes. [alexv]


0.4.0 (2017-01-18)
------------------
- V0.4.0. [alexv]
- More fixes to get other tests to pass. [alexv]
- Restructuring pyros_common to simplify things. added cmakelists and
  package.xml temporarily, while we get everything working together from
  source... [alexv]
- Adding pyros protocol. [alexv]
- Fixed setup.py. [alexv]
- Moving code from pyros. [alexv]
- Initial commit. [AlexV]


