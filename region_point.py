import numpy as np

def region_point(image, size):
    # print(image.size)
    # print(size[0])
    # print(size[1])
    data = np.array(image)

    startp = (0, 0)
    # find first point
    done = False
    for i in range(size[0]):
        for j in range(size[1]):
            if (data[i, j] == True):
                startp = (j, i)
                done = True
                break
        if done:
            break

    all_points = []
    j = startp[0]
    i = startp[1]

    connect = False
    # 右
    down = False
    while (True):
        if (data[i, j-1] == True and not(down)):
            all_points.append((j, i))
            j = j - 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i+1, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            i = i + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i+1, j] == True):
            all_points.append((j, i))
            i = i + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i+1, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            i = i + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            down = True
            continue
        elif ((j, i) in all_points):
            break
        else:
            break

    # 下
    left = False
    while (True):
        if (data[i+1, j] == True and not(left)):
            all_points.append((j, i))
            i = i + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i+1, j+1] == True):
            all_points.append((j, i))
            i = i + 1
            j = j + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i-1, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            i = i - 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i-1, j] == True):
            all_points.append((j, i))
            i = i - 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            left = True
            continue
        elif ((j, i) in all_points):
            break
        else:
            break

    # 左
    up = False
    while ((j, i) != startp):
        if (data[i, j+1] == True and not(up)):
            all_points.append((j, i))
            j = j + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i-1, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            i = i - 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i-1, j] == True):
            all_points.append((j, i))
            i = i - 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i-1, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            i = i - 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            up = True
            continue
        elif ((j, i) in all_points):
            break
        else:
            break

    # 上
    right = False
    while ((j, i) != startp):
        if (data[i-1, j] == True and not(right)):
            if ((j, i) == startp):
                break
            all_points.append((j, i))
            i = i - 1
            print("Current Point: ", j, i)
            continue
        elif (data[i-1, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            i = i - 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i+1, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            i = i + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            continue
        elif (data[i+1, j] == True):
            all_points.append((j, i))
            i = i + 1
            if ((j, i) == startp):
                break
            print("Current Point: ", j, i)
            right = True
            continue
        elif ((j, i) in all_points):
            break
        else:
            break


    print(startp)
