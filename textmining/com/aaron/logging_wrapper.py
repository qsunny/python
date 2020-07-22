from functools import wraps, partial
import logging


def attach_wrapper(obj, func=None):  # Helper function that attaches function as attribute of an object
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def log(level, message):  # Actual decorator
    def decorate(func):
        logger = logging.getLogger(func.__module__)  # Setup logger
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        log_message = f"{func.__name__} - {message}"

        @wraps(func)
        def wrapper(*args, **kwargs):  # Logs the message and before executing the decorated function
            logger.log(level, log_message)
            return func(*args, **kwargs)

        @attach_wrapper(wrapper)  # Attaches "set_level" to "wrapper" as attribute
        def set_level(new_level):  # Function that allows us to set log level
            nonlocal level
            level = new_level

        @attach_wrapper(wrapper)  # Attaches "set_message" to "wrapper" as attribute
        def set_message(new_message):  # Function that allows us to set message
            nonlocal log_message
            log_message = f"{func.__name__} - {new_message}"
        return wrapper
    return decorate


# Example Usage
@log(logging.WARN, "example-param")
def somefunc(args):
    return args


somefunc("some args")
somefunc.set_level(logging.CRITICAL)  # Change log level by accessing internal decorator function
somefunc.set_message("new-message")  # Change log message by accessing internal decorator function
somefunc("some args")


