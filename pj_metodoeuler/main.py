
def f(x,y):
    return

def mtd_euler(f,x0,y0,h,n):
    "h es el paso"

    val_x = [x0]
    val_y = [y0]

    for i in range(n):
        x = val_x[-1]
        y = val_y[-1]

        xn = n + h
        yn = y + h*f(x,y)

        val_x.append(xn)
        val_y.append(yn)


    return val_x, val_y