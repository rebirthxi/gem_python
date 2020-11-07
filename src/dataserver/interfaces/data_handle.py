from abc import ABC, abstractmethod


class DataHandle(ABC):

    @abstractmethod
    def AuthenticateAccount(self, account_name, passwd):
        pass
