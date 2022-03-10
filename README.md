# Solien Gallery

To learn more about this project, please read the doumentation in the documentation folder.

If you're interested in the project at large checkout the ProjectOverview. If you're interested in the system and design, take a look at the ProgrammersGuide.

## Instructions to run `runserver.py`

### Install Python with the default settings:
https://www.python.org/downloads/

### Download the latest version of Redis:
https://redis.io/ <br />

Windows users should follow this tutorial: https://redis.com/blog/redis-on-windows-10/. Unfortunately, it's a little tedious. You will need to use Ubuntu.

### Run the following commands in terminal:
`pip install cloudinary` <br />
`pip install flask` <br />
`pip install imageio` <br />
`pip install pillow` <br />
`pip install rq` <br />
`pip install theblockchainapi`

### Run the server:
`redis-server`
`python worker.py`
`python runserver.py 8080`

The server should be on port 8080.
