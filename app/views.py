from core.view import View


class HomePage(View):
    def get(self, request, *args, **kwargs):
        return "Hello, World. From View!"
