import enum
from datetime import datetime
from typing import Optional, Self
try:
    from pydantic import BaseModel, Field, model_validator, ValidationError
except ImportError:
    print("Error: install/activate .venv and install pydantic")


class ContactType(enum.Enum):
    radio=0
    visual=1
    physical=2
    telepathic=3

    '''
•contact_id: String, 5-15 characters
•timestamp: DateTime of contact
•location: String, 3-100 characters
•contact_type: ContactType enum
•signal_strength: Float, 0.0-10.0 scale
•duration_minutes: Integer, 1-1440 (max 24 hours)
•witness_count: Integer, 1-100 people
•message_received: Optional string, max 500 characters
•is_verified: Boolean, defaults to False
    '''
class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: Optional[str] = Field(default=None, max_length=500)
    is_verified: bool = Field(default=False)

    @model_validator(mode='after')
    def validate(self) -> Self:
        if self.contact_type == ContactType.physical:
            if self.is_verified is False:
                raise ValueError("ContactType physical not verified")
        if self.contact_type is ContactType.telepathic:
            if self.witness_count < 3:
                raise ValueError("Telepathic contact requires at least 3 witnesses")
        if self.signal_strength > 7.0:
            if self.message_received is None:
                raise ValueError("Strong signal with no message received")
        if self.contact_id[:1] == 'AC':
            raise ValueError("Contact ID doesnt start with AC")
        return self

if __name__ == "__main__":
    print("Alien Contact Log Validation")
    print("======================================")
    try:
        ac_valid: AlienContact = AlienContact(
            contact_id='AC_2024_001',
            timestamp=datetime(2024,4,24),
            location='Area 51, Nevada',
            contact_type=ContactType.radio,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received='Greetings from Zeta Reticuli'
        )
        ac_valid.validate()
        print("Valid contact report:")
        print(f"ID: {ac_valid.contact_id}")
        print(f"Type: {ac_valid.contact_type.name}")
        print(f"Location: {ac_valid.location}")
        print(f"Signal: {ac_valid.signal_strength}/10")
        print(f"Duration: {ac_valid.duration_minutes}minutes")
        print(f"Witnesses: {ac_valid.witness_count}")
        print(f"Message: {ac_valid.message_received}")
    except (ValueError, ValidationError) as ve:
        print(f"{ve}")

    print("======================================")
    try:
        ac_not_valid: AlienContact = AlienContact(
            contact_id='AC_2024_001',
            timestamp=datetime(1998,4,26),
            location='Area 51, Nevada',
            contact_type=ContactType.telepathic,
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received='Greetings from Zeta Reticuli'
        )
        ac_not_valid.validate()
    except (ValueError, ValidationError) as ve:
        print(f"{ve}")