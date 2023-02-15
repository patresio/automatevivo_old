import configparser

cfg = configparser.ConfigParser()

cfg.read('Config.ini')

cpf = cfg.get('usuario','user')
email = cfg.get('usuario', 'email')
senha = cfg.get('usuario', 'password')