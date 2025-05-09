cmake_minimum_required(VERSION 3.10)
project(test)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

# No se compila el script, solo se instala
install(PROGRAMS
  src/test/prueba.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
