import inspect
import os


class Debug:
    show_logs = True
    show_files = []

    @classmethod
    def out(cls, message):
        split_message = message.split(',')
        caller = inspect.stack()[2].filename
        file = os.path.splitext(os.path.basename(caller))[0]
        if cls.show_logs or file in cls.show_files:
            print(f"{split_message[0]}::{file.upper()}::{split_message[1]}")

    @classmethod
    def log(cls, message):
        cls.out(f"DEBUG,{message}")

    @classmethod
    def log_error(cls, message):
        cls.out(f"ERROR,{message}")

    @classmethod
    def log_warning(cls, message):
        cls.out(f"WARNING,{message}")
