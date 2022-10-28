from pathlib import Path
import shutil
p = Path('.')

pattern1 = list(p.glob('* '))

for plik in pattern1:
 src = plik
 dst = str(src).strip()
 shutil.move(src, dst)

pattern2 = list(p.glob(' *'))

for plik in pattern2:
 src = plik
 dst = str(src).strip()
 shutil.move(src, dst)





