# globals.py

class DbConfig:
    def __init__(self):
        self.some_global_value = "Initial Value"
        self.database_connection = None  # Placeholder for a database connection object

        # database connection
        self.host = "167.71.208.107"
        # self.host = "46.101.226.144"
        self.port = 3306
        self.user = "kolab"
        self.password = "Qazplm_123Qazplm"
        self.database = "kolab"

# Create an instance of GlobalVars to be used throughout the application
db_config = DbConfig()

