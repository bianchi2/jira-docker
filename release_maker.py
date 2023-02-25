import docker

client = docker.from_env()

build = client.api.build(quiet=False, path='/Users/yivantsov/projects/atlassian-docker/test1', platform='linux/arm64',
                         tag='eivantsov/nodejs:1.0.0')

for line in build:
    print(line)

push = client.api.push(
    'eivantsov/nodejs:1.0.0',
    stream=True,
    decode=True,
)

for line in push:
    print(line)
