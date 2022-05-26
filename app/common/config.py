from database import dataclass, asdict
from os import path, environ

# fast-api-notification을 가리키고 있다. 
base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

@dataclass
class Config:
    """
    기본 configuration
    """
    BASE_DIR = base_dir

    DB_POOL_RECYCLE : int = 900
    DB_ECHO: bool = True

@dataclass
class LocalConfig(Config):
    PROJ_RELOAD: bool = True

@dataclass
class ProdConfig(Config):
    PROJ_RELOAD: bool = False

print(asdict(LocalConfig))

def conf():
    '''
    환경 불러오기
    :return:
    '''
    config = dict(prod = ProdConfig(), local = LocalConfig)
    return config.get(environ.get("API_ENV","local"))
    
