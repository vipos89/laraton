from abc import abstractmethod


class AbstractConnector:
    def __init__(self, config):
        self.connect(config)

    @abstractmethod
    def connect(self, config):
        pass

    @abstractmethod
    def execute(self, query):
        pass
