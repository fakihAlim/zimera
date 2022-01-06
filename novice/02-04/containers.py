from dependency_injector import containers, providers
from email_client import EmailClient
from email_reader import EmailReader as er


class Configs(containers.DeclarativeContainer):
    config = providers.Configuration("config")


class Clients(containers.DeclarativeContainer):
    email_client = providers.Singleton(EmailClient, Configs.config)


class Readers(containers.DeclarativeContainer):
    er = providers.Factory(er, client=Clients.email_client)
