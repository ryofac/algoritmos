def main():
    x1,y1,xr,yr = map(int, input().split())
    
    cruzamentos = (xr + yr) - (x1 +y1)
    
    print(cruzamentos)

main()