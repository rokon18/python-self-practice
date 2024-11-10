#arithmetic op:+ - */%**//
a=3
b=4
sum=a+b
sub=a-b
div=a/b
mul=a*b
pow=a**b
fdiv=a//b
mod=a%b
print(f"{a}+{b}={sum}")
print(f"{a}-{b}={sub}")
print(f"{a}*{b}={mul}")
print(f"{a}/{b}={div}")
print(f"{a}**{b}={pow}")
print(f"{a}//{b}={fdiv}")
print(f"{a}%{b}={mod}")

#assignment op
# = += -+ *= %= **= //=
x=10
y=15
x+= y
print(x)
x-=y
print(x)
x/=y
print(x)
x*=y
x%=y
print(x)
x**=y
print(x)
x//=y
print(x)
#comparison op
#> >= < <= == !=
c=5
d=6
print(f"{c}>{d}=>{c>d}")
print(f"{c}<{d}=>{c<d}")
print(f"{c}=={d}=>{c==d}")
print(f"{c}!={d}=>{c!=d}")

#logical op
#and,or ,not
z=50
compare =z>10 and z<40
print(compare)
compare =z>10 or z<40
print(compare)
print(not(compare))
