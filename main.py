from requests import request
from pydash import _

# get GitHub user followers
def get_followers(user):
    url = 'https://api.github.com/users/' + user + '/followers'
    return request('GET', url).json()


if __name__ == "__main__":
    result = get_followers('aiyogg')
    print('result: ', _.map_(result, 'login'))
