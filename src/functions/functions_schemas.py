functions_schemas = [
  {
    "type": "function",
    "function": {
      "name": "list_files",
      "description": "Lists the names of files and directories at the specified path. Directory names are suffixed with '/'. Results are sorted alphabetically. Returns 'Empty Directory' if the directory contains no entries, or an error message if the operation fails.",
      "parameters": {
        "type": "object",
        "properties": {
          "path": {
            "type": "string",
            "description": "Path of the directory to list. Defaults to the current working directory ('.')."
          }
        },
        "required": [],
        "additionalProperties": False
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "read_file",
      "description": "Reads and returns the complete contents of a UTF-8 encoded text file. Returns an error message if the file cannot be read.",
      "parameters": {
        "type": "object",
        "properties": {
          "path": {
            "type": "string",
            "description": "Path to the file to read."
          }
        },
        "required": ["path"],
        "additionalProperties": False
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "write_file",
      "description": "Writes text content to a UTF-8 encoded file, creating the file if it does not exist and overwriting it if it does. Returns a success message or an error message.",
      "parameters": {
        "type": "object",
        "properties": {
          "path": {
            "type": "string",
            "description": "Path to the file to write."
          },
          "content": {
            "type": "string",
            "description": "Text content to write to the file. Existing file contents will be overwritten."
          }
        },
        "required": ["path", "content"],
        "additionalProperties": False
      }
    }
  },
  {
    "type": "function",
    "function": {
      "name": "run_command",
      "description": "Requests user confirmation and, if approved, executes a shell command. Returns combined standard output and standard error, or a message indicating no output, user refusal, or an error. Commands have a 120-second timeout.",
      "parameters": {
        "type": "object",
        "properties": {
          "command": {
            "type": "string",
            "description": "Shell command to execute. This can execute arbitrary commands with the permissions of the Python process, so use caution."
          }
        },
        "required": ["command"],
        "additionalProperties": False
      }
    }
  }
]