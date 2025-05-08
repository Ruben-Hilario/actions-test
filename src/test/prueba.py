import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MiNodo(Node):
    def __init__(self):
        super().__init__('nodo_test')
        self.publisher_ = self.create_publisher(String, 'topic', 10)
        self.timer = self.create_timer(1, self.publicar_mensaje)

    def publicar_mensaje(self):
        msg = String()
        msg.data = 'Iniciando'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publicando: "{msg.data}"')

def main(args=None):
    rclpy.init(args=args)
    nodo = MiNodo()
    rclpy.spin(nodo)
    nodo.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

