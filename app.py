from flask import Flask
app=__name__
@app.route('/')
def home():
  return "Hello this is from the insdie of the Container"
if __name__=='__main__':
  app.run(host='0.0.0.0',port=5000)
