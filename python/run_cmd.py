import os
import re
import pwd
import sys
import time
import Queue
import random
import signal
import logging
import smtplib
import datetime
import threading
import subprocess

def run_cmd(cmd, timeout=None):

    """run_cmd - Run a command and return a dict with return code and output"""

    child = subprocess.Popen(cmd,
                             shell = True,
                             stdout = subprocess.PIPE,
                             stderr = subprocess.PIPE)

    start_time = int(time.time())

    if timeout:
        kill_time = start_time + int(timeout)

    while True:
        rc = child.poll()
        if rc != None:
            # get run time
            run_time=int(time.time() - start_time)

            # get STDOUT and STDERR from the child pipe
            (stdout, stderr) = child.communicate()

            return( {'rc': rc,
                     'stdout': stdout,
                     'stderr': stderr,
                     'run_time': run_time,
                     'timed_out': False} )

        elif(timeout and time.time() > kill_time):
            # time to kill the process
            os.kill(child.pid, signal.SIGTERM)

            # get run time
            run_time=int(time.time() - start_time)

            # get STDOUT and STDERR from the child pipe
            (stdout, stderr) = child.communicate()

            return( {'rc': None,
                     'stdout': stdout,
                     'stderr': stderr,
                     'run_time': run_time,
                     'timed_out': True} )

        else:
            # Not done running, but not exceeded our maximum run time.
            # Sleep for a second and process the situation again.
            time.sleep(1)