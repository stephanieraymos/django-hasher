from django.test import TestCase
from selenium import webdriver
from .forms import HashForm
import hashlib 


# class FunctionalTestCase(TestCase):


#     def setUp(self):
#         self.browser = webdriver.Firefox()


#     def test_there_is_homepage(self):
#         self.browser.get('http://localhost:8000') # To go to the homepage
#         self.assertIn('Enter hash here',self.browser.page_source)

#     def test_hash_of_hello(self):
#         self.browser.get('http://localhost:8000')
#         text = self.browser.find_element_by_id('id_text') # selenium function that says go find something in the html that has the following id
#         text.send_keys('hello') # entering text hello
#         self.browser.find_element_by_name('submit').click() # submitting button
#         self.assertIn('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

#     def tearDown(self):
#         self.browser.quit()

class UnitTestCase(TestCase):

    def test_home_homepage_template(self):
        response = self.client.get('/') # getting homepage
        self.assertTemplateUsed(response, 'hashing/home.html') # checking if home template is being used for the path above ('/')

    def test_hash_form(self):
        form = HashForm(data = {'text':'hello'})
        self.assertTrue(form.is_valid)

    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest() # hexdigest passes back string so we can do some assertion
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash) # asserting that the hashed string (2CF2...) is equal to text_hash