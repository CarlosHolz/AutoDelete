import os, time

path = r"C:\Users\User\Desktop\PNG"
path2 = r"C:\Users\User\Desktop\Teste2"
path3 = r"C:\Users\User\Desktop\Teste3"

while True:
  now = time.time()

  for f in os.listdir(path):
    f = os.path.join(path, f)

    if os.stat(f).st_mtime < now - 10 * 86400:
      if os.path.isfile(f):
        os.remove(f)

  for f in os.listdir(path2):
    f = os.path.join(path2, f)

    if os.stat(f).st_mtime < now - 10 * 86400:
      if os.path.isfile(f):
        os.remove(f)
  
  for f in os.listdir(path3):
    f = os.path.join(path3, f)

    if os.stat(f).st_mtime < now - 10 * 86400:
      if os.path.isfile(f):
        os.remove(f)

time.sleep(5)