# CursorAgent Permission System Guide

## Introduction and Overview

The CursorAgent permission system provides a flexible and secure way to handle potentially sensitive operations, such as file system modifications and command execution. It ensures that sensitive operations require user confirmation before proceeding, while still allowing for an optional "yolo mode" that can bypass certain permission checks for efficiency.

Any operation that could potentially modify the user's system or access sensitive information requires permission. The permission system allows you to configure how these permissions are handled, ranging from requiring explicit confirmation for every operation to automatically approving certain operations based on configurable rules.

## Key Features

- **Permission-based Operation**: Sensitive operations like file modifications and command executions require explicit permission.
- **Yolo Mode**: Optional mode that allows operations without confirmation based on configurable settings.
- **Command Allowlist/Denylist**: Specific control over which commands can run automatically in yolo mode.
- **File Deletion Protection**: Special protection for file deletion operations, even in yolo mode.
- **Customizable Callbacks**: Ability to provide custom permission handling logic.
- **Operation Memory**: Remembers approved operations to avoid repeatedly asking for the same permissions.

## Using the PermissionOptions Class

The `PermissionOptions` class is the central configuration point for the permission system. You can create an instance of this class and pass it to the agent factory when creating an agent:

```python
from cursor_agent_tools.permissions import PermissionOptions
from cursor_agent_tools import create_agent

# Create permission options
permissions = PermissionOptions(
    yolo_mode=True,
    yolo_prompt="YOLO mode enabled - some operations will be auto-approved",
    command_allowlist=["ls", "echo", "cat"],
    command_denylist=["rm -rf", "sudo"],
    delete_file_protection=True
)

# Create an agent with these permission options
agent = create_agent(
    model="gpt-4o",
    api_key="your-api-key",
    permission_options=permissions
)
```

## Configuration Options

The `PermissionOptions` class accepts the following parameters:

- `yolo_mode` (bool, default: False): Whether to automatically grant permissions without confirmation. When set to True, many operations will be automatically approved based on the other settings.

- `yolo_prompt` (Optional[str], default: None): Message to display when YOLO mode is enabled. If not specified, a default message will be shown.

- `command_allowlist` (List[str], default: []): List of commands or command prefixes that are always allowed in YOLO mode. If this list is empty, all commands not in the denylist will be allowed in YOLO mode.

- `command_denylist` (List[str], default: []): List of commands or command prefixes that are always denied, even in YOLO mode.

- `delete_file_protection` (bool, default: True): Whether to require confirmation for file deletions even in YOLO mode.

- `permission_callback` (Optional[Callable], default: None): Custom callback function to handle permission requests. If not provided, the agent's default permission callback will be used.

## Permission Levels

The system has different permission types for different operations:

1. **Read Operations**: No permission required (e.g., reading files, listing directories)
2. **Write Operations**: Permission required unless in yolo mode (e.g., editing files, creating files)
3. **Delete Operations**: Special permission required even in yolo mode if delete_file_protection is enabled
4. **Command Execution**: Permission required based on command allowlist/denylist in yolo mode

## Integration with Tools

The permission system is integrated with all tools that can modify the system:

- **File Tools**: `create_file`, `edit_file`, `delete_file`
- **System Tools**: `run_terminal_command`

Search tools and read-only operations don't require permission.

## Permission Request Interface

The permission system uses a flexible permission request interface that can be customized to fit different environments and UI requirements. The core of this interface is the `request_permission` method on the BaseAgent class, which accepts:

- The operation type (e.g., "create_file", "delete_file", "run_terminal_command")
- A details dictionary containing the specific parameters of the operation

### Permission Request Flow

1. A tool function requires permission for an operation
2. It calls the agent's `request_permission` method
3. The agent processes the request through its permission handler
4. The permission handler either auto-approves (based on rules) or calls the permission request callback
5. The callback presents the request to the user and returns the user's decision

### Customizing the Permission Request UI

You can completely customize how permission requests are presented to users by providing a custom permission callback function. This makes the permission system adaptable to various interfaces:

#### Command Line Interface (Default)

The default implementation uses a simple command line interface:

```python
def custom_permission_callback(request: PermissionRequest) -> PermissionStatus:
    """Default permission request implementation using console input."""
    print(f"\n{'-'*40}")
    print(f"Permission Request: {request.operation}")
    print(f"Details: {request.details}")
    response = input("Allow this operation? (y/n): ").strip().lower()
    if response in ("y", "yes"):
        return PermissionStatus.GRANTED
    else:
        return PermissionStatus.DENIED
```

#### GUI Application Example

For a GUI application, you might implement a dialog-based permission request:

