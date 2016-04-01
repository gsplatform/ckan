#from __future__ import with_statement
import sys
sys.path.append('/usr/lib/python2.6/site-packages/daemon')
import daemon
import runner
import os
import pidlockfile
import ckanserviceprovider.web as web
import time
import jobs

from daemon import DaemonContext
from pidlockfile import PIDLockFile

# check whether jobs have been imported properly
assert(jobs.push_to_datastore)

#dc = DaemonContext(
#    pidfile=PIDLockFile('/tmp/dtpusher.pid'),stderr=open('/var/log/stderr.txt', 'w+'))

class App:

    def __init__(self):
        print time.strftime('%Y-%m-%d %H:%M:%S start')
        #self.stdin_path = '/dev/null'
        self.pidfile_timeout = 10
        #self.directory = os.path.expanduser('~/.test/')
        #if not os.path.isdir(self.directory):
        #    os.mkdir(self.directory)
        #self.pidfile_path = os.path.join(self.directory, 'test.pid')
        print time.strftime('%Y-%m-%d %H:%M:%S start2')

def run():
        while True:
           print time.strftime('%Y-%m-%d %H:%M:%S start3')
           os.environ['JOB_CONFIG'] = os.path.abspath('deployment/datapusher_settings.py')
           web.init()
           web.app.run(web.app.config.get('HOST'), web.app.config.get('PORT'))

def main():
    daemon_runner = runner.DaemonRunner(run())
#    lockfile = runner.make_pidlockfile('/tmp/dtpusher.pid', 1)
#    if lockfile.is_locked():
#       print 'It looks like a daemon is already running!'
#       exit()
    daemon_runner.do_action()

if __name__ == '__main__':
    main()

