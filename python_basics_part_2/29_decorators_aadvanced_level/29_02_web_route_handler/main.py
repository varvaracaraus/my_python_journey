from decorators import get_route
from route_handler import RouteHandler

handler = RouteHandler()

print("Testing the route '//':")
route = get_route('//')
if route:
    response = route(handler)
    print('Response:', response)
else:
    print('No such path')

print("\nTesting a non-existing route '/nonexistent':")
route = get_route('/nonexistent')
if route:
    response = route(handler)
    print('Response:', response)
else:
    print('No such path')
