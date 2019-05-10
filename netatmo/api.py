import requests


class NetatmoApi():

    def __init__(self, username, password, client_id, client_secret):
        self.username = username
        self.password = password
        self.client_id = client_id
        self.client_secret = client_secret
        self._access_token = None
        self._data = None

    def _get_token(self, refresh=False):
        if self._access_token is None or refresh:
            response = requests.post(
                'https://api.netatmo.com/oauth2/token',
                data={
                    'grant_type': 'password',
                    'username': self.username,
                    'password': self.password,
                    'client_id': self.client_id,
                    'client_secret': self.client_secret,
                    'scope': 'read_station'
                }
            )
            response.raise_for_status()
            self._access_token = response.json()['access_token']

        return self._access_token

    def get_stations_data(self, refresh=False):
        if self._data is None or refresh:
            response = requests.post(
                'https://api.netatmo.com/api/getstationsdata',
                params={
                    'access_token': self._get_token(),
                }
            )
            response.raise_for_status()
            self._data = response.json()['body']
        return StationsData(self._data)



class StationsData():

    def __init__(self, data):
        self._data = data
    
    def get_module_names(self):
        return [self._data['devices'][0]['module_name']] + list(map(
            lambda m: m['module_name'],
            self._data['devices'][0]['modules']
        ))

    def get_module_data(self, module_name):
        if module_name == self._data['devices'][0]['module_name']:
            return self._data['devices'][0]
        module = list(filter(
            lambda m: module_name == m['module_name'],
            self._data['devices'][0]['modules']
        ))
        assert len(module) == 1, "found {} module with name {}".format(
            len(module), module_name
        )
        return module[0]
