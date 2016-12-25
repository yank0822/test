#!/usr/bin/env python
import random
import requests
import unittest
import yaml


class TestPod(unittest.TestCase):
    '''
    Pod test class
    '''
    def setUp(self):
        super(TestPod, self).setUp()
        self.fp = open('pods.yaml', 'rb')
        self.data = yaml.load(self.fp)
        self.endpoint = 'http://localhost:9090'

    def tearDown(self):
        self.fp.close()
        super(TestPod, self).tearDown()

    def test_get_pods(self):
        '''
        test to get all pods list
        '''
        url = '{0}/{1}'.format(self.endpoint, 'pods')
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(eval(response.text), self.data.get('pods'))

    def test_get_pod(self):
        '''
        test to get a pod
        '''
        pod = random.choice(self.data.get('pods'))
        url = '{0}/{1}/{2}'.format(self.endpoint, 'pods', pod)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, pod)

    def test_get_non_exist_pot(self):
        '''
        test to get a non-exist pot
        '''
        pod = 'fakepod'
        url = '{0}/{1}/{2}'.format(self.endpoint, 'pods', pod)
        response = requests.get(url)
        self.assertEqual(response.status_code, 404)
