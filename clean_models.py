# clean_models.py — elimina todos los null bytes de models.py
import sys

path = "correspondencia_app/models.py"
try:
    data = open(path, "rb").read().replace(b"\x00", b"")
    open(path, "wb").write(data)
    print("✅ Null bytes eliminados de:", path)
except Exception as e:
    print("❌ Error limpiando null bytes:", e)
    sys.exit(1)
