import enum
from datetime import datetime
from typing import Self
try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
except ImportError:
    print("Error: install/activate .venv and install pydantic")
    raise SystemExit


class Rank(enum.Enum):
    cadet = 0
    officer = 1
    lieutenant = 2
    captain = 3
    commander = 4


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = Field(default='planned')
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode='after')
    def validation(self) -> Self:
        if self.mission_id[:1] != 'M':
            raise ValueError("Mission ID doesnt start with 'M'")

        has_leader: bool = False
        for mem in self.crew:
            if mem.rank is Rank.commander or mem.rank is Rank.captain:
                has_leader = True
        if has_leader is False:
            raise ValueError("Crew doesnt have a Captain/Commander")

        crew_size: int = len(self.crew)
        crew_min: int = 1
        counter: int = 0
        if crew_size > 1:
            crew_min: int = crew_size // 2
        else:
            crew_min = 1

        if self.duration_days > 365:
            for mem in self.crew:
                if mem.years_experience >= 5:
                    counter += 1
        if counter < crew_min:
            raise ValueError("Not enough experience crew members")

        are_active: bool = True
        for mem in self.crew:
            if mem.is_active is False:
                are_active = False
        if are_active is False:
            raise ValueError("Not all crew members are active")
        return self


if __name__ == "__main__":
    print("Space Mission Crew Validation")
    print("=========================================")
    try:
        crew_mem1: CrewMember = CrewMember(
            member_id="M_001",
            name="Sarah Connor",
            rank=Rank.commander,
            age=45,
            specialization="Mission Command",
            years_experience=25,
            is_active=True
        )

        crew_mem2: CrewMember = CrewMember(
            member_id="M_002",
            name="John Smith",
            rank=Rank.lieutenant,
            age=35,
            specialization="Navigation",
            years_experience=10,
            is_active=True
        )

        crew_mem3: CrewMember = CrewMember(
            member_id="M_003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=25,
            specialization="Engineering",
            years_experience=5,
            is_active=True
        )

        space_miss: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(3100, 4, 26),
            duration_days=900,
            crew=[
                crew_mem1,
                crew_mem2,
                crew_mem3
            ],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {space_miss.mission_name}")
        print(f"ID: {space_miss.mission_id}")
        print(f"Destination: {space_miss.destination}")
        print(f"Duration: {space_miss.duration_days} days")
        print(f"Budget: ${space_miss.budget_millions} M")
        print(f"Crew Size: {len(space_miss.crew)}")
        print("Crew members:")
        for mem in space_miss.crew:
            print(f"- {mem.name} ({mem.rank.name}) - {mem.specialization}")

    except (ValueError, ValidationError) as ve:
        print(f"{ve}")

    print("=========================================")
    print("Expected validation error:")
    try:
        crew_mem1: CrewMember = CrewMember(
            member_id="M_001",
            name="Sarah Connor",
            rank=Rank.officer,
            age=45,
            specialization="Mission Command",
            years_experience=25,
            is_active=True
        )

        crew_mem2: CrewMember = CrewMember(
            member_id="M_002",
            name="John Smith",
            rank=Rank.officer,
            age=35,
            specialization="Navigation",
            years_experience=10,
            is_active=True
        )

        crew_mem3: CrewMember = CrewMember(
            member_id="M_003",
            name="Alice Johnson",
            rank=Rank.officer,
            age=25,
            specialization="Engineering",
            years_experience=5,
            is_active=True
        )

        space_miss: SpaceMission = SpaceMission(
            mission_id="M2024_MARS",
            mission_name="Mars Colony Establishment",
            destination="Mars",
            launch_date=datetime(3100, 4, 26),
            duration_days=900,
            crew=[
                crew_mem1,
                crew_mem2,
                crew_mem3
            ],
            budget_millions=2500.0
        )
        print("Valid mission created:")
        print(f"Mission: {space_miss.mission_name}")
        print(f"ID: {space_miss.mission_id}")
        print(f"Destination: {space_miss.destination}")
        print(f"Duration: {space_miss.duration_days} days")
        print(f"Budget: ${space_miss.budget_millions} M")
        print(f"Crew Size: {len(space_miss.crew)}")
        print("Crew members:")
        for mem in space_miss.crew:
            print(f"- {mem.name} ({mem.rank.name}) - {mem.specialization}")

    except (ValueError, ValidationError) as ve:
        print(f"{ve}")
