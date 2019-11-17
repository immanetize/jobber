.. abstract::
  The jobber runs random jobs.


=============
 jobber
=============
----------------------
your job running buddy
----------------------
jobber is a buildbot instance and swiss army knife cli tool.

Quick Start
===========
pick a shortname for your projects. /[a-z0-9_]*/ please.
::
   git clone https://github.com/immanetize/jobber.git yourproject
   cd yourproject
   git remote rename origin jobber-template # you probably won't reference this again
   git remote add origin git@github.com:youruser/yourproject
   find . -not -path '*git*' -type f -exec sed -i -e 's/jobber/yourproject/g' {} \;
   git add -u; git commit -m 'create yourproject from jobber template'
   git push --set-upstream origin master



