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

   # Define the root path of this project
   project_root = Path("/glade/u/home/awells/air_quality_project").resolve()
   cwd = Path.cwd().resolve()

   # Only add to sys.path if working within the project directory
   if project_root in cwd.parents or cwd == project_root:
       if str(project_root) not in sys.path:
           sys.path.append(str(project_root))
   ```

### 📦 Result

* When a Jupyter kernel starts inside `air_quality_project/` (or its subdirectories), the project root is automatically added to `sys.path`.

* This allows you to import shared utility modules cleanly:

  ```python
  from utils.processing_utils import func
  ```

* No need to manually modify `sys.path` in individual notebooks.


