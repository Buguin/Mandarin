import os.path

import toolkit.svntools.common as svn_common
import toolkit.svntools.constants as svn_constants


class LocalClient(svn_common.CommonClient):
    def __init__(self, url_or_path, **kwargs):
        if os.path.exists(url_or_path) is False:
            raise EnvironmentError("Path does not exist: %s" % url_or_path)
        super(LocalClient, self).__init__(url_or_path, svn_constants.LT_LC, **kwargs)

    def update(self, revision=None):
        cmd = []
        if revision is not None:
            cmd += ['-r', str(revision)]

        cmd += [self.path]
        self.run_command('update', cmd)
        return 0

    def __repr__(self):
        return '<SVN(LOCAL) %s>' % self.path
