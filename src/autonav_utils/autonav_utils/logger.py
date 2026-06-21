from rclpy.logging import get_logger


class AutoNavLogger:

    @staticmethod
    def info(node_name, message):
        get_logger(node_name).info(message)

    @staticmethod
    def warn(node_name, message):
        get_logger(node_name).warn(message)

    @staticmethod
    def error(node_name, message):
        get_logger(node_name).error(message)

    @staticmethod
    def fatal(node_name, message):
        get_logger(node_name).fatal(message)
