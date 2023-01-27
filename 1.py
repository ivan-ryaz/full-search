import sys
from Samples.geocoder import get_coordinates, get_ll_span
from Samples.mapapi_PG import show_map


def main():
    top = " ".join(sys.argv[1:])
    if top:
        l1, l2 = get_coordinates(top)
        par = f'll = {l1}, {l2} & spn = 0.005, 0.005'
        show_map(par, 'map')
        ll, spn = get_ll_span(top)
        par = f'll={ll}&spn={spn}'
        show_map(par, 'map')
        show_map(par, 'map', add_params=f'pt={ll}')
    else:
        print('No data')


if __name__ == "__main__":
    main()
