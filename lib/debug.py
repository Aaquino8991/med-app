from models.__init__ import CURSOR, CONN
from models.doctor import Doctor
from models.patient import Patient

def reset_table():

    Doctor.drop_table()
    Doctor.create_table()

    Patient.drop_table()
    Patient.create_table()

reset_table()

import ipdb; ipdb.set_trace()