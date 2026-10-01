import subprocess
import os

def list_files(path = '.'):
    """List files and directories available in the configured workspace.

    Returns:
        list[str]: A list of file and directory names or paths.
    """
    files = []

    try:
        for file in os.scandir(path):
            files.append(file.name + ('/' if file.is_dir() else ""))

        return ("\n".join(sorted(files)) or "Empty Directory")

    except Exception as e:
        return (str(e))


def read_file(path = ""):
    """Read and return the contents of a file.

    Args:
        path (str): The path of the file to read.

    Returns:
        str: The contents of the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        OSError: If the file cannot be accessed or read.
    """
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return (file.read())

    except Exception as e:
        return (str(e))


def write_file(path = "", content = ""):
    """Write content to a file at the specified path.

    Args:
        path (str): The path of the file to create or modify.
        content (str): The content to write to the file.

    Returns:
        dict: A result indicating whether the file was written successfully.
    """

    try:
        with open(path, 'w', encoding='utf-8') as file:
            file.write(content)
            return ("Wrote in file successfully")

    except Exception as e:
        return(str(e))

def run_command(command = ""):
    """Execute a shell command and capture its output.

    Args:
        command (str): The shell command to execute.

    Returns:
        dict: A result containing the command's output, error output,
            and execution status.
    """

    try:
        answer = input(f"Run '{command}'? [y/N]: ")

        if ('y' in answer.lower()):
            result = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=120)
            output = (result.stdout + result.stderr).strip()
            return (output or f"(no output, exit code {result.returncode})")

        else:
            return ("The user declined to run the command")

    except Exception as e:
        return (str(e))
