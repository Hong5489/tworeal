from subprocess import Popen,PIPE
def cmdline(cmd, sh=True):
    """ Execute command @cmd and return output using Popen(). """
    process = Popen(
        args=cmd,
        stdout=PIPE,
        shell=sh
    )
    return process.communicate()[0].decode("ISO-8859-1")