import os
inp = "/home/grigory/MyStem/input_texts"
lst = os.listdir(inp)
#print(lst)
for fl in lst:
    os.system(r"/home/grigory/MyStem/mystem " + inp + os.sep + fl + " /home/grigory/MyStem/output_texts" + os.sep + fl)

'''
os.listdir(path)

    Return a list containing the names of the entries in the directory given by path. The list is in arbitrary order.
    It does not include the special entries '.' and '..' even if they are present in the directory.

    This function can be called with a bytes or string argument, and returns filenames of the same datatype.

    Availability: Unix, Windows.


os.system(command)

    Execute the command (a string) in a subshell.

    On Unix, the return value is the exit status of the process encoded in the format specified for wait().
     Note that POSIX does not specify the meaning of the return value of the C system() function,
     so the return value of the Python function is system-dependent.

    On Windows, the return value is that returned by the system shell after running command.
    The shell is given by the Windows environment variable COMSPEC: it is usually cmd.exe,
     which returns the exit status of the command run; on systems using a non-native shell,
     consult your shell documentation.


os.sep
    The character used by the operating system to separate pathname components.
    This is '/' for POSIX and '\\' for Windows. Note that knowing this is not sufficient to be able to
    parse or concatenate pathnames — use os.path.split() and os.path.join() — but it is occasionally useful.
    Also available via os.path.
'''