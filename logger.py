class systemLogger:
    def __init__(self, file_name):
        self.file = file_name

    def log_error(self, error_message):
        with open(self.file, "a") as file:
            file.write(error_message + "\n")
        print(f"logged error : {error_message}")

if __name__ == "__main__":
    my_logger = systemLogger("system_errors.txt")
    my_logger.log_error("database connection failed")