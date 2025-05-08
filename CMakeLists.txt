cmake_minimum_required(VERSION 3.5)
project(test)

find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

add_executable(prueba src/test/prueba.py)

ament_target_dependencies(prueba rclpy std_msgs)

install(TARGETS
  prueba
  DESTINATION lib/${PROJECT_NAME})

ament_package()
