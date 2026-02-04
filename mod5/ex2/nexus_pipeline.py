from abc import ABC, abstractmethod
from typing import Protocol, List, Dict, Union, Optional, Any
import collections

class ProcessingStage(Protocol):

    def process(self, data: Any) -> Any:
        pass


class InputStage:

    def process(self, data: Any) -> Dict:
        pass


class TransformStage:

    def process(self, data: any) -> Dict:
        pass


class OutputStage:

    def process(self, data: Any) -> str:
        pass


class ProcessingPipeline(ABC):

    def __init__(self) -> None:
        self.stages: ProcessingStage = []

    def add_stage(self, stage: ProcessingStage):
        self.stages = self.stages + [stage]

    @abstractmethod
    def process() -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    def __init__(self,parameter_id):
        super().__init__()
        self.parameter_id = parameter_id

    def process():
        pass


class CSVAdapter(ProcessingPipeline):
    def __init__(self,parameter_id):
        super().__init__()
        self.parameter_id = parameter_id
    def process():
        pass


class StreamAdapter(ProcessingPipeline):
    def __init__(self,parameter_id):
        super().__init__()
        self.parameter_id = parameter_id
    def process():
        pass

class NexusManager:
    pass


if __name__ == "__main__":
    pass