```python
def gui_permission_callback(request: PermissionRequest) -> PermissionStatus:
    """Custom GUI-based permission request handler."""
    import tkinter as tk
    from tkinter import messagebox
    
    # Create a temporary root window
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    # Format the message
    message = f"Operation: {request.operation}\n"
    for key, value in request.details.items():
        message += f"{key}: {value}\n"
    
    # Show dialog and get result
    result = messagebox.askyesno(
        title="Permission Request",
        message=f"{message}\n\nAllow this operation?",
        icon=messagebox.WARNING
    )
    
    # Clean up
    root.destroy()
    
    return PermissionStatus.GRANTED if result else PermissionStatus.DENIED
```

#### Web Application Integration

For web applications, you might implement a callback that returns a deferred response and resolves it when the user interacts with the UI:

```python
async def web_permission_callback(request: PermissionRequest) -> PermissionStatus:
    """Asynchronous web-based permission request handler."""
    # Store the request in a database or session
    request_id = await store_permission_request(request)
    
    # Wait for the user to respond via the web UI
    # This could be implemented with websockets, polling, or other mechanisms
    response = await wait_for_user_response(request_id)
    
    return PermissionStatus.GRANTED if response == "approve" else PermissionStatus.DENIED
```

### Implementing Custom Permission Interfaces

To create your own permission request interface:

1. Create a custom callback function that accepts a `PermissionRequest` and returns a `PermissionStatus`
2. The callback can be synchronous or asynchronous
3. Pass your callback to the agent via the `PermissionOptions` class

```python
from cursor_agent_tools.permissions import PermissionOptions, PermissionRequest, PermissionStatus
from cursor_agent_tools import create_agent

def custom_permission_callback(request: PermissionRequest) -> PermissionStatus:
    # Your custom implementation here
    # ...
    return PermissionStatus.GRANTED  # or DENIED

# Create permission options with your callback
permissions = PermissionOptions(
    yolo_mode=False,
    permission_callback=custom_permission_callback
)

# Create an agent with these options
agent = create_agent(
    model="gpt-4o",
    permission_options=permissions
)
```

## Examples

### Normal Mode (Requiring Confirmation)

```python
from cursor_agent_tools.permissions import PermissionOptions
from cursor_agent_tools import create_agent

permissions = PermissionOptions(yolo_mode=False)
agent = create_agent(
    model="gpt-4o",
    permission_options=permissions
)
agent.register_default_tools()

# This will prompt for confirmation
result = agent.available_tools["edit_file"]["function"](
    target_file="example.txt",
    instructions="Add a line",
    code_edit="New content",
    agent=agent,  # Pass agent reference for permission handling
)
```

### Yolo Mode (Automatic Approval)

```python
from cursor_agent_tools.permissions import PermissionOptions
from cursor_agent_tools import create_agent

permissions = PermissionOptions(
    yolo_mode=True,
    command_allowlist=["ls", "echo", "git"],
)
agent = create_agent(
    model="gpt-4o",
    permission_options=permissions
)
agent.register_default_tools()

# This will be automatically approved
result = agent.available_tools["run_terminal_command"]["function"](
    command="ls -la",
    explanation="List files",
    agent=agent,
)
```

### Basic Permission Configuration

```python
from cursor_agent_tools.permissions import PermissionOptions

# Strict mode - require confirmation for everything
permissions = PermissionOptions(
    yolo_mode=False
)

# YOLO mode with command restrictions
permissions = PermissionOptions(
    yolo_mode=True,
    command_allowlist=["ls", "echo", "cat", "pwd"],
    command_denylist=["rm", "sudo", "chmod", "chown"]
)

# YOLO mode but protect against file deletion
permissions = PermissionOptions(
    yolo_mode=True,
    delete_file_protection=True
)
```

## Permission Operations

The permission system handles the following types of operations:

- `create_file`: Creating a new file
- `edit_file`: Modifying an existing file
- `delete_file`: Deleting a file
- `run_terminal_command`: Executing a system command

Each operation type has specific permission handling logic.

## Demo

Run the permission system demo to see it in action:

```bash
python examples/permission_demo.py
```

## Best Practices

1. **Production Use**: Always disable YOLO mode in production environments
2. **Sensitive Operations**: Use a denylist to block potentially dangerous commands
3. **File Operations**: Enable delete_file_protection to prevent accidental file deletion
4. **Custom Callback**: Implement a custom permission callback for logging and auditing
5. **Testing**: Create specific test cases to verify permission handling

By configuring the permission system appropriately, you can balance convenience and security based on your specific needs. 