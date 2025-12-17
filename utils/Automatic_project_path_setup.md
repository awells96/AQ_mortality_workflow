## 🔧 Jupyter Startup Script for Automatic Project Path Setup

To avoid repeating `sys.path.append(...)` in every notebook, this project uses a **Jupyter startup script** to automatically add the project root to Python’s import path — but **only when working inside this project directory**.

### ✅ Setup Instructions

1. **Create the Jupyter startup directory** (if it doesn't exist):

   ```bash
   mkdir -p ~/.ipython/profile_default/startup
   ```

2. **Create a startup script** named `00-startup-path.py`:

   ```bash
   nano ~/.ipython/profile_default/startup/00-startup-path.py
   ```

3. **Paste the following code** into that file:

   ```python
   import sys
   from pathlib import Path
    
    # List of project roots that should be added to sys.path
    PROJECT_ROOTS = [
        Path("/path/to/project"),
        Path("/path/to/different_project"),
        Path("/path/to/another_project"),
    ]
    
    cwd = Path.cwd().resolve()
    
    for project_root in PROJECT_ROOTS:
        project_root = project_root.resolve()
    
        # Check if we're inside this project
        if cwd == project_root or project_root in cwd.parents:
            if str(project_root) not in sys.path:
                sys.path.append(str(project_root))

   ```

### 📦 Result

* When a Jupyter kernel starts inside `project/` (or its subdirectories, or any other directed projects), the project root is automatically added to `sys.path`.

* This allows you to import shared utility modules cleanly:

  ```python
  from utils.utils import func
  ```

* No need to manually modify `sys.path` in individual notebooks.


