import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class HexagonTurtle(Node):
    def __init__(self):
        super().__init__('hexagon_turtle')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.draw_hexagon)

        self.state = "FORWARD"
        self.step_count = 0
        self.forward_time = 15  # Mozgás hossza
        self.turn_time = 10      # Fordulási idő
        self.sides_drawn = 0  # Hány oldalt rajzolt már meg

    def draw_hexagon(self):
        """A teknős hatszöget rajzol."""
        msg = Twist()

        if self.sides_drawn < 6:
            if self.state == "FORWARD":
                msg.linear.x = 2.0  # Egyenes mozgás
                msg.angular.z = 0.0
                self.step_count += 1

                if self.step_count >= self.forward_time:
                    self.state = "TURN"
                    self.step_count = 0

            elif self.state == "TURN":
                msg.linear.x = 0.0
                msg.angular.z = 1.047  # 60 fokos fordulás (radianban: 60° = π/3)
                self.step_count += 1

                if self.step_count >= self.turn_time:
                    self.state = "FORWARD"
                    self.step_count = 0
                    self.sides_drawn += 1  # Egy új oldal elkészült

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = HexagonTurtle()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
