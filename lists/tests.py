from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

    ## Checks the url to see which view function it should go to, looks for home_page
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)



    def test_home_page_returns_correct_html(self):
        ## http request, pass the request to homepage which gives back a response, we decode the .content to html string
        ## make sure its inside <html></html>, add a title then content of the html
        
        request = HttpRequest()  
        response = home_page(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<html>'))  
        self.assertIn('<title>To-Do lists</title>', html)  
        self.assertTrue(html.endswith('</html>'))  