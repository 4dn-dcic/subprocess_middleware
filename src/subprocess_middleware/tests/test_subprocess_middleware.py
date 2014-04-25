def test_transform(testapp):
    res = testapp.get('/')
    assert 'X-Transformed' in res.headers
    res = testapp.get('/')
    assert 'X-Transformed' in res.headers


def test_should_transform(testapp):
    res = testapp.get('/', headers={'X-No-Transform': 'true'})
    assert 'X-Transformed' not in res.headers


def test_transform_error(testapp):
    res = testapp.get('/transform_error', status=500)
    assert 'X-Transformed' not in res.headers
    res = testapp.get('/')
    assert 'X-Transformed' in res.headers


def test_bad_request(testapp):
    res = testapp.get('/bad_request', status=400)
    assert 'X-Transformed' in res.headers
