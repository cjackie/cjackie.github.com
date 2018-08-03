###################################################################
# automatically generate thumbnails for all images in a directory
#  and their meta data for the website.
###################################################################
import os, sys
import Image
import glob

# adjustable parameters
tn_width = 500                                  # the height will be scaled accordingly
im_ending = [ "jpg", "png", "jpeg"]             # ending of images. add more if needed

# file out the path to the folder
path = "/Users/chaojiewang/Desktop/tmp/tmp2"                                     # path to the directory

fns = []
for ending in im_ending:
    fns = fns + glob.glob(os.path.join(path, "".join(["*.", ending])))

metafile = open(os.path.join(path, "metadata"), "w")
for fn in fns:
    l = fn.split(".")
    l[-2] = l[-2] + "_tn"
    outfile = ".".join(l)
    print(outfile)
    im = Image.open(fn)
    original_size = im.size
    im.thumbnail((tn_width, tn_width))          # the ratio is preserved by default
    im.save(outfile)
    # write meta data
    data = '- name: {0}\nthumbnail: {1}\ntext: \nw: {2:d}\n h: {3:d}\n'.format(fn, outfile, original_size[0], original_size[1])
    metafile.write(data)

metafile.close()
