def midPointShapeDraw(x_c,y_c,a):
    points = []
    y=0
    x=0

    points.append((y,x))
    points.append([(x,y),(x-y),(y,-x),(-y,-x),(-x,-y),(-x,y),(-y,x)])

    P = 1-a

    while y<x:
        y +=1
        if P < 0:
            P = P + 2 *y+1
        else:
            x -=1
            P = P +2*y+1-2*x
        points.append((y,x))
        points.append([(x,y),(x-y),(y,-x),(-y,-x),(-x,-y),(-x,y),(-y,x)])

        if (y >= x):
            points_unique = [*set(points)]
            points_center.extend([(x+x_c,y+y_c) for (x,y) in points_unique])
            break



if __name__ == '__main__':
    points_center =[]
    midPointShapeDraw(0,0,10)

    print(len(points_center),points_center)
    print("x = ",points_center[0][0],"y = ", points_center[0][1]) 

