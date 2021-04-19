cmake_minimum_required(VERSION 3.5)

project(sparsh_braille)

if(NOT CMAKE_CXX_STANDARD)

    set(CMAKE_CXX_STANDARD 17)

endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")

    add_compile_options(-Wall -Wextra -Wpedantic)

endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)

set(dependencies
    rclcpp
)

include_directories(include)

add_executable(braille src/main.cpp)

add_library(braille_core SHARED
    src/braille.cpp
)

ament_target_dependencies(braille ${dependencies})
target_include_directories(braille
    PUBLIC include
)
target_link_libraries(braille braille_core)

ament_target_dependencies(braille_core ${dependencies})
target_include_directories(braille_core
    PUBLIC include
)
target_link_libraries(braille_core)

install(TARGETS braille_core
    ARCHIVE DESTINATION lib
    LIBRARY DESTINATION lib
    RUNTIME DESTINATION bin
    INCLUDES DESTINATION include
)

install(TARGETS braille
    DESTINATION lib/${PROJECT_NAME}
)

install(DIRECTORY launch
    DESTINATION share/${PROJECT_NAME}
)

install(DIRECTORY include/
    DESTINATION include
)

if(BUILD_TESTING)

    find_package(ament_lint_auto REQUIRED)
    ament_lint_auto_find_test_dependencies()

endif()

ament_export_include_directories(include)
ament_export_libraries(braille_core)
ament_export_dependencies(${dependencies})

ament_package()
