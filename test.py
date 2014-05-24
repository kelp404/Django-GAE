import os, sys, unittest


if __name__ == '__main__':
    # gae
    if os.path.isdir('./google_appengine'):
        gae_path = './google_appengine'
    else:
        gae_path = '/usr/local/google_appengine'
    sys.path.append(gae_path)
    sys.path.extend([
        os.path.join(gae_path, 'google'),
        os.path.join(gae_path, 'lib', 'yaml', 'lib'),
    ])

    tests = unittest.TestLoader().discover('tests_python')
    unittest.TextTestRunner(verbosity=2).run(tests)
