# -*- codeing:utf-8 -*-
import toolkits.svntools.common as svn_common
import toolkits.svntools.constants as svn_constants


class RemoteClient(svn_common.CommonClient):
    def __init__(self, url_or_path, **kwargs):
        super(RemoteClient, self).__init__(url_or_path, svn_constants.LT_RM, **kwargs)

    def checkout(self, local_path, revision=None):
        cmd = []
        if revision is not None:
            cmd += ['-r', str(revision)]

        cmd += [self.path, local_path]

        self.run_command('checkout', cmd)
        return 0

    def __repr__(self):
        return '<SVN(REMOTE) %s>' % self.path
