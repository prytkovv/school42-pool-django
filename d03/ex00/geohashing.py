import sys
import antigravity


def get_geohash(latitude, longitude, date, dow_jones_index):
    return antigravity.geohash(
        latitude,
        longitude,
        ('%s-%s'
        % (date, dow_jones_index)).encode('utf-8'))


if __name__ == '__main__':
    if len(sys.argv) == 5:
        try:
            get_geohash(float(sys.argv[1]),
                        float(sys.argv[2]),
                        sys.argv[3],
                        sys.argv[4])
        except ValueError:
            print('The latitude or longutude type should be float')

