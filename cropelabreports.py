from PIL import Image
import os
outpath = 'elabjavapradeep/'
inpath = 'pradeepjava/'
cords = (0,92,1920,965)
files = os.listdir(inpath)
print('Crop Operation Started')
for file in files:
    img = Image.open(inpath+file)
    print('Cropping image '+file)
    imgnew = img.crop(cords)
    imgnew.save(outpath+file)

print('\nCrop Operation Done')
