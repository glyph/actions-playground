FROM python:3.7

LABEL "com.github.actions.name"="Re-request reviews and stuff"
LABEL "com.github.actions.description"="Like... do stuff? when comments?"
LABEL "com.github.actions.icon"="mic"
LABEL "com.github.actions.color"="purple"

LABEL "repository"="http://github.com/glyph/actions-playground"
LABEL "homepage"="http://github.com/glyph/actions-playground"
LABEL "maintainer"="Glyph <glyph@twistedmatrix.com>"

RUN apt update -qyy;
RUN python3.7 -m venv /e;
RUN /e/bin/pip install gidgethub treq hyperlink;
ADD entrypoint.py /entrypoint.py

ENTRYPOINT ["/entrypoint.py"]
