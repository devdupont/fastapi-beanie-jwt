"""
This script generates a new bcrypt password salt and updates to local .env file
"""

from pathlib import Path
import bcrypt

path = Path.cwd() / ".env"
env = path.read_text()
target = 'SALT="'
start = env.find(target) + len(target)
prefix, postfix = env[:start], env[start:]
end = postfix.find('"')
output = prefix + str(bcrypt.gensalt())[2:-1] + postfix[end:]
with path.open("w") as out:
    out.write(output)
