# Let’s compare subprocess to two of its alternatives: OS, which has been covered in other readings, and Pathlib. For tasks like getting the current working directory or creating a directory, OS and Pathlib are more direct (or “Pythonic,” meaning it uses the language as it was intended). Using subprocess for tasks like these is like using a crowbar to open a nut. It's more heavy-duty and can be overkill for simple operations. 

# As a comparison example, the following commands accomplish the exact same tasks of getting the current working directory. 

# Subprocess: 

# cwd_subprocess = subprocess.check_output(['pwd'], text=True).strip()

# OS: 

# cwd_os = os.getcwd()

# Pathlib: 

# cwd_pathlib = Path.cwd()

# And these following commands accomplish the exact same tasks of creating a directory. 

# Subprocess: 

# subprocess.run(['mkdir', 'test_dir_subprocess2'])

# OS: 

# os.mkdir('test_dir_os2')

# Pathlib: 

# test_dir_pathlib2 = Path('test_dir_pathlib2')

# test_dir_pathlib2.mkdir(exist_