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

### Difference Between root and alias on NGINX
- **root:** Specifies the document root directory where files will be served from.
- **alias:** Creates a mapping between a URI and a specific location in the file system, allowing files to be served from outside the document root.

## What is a tgz archive?
A `.tgz` archive, also known as a tarball, combines the capabilities of two Unix/Linux utilities: **tar** and **gzip**. It's a common way to bundle multiple files and directories into a single compressed file for distribution or backup purposes. The .tgz extension indicates that the archive has been created by first using tar to bundle the files and directories together, and then using gzip to compress the resulting archive.

Here's how you can create a .tgz archive from the command line:
```shell
tar -czvf archive_name.tgz file1 file2 directory1
```
Explanation of the options used:

- ***-c***: Create a new archive.
- ***-z***: Compress the archive using gzip.
- ***-v***: Verbose mode (optional, shows the files being archived).
- ***-f***: Specify the filename of the archive.

To extract files from a .tgz archive, you can use:
```shell
tar -xzvf archive_name.tgz
```
This command will extract the contents of the archive while preserving the directory structure.
### With Python
In Python, you can create and extract .tgz archives using the tarfile module:
```py
import tarfile

# Create a .tgz archive
with tarfile.open('archive_name.tgz', 'w:gz') as tar:
    tar.add('file1')
    tar.add('file2')
    tar.add('directory1')

# Extract a .tgz archive
with tarfile.open('archive_name.tgz', 'r:gz') as tar:
    tar.extractall()
```
In the above code:

- **open('archive_name.tgz', 'w:gz')** opens the archive for writing and gzip compression.
- **tar.add('file1')** adds file1 to the archive.
- **tar.extractall()** extracts all files from the archive to the current directory.

`.tgz` archives are commonly used for packaging software distributions, transferring files over the internet, or creating backups due to their efficient compression and preservation of directory structure.

## Let's connect
**Twitter:** https://twitter.com/_ELOUARDY \
**Email:** ouadia@elouardy.com
