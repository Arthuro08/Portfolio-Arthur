import pyodbc

config = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-MLFI9DN;'
    'Database=Users_Sistema;'
    'Trusted_Connection=yes;'
)