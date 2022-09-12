#!/usr/bin/python

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

import os.path

class FileTransferObject( object ):
  def __init__ (self,source_directory,source_file,target_directory,target_file):
    def setSourceDirectory( self, directoryString ):
      if ( not os.path.dirname( directoryString ) ):
        raise_error( 'Directory ' + directoryString + 'does not exist\n', True )
        self.source_directory = os.path.dirname( directoryString )

    def setSourceFile( self, fileString ):
      if ( not os.path.basename( fileString ) ):
        raise_error( 'File ' + fileString + ' does not exist!\n', True )
        self.source_file = os.path.basename( fileString )

    def setTargetDirectory( self, directoryString ):
      if ( not os.path.dirname( directoryString ) ):
        raise_error( 'Directory ' + directoryString + ' does not exist!\n', True )
        self.target_directory = os.path.dirname( directoryString )

    def setTargetFile( self, fileString ):
      if ( not os.path.basename( fileString ) ):
        raise_error( 'File ' + fileString + ' does not exist!\n', True )
        self.target_file = os.path.basename( fileString )

    def getSourceDirectory( self ):
      return self.source_directory

    def getSourceFile( self ):
      return self.source_file

    def getTargetDirectory( self ):
      return self.target_directory

    def getTargetFile( self ):
      return self.target_file