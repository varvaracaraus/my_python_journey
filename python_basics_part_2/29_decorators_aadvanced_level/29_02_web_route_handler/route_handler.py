from decorators import callback, log_call


class RouteHandler:
    @callback('//')
    @log_call
    def example(self) -> str:
        print('Example function that returns a server response')
        return 'OK'
