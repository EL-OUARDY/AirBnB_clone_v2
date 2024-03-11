# Deploy static — AirBnB clone
0x03. AirBnB clone - Deploy static

```DevOps```
```Python```
```SysAdmin```
```Scripting```
```CI/CD```

## CI/CD
**Continuous Integration (CI)** and **Continuous Deployment (CD)** are practices used in software development to automate the process of testing and deploying code changes. CI/CD pipelines help ensure that changes to the codebase are automatically tested and deployed in a consistent and reliable manner.

**CI** and **CD** are essential practices in modern software development, particularly in Agile and Lean methodologies. Here's a bit more about each:

## Continuous Integration (CI)
**CI** is the practice of frequently integrating code changes into a shared repository. Each integration is then verified by an automated build and automated tests. By integrating regularly, you can detect errors quickly, and locate them more easily. This allows teams to catch and fix integration errors early in the development process, reducing the time and effort required to resolve them.

Key benefits of CI include:

- **Early detection of defects:** By integrating code frequently, defects are detected and fixed early in the development process.
- **Faster feedback:** Developers receive immediate feedback on the impact of their code changes, allowing them to address issues promptly.
- **Improved collaboration:** CI encourages collaboration among team members, as it requires frequent communication and integration of code changes.

## Continuous Deployment (CD)
**CD** is the practice of automatically deploying code changes to production or staging environments after passing through the CI pipeline. It aims to automate the entire software release process, from code commit to production deployment. By automating deployment, teams can release new features and updates more frequently, reduce the risk of human error, and improve the overall efficiency of the development process.

Key benefits of CD include:

- **Faster time to market:** CD enables teams to release new features and updates more frequently, reducing the time it takes to deliver value to customers.
- **Reduced risk:** Automated deployments reduce the risk of human error and ensure consistent deployments across environments.
- **Continuous feedback:** CD provides continuous feedback on the stability and performance of the application in production, allowing teams to make informed decisions and iterate quickly.

## Fabric
Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.

## Using Fabric in Python
```py
from fabric import Connection

def deploy():
    c = Connection('your_server')
    c.run('git pull origin master')
    c.run('docker-compose up -d')
```

## Fabric and Command Line Options
Fabric provides command-line options to facilitate remote execution of tasks.
```bash
fab -H user@host deploy
```

## Nginx Configuration for Beginners
Nginx is a web server that can also be used as a reverse proxy, load balancer, and HTTP cache. Here's a basic Nginx configuration for beginners:
```nginx
server {
    listen 80;
    server_name example.com;

    location / {
        root /var/www/html;
        index index.html;
    }
}
```

## Difference Between root and alias on NGINX
- **root:** Specifies the document root directory where files will be served from.
- **alias:** Creates a mapping between a URI and a specific location in the file system, allowing files to be served from outside the document root.

## Let's connect
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
