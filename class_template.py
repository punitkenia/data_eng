#!/usr/bin/env python
# =============================================================================
# $Id: Exp $
# =============================================================================
# Module: package.sub_package
# Contacts: Name (emailId)
#           Ardentisys Ltd.
# =============================================================================
"""What is this package for (one line).

Classes:
    className - what does this class do in
"""

# =============================================================================
# IMPORTS
# =============================================================================

# Standard imports
import os

# Non-Standard Package imports
import pandas

# Ardentisys imports
import package

# Globals
SFINFO = '/usr/bin/sfinfo'

# =============================================================================
# CLASSES
# =============================================================================

class Class_name(object):
    """Object representing the header data for an audio file.

    Example:
        
        >>> from rh.audio import Header
        >>> audio = Header('wa034.240Snd.Main.0001-0440.aiff')
        >>> print audio.fps
        23.976

    """
    def __init__(self, path):
        with open(path, 'r'):
            pass # trigger an appropriate error if file can't be read

        cmd = "{sfinfo} {file}".format(sfinfo=SFINFO, file=path)
        self._data = self._parseOutput(commands.getoutput(cmd))
        self._path = path

    # -------------------------------------------------------------------------
    #    Name: function_Name()
    #    Args: Arguments passed and single line explainition, e.g. string representing the output of sfinfo
    # Returns: (dict) header fields and their values
    #  Raises: n/a
    #    Desc: Given the output of the sfinfo command, build a dictionary of
    #          the header fields and their values.
    # -------------------------------------------------------------------------
    def function_name(args,**kwargs):
        #Function definition
        
        return
