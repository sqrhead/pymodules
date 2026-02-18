try:
    from pydantic import BaseModel, Field, ValidationError
except ImportError:
    print("Error: create a .venv and install pydantic")
    raise SystemExit

from datetime import datetime
from typing import Optional


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime
    is_operational: bool = Field(default=True)
    notes: Optional[str] = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")
    try:
        space_station_valid: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(1998, 4, 26),
        )
        print("Valid station created:")
        print(f"ID: {space_station_valid.station_id}")
        print(f"Name: {space_station_valid.name}")
        print(f"Crew: {space_station_valid.crew_size} people")
        print(f"Power: {space_station_valid.power_level}%")
        print(f"Oxygen: {space_station_valid.oxygen_level}%")
        if space_station_valid.is_operational:
            print("Status: Operational")
        else:
            print("Status: Not Operational")
    except ValidationError as ve:
        print(f"{ve}")
    print("========================================")
    print("Expected validation error:")
    try:
        space_station__not_valid: SpaceStation = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=21,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(1998, 4, 26),
            is_operational=True,
        )
        print(f"{space_station__not_valid.name}")
    except ValidationError as ve:
        # for error in ve.errors():
        #     field = error["loc"][0]
        #     msg = error["msg"]
        #     print(f"{field}: {msg}")
        print(f"{ve}")


if __name__ == "__main__":
    main()
