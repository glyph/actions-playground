#!/e/bin/python3.7

from os import environ
from json import load

from twisted.internet import defer, task
from gidgethub.treq import GitHubAPI

async def main(reactor):
    with open("/github/workflow/event.json") as f:
        event = load(f)
        print("comment said", event['comment']['body'])
    gh = GitHubAPI("glyph-actions-playground", oauth_token=environ["GITHUB_TOKEN"])
    print(await gh.getitem("/repos/glyph/actions-playground/issues/comments/531545265"))

task.react(lambda reactor, *argv: defer.ensureDeferred(main(reactor)))
