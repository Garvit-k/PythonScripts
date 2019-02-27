from PIL import Image, ImageOps

desired_size = int(input("Desired size of image "))
im_pth = "test.jpg"
im = Image.open(im_pth)
old_size = im.size
ratio = float(desired_size)/max(old_size)
new_size = tuple([int(x*ratio) for x in old_size])
im = im.resize(new_size, Image.ANTIALIAS)
new_im = Image.new("RGB", (desired_size, desired_size),"white")
new_im.paste(im, ((desired_size-new_size[0])//2,(desired_size-new_size[1])//2))
delta_w = desired_size - new_size[0]
delta_h = desired_size - new_size[1]
padding = (delta_w//2, delta_h//2, delta_w-(delta_w//2), delta_h-(delta_h//2))
new_im = ImageOps.expand(im, padding)
new_im.save("newtest.jpg")
new_im.show()