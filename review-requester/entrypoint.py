#!/e/bin/python3.7

from sys import stdin
from os import environ
from twisted.internet import defer, task
from gidgethub.treq import GitHubAPI

async def main(reactor):
    print("STANDARD INPUT", stdin.read())
    gh = GitHubAPI("", oauth_token=environ["GITHUB_TOKEN"])
    print(await gh.getitem("/repos/octocat/Hello-World/issues/comments/1"))

task.react(lambda reactor, *argv: defer.ensureDeferred(main(reactor)))
