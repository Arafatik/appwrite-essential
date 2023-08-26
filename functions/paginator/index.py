import random

def main(req, res):
  payload = req.payload or 'No payload provided. Add custom data when executing function.'

  secretKey = req.variables.get(
    'SECRET_KEY',
    'SECRET_KEY variable not found. You can set it in Function settings.'
  )

  randomNumber = random.random()

  trigger = req.variables['APPWRITE_FUNCTION_TRIGGER']

  return res.json({
    'message': 'Hello from Appwrite!',
    'payload': payload,
    'secretKey': secretKey,
    'randomNumber': randomNumber,
    'trigger': trigger,
  })
