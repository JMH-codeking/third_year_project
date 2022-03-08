import os
import pathlib

_pa = pathlib.Path(__file__).parent
for n in [250]:
	os.system(f'mkdir {_pa}/{n}ahead/Generalisation')
	os.system(f'mkdir {_pa}/{n}ahead/test_magnified')
	os.system(f'mkdir {_pa}/{n}ahead/test')

