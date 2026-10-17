class Patient:
    patient_count = 0

    def __init__(self, patient_id, name, age, condition):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.condition = condition
        Patient.patient_count += 1

    def update_record(self, new_condition):
        self.condition = new_condition

    def display_info(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Condition: {self.condition}")

    @classmethod
    def total_patients(cls):
        return cls.patient_count

    @staticmethod
    def valid_age(age):
        return isinstance(age, int) and 0 <= age <= 120


class Doctor:

    def __init__(self, doctor_id, name, specialty):
        self.doctor_id = doctor_id
        self.name = name
        self.specialty = specialty

    def view_patient(self, patient):
        print(f"\nDoctor: {self.name}")
        print(f"Specialty: {self.specialty}")
        print(f"Reviewing patient: {patient.name}")
        print(f"Condition: {patient.condition}")


# Dictionary for storing patient objects
patients = {}


def add_patient(patient):
    patients[patient.patient_id] = patient
    print(f"Patient {patient.name} added successfully.")


def display_all_patients():
    print("\n===== ALL PATIENT RECORDS =====")

    for patient in patients.values():
        patient.display_info()
        print("------------------------------")


# Create Patient objects
patient1 = Patient("P001", "Mohamed Kamara", 22, "Malaria")
patient2 = Patient("P002", "Fatmata Sesay", 25, "Routine check-up")
patient3 = Patient("P003", "Abdul Conteh", 30, "Asthma")

# Create Doctor object
doctor1 = Doctor("D001", "Dr. Ibrahim", "General Medicine")


# Add patients to dictionary
add_patient(patient1)
add_patient(patient2)
add_patient(patient3)


# Display all patients
display_all_patients()


# Update a patient record
print("\n===== UPDATING RECORD =====")
patient1.update_record("Recovered")
patient1.display_info()


# Doctor interacts with patient
doctor1.view_patient(patient1)


# Static method
print("\n===== STATIC METHOD =====")
print("Is age 22 valid?", Patient.valid_age(22))
print("Is age 150 valid?", Patient.valid_age(150))


# Class method
print("\n===== CLASS METHOD =====")
print("Total patients:", Patient.total_patients())