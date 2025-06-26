import os

# Ruta al models.py de tu app
path = os.path.join('correspondencia_app', 'models.py')

# Lee en modo binario, quita \x00, y sobrescribe
with open(path, 'rb') as f:
    data = f.read().replace(b'\x00', b'')

with open(path, 'wb') as f:
    f.write(data)

print('✅ Bytes nulos eliminados de:', path)
