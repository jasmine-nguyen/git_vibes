import subprocess

result = subprocess.run(['git', 'log', '-5'], capture_output=True, text=True)

print(result.stdout)
