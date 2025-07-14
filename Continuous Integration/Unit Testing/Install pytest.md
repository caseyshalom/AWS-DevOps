# How to Install pytest

### 1. Install pytest globally
```bash
pip install pytest
   ```

### 2. Verify installation
```bash
pytest --version
# Expected output: pytest 8.x.x
   ```

### 3. Alternative: Install in a Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install pytest in the virtual environment
pip install pytest
   ```

## Basic Usage
Create a test file (e.g., test_sample.py):
```bash
def test_addition():
    assert 1 + 1 == 2
   ```

Run tests:
```bash
pytest test_sample.py 
   ```

## Common Issues & Solutions
If you see "pytest not found":
```bash
# Ensure pip is up-to-date
python -m pip install --upgrade pip

# Reinstall pytest
pip install --force-reinstall pytest
   ```

Permission errors (Linux/Mac):
```bash
# Use --user flag if needed
pip install --user pytest
   ```

Uninstall pytest:
```bash
pip uninstall pytest
   ```