#!/usr/bin/env python3

import click
import sys
import json

from netatmo.api import NetatmoApi
from netatmo.util import draw_data


@click.command()
@click.option('username', '--username', envvar='NETATMO_USERNAME')
@click.option('password', '--password', envvar='NETATMO_PASSWORD')
@click.option('client_id', '--client_id', envvar='NETATMO_CLIENT_ID')
@click.option('client_secret', '--client_secret', envvar='NETATMO_CLIENT_SECRET')
@click.option('font_file', '--font-file', default='fonts/BebasNeue-Regular.ttf')
@click.option('output_file', '--output-file')
def run(username, password, client_id, client_secret, font_file, output_file):
    api = NetatmoApi(username, password, client_id, client_secret)
    data = api.get_stations_data()
    with open('stations_data.json', 'w') as f:
        json.dump(f, data)
    draw_data(data, font_file, output_file)


if __name__ == '__main__':
    sys.exit(run())