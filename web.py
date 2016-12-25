#!/usr/bin/env python

import yaml

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


YAML_FILE = 'pods.yaml'


class PodHandler(BaseHTTPRequestHandler):
    '''
    handler for pod infos
    '''
    def response(self, code, body='', headers=None):
        '''
        responses for status code, body and headers
        '''
        self.send_response(code)

        if headers:
            for i in headers:
                self.send_header(i, headers[i])
        self.end_headers()

        if body:
            self.wfile.write(body)
            self.wfile.flush()

    def do_GET(self):
        if self.path.startswith('/pods'):
            return self.get_pod()
        elif self.path.startswith('/services'):
            return self.service()
        else:
            return self.response(404, 'URL not found\n')

    def get_pod(self):
        '''
        get pod info
        '''
        pods = self.load_yaml('pods')
        if pods is None:
            return self.response(404, 'no pods list')

        if self.path in ['/pods', '/pods/']:
            return self.response(200, pods)

        _, _, pod_name = self.path.split('/')
        if pod_name in pods:
            return self.response(200, pod_name)
        else:
            return self.response(404, 'pod: {0} not found'.format(pod_name))

    def get_service(self):
        '''
        get service info
        '''
        services = self.load_yaml('services')
        if services is None:
            return self.response(404, 'no services list')

        if self.path in ['/services', '/services/']:
            return self.response(200, services)

        _, _, service_name = self.path.split('/')
        if service_name in services:
            return self.response(200, service_name)
        else:
            return self.response(404, 'service: {0} not found'.format(service_name))

    def load_yaml(self, key):
        '''
        load info from yaml file
        '''
        with open(YAML_FILE, 'rb') as fp:
            data = yaml.load(fp)

        return data.get(key)


def main():
    '''
    main function
    '''
    try:
        server = HTTPServer(('', 9090), PodHandler)
        server.serve_forever()
    except Exception as err:
        print(err)
        server.socket.close()


if __name__ == '__main__':
    main()
