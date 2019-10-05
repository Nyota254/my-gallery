from django.db import models

class Location(models.Model):
    '''
    This class will contain the location model
    '''
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location

    def save_location(self):
        '''
        Saves the location data to the database
        '''
        self.save()
    
    def delete_location(self):
        '''
        Deletes the location from the database
        '''
        self.delete()
    def update_location(self):
        '''
        Updates the location from the database
        '''
        pass


class Category(models.Model):
    '''
    This class will contain the Category model
    '''
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category

    def save_category(self):
        '''
        Saves the category data to the database
        '''
        self.save()
    
    def delete_category(self):
        '''
        Deletes the category from the database
        '''
        self.delete()
    def update_category(self):
        '''
        Updates the category from the database
        '''
        pass


class Tag(models.Model):
    '''
    Adds the tags class to the models
    '''
    name = models.CharField(max_length=30) 

    def __str__(self):
        return self.name


class Image(models.Model):
    '''
    This class will contain the Images model
    '''
    image = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=40)
    image_description = models.TextField()
    image_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    image_category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.image_name

    def save_image(self):
        '''
        Saves data to database from the image fields
        '''
        self.save()

    def delete_image(self):
        '''
        Deletes image data from database
        '''
        self.delete()

    def update_image(self):
        '''
        Updates data of the image in the database
        '''
        pass

    @classmethod
    def get_all_images(cls):
        '''
        Querys the entire database and gets all the images
        '''
        return cls.objects.all()

    @classmethod
    def get_image_by_id(cls,id):
        '''
        Querys the database to get the images by id
        '''
        image_found = cls.objects.filter(pk = id)
        return image_found

    @classmethod
    def search_image_by_category(cls,category):
        '''
        Querys the database to get the images by category
        '''
        image_found = cls.objects.filter(image_category = category)
        return image_found

    @classmethod
    def filter_by_location(cls,location):
        '''
        Querys the database to search for images by their location
        '''
        image_found = cls.objects.filter(image_location=location)
        return image_found



