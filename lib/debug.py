from models.__init__ import CURSOR, CONN
from models.doctor import Doctor

def reset_table():

    Doctor.drop_table()
    Doctor.create_table()

reset_table()

import ipdb; ipdb.set_trace()