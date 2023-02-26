import docker

platforms = ['linux/arm64', 'linux/amd64']
repo = 'eivantsov/jira'
tag = '9.4.0'
client = docker.from_env()

for platform in platforms:
    print(f'Building Jira for {platform} architecture')
    build = client.api.build(quiet=False, buildargs={'JIRA_VERSION': tag}, path='.', platform=platform,
                             tag=repo+':'+tag)

    for line in build:
        print(line)

    push = client.api.push(
        repo+':'+tag,
        stream=True,
        decode=True,
    )

    for line in push:
        print(line)
