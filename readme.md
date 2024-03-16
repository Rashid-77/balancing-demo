This demo shows typical infrastrucuture to achieve load balance and fault tolerance for web app and db.

**Start mysql cluster**

<code>docker compose -f msql-percona-cluster/docker-compose.yml build</code>

<code>docker compose -f msql-percona-cluster/docker-compose.yml up -d</code>

**Populate db with data**

Set your "master_db" IP in fill_db.py of "common" folder

Install requirements from "common" folder and fill master_db with data

<code>python3 common/fill_db.py </code>

**Start haproxy**

<code>docker compose -f haproxy/docker-compose.yml build</code>

<code>docker compose -f haproxy/docker-compose.yml up</code>

**Start web application cluster**

Open one more terminal:

<code>docker compose -f app_cluster/docker-compose.yml build</code>

<code>docker compose -f app_cluster/docker-compose.yml up</code>

Get nginx_lb IP address and set nginx host name "nginx-lb.test" to the /etc/hosts

In another terminal you can watch docker containers state:

<code>docker stats</code>

Open one more terminal and use curl to check cluster works:

<code>curl http://nginx-lb.test/api/v1/users/1</code>

or

<code>ab -n 10000 http://nginx-lb.test/api/v1/users/1</code>

During AB test you can kill one of the mysql slave_db, and check if all ok.
