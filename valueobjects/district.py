

class District:
    def __init__(self, district_name: str):
        self.district_name = district_name

    @classmethod
    def new_district(cls, district_name: str):
        return cls(district_name)
