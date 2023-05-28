def main():
    x01,y01,x11,y11 = [int(x) for x in input().split()]
    x02,y02,x12,y12 = [int(x) for x in input().split()]
    
    print(1) if tem_colisao(x01,y01,x11,y11,x02,y02,x12,y12) else print(0)
    
    
def tem_colisao(x01,y01,x11,y11, x02,y02,x12,y12):
    colisoes_em_x = (x01 <= x02 <= x11 or x01 <= x12 <= x11) or (x02 <= x11 <= x12 or x02 <=x01 <= x12)
    colisoes_em_y = (y01 <= y02 <=y11 or y01 <= y12 <=y11) or (y02 <= y12 <= y11) or (y02 <= y01 <= y12)

    return colisoes_em_x and colisoes_em_y
main()