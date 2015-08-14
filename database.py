import os
from sqlalchemy import create_engine

#if os.path.exists('/tmp/brecorder.db'):
#    os.unlink('/tmp/brecorder.db')

engine = create_engine('sqlite:////tmp/brecorder.db', echo=True)
