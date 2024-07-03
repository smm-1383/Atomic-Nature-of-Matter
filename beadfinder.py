import cv2
import numpy as np
from sys import argv
from blob import Blob


class BeadFinder:
    def __init__(self, img, tau):
        img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        tau_img = np.where(img > tau, img, 0)
        r, c = img.shape
        lasts = np.zeros_like(img)

        def blobs(img, x, y, blob, lasts):
            if (not 0 <= x < r) or (not 0 <= y < c) or (not img[x, y]) or lasts[x, y]:
                return
            lasts[x, y] = 1
            blob.add(x, y)
            for i in (-1, 0, 1):
               for j in (-1, 0, 1):
                   if i + j in (-1, 1):
                       blobs(img, x + i, y + j, blob, lasts)

        self.all_blobs = []

        for y in range(c):
            for x in range(r):
                b = Blob()
                blobs(tau_img, x, y, b, lasts)
                if b.mass() > 0:
                    self.all_blobs.append(b)

    def getBeads(self, min_pixels):
        return list(filter(lambda i: i.mass() >= min_pixels, self.all_blobs))


def main():
    min_pixels, tau, pic_add = argv[1:]
    min_pixels, tau, pic_add = int(
        min_pixels), float(tau), './atomic/' + pic_add

    bead = BeadFinder(pic_add, tau)
    print(*bead.getBeads(min_pixels), sep='\n')

if __name__ == '__main__':
    main()