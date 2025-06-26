# DevOps Intern Assignment: Nginx Reverse Proxy + Docker

📁 Project Structure

<pre>
.  
├── docker-compose.yml  
├── nginx  
     ├── nginx.conf  
     └── Dockerfile  
├── service_1  
     ├── Dockerfile  
     ├── README.md  
     ├── go.mod  
     └── main.go  
├── service_2  
      ├── Dockerfile  
      ├── README.md  
      ├── app.py  
      ├── requirements.txt  
      ├── pyproject.toml  
      └── uv.lock  
└── README.md (this file)
</pre>

🚀 Setup Instructions
1. Clone the Repository

  <pre>git clone https://github.com/Manojravichandran0307/DevOps-Intern-Assignment.git
cd DevOps-Intern-Assignment</pre>  
   
2. Build and Run the Application   


<pre>sudo docker-compose up --build</pre>
This command will build and start all three services:  

service1: Golang application on port 8001  

service2: Python Flask application on port 8002  

nginx_proxy: Reverse proxy accessible on localhost:8080  

3. Test the Endpoints
   
<pre>curl http://localhost:8080/service1/hello   
curl http://localhost:8080/service2/hello  
curl http://localhost:8080/service2/ping  
</pre>

🔁 How Routing Works

The Nginx container listens on port 80, which is mapped to host's 8080. It routes based on path prefix as follows:  
* /service1 → routed to Golang app (Service 1) at service1:8001  

* /service2 → routed to Python app (Service 2) at service2:8002

Nginx Configuration Snippet:

<pre>
location /service1/ {
    proxy_pass http://service1:8001/;
}

location /service2/ {
    proxy_pass http://service2:8002/;
}
</pre>

Bonus Implementations  

✅ Health Checks: Each service is health-checked using curl in docker-compose.yml  

✅ Custom Logging: Nginx logs incoming requests with a custom log format:

<pre>log_format custom '$remote_addr - [$time_local] "$request"';
access_log /var/log/nginx/access.log custom;</pre>

✅ Single Port Access: All services are accessible via localhost:8080

✅ Bridge Networking: Docker's default bridge network used (no host networking)

🧪 Example Output
<pre>
$ curl http://localhost:8080/service1/hello
{"message":"Hello from Service 1"}

$ curl http://localhost:8080/service2/hello
{"message":"Hello from Service 2"}

$ curl http://localhost:8080/service2/ping
{"service":"2","status":"ok"}
</pre>
