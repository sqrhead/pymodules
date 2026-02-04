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

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "reading processed":self.total_reading,
        }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == None:
            return data_batch
        else:
            return [item[criteria] for item in data_batch if item[criteria] > 100]


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

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "operations processed":self.total_operations,
        }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        try:
            if criteria == None:
                return data_batch
            elif criteria == "sell":
                return [item for item in data_batch if "sell" in item and item[criteria] > 100]
            elif criteria == "buy":
                return [item for item in data_batch if "buy" in  item and item[criteria] > 100]
            else:
                raise Exception("Wrong criteria inputed: 'buy' or 'sell' valid")
        except KeyError as ke:
            print(f"KEY_ERROR: {ke}")
        except Exception as e:
            print(f"ERROR: {e}")



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

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "events processed":self.total_events,
        }

    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if criteria == None:
            return data_batch
        else:
                return [item for item in data_batch if item == criteria]

class StreamProcessor:
    def __init__(self, streams: List[List[DataStream]]) -> None:
        print("Processing mixed stream types through unified interface...")
        self.streams = streams
        self.ssdata: List[Any] = [
            {"temp": 22.5, "humidity": 65, "pressure": 1013},
            {"temp": 120, "humidity": 10000, "pressure": 500},
            {"temp": 480, "humidity": 400, "pressure": 300},
        ]
        self.tsdata: List[Dict] = [
            {"buy": 120},
            {"sell": 120},
            {"buy": 75},
            {"buy": 20},
        ]
        self.esdata: List[str] = [
            "error","login","logout"
        ]

    def __len_res(self, stream: List[Any]) -> int:
        len_stream: int = 0
        try:
            for _ in stream:
                len_stream += 1
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            return len_stream

    def process_batch(self) -> None:
        batch_counter: int = 0
        try:
            for l in self.streams:
                batch_counter += 1
                print(f"\nBatch {batch_counter} result:")
                for s in l:
                    data = s.get_stats()
                    if isinstance(s, SensorStream) is True:
                        for k in data:
                            print(f"- Sensor data: {data[k]} {k}")
                    elif isinstance(s, EventStream) is True:
                         for k in data:
                            print(f"- Event data: {data[k]} {k}")
                    elif isinstance(s, TransactionStream) is True:
                        for k in data:
                            print(f"- Transaction data: {data[k]} {k}")
                    else:
                        raise Exception("WRONG STREAM INPUTED")
        except Exception as e:
            print(f"ERROR: {e}")

    def filter_batch(self) -> None:
        sensor_result: List[Any]
        trans_result: List[Any]
        event_result: List[Any]
        try:
            for list_stream in self.streams:
                for stream in list_stream:
                    if isinstance(stream, SensorStream) is True:
                        sensor_result = stream.filter_data(self.ssdata, "temp")
                    elif isinstance(stream, TransactionStream) is True:
                        trans_result = stream.filter_data(self.tsdata, "buy")
                    elif isinstance(stream, EventStream) is True:
                        event_result = stream.filter_data(self.esdata, "error")
                    else:
                        raise Exception("Wrong stream inputed")
        except Exception as e:
            print(f"ERROR: {e}")
            return
        print(
            f"Filtered result: "+
            f"{self.__len_res(sensor_result)} critical sensor alerts, " +
            f"{self.__len_res(trans_result)} large transaction, " +
            f"{self.__len_res(event_result)} important events"
        )

if __name__ == "__main__":
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    ssdata: List[Dict] = [
        {"temp": 22.5, "humidity": 65, "pressure": 1013},
        {"temp": 120, "humidity": 10000, "pressure": 500},
        {"temp": 480, "humidity": 400, "pressure": 300},
    ]
    tsdata: List[Dict] = [
        {"buy": 100},
        {"sell": 150},
        {"buy": 75},
        {"buy": 20},
    ]
    esdata: List[str] = [
        "error","login","logout"
    ]
    ss: SensorStream = SensorStream("SENSOR_001")
    print(ss.process_batch(ssdata))
    ts: TransactionStream = TransactionStream("TRANS_001")
    print(ts.process_batch(tsdata))
    es: EventStream = EventStream("EVENT_001")
    print(es.process_batch(esdata))

    print("=== Polymorphic Stream Processing ===")
    streamprocessor: StreamProcessor = StreamProcessor([[ss, ts, es]])
    streamprocessor.process_batch()
    streamprocessor.filter_batch()
