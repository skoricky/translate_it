from abc import ABCMeta, abstractmethod, abstractproperty


class AbsModel:
    """
    Абстрактный класс для описания стандартных методов для моделей
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_blocks(self):
        pass

    @abstractmethod
    def set_blocks(self):
        pass

    @abstractmethod
    def save_to_file(self):
        pass


class JsonModel(AbsModel):
    def __init__(self):
        pass

    def get_blocks(self):
        pass

    def set_blocks(self):
        pass

    def get_project_id(self):
        pass

    def save_to_file(self):
        pass