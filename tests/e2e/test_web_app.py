import pytest

from flask import session


def test_register(client):
    # Check that we retrieve the register page.
    response_code = client.get('/authentication/register').status_code
    assert response_code == 200

    # Check that we can register a user successfully, supplying a valid username and password.
    response = client.post(
        '/authentication/register',
        data={'username': 'gmichael', 'password': 'CarelessWhisper1984'}
    )
    assert response.headers['Location'] == 'http://localhost/authentication/login'


@pytest.mark.parametrize(('username', 'password', 'message'), (
        ('', '', b'Your username is required'),
        ('cj', '', b'Your username is too short'),
        ('test', '', b'Your password is required'),
        ('test', 'test', b'Your password must be at least 8 characters, and contain an upper case letter,             a lower case letter and a digit'),
        ('kilic20', 'Test#6^0', b'Your username is already taken - please supply another'),
))
def test_register_with_invalid_input(client, username, password, message):
    # Check that attempting to register with invalid combinations of username and password generate appropriate error
    # messages.
    response = client.post(
        '/authentication/register',
        data={'username': username, 'password': password}
    )
    assert message in response.data


def test_login(client, auth):
    # Check that we can retrieve the login page.
    status_code = client.get('/authentication/login').status_code
    assert status_code == 200

    # Check that a successful login generates a redirect to the homepage.
    response = auth.login()
    assert response.headers['Location'] == 'http://localhost/'

    # Check that a session has been created for the logged-in user.
    with client:
        client.get('/')
        assert session['username'] == 'bmarshall7688'


def test_logout(client, auth):
    # Login a user.
    auth.login()

    with client:
        # Check that logging out clears the user's session.
        auth.logout()
        assert 'user_id' not in session


def test_index(client):
    # Check that we can retrieve the home page.
    response = client.get('/')
    assert response.status_code == 200
    assert b'Movie Web App' in response.data


def test_login_required_to_comment(client):
    response = client.post('/review')
    assert response.headers['Location'] == 'http://localhost/authentication/login'


def test_comment(client, auth):
    # Login a user.
    auth.login()

    # Check that we can retrieve the comment page.
    response = client.get('/movies?rank=1')

    response = client.post(
        '/review',
        data={'review': 'Bad movie not even good', 'movie_rank': 1}
    )
    assert response.headers['Location'] == 'http://localhost/movies?rank=1&view_reviews_for=1'


@pytest.mark.parametrize(('comment', 'messages'), (
        ('Who thinks this movie is fucking dogshit?', (b'Your review must not contain profanity')),
        ('Hey', (b'Your review is too short')),
        ('ass', (b'Your review is too short', b'Your review must not contain profanity')),
))
def test_comment_with_invalid_input(client, auth, comment, messages):
    # Login a user.
    auth.login()

    # Attempt to comment on an article.
    response = client.post(
        '/review',
        data={'review': comment, 'movie_rank': 2}
    )
    # Check that supplying invalid comment text generates appropriate error messages.
    for message in messages:
        assert message in response.data


def test_articles_without_date(client):
    # Check that we can retrieve the articles page.
    response = client.get('/movies')
    assert response.status_code == 200

    # Check that without providing a date query parameter the page includes the first article.
    assert b'A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.' in response.data
    assert b'Guardians of the Galaxy' in response.data


def test_articles_with_date(client):
    # Check that we can retrieve the articles page.
    response = client.get('/movies?rank=3')
    assert response.status_code == 200

    # Check that all articles on the requested date are included on the page.
    assert b'Three girls are kidnapped by a man with a diagnosed 23 distinct personalities. They must try to escape before the apparent emergence of a frightful new 24th.' in response.data
    assert b'Split' in response.data


def test_articles_with_comment(client):
    # Check that we can retrieve the articles page.
    response = client.get('/movies?rank=1&view_reviews_for=1')
    assert response.status_code == 200

    # Check that all comments for specified article are included on the page.
    assert b'Eh, it was ok' in response.data
    assert b'The movie was recommended to me by a friend who saw the reviews and somehow believed those' in response.data




