FROM fedora:31
MAINTAINER https://jobber.randomuser.org

RUN dnf update -y && dnf clean all
RUN dnf install -y python-setuptools GitPython git buildbot-slave buildbot && dnf clean all

RUN mkdir -p /srv/buildbot

ADD ./src /srv/jobber
RUN cd /srv/jobber && python setup.py develop

RUN buildslave create-slave -r /srv/buildbot/jobber-slave jobber-master:9989 jobber-slave 'PLACEHOLDER'

WORKDIR /srv/buildbot/jobber-slave 
CMD buildslave start && tail -f twistd.log
