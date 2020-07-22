import logging

logging.basicConfig(
    filename='application.log',
    level=logging.WARNING,
    format= '[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
    datefmt='%H:%M:%S'
)


if __name__ == "__main__":
    logging.error("Some serious error occurred.")
    logging.warning('Function you are using is deprecated.')