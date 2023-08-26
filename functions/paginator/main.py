import mock

from dotenv import dotenv_values

from index import main

req = mock.Mock()
req.headers = {}
req.payload = ""
req.variables = dict(dotenv_values(".env"))

res = mock.Mock()
res.send = lambda text, status = "" : print(text, status)
res.json = lambda data, status = "" : print(data, status)

main(req, res)
