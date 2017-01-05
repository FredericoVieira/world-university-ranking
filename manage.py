from app import manager
from flask_script import Server
from flask_migrate import MigrateCommand
from scripts.load_data import LoadData
from os import getenv


manager.add_command('loaddata', LoadData)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server(host='0.0.0.0', port=int(getenv('PORT', 5000))))
manager.run()
