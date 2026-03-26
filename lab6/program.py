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

requirements.py
flask

deploy.sh
#!/bin/bash
port=8000
echo "Building Docker image..."
  docker build -t myapp:latest .
echo "stopping old containers..."
  docker stop myapp//true
echo "Running new container on port $port..." 
  docker run -d __name myapp -p $port:8080 myapp:latest
echo"App deployment"
echo "use killercoda Traffic tab port $port"
~                                                                                                                                                                                          
~                                                                                                                                                                                          
~                                                                                                                                                                                          
~                                                                                                                                                                                          
~                                                                                                                                                                                          
~                                                                                        
