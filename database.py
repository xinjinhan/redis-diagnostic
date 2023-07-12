#!/usr/bin/env python
# -*- coding:utf-8 _*-

import aiomongo
import aiomysql
from ccms_server import server
import ssl


async def mysql_engine(app):
    db_secret = server.get_db_secret(app['ccms_client'])
    db_conf = app['config']['database']
    #mysql_conf = app['config']['database']
    host, port, user, password, db, ssl_ca_path = db_conf['host'], int(db_conf['port']), db_secret.username, \
                                                  db_secret.password, db_conf['db'], db_conf['certFile']
    ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ssl_ctx.load_verify_locations(cafile=ssl_ca_path)
    app['mongo_engine'] = await aiomongo.create_client(host=host, port=port, user=user, password=password, db=db,
                                                     loop=app.loop, ssl=ssl_ctx)
    yield
    app['mysql_engine'].close()
    await app['mysql_engine'].wait_closed()
