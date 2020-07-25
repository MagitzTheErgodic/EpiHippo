class ClinicProfile:
    def __init__(
        self, 
        disease_begin_date: str = None,
        symptoms: {
            max_heat: int = None,
            cough: bool = False,
            sore_throat: bool = False,
            shortness_of_breath: bool = False
            chills: bool = False,
            head_aches: bool = False,
            muscle_aches: bool = False,
            stomach_aches: bool = False,
            throwup: bool = False,
            diarrheas: bool = False,
            other: str = None
        },
        medical_background: {
            heart_disease: bool = False,
            diabetes: bool = False,
            blood_pressure: bool = False,
            pregnant: bool = False,
            Immunodeficiency: bool = False,
            chronic_lungs_disease: bool = False,
            chronic_liver_disease: bool = False,
            other: str = None
        },
        additional_details: {
            hepoxy: bool = False,
            flu_vaccination: bool = False,
            chest_x_ray: str = None
        },
        hospitalization: {
            hospitalization: bool = False,
            hospital: str = None,
            start_date: str = None,
            end_date: str = None,
            hospitalization_type: str = None
        }
    ):
        self.disease_begin_date = disease_begin_date
        self.symptoms = symptoms
        self.medical_background = medical_background
        self.additional_details = additional_details
        self.hospitalization = hospitalization