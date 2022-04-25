# coding=utf-8
import argparse
import logging
import os

from declarative import Base
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy_utils import database_exists, create_database


LOGGING_LEVEL = os.environ.get(
    'INITIALIZE_DATABASE_LOGGING_LEVEL',
    'INFO'
)

STR_CONNECTION = os.environ.get(
    'STR_CONNECTION',
    'mysql://user:pass@localhost:3306/usage'
)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-l',
        '--loglevel',
        default=LOGGING_LEVEL,
    )

    params = parser.parse_args()

    logging.basicConfig(level=params.loglevel,
                        format='[%(asctime)s] %(levelname)s %(message)s',
                        datefmt='%d/%b/%Y %H:%M:%S')

    try:
        ENGINE = create_engine(STR_CONNECTION)
        if not database_exists(ENGINE.url):
            create_database(ENGINE.url)
            logging.info(f'Banco de dados {ENGINE.url} foi criado')
    
        Base.metadata.create_all(ENGINE)
        logging.info(f'Estrutura de tabelas COUNTER R5 & SUSHI foi criada')
    except OperationalError:
        logging.error(f'Não foi possível conectar-se ao banco de dados por meio de {STR_CONNECTION}. Defina corretamente a variável de ambiente STR_CONNECTION.')
