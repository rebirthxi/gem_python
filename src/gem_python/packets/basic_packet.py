from abc import ABC, abstractmethod


class BasicPacket(ABC):
    PACKET_SIZE = 1

    @abstractmethod
    def to_bytes(self) -> bytes:
        pass

    @abstractmethod
    def from_bytes(self, data: bytes) -> None:
        pass
