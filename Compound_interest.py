p,r,t=map(int,input().split())
ci=p*pow((1+r/100.0),t)
print(f"{ci:.2f}")