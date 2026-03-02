import paramiko
import subprocess, os

class LocalDestination:
    '''Serves as a wrapper for doing anything that may interact with the filesystem on the local machine'''

    def __init__():
        pass


    def exec_command(self, command: str, cwd: str = None, env: dict[str, str] = None) -> tuple[bytes, bytes]:
        '''Runs a command on the local machine

        This pretty much serves as a wrapper for subprocess.run
        
        :param command: The command to run
        :type command: str
        :param cwd: The current working directory to run the command in. 
        :type cwd: str
        :param env: The environment variables to run the command with. These are merged with the local machine's default environment variables
        :type env: dict[str, str]

        :returns: A tuple of stdout and stderr. These are both bytes, as that's what subprocess.run returns by default
        '''
        # running the command
        output = subprocess.run(command, cwd=cwd, env=os.environ + env, capture_output=True)

        # returning the output
        return (output.stdout, output.stderr)
    
    
    def open_file(self, path: str, mode: str = 'r'):
        return open(path, mode)


class RemoteDestination:
    '''Serves as a wrapper for doing anything that may interact with the filesystem on a remote machine'''
    def __init__(self, load_system_host_keys: bool = True):
        '''Initialises a RemoteDestination object
        
        :param load_system_host_keys: If we should automatically load the known host keys'''
        # initialising an SSH client
        self.client = paramiko.SSHClient()

        # loading the system host keys
        if load_system_host_keys:
            self.client.load_system_host_keys()

        # making a variable to store an SFTP session if we open one
        self.sftp_session: paramiko.SFTPClient = None


    def connect(self, hostname: str, username: str, password: str, port: int = 22, trust_host_if_host_key_is_missing: bool = False):
        '''Connects self.client to a host
        
        Note: The parameters here are named the same as paramiko.SSHClient.connect, so if documentation isn't detailed enough, refer to those docs too
        
        :param hostname: The hostname to connect to
        :type hostname: str
        :param username: The user to ssh as
        :type username: str
        :param password: The password for the user
        :type password: str
        :param port: The port where the SSH server is running
        :type port: int
        :param trust_host_if_host_key_is_missing: If we should still SSH into a host if it's not in known_hosts
        :type trust_host_if_host_key_is_missing: bool
        '''
        # setting it so we trust unknown hosts if the user passed it as true
        if trust_host_if_host_key_is_missing:
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # doing the actual connection
        self.client.connect(hostname, port, username, password)


    def open_sftp_session(self):
        '''Opens a SFTP session.
        
        The SFTP session is stored at self.sftp_session, and should be reused to prevent making more connections then necessary
        
        If a connection has already been made, it will not create a new one'''
        if self.sftp_session is None:
            self.sftp_session = self.client.open_sftp()


    def exec_command(self, command: str, cwd: str = None, env: dict[str, str] = None) -> tuple[bytes, bytes]:
        '''Runs a command on the remote machine

        IMPORTANT NOTE: cwd under the hood adds "cd [cwd];" to the command, so keep that in mind when using cwd
        
        :param command: The command to run
        :type command: str
        :param cwd: The current working directory to run the command in. 
        :type cwd: str
        :param env: The environment variables to run the command with. These are merged with the remote machine's default environment variables
        :type env: dict[str, str]

        :returns: A tuple of stdout and stderr. These are both bytes, as that's what subprocess.run returns by default
        '''
        # first if a cwd was passed, we add cd to the command
        # TODO this solution isn't great, since the user doesn't know if when the command fails, it was their command or cd
        # along with that, the user doesn't even know we're running cd, so it may be confusing
        # this issue on the paramiko gitub has something, but it's been silent for over 2 years at the time of writing
        # https://github.com/paramiko/paramiko/issues/1254
        if cwd is not None:
            command = f'cd {cwd}; {command}'

        # then we run the command
        stdin, stdout, stderr = self.client.exec_command(command, environment=env)

        # finally we return the output
        return (stdout.read(), stderr.read())


    
    def open_file(self, path: str, mode: str = 'r') -> paramiko.SFTPFile:
        # opening an sftp session if we haven't already
        self.open_sftp_session()

        # returning an object that you can edit
        return self.sftp_session.file(path, mode)