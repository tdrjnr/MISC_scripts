###########################################################
## File        : SohoBaseWithSQL.py
## Description : 
'''
The base class for all jobs that need database access. 

'''

import Hydra.Util._time

import Soho.Util._time

# Class Dependencies

import SohoBase

class SohoBaseWithSQL(SohoBase.SohoBase):
    '''

    The __init__ method calculates which SOHO_Tn schema to use, based on the current date 
    versus the ``run_date``. 

    Args:
        None. 

    Attributes:
        None. 

    '''

# Class Attributes


# Constructor

    def __init__(self):

# Instance Attributes


# Class Initialisation

        super(SohoBaseWithSQL, self).__init__()
        DateStr=Soho.Util._time.GetCurrentDate()
        i=0
        while True:
            i-=1
            DateStr=Hydra.Util._time.GetPreviousWorkingDay(DateStr)
            if DateStr==self.RunDate:
                break
            assert i>-6
        self._DatabaseSchema='SOHO_T'+str(abs(i))
        return

# Operations

    def _OnStart(self,unnamedArgs,namedArgs):
        super(SohoBaseWithSQL, self)._OnStart(unnamedArgs,namedArgs)
        self._DatabaseName=namedArgs.get('DatabaseName',self.DatabaseName) # Override, if specified
        self.Log('DatabaseName: {0}'.format(self.DatabaseName))
        self._DatabaseUser=namedArgs.get('DatabaseUser',self.DatabaseUser) # Override, if specified
        self.Log('DatabaseUser: {0}'.format(self.DatabaseUser))
        self._DatabaseSchema=namedArgs.get('DatabaseSchema',self.DatabaseSchema) # Override, if specified
        self.Log('DatabaseSchema: {0}'.format(self.DatabaseSchema))
        return

    @property
    def DatabaseName(self):
        return self._DatabaseName

    @property
    def DatabaseUser(self):
        return self._DatabaseUser

    @property
    def DatabaseSchema(self):
        return self._DatabaseSchema

