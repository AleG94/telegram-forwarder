import logging
from . import config
from .forwarder import Forwarder


def main():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    forwarder = Forwarder(config)
    forwarder.start()


if __name__ == "__main__":
    main()
