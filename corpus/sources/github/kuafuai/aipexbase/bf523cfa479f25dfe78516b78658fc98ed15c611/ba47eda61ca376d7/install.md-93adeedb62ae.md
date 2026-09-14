# Docker Compose Deployment Guide

## Prerequisites
- Linux
- Docker
- Docker Compose v2.5 or higher


## Configuration

##### Edit ./install/docker-compose.yaml

- Modify the log output mount directory for the `backend-new` service (default is acceptable)
- Modify the MySQL data directory for the `mysql-new` service
- Configure the port numbers for exposing services as needed
- Other items can remain as default. Modify as needed.

## Running
```bash
docker-compose up -d
```


## Notes
If you are setting up a proxy service externally to forward requests to AIPEXBASE, configure the following proxy settings. Example nginx configuration snippet:
```bash
    location / {
        root /usr/share/nginx;
        try_files $uri $uri/ /index.html;
    }
    location /baas-api {
        proxy_pass http://1.1.1.1:8080;
        rewrite ^/baas-api/(.*)$ /$1 break;
        proxy_set_header REMOTE-HOST $remote_addr;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    location /mcp {
       proxy_pass http://1.1.1.1:8080;
       proxy_set_header Host $host;

       # Preserve client real IP
       proxy_set_header X-Real-IP $remote_addr;
       proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
       proxy_set_header X-Forwarded-Proto $scheme;
       proxy_set_header Connection '';
       proxy_http_version 1.1;
       proxy_buffering off;
       proxy_cache off;

       # Maintain long connection
       proxy_read_timeout 86400s;
       proxy_send_timeout 86400s;
    }
```
