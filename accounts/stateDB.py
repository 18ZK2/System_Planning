import sqlite3 
from .models import EmployeeState
from .forms import RadioForm


conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor


conn.commit()
conn.close