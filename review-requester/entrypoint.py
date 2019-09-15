#!/e/bin/python3.7

from os import environ
from json import load

from twisted.internet import defer, task
from gidgethub.treq import GitHubAPI

async def main(reactor):
    with open(environ['GITHUB_EVENT_PATH']) as f:
        event = load(f)
    labels_url = event['issue']['labels_url']
    command = event['comment']['body']
    cmdwords = command.strip().split(" ")
    if cmdwords[0] == '/label':
        label = cmdwords[1]
        operation = 'append'
    elif cmdwords[0] == '/unlabel':
        label = cmdwords[1]
        operation = 'remove'
    else:
        print("nevermind")
        return
    gh = GitHubAPI("glyph-actions-playground", oauth_token=environ["GITHUB_TOKEN"])
    llist = [each['name'] for each in (await gh.getitem(labels_url))]
    print("got", llist)
    getattr(llist, operation)(label)
    print("modified", llist)
    await gh.post(labels_url, data=llist)

task.react(lambda reactor, *argv: defer.ensureDeferred(main(reactor)))
