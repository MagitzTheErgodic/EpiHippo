class UserProfile:
    def __init__(
        self, 
        first_name: str = None,
        last_name: str = None,
        gender: bool = False,
        nationality: str = "Israel",
        ID_number: int = None,
        birth_date: str = None,
        religion: str = "Jewish",
        hmo: str = None,
        clinic: str = None,
        doctor: str = None,
        doctor_phone_number: int = None,
        address = {
            city: str = None,
            street: str = None,
            house_number: str = None
        },
        number_of_people_living_with: int = None,
        house_phone_number: int = None,
        cell_phone_number: int = None
        profession: str = None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.nationality = nationality
        self.ID_number = ID_number
        self.birth_date = birth_date
        self.religion = religion
        self.hmo = hmo
        self.clinic = clinic
        self.doctor = doctor
        self.doctor_phone_number = doctor_phone_number
        self.address = address
        self.number_of_people_living_with - number_of_people_living_with
        self.house_phone_number = house_phone_number
        self.cell_phone_number = cell_phone_number
        self.profession = profession