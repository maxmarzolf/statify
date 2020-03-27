from flask import Flask, redirect, url_for
import os

app = Flask(__name__)
client_id = os.environ['client_id']


@app.route('/')
def initialize():
    return redirect('https://accounts.spotify.com/en/authorize?'
                    'client_id=' + client_id +
                    '&response_type=token&redirect_uri=https:%2F%2Fgoogle.com')


class OAuthSignIn(object):
    providers = None

    def __init__(self, provider_name):
        self.provider_name = provider_name
        credentials = app.config[client_id][provider_name]
        self.consumer_id = credentials['id']
        self.consumer_secret = credentials['secret']

    def authorize(self):
        pass

    def callback(self):
        pass

    def get_callback_url(self):
        return url_for('oauth_callback', provider=self.provider_name,
                       _external=True)

    @classmethod
    def get_provider(self, provider_name):
        if self.providers is None:
            self.providers = {}
            for provider_class in self.__subclasses__():
                provider = provider_class()
                self.providers[provider.provider_name] = provider
        return self.providers[provider_name]


class SpotifySignIn(OAuthSignIn):
    pass


if __name__ == '__main__':
    app.run()
