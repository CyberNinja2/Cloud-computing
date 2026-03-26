vi Dockerfile
FROM python:3.10-slim
WORKDIR /app
copy..
Run pip install -r requirements.txt
  CMD["python 3", "app.py"]

vi app.py
 app=Flask(--name--)
  @app.route ('/')
  def hello():
    return "hello from CI/CD automated container"
     if __name__ =="__main__":
      app.run (host:"0.0.00",port=8000)
~                                                                                                                                                                                          
~                                                            
