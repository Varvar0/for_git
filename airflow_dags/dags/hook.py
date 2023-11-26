from airflow.models import BaseOperator
from airflow.hooks.base_hook import BaseHook
import argparse

class CustomDbHook(BaseHook):
    def __init__(self, conn_id):
        super().__init__(source=None)
        self.conn_id = conn_id
        self.connection = self.get_connection(conn_id)

    def get_conn(self):
        conn = self.connection
       
        return conn

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--conn_id', help='Connection id for the database', required=True)
    args = parser.parse_args()
    return args

args = parse_args()
hook = CustomDbHook(args.conn_id)
conn = hook.get_conn()

