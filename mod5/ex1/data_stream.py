from abc import ABC, abstractmethod
from typing import *

class DataStream(ABC):

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == None:
            return data_batch
        else:
            return [item for item in data_batch if criteria == item]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        pass


class SensorStream(DataStream):

    def __init__(self, stream_id: int) -> None:
        self.stream_id = stream_id
        self.total_reading: int = 0
        self.total_temperature: float = 0.0
        self.average_temperature: float = 0.0
        print("\nInitializing Sensor Stream ...")
        print(f"Stream ID: {stream_id}, Type: Enviromental Data")
        pass

    def process_batch(self, data_batch: List[Any]) -> str:
        try:

            for k in data_batch:
                self.total_reading += 1
                self.total_temperature += k["temp"]
        except Exception as e:
            return f"Error: {e}"
        self.average_temperature = self.total_temperature / self.total_reading
        return (
            f"Processing sensor batch: {data_batch}\n" +
            f"Sensory analysis batch: {self.total_reading} readings proceeded, "+
            f"avg temp: {self.average_temperature}C"
        )


    # def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:


class TransactionStream(DataStream):

    def __init__(self, stream_id: int) -> None:
        self.stream_id = stream_id
        self.net_flow: float = 0
        self.total_operations: int = 0
        print("\nInitializing Transaction Stream...")
        print(f"Stream ID: {stream_id}, Type: Financial Data")
        pass

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            for index in data_batch:
                self.total_operations += 1
                if "sell" in index:
                    self.net_flow -= index["sell"]
                elif "buy" in index:
                    self.net_flow += index["buy"]
                else:
                    raise Exception("Wrong type of data inserted")
        except Exception as e:
            return f"Error: {e}"
        return (
            f"Processing transaction batch: {data_batch}\n" +
            f"Transaction analysis batch: {self.total_operations} operations, "+
            f"net flow: {self.net_flow} units"
        )

class EventStream(DataStream):

    def __init__(self, stream_id: int) -> None:
        self.stream_id = stream_id
        self.total_events: int = 0
        self.total_errors: int = 0
        print("\nInitializing Event Stream...")
        print(f"Stream ID: {stream_id}, Type: System Events")
        pass

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            for k in data_batch:
                self.total_events += 1
                if k == "error":
                    self.total_errors += 1
                elif k == "login" or k == "logout":
                    continue
                else:
                    raise Exception("Wrong inputed data")
        except Exception as e:
            return f"Error: {e}"

        return (
            f"Processing event batch: {data_batch}\n"
            f"Event analysis: {self.total_events} events, {self.total_errors} error detected"
        )

class StreamProcessor:
    def __init__(self, batch: List[Any]) -> None:
        pass


if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    ssdata: List[Any] = [
        {"temp": 22.5, "humidity": 65, "pressure": 1013},
        {"temp": 120, "humidity": 10000, "pressure": 500},
        {"temp": 480, "humidity": 400, "pressure": 300},
    ]
    tsdata: List[Dict] = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75}
    ]
    esdata: List[str] = [
        "error","login","logout"
    ]
    streamprocessor: StreamProcessor = StreamProcessor([])
    ss: SensorStream = SensorStream("SENSOR_001")
    print(ss.process_batch(ssdata))
    ts: TransactionStream = TransactionStream("TRANS_001")
    print(ts.process_batch(tsdata))
    es: EventStream = EventStream("EVENT_001")
    print(es.process_batch(esdata))

    print("=== Polymorphic Stream Processing ===")