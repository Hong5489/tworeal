import numpy as np
from PIL import Image
def computeLayers(arr, mode, filename, folder):
    """ Compute each bits visual image for a given layer `arr` """
    for i in range(8):  # 8 bits layer
        newdata = (arr >> i) % 2 * 255  # Highlighting the layer bit `i`
        if mode == 'RGBA':  # Force alpha layer (4th) to 255 if exist
            newdata[:, :, 3] = 255
        Image.fromarray(newdata, mode).save(f"{folder}{filename}_{i+1}.png")


def processImage(img, folder="./images/"):
    """ Apply computeLayers() on each `img` layers and save images """
    filename = "test"
    img_pil = Image.open(img)

    # Convert all in RGBA exept RGB images
    if img_pil.mode in ["P", "1", "L", "LA", "RGBX", "RGBa", "CMYK", "LAB",
                        "YCbCr", "HSV", "I", "F"]:
        img_pil = img_pil.convert('RGBA')

    images_name = {}

    # Get numpy array
    npimg = np.array(img_pil)  # rgb
    imgr = npimg[:, :, 0]  # r
    imgg = npimg[:, :, 1]  # g
    imgb = npimg[:, :, 2]  # b

    # generate images from numpy array and save
    computeLayers(npimg, img_pil.mode, f"{filename}_rgb", folder)  # rgb
    computeLayers(imgr, 'L', f"{filename}_r", folder)  # r
    computeLayers(imgg, 'L', f"{filename}_g", folder)  # g
    computeLayers(imgb, 'L', f"{filename}_b", folder)  # b

    # set images names
    images_name["Supperimposed"] = [f"{filename}_rgb_{i+1}.png" for i
                                    in range(8)]
    images_name["Red"] = [f"{filename}_r_{i+1}.png" for i in range(8)]
    images_name["Green"] = [f"{filename}_g_{i+1}.png" for i in range(8)]
    images_name["Blue"] = [f"{filename}_b_{i+1}.png" for i in range(8)]

    if img_pil.mode == "RGBA":  # Should be RGB or RGBA
        computeLayers(npimg[:, :, 3], 'L', f"{filename}_a", folder)  # b
        images_name["Alpha"] = [f"{filename}_a_{i+1}.png" for i in range(8)]

    return images_name
