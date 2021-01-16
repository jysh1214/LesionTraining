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

    print(startp)

    # 右
    down = False
    while (True):
        if (data[i, j-1] == True and not(down)):
            all_points.append((j, i))
            j = j - 1
            print("Current Point: ", j, i)
            continue
        elif (data[i+1, j-1] == True):
            all_points.append((j, i))
            j = j - 1
            i = i + 1
            print("Current Point: ", j, i)
            continue
        elif (data[i+1, j] == True):
            all_points.append((j, i))
            i = i + 1
            print("Current Point: ", j, i)
            continue
        elif (data[i+1, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            i = i + 1
            print("Current Point: ", j, i)
            continue
        elif (data[i, j+1] == True):
            all_points.append((j, i))
            j = j + 1
            print("Current Point: ", j, i)
            down = True
            continue
        elif ((j, i) in all_points):
            break
        else:
            break
