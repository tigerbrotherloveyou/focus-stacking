#!/usr/bin/env python3

import matplotlib.pyplot as plt
from PIL import Image, ImageFilter

filename = "../images/fly1.jpg"
debug_show = False
rows = 2 + 1 * debug_show
print("rows = ", rows)

image0 = Image.open(filename)
w, h = image0.size

fig = plt.figure()
ax = fig.add_subplot(rows, 2, 1)
ax.set_title("Original")
plt.axis("off")
plt.imshow(image0)


image1 = image0.crop((0, 0, (w >> 1), h))
print(image1.size)
blurred1 = image1.filter(ImageFilter.GaussianBlur(radius=1))
if debug_show:
    ax = fig.add_subplot(rows, 2, 3)
    plt.imshow(blurred1)


image2 = image0.crop(((w >> 1), 0, w, h))
print(image2.size)
blurred2 = image2.filter(ImageFilter.GaussianBlur(radius=1))
if debug_show:
    ax = fig.add_subplot(rows, 2, 4)
    plt.imshow(blurred2)


image3 = Image.new("RGB", (w, h))
image3.paste(blurred1, (0, 0, (w >> 1), h))
image3.paste(image2, ((w >> 1), 0, w, h))

ax = fig.add_subplot(rows, 2, rows * 2 - 1)
plt.imshow(image3)


image4 = Image.new("RGB", (w, h))
image4.paste(image1, (0, 0, (w >> 1), h))
image4.paste(blurred2, ((w >> 1), 0, w, h))

ax = fig.add_subplot(rows, 2, rows * 2)
plt.imshow(image4)

plt.show()
