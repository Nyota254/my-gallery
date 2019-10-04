from django.db import models

class Image(models.Model):
    '''
    This class will contain the Images model
    '''
    pass
    def save_image(self):
        '''
        Saves data to database from the image fields
        '''
        pass

    def delete_image(self):
        '''
        Deletes image data from database
        '''
        pass

    def update_image(self):
        '''
        Updates data of the image in the database
        '''
        pass

    @classmethod
    def get_image_by_id(cls,id):
        '''
        Querys the database to get the images by id
        '''
        pass

    @classmethod
    def search_image(cls,category):
        '''
        Querys the database to get the images by category
        '''
        pass
    @classmethod
    def filter_by_location(cls,location):
        '''
        Querys the database to search for images by their location
        '''
        pass

class Location(models.Model):
    '''
    This class will contain the location model
    '''
    pass

    def save_location(self):
        '''
        Saves the location data to the database
        '''
        pass
    
    def delete_location(self):
        '''
        Deletes the location from the database
        '''
        pass
    def update_location(self):
        '''
        Updates the location from the database
        '''
        pass

class Category(models.Model):
    '''
    This class will contain the Category model
    '''
    pass

    def save_category(self):
        '''
        Saves the category data to the database
        '''
        pass
    
    def delete_category(self):
        '''
        Deletes the category from the database
        '''
        pass
    def update_category(self):
        '''
        Updates the category from the database
        '''
        pass

