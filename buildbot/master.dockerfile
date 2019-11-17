FROM fedora
MAINTAINER https://jobber.randomuser.org

RUN dnf update -y --setopt="deltarpm=0" && dnf clean all
RUN dnf install -y PyYAML python-setuptools packagedb-cli GitPython git buildbot-master  && dnf clean all

RUN mkdir -p /srv/buildbot

ADD src /srv/jobber
RUN cd /srv/jobber && python setup.py develop

RUN buildbot create-master -r /srv/buildbot/anerist
ADD ./resources/buildbot/master.py /srv/buildbot/anerist/master.cfg

EXPOSE 8010
EXPOSE 9989

WORKDIR /srv/buildbot/anerist 
CMD buildbot start || tail -f twistd.log
