import docker
import os

platforms = ['linux/arm64', 'linux/amd64']
repo = 'eivantsov/jira'
tag = '9.4.0'
client = docker.from_env()

ARCH = os.getenv('ARCH')
PASSWORD = os.getenv('DOCKER_PASSWORD')

auth_config = {'username': 'eivantsov', 'password': PASSWORD}
print(f'Building Jira for {ARCH} architecture')
build = client.api.build(quiet=False, buildargs={'JIRA_VERSION': tag}, path='.', platform=ARCH,
                         tag=repo+':'+tag)

for line in build:
    print(line)

push = client.api.push(
    repo+':'+tag,
    stream=True,
    decode=True,
    auth_config=auth_config
)

for line in push:
    print(line)
