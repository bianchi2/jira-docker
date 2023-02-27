# import docker
from python_on_whales import DockerClient
import os

docker = DockerClient()

platforms = ['linux/arm64', 'linux/amd64']
repo = 'eivantsov/jira'
tags = ['9.4.0']

PASSWORD = os.getenv('DOCKER_PASSWORD')
docker.login(username='eivantsov', password=PASSWORD)

build = docker.buildx.build(build_args={'JIRA_VERSION': tags[0]}, context_path='.', platforms=platforms,
                            output={'type': 'registry', 'name': repo}, tags=[repo+':'+tags[0]], stream_logs=True)

for line in build:
    print(line)
