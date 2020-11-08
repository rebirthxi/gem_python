from abc import ABC, abstractmethod


class BasicPacket(ABC):
    PACKET_SIZE = 1

    @abstractmethod
    def to_bytes(self) -> bytes:
        pass
