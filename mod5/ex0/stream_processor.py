from abc import ABC, abstractmethod
from typing import Any, List


# this module is kind of abstract ah ah ah
class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Default Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self):
        super().__init__()
        print("\nInitializing Numeric Processor...")
        self.len: int = 0
        self.sum: int = 0
        self.avg: float = 0.0

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        self.len = 0
        self.sum = 0
        self.avg = 0.0
        if self.validate(data) is True:
            print("Validation: Numeric data verified")
        else:
            print("Validation: Numeric data not verified")
            return f"Processed {self.len} numeric values, " +\
                f"sum={self.sum}, avg={self.avg}"

        for n in data:
            self.len += 1
            self.sum += n
        self.avg = self.sum / self.len
        return f"Processed {self.len} numeric values, " +\
            f"sum={self.sum}, avg={self.avg}"

    def validate(self, data: Any) -> bool:
        try:
            for x in data:
                x += 0
            return True
        except Exception:  # TypeError
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class TextProcessor(DataProcessor):
    def __init__(self):
        print("\nInitializing Text Processor...")
        self.len: int = 0
        self.words: int = 0

    def str_len(self, string: str) -> int:
        size: int = 0
        for i in string:
            size += 1
        return size

    def counter_words(self, words: str) -> int:
        words_count: int = 0
        trigger: bool = False
        for x in words:
            if x == " ":
                trigger = False
            if x != " " and trigger is False:
                trigger = True
                words_count += 1
        return words_count

    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")
        if self.validate(data) is True:
            print("Validation: Text data verified")
        else:
            print("Validation: Text data not verified")
            return f"Processed text: {self.len} characters, {self.words} words"

        self.len = self.str_len(data)
        self.words = self.counter_words(data)
        return f"Processed text: {self.len} characters, {self.words} words"

    def validate(self, data: Any) -> bool:
        try:
            data += ""
            return True
        except Exception:  # TypeError
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class LogProcessor(DataProcessor):
    def __init__(self):
        print("\nInitializing Log Processor...")

    def process(self, data: Any) -> str:
        print(f'Processing data: {data}')
        if self.validate(data) is True:
            print("Validation: Log entry verified")
        else:
            print("Validation: Log entry not verified")
            return "NOT_VALID_DATA_INSERTED"
        if data[0] == "E":
            return f"[ALERT] {data}"
        else:
            return f"[INFO] {data}"

    def validate(self, data: Any) -> bool:
        str_error: str = "ERROR"
        str_info: str = "INFO"
        counter: int = 0
        try:
            for x in [0, 1, 2, 3, 4]:
                if data[x] == str_error[x]:
                    counter += 1
                else:
                    counter -= 1
            if counter == 5:
                return True
            else:
                counter = 0
            for x in [0, 1, 2, 3]:
                if data[x] == str_info[x]:
                    counter += 1
                else:
                    counter -= 1
            if counter == 4:
                return True
            else:
                return False
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    np: NumericProcessor = NumericProcessor()
    print(np.format_output(np.process([1, 2, 3, 4, 5])))

    tp: TextProcessor = TextProcessor()
    print(tp.format_output(tp.process("Hello Nexus World")))

    lp: LogProcessor = LogProcessor()
    print(lp.format_output(lp.process("ERROR: Connection timeout")))

    print("=== Polymorphic Processing Demo ===")
    pro: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
        ]
    inp: List[Any] = [[1, 2, 3], "Hello", "INFO: [OK]"]
    print("Processing multiple data types through same interface...\n")
    for x in [0, 1, 2]:
        print(f"Result {x + 1}: {pro[x].process(inp[x])}\n")
