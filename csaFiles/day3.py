crates = ['BQC', 'RQWZ', 'BMRLV', 'CZHVTW', 'DZHBNVG', 'HNPCGFVQ', 'DGTRWZS', 'CGMNBWZP', 'NJBMWQFP']
with open('input.txt', 'r') as inp:
  moves = [[int(line.strip().split()[1]), int(line.strip().split()[3]), int(line.strip().split()[5])] for line in inp]
for move in moves:
  crate = crates[move[1]-1][0-move[0]:]
  crates[move[1]-1] = crates[move[1]-1][:0-move[0]]
  crates[move[2]-1] = f'{crates[move[2]-1]}{crate}'
print(''.join([crate[-1] for crate in crates]))