import sys
import pprint

if __name__ == '__main__':
  line1 = input()
  line2 = input()
  n_map = line1.split()
  N = int(n_map[0])# 商品の値段
  K = line2.split()#嫌いな数字の整数リスト


  while True:
    N_tmp_list = list(str(N))
    N_tmp_uniq = list(set(N_tmp_list))
    #商品の値段のリストと嫌いな数字のリストの論理積をとる
    matched_list = []
    for tag in N_tmp_uniq:
      for src in K:
        if tag == src:
          matched_list.append(tag)
    if len(matched_list) is 0:
      break
    N += 1

  print (N)

