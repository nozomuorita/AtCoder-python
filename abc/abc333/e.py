#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import deque
n = int(input())
tx = [tuple(map(int, input().split())) for _ in range(n)]
portion = [deque() for _ in range(n+1)]  # portion[x]: �^�C�vx�̃|�[�V�������E��������

cnt = 0
for i in range(n):
    if tx[i][0]==1: cnt+=1
ans = [0]*cnt         #  �o������|�[�V����������0�ŏ�����

crr = 0               #  ���݂܂łɓo�ꂵ���|�[�V�����̐�
for i in range(n):
    t, x = tx[i][0], tx[i][1]
    if t==1:
        portion[x].appendleft(crr)    # �^�C�vx�Ƀ|�[�V�����ԍ���ǉ�(������)
        crr += 1                      # �o�ꂵ���|�[�V��������1�ǉ�
    else:
        if len(portion[x])==0: exit(print(-1))   # �^�C�vx�̃|�[�V�������Ȃ��Ȃ�s��(-1)
        idx = portion[x].popleft()               # ��ԍŌ�ɏE�����^�C�vx�̃|�[�V�������g��
        ans[idx] = 1                             # �g�p����|�[�V������1�ɂ���

# kmx: �������Ă���|�[�V�������̃}�b�N�X, p: �������Ă���|�[�V������
kmx, p, crr = 0, 0, 0
for i in range(n):
    t, x = tx[i][0], tx[i][1]
    if t==1:
        if ans[crr]==1: p+=1    # �|�[�V�������E���ꍇ��p��1�ǉ�
        crr += 1                
    else:
        p -= 1                  # �|�[�V�������g�p����ꍇ��1���炷
    kmx = max(kmx, p)           # �ő及�����ƍ������Ă���|�[�V�������ōX�V

print(kmx)
print(*ans)
