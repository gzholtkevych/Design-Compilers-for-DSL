alphabet = {}
alphabet['chars'] = {chr(i) for i in range(ord('a'), ord('z') + 1)}.union(
    {chr(i) for i in range(ord('A'), ord('Z') + 1)})
alphabet['digits'] = {chr(i) for i in range(ord('0'), ord('9') + 1)}

print(alphabet['chars'])
print(alphabet['digits'])