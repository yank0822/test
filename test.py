#!/usr/bin/env python


# combine all the argument types
def list_arguments(arg1, arg2='defaultB', *args, **kwargs):
    '''
    display regular args and all variable args'
    '''
    print('arg1 is:', arg1)
    print('arg2 is:', arg2)
    
    for eachNKW in args: 
        print('additional non-keyword arg:', eachNKW)
    for eachKW in kwargs.keys():
        print("additional keyword arg '%s': %s" % (eachKW, kwargs[eachKW]))


if __name__ == '__main__':
    list_arguments('one', 3, 'python', 'shell', name='landers', project='rubicon')

    tupleA = ('python', 'shell')
    dictA = {'name': 'landers', 'project': 'rubion'}

    list_arguments('one', 3, *tupleA, **dictA)
    list_arguments('one', 3, 'go', project2='atmos', *tupleA, **dictA)

