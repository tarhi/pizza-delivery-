from dependency_injector import containers, providers
from app.auth.repositories import AuthRepositories
from app.auth.services import AuthServices
from app.bd.database import Database
from app import bd



class Containers(containers.DeclarativeContainer):
    config = providers.Configuration()
    
    bd = providers.Singleton(Database, db_url = config.services.app.environnement.SQLITE_URL)
    
    
# auth 

auth_reporsitory = providers.Factory(
    AuthRepositories,
    session_factory= bd.provided.session
)

auth_services = providers.Factory(
    AuthServices,
    auth_reporsitory=auth_reporsitory
)