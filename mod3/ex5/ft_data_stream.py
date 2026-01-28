def stream_data(n: int):
    for i in range(n):
        yield f"Event {i}: NOTHING!"

if __name__ == "__main__":
    for x in stream_data(100):
        print(x)