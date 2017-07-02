# -*- codeing:utf-8 -*-
import logging
import os
import subprocess

import toolkit.svntools.constants

_logger = logging.getLogger('svn')


class SvnException(Exception):
    """
    Raised when the SVN CLI command returns an error code.
    """

    def __init__(self, message):
        self.message = message
        Exception.__init__(self, message)


class CommonClient(object):
    def __init__(self, url_or_path, type_, **kwargs):
        self.__url_or_path = url_or_path
        self.__username = kwargs.pop('username', None)
        self.__password = kwargs.pop('password', None)
        self.__env = kwargs.get('env', {})

        if type_ not in (toolkit.svntools.constants.LT_RM, toolkit.svntools.constants.LT_LC):
            raise SvnException("Type is invalid: %s" % type_)

        self.__type = type_

    def run_command(self, subcommand, args, return_type=0):
        cmd = ['svn']
        # --non-interactive: No interaction for automation
        cmd += ['--non-interactive']
        # --trust-server-cert: Trust any SSL connection
        cmd += ['--trust-server-cert']
        # -no-auth-cache: Do not cache user token
        if self.__username is not None and self.__password is not None:
            cmd += ['--username', self.__username]
            cmd += ['--password', self.__password]
            cmd += ['--no-auth-cache']

        cmd += [subcommand] + args

        _logger.debug("RUN: %s" % (cmd,))

        environment_variables = os.environ.copy()
        environment_variables.update(self.__env)
        environment_variables['LANG'] = 'en_US.UTF-8'

        p = subprocess.Popen(cmd,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             env=environment_variables)

        stdout = p.stdout.read()
        p.wait()
        p.stdout.close()

        if return_type == 0:
            return 0
        elif return_type == 1:
            print(stdout)
            return stdout
        elif return_type == 2:
            # fixme need encode as utf-8
            # return stdout.decode().strip('\n').split('\n')
            return stdout

    @property
    def path(self):
        return self.__url_or_path
