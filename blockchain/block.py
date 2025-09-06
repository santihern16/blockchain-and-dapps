from dataclasses import dataclass

@dataclass
class Block:
    index: int
    data: str
    previous_index: int
