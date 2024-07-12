
# models.py
from mongoengine import Document, StringField, IntField, ListField, EmbeddedDocumentField, EmbeddedDocument
from enum import Enum

class GenderEnum(Enum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class MedicalHistory(EmbeddedDocument):
    description = StringField(required=True)

class Prescription(EmbeddedDocument):
    medication = StringField(required=True)

class LabResult(EmbeddedDocument):
    result = StringField(required=True)

class Patient(Document):
    name = StringField(required=True, unique=True)
    age = IntField(required=True)
    gender = StringField(required=True, choices=[gender.value for gender in GenderEnum])
    medical_history = ListField(EmbeddedDocumentField(MedicalHistory))
    prescriptions = ListField(EmbeddedDocumentField(Prescription))
    lab_results = ListField(EmbeddedDocumentField(LabResult))
