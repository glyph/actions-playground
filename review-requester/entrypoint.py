#!/e/bin/python3.7

from os import environ
from twisted.internet import defer, task
from gidgethub.treq import GitHubAPI

async def main(reactor):
    with open("workflow/event.json") as f:
        print("EVENT JSON", f.read())
    gh = GitHubAPI("", oauth_token=environ["GITHUB_TOKEN"])
    print(await gh.getitem("/repos/glyph/actions-playground/issues/comments/1"))

task.react(lambda reactor, *argv: defer.ensureDeferred(main(reactor)))
