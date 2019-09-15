FROM python:3.7

LABEL "com.github.actions.name"="Re-request reviews and stuff"
LABEL "com.github.actions.description"="Like... do stuff? when comments?"
LABEL "com.github.actions.icon"="mic"
LABEL "com.github.actions.color"="purple"

LABEL "repository"="http://github.com/glyph/actions-playground"
LABEL "homepage"="http://github.com/glyph/actions-playground"
LABEL "maintainer"="Glyph <glyph@twistedmatrix.com>"

RUN apt update;
RUN pip install gidgethub treq;
ADD entrypoint.py /entrypoint.py

ENTRYPOINT ["/entrypoint.py"]
