# Temporary production setup (while CI is WIP)

These commands are to set up a production server with letsencrypt without CI.
All of this will be replaced by the CI system once it is done.

### Step 1: Building the frontend app

```
 docker-compose run --rm frontend /bin/sh -c 'yarn install && yarn prod'
```

### Step 2: Starting the production containers

```
docker-compose -f docker-compose.yml -f docker-compose.production.yml up -d --build
```

### Step 3: Configuring nginx with SSL

```
domain=staging.skael.com
ip=$(sudo docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(sudo docker-compose -f docker-compose.yml -f docker-compose.production.yml ps -q frontend_prod))

apt-get install letsencrypt
letsencrypt -d "$domain" certonly
openssl dhparam -out /etc/ssl/certs/dhparam.pem 2048

apt-get install nginx
cat > /etc/nginx/sites-available/default <<<EOF
server {
  listen 80 default_server;
  listen [::]:80 default_server;
  server_name _;
  return 301 https://$host$request_uri;
}

server {
  server_name DOMAIN;
  # SSL configuration

  listen 443 ssl http2 default_server;
  listen [::]:443 ssl http2 default_server;

  ssl_protocols TLSv1 TLSv1.1 TLSv1.2;
  ssl_prefer_server_ciphers on;
  ssl_ciphers "EECDH+AESGCM:EDH+AESGCM:AES256+EECDH:AES256+EDH";
  ssl_ecdh_curve secp384r1;
  ssl_session_cache shared:SSL:10m;
  ssl_session_tickets off;
  ssl_stapling on;
  ssl_stapling_verify on;
  resolver 8.8.8.8 8.8.4.4 valid=300s;
  resolver_timeout 5s;
  # disable HSTS header for now
  #add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload";
  add_header X-Frame-Options DENY;
  add_header X-Content-Type-Options nosniff;

  ssl_dhparam /etc/ssl/certs/dhparam.pem;

  ssl_certificate /etc/letsencrypt/live/DOMAIN/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/DOMAIN/privkey.pem;

  location / {
    proxy_pass http://DOCKERIP:4200;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header Host $host;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
  }
}
EOF
perl -p -i -e "s/DOMAIN/$domain/g; s/DOCKERIP/$ip/g" /etc/nginx/sites-available/default
update-rc.d nginx enable
service nginx start
```

### Rebuilding after a code change

Once a developer has pushed a change to master, you can rebuild and deploy by doing:

```
docker-compose down
```

and reexecuting commands from (step 1) and (step 2).
