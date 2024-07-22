import yaml
import psycopg2
from sqlalchemy import create_engine
from sqlalchemy import inspect




class DataConnector:
    def __init__(self):
        self.alchemy_engine = None
        self.db_cred = None

    def read_db_creds(self, cred_file_path):
        """_summary_
         Read the database credentials from a YAML file and initialise the database engine
        Parameters
        ----------
        cred_file_path : (str)
            _description_

        Returns
        -------
         sqlalchemy.engine.base.Engine: The initialized SQLAlchemy engine
        """
        with open(cred_file_path, 'r') as file:
            self.db_cred = yaml.safe_load(file)
        return self.init_db_engine(self.db_cred)

    def init_db_engine(self, db_cred):
        """_summary_
         Initialise a SQLAlchemy engine using the provided database credentials
        Parameters
        ----------
        db_cred : Dictionary containing database credentials

        Returns
        -------
          sqlalchemy.engine.base.Engine: The initialized SQLAlchemy engine
        """
        DATABASE_TYPE = 'postgresql'
        DBAPI = 'psycopg2'
        # defining alchemy_engine
        self.alchemy_engine = create_engine(
            f"{DATABASE_TYPE}+{DBAPI}://{db_cred['RDS_USER']}:"
            f"{db_cred['RDS_PASSWORD']}@{db_cred['RDS_HOST']}:"
            f"{db_cred['RDS_PORT']}/{db_cred['RDS_DATABASE']}"
        )

        return self.alchemy_engine

    def list_db_tables(self):
        """_summary_
         List all the tables in  connected database.
        Parameters
        Returns
        -------
       list:  list of table names in the database.
        """
        inspector = inspect(self.alchemy_engine)
        return print(inspector.get_table_names())

    def upload_to_db(self, engine, table_name, data_frame):
        """_summary_
        Upload a data to the specified table in  database.
        Parameters
        ----------
        engine : The SQLAlchemy engine connected to the database
        table_name :(str): The name of the table where the data will be uploaded
        data_frame :(pandas data frame) The DataFrame containing the data to be uploaded
        """
        try:
            data_frame.to_sql(table_name, engine,
                              index=False, if_exists='replace')
            print(f"Data uploaded to {table_name} successfully.")
        except Exception as e:
            print(f"Error uploading data to legacy_users: {e}")
            