# -*- python -*-
# ex: set syntax=python:

from buildbot.schedulers.basic import SingleBranchScheduler
from buildbot.schedulers.basic import AnyBranchScheduler
from buildbot.schedulers.forcesched import ForceScheduler
from buildbot.changes.filter import ChangeFilter
from buildbot.scheduler import Nightly
c = BuildmasterConfig = {}

####### BUILDSLAVES
from buildbot.buildslave import BuildSlave
c['slaves'] = [
        BuildSlave("anerist-slave", "PLACEHOLDER"),
	]
c['protocols'] = {'pb': {'port': 9989}}

####### CHANGESOURCES

from buildbot.changes.gitpoller import GitPoller
import random

####### BUILDERS

from buildbot.process.factory import BuildFactory
from buildbot.steps.source.git import Git
from buildbot.steps.shell import ShellCommand
from buildbot.steps.transfer import DirectoryUpload
from buildbot.process.properties import Interpolate
from datetime import datetime
from anerist.buildsteps import *

def _make_factory_step_generator(project_name, project_git_uri, make_command=None, workdir="/srv/buildbot"):
    make_factory_steps = [
            Git(
                name = "Executing %s content fetch" % project_name,
                repourl=project_git_uri,
                mode='incremental'
                ),
            ShellCommand(
                name = "Executing %s: 'make %s'" % ( project_name, make_command ),
                command = [
                    "make",
                    make_command
                    ]
                ),
            DirectoryUpload(
                slavesrc="build",
                masterdest=Interpolate(
                    "/srv/output/%(kw:project_name)s/%(src::branch)s", 
                    ) 
                )
            ]
    return make_factory_steps
from buildbot.config import BuilderConfig

lan_buildslaves = []
lan_buildslaves.append("anerist-slave")

all_publican_builders = [] 
all_translation_builders = {}
c['schedulers'] = []
c['change_source'] = []
c['builders'] = []
defined_factories = {}

pp = {
    'name': 'Placeholder Project',
    'uri': 'https://gitlab.randomuser.org/pete/placeholder.git',
    'command': all
    'branches' = ChangeFilter(
        branch_fn = [
            'master'
            ]
        )

   }
defined_factories['pp_maker_factory'] = BuildFactory(
        _make_factory_step_generator(pp['name'], pp['uri'], pp['command'] )
    )
c['change_source'].append(GitPoller(
        pp['uri'], 
        workdir='/srv/buildbot',
        branches=pp['branches'],
        pollinterval=random.randint(300,600)
        ))
c['builders'].append(
    BuilderConfig(
        name='%s Builder' % pp['name'],
        slavenames=lan_buildslaves,
        factory=defined_factories['pp_maker_factory']
        )
    )
c['schedulers'].append(AnyBranchScheduler(
    name="%s_scheduler" % guide_publisher,
    builderNames=['%s Builder' % pp['name']],
    change_filter=pp['branches'],
    treeStableTimer=None
    ))
