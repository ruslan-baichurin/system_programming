import os

print('setenv...', end=' ')
print(os.environ['USER'])  # show current shell variable value

os.environ['USER'] = 'Natalia'  # runs os.putenv behind the scenes
os.system('python echoenv.py')

os.environ['USER'] = 'Polina'  # changes passed to spawned programs
os.system('python echoenv.py')  # and linked-in C library modules

os.environ['USER'] = input('? ')
print(os.popen('python echoenv.py').read())