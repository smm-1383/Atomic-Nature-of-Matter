from sys import argv
from glob import glob
from beadfinder import BeadFinder

def diff_frame(bl1, bl2):
    dic = {}
    for i in bl1:
        d = sorted(i.distanceTo(j) for j in bl2)[0]
        dic[i] = d
    return dic


def main():
    min_pixel, tau, delta, pics_folder = argv[1:]
    pics_add = glob('./atomic/' + pics_folder)
    min_pixel, tau, delta = int(min_pixel), float(tau), float(delta)

    for B1, B2 in zip(pics_add[1:], pics_add[:-1]):
        dic = diff_frame(BeadFinder(B1, tau).getBeads(min_pixel), BeadFinder(B2, tau).getBeads(min_pixel))
        dists = filter(lambda i: i <= delta, dic.values())
        print(*[f'{i:.4f}' for i in dists], sep='\n')
        print()


if __name__ == '__main__':
    main()
