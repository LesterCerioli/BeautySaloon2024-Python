from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class District:
    district_name: Optional[str]

    def __post_init__(self):
        # You can add any additional initialization logic here
        pass

    def __eq__(self, other) -> bool:
        if not isinstance(other, District):
            return False
        return self.district_name == other.district_name

    def __hash__(self) -> int:
        return hash(self.district_name)

    def __str__(self) -> str:
        return self.district_name or ""

    # Custom method to get equality components
    def get_equality_components(self) -> list[Optional[str]]:
        # Return a list of components used to determine equality
        return [self.district_name]
