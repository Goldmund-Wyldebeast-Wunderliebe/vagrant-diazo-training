from fabric.api import env, run, cd

env.hosts = ["localhost"]
def list_dir(dir_=None):
    """returns a list of files in a directory (dir_) as absolute paths"""
    dir_ = dir_ or env.cwd
    string_ = run("for i in %s*; do echo $i; done" % dir_)
    files = string_.replace("\r","").split("\n")
    print files
    return files

def add_cronjob(cmd):
    """ Add cronjob to current user"""
    run('echo "{0}" >> /tmp/crondump'.format(cmd))
    run('crontab /tmp/crondump')
