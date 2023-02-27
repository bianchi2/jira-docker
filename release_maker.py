# import docker
from python_on_whales import DockerClient
import os

docker = DockerClient()

platforms = ['linux/arm64', 'linux/amd64']
repo = 'eivantsov/jira'
tags = ['9.4.0']

ARCH = os.getenv('ARCH')
PASSWORD = os.getenv('DOCKER_PASSWORD')
print(PASSWORD)
docker.login(username='eivantsov', password=PASSWORD)

build = docker.buildx.build(build_args={'JIRA_VERSION': tags[0]}, context_path='.', platforms=platforms,
                            tags=tags, stream_logs=True, push=True)

for line in build:
    print(line)
