import abc


class _BaseError(Exception):
    @classmethod
    @abc.abstractmethod
    def status_code(cls) -> int: ...

    @classmethod
    @abc.abstractmethod
    def code(cls) -> str: ...

    @classmethod
    @abc.abstractmethod
    def message(cls) -> str: ...
