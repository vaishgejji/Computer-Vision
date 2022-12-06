import numpy as np

def convolve2D(image, kernel, padding, stride):
    W = image.shape[0]
    K = kernel.shape[0]
    P = padding
    S = stride
    convolved_image_size = int(((W-K+(2*P))/S)+1)
    convolved_image = np.zeros((convolved_image_size, convolved_image_size))

    kernel_height = kernel.shape[0]
    kernel_width = kernel.shape[1]

    j_stop = image.shape[1]-kernel_width+1
    i_stop = image.shape[0]-kernel_height+1

    for i in range(i_stop):
        for j in range(j_stop):
            image_kernel = image[i:kernel_height+i,j:kernel_width+j]
            convolved_image[i,j] = np.sum(np.multiply(image_kernel, kernel))

    return convolved_image
    

if __name__ == "__main__":

    image = np.array([[7,2,3,3,8],
                      [4,5,3,8,4],
                      [3,3,2,8,4],
                      [2,8,7,2,7],
                      [5,4,4,5,4]])
    
    kernel = np.array([[1,0,-1],
                       [1,0,-1],
                       [1,0,-1]])

    ans = convolve2D(image, kernel, padding=0, stride=1)
    print(ans)