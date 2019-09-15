#!/e/bin/python3.7

from os import environ
from json import load

from twisted.internet import defer, task
from gidgethub.treq import GitHubAPI
from hyperlink import parse as parse_url

async def main(reactor):
    with open(environ['GITHUB_EVENT_PATH']) as f:
        event = load(f)
    labels_url = event['issue']['labels_url']
    command = event['comment']['body']
    cmdwords = command.strip().split(" ")
    gh = GitHubAPI("glyph-actions-playground", oauth_token=environ["GITHUB_TOKEN"])
    if cmdwords[0] == '/label':
        label = cmdwords[1]
        await gh.post(labels_url, data=[label])
    elif cmdwords[0] == '/unlabel':
        label = cmdwords[1]
        await gh.delete(parse_url(labels_url).child(label).to_text())
    else:
        print("nevermind")
        return

task.react(lambda reactor, *argv: defer.ensureDeferred(main(reactor)))
