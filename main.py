import os

import SSL_retriever.SSL_retriever as SSL_retriever
import config.config as config

if not os.path.exists('config.ini'):
    config.create_default_config()

SSL_retriever.ssl_getter()
