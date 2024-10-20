import uos

try:
    version = uos.uname()
    print(f"OS Version: {version}")
except Exception as e:
    print(f"Error determining OS version: {e}")