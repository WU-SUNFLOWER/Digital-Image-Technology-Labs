import cv2

"""             PART 1 BEGIN                 """
def part1(image):
    # 分离颜色通道
    # 返回得到一个用于储存图像信息的numpy.ndarray对象
    
    """
    以下代码等价于
    B = image[:,:,0]
    G = image[:,:,1]
    R = image[:,:,2]
    """
    B, G, R = cv2.split(image)
    # 彩色图像image的维数为3，而分离后的单通道图像维数只有2
    print(f"dim of image is {image.ndim}, dim of single-channel image is {B.ndim}")
    # 单独显示各颜色通道
    cv2.imshow('Red Channel', R)
    cv2.imshow('Green Channel', G)
    cv2.imshow('Blue Channel', B)
    cv2.waitKey(0)

    # 合并通道 - 正确顺序
    merged = cv2.merge([B, G, R])
    cv2.imshow('Merged Image - Original Order', merged)
    cv2.waitKey(0)

    # 尝试一个不同的顺序 - 红蓝交换
    merged_swapped = cv2.merge([R, G, B])
    cv2.imshow('Merged Image - Swapped Red and Blue', merged_swapped)
    cv2.waitKey(0)

    # 另外一个顺序 - 绿色和蓝色交换
    merged_green_blue_swapped = cv2.merge([G, B, R])
    cv2.imshow('Merged Image - Swapped Green and Blue', merged_green_blue_swapped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""             PART 1 END                   """

"""             PART 2 BEGIN                 """
def part2(image):
    # cvtColor的第二个参数表示将原图转换到哪种颜色空间
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 灰度图像也是单通道图像
    print(f"dim of gray image is {gray_image.ndim}")
    cv2.imshow("Gray Image", gray_image)
    cv2.waitKey(0)
    R, G, B = cv2.split(image)
    cv2.imshow('Red Channel', R)
    cv2.imshow('Green Channel', G)
    cv2.imshow('Blue Channel', B)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""             PART 2 END                   """

"""             PART 3 BEGIN                 """
def part3(image):
    clip_image = image[20:180, 30:220, :]
    cv2.imwrite("lenna_clip.jpg", clip_image)
    print("success to save new jpg file")
"""             PART 3 END                   """

"""             PART 4 BEGIN                 """
def part4(image):
    cv2.imshow("Original Image", image)

    # cv2.flip方法只支持1（水平翻转）、0（垂直翻转）、-1（对角翻转）这三个参数

    # 水平镜像，flipCode=1
    horizontal_flip = cv2.flip(image, 1)
    cv2.imshow('Horizontal Flip', horizontal_flip)

    # 垂直倒影，flipCode=0
    vertical_flip = cv2.flip(image, 0)
    cv2.imshow('Vertical Flip', vertical_flip)

    # 对角翻转，flipCode=-1
    diagonal_flip = cv2.flip(image, -1)
    cv2.imshow('Diagonal Flip', diagonal_flip)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
"""             PART 4 END                   """

def main():
    # 读取图像
    # 返回得到一个用于储存图像信息的numpy.ndarray对象
    image = cv2.imread('lenna.jpg')
    while True:
        user_input = input("Please input the part number between 1 to 4:  ")
        if user_input == "exit":
            break
        if user_input == '\n':
            continue
        elif user_input.isdigit():
            num = int(user_input)
            if num == 1:
                part1(image)
            elif num == 2:
                part2(image)
            elif num == 3:
                part3(image)
            elif num == 4:
                part4(image)
            else:
                print("Error: Please enter a number between 1 and 4")
        else:
            print("Error: Please enter a valid number")
    
if __name__ == "__main__":
    main()