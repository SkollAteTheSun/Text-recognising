from rep_image import repair, gauss_filter
from get_let import model, parall


if __name__ == '__main__':
    gauss_filter('tests/test_3.png')
    print(parall(path='tests/test_3_rep.png'))