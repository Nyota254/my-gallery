from django.test import TestCase
from .models import Image,Location,Category

class ImageTest(TestCase):
    '''
    Test class for the Image model
    '''
    def setUp(self):
        '''
        Sets up the tests
        '''
        # self.new_image = Image(image='media/images.png',image_name='moringa_day1',image_description='this is my first pic of my first day in moringa')
        self.new_location = Location(location='nairobi')
        self.new_location.save()
        self.new_category = Category(category='studies')
        self.new_category.save()
        self.new_image = Image(image='media/images.png',image_name='moringa_day1',image_description='this is my first pic of my first day in moringa',image_location=self.new_location,image_category=self.new_category)
        self.new_image.save()

    def tearDown(self):
        '''
        clears the database after every test
        '''
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()
        
    def test_instance(self):
        '''
        Test Whether the image object is an instance of the model class
        '''
        self.assertTrue(isinstance(self.new_image,Image))

    def test_save_method(self):
        '''
        Test whether the class method save_image works 
        '''
        self.another_image = Image(image='media/another_image.png',image_name='moringa_day2',image_description='this is my first pic of my second day in moringa',image_location=self.new_location,image_category=self.new_category)
        self.another_image.save()
        saved_images = Image.objects.all()
        self.assertTrue(len(saved_images)>1)

    def test_delete_method(self):
        '''
        Test whether the class method delete_image works
        '''
        self.new_image.delete_image()
        saved_images = Image.objects.all()
        self.assertTrue(len(saved_images)==0)

    def test_update_method(self):
        '''
        Test whether the class method update_image works
        '''
        image_found = Image.objects.filter(pk=1)
        image_found.update(image_name ='moringa-firstday')
        searched_image = Image.objects.filter(pk=1)
        self.assertEqual(searched_image,'moringa-firstday')

    def test_get_image_by_id(self):
        '''
        Test whether this class method can search for an image using its id
        '''
        self.another_image = Image(image='media/another_image.png',image_name='moringa_day2',image_description='this is my first pic of my second day in moringa',image_location=self.new_location,image_category=self.new_category)
        self.another_image.save()
        searched_image = Image.get_image_by_id(self.another_image.pk)
        self.assertEqual(searched_image,self.another_image)

    def test_get_image_by_location(self):
        '''
        Test whether this class method can search for an image using its id
        '''
        self.another_location = Location(location='mombasa')
        self.another_location.save()
        self.another_image = Image(image='media/another_image.png',image_name='moringa_day2',image_description='this is my first pic of my second day in moringa',image_location=self.another_location,image_category=self.new_category)
        self.another_image.save()
        searched_image = Image.filter_by_location('mombasa')
        self.assertEqual(searched_image,self.another_image)

    def test_get_image_by_category(self):
        '''
        Test whether this class method can search for an image using its id
        '''
        self.another_category = Category(category='fun')
        self.another_category.save()
        self.another_image = Image(image='media/another_image.png',image_name='moringa_day2',image_description='this is my first pic of my second day in moringa',image_location=self.new_location,image_category=self.another_category)
        self.another_image.save()
        searched_image = Image.search_image_by_category('fun')
        self.assertEqual(searched_image,self.another_image)

    