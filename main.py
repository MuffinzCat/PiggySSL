import os

import SSL_retriever.SSL_retriever as SSL_retriever
import default_config_generation.config as config

if not os.path.exists('default_config_generation.ini'):
    config.create_default_config()

SSL_retriever.ssl_getter()
