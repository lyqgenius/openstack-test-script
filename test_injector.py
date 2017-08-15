import os
import subprocess
import platform

def inject(pid, python_code, verbose=False, gdb_prefix=''):
    """Executes a file in a running Python process."""
    gdb_cmds = [
        'PyGILState_Ensure()',
        'PyRun_SimpleString("exec(%s)")' % python_code,
        'PyGILState_Release($1)',
        ]
    p = subprocess.Popen('%sgdb -p %d -batch %s' % (gdb_prefix, pid,
        ' '.join(["-eval-command='call %s'" % cmd for cmd in gdb_cmds])),
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if verbose:
        print(out)
        print(err)

def inject_file(pid, filename, verbose=False, gdb_prefix=''):
    """Executes a file in a running Python process."""
    filename = os.path.abspath(filename)
    gdb_cmds = [
        'PyGILState_Ensure()',
        'PyRun_SimpleString("'
            'import sys; sys.path.insert(0, \\"%s\\"); '
            'sys.path.insert(0, \\"%s\\"); '
            'exec(open(\\"%s\\").read())")' %
                (os.path.dirname(filename),
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')),
                filename),
        'PyGILState_Release($1)',
        ]
    p = subprocess.Popen('%sgdb -p %d -batch %s' % (gdb_prefix, pid,
        ' '.join(["-eval-command='call %s'" % cmd for cmd in gdb_cmds])),
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate()
    if verbose:
        print(out)
        print(err)


if __name__ == "__main__":
    pid = 8888
    python_code = 'print 123'
    filename = '/root/test_file.py'
    inject_file(pid, python_code, verbose=True)
