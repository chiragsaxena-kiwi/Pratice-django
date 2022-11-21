from datetime import timezone
from django.test import TestCase

# Create your tests here.


class Trydjango(TestCase):
    def test_abcd(self):
        self.assertTrue(1==1)



from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Book, Student,Post,Musician


class StudentTestCase(APITestCase):

    url = reverse("student-list")
      

    def setUp(self):
       
        self.student_setup = Student.objects.create(
            id=123,
            name="django",
            address="noida"
            
        )
        
        self.data={
            "id": 1234,
            "name": "hey",
            "address":"goa"
        }

    def test_invalid_sid_id(self):
        """The reset password page loads properly"""

     
        response = self.client.post(self.url, data=self.data)
        #response = self.client.post(f"{self.url}", self.post)
        self.assertEqual(response.status_code, 400)



    def test_invalid_name(self):
        """The reset password page loads properly"""

     
        response = self.client.post(self.url, data=self.data)
        #response = self.client.post(f"{self.url}", self.post)
        self.assertEqual(response.status_code, 400)


    def test_invalid_address(self):
        """The reset password page loads properly"""

     
        response = self.client.post(self.url, data=self.data)
        #response = self.client.post(f"{self.url}", self.post)
        self.assertEqual(response.status_code, 400)        


    def test_invalid_ssid_id(self):
        """The reset password page loads properly"""

        # url = self.url + "?token={}".format(self.token)
        #    response = self.client.get(self.url)
        response = self.client.get(f"{self.url}")
        print(response.data)
        self.assertEqual(response.status_code, 200)


    def test_invalid_sname(self):
        """The reset password page loads properly"""

        # url = self.url + "?token={}".format(self.token)
        #    response = self.client.get(self.url)
        response = self.client.get(f"{self.url}")
        print(response.data)
        self.assertEqual(response.status_code, 200)    

          

    def test_invalid_saddress(self):
        """The reset password page loads properly"""

        # url = self.url + "?token={}".format(self.token)
        #    response = self.client.get(self.url)
        response = self.client.get(f"{self.url}")
        print(response.data)
        self.assertEqual(response.status_code, 200)     



# class BookApiTestCase(APITestCase):

#     url = reverse("book-list")


#     def setUp(self):
       
#         self.book_setup = Book.objects.create(
#             id=123,
#             title="django",
#             author="james bond"
            
#         )
        
#         self.data={
#             "id": 1234,
#             "title": "harry ",
#             "author":"peter"
#         }

#     def test_invalid_bid_id(self):
#         """The reset password page loads properly"""

     
#         response = self.client.post(self.url, data=self.data)
#         #response = self.client.post(f"{self.url}", self.post)
#         self.assertEqual(response.status_code, 400)



#     def test_invalid_title(self):
#         """The reset password page loads properly"""

     
#         response = self.client.post(self.url, data=self.data)
#         #response = self.client.post(f"{self.url}", self.post)
#         self.assertEqual(response.status_code, 400)


#     def test_invalid_author(self):
#         """The reset password page loads properly"""

     
#         response = self.client.post(self.url, data=self.data)
#         #response = self.client.post(f"{self.url}", self.post)
#         self.assertEqual(response.status_code, 400)        


#     def test_invalid_bbid_id(self):
#         """The reset password page loads properly"""

#         # url = self.url + "?token={}".format(self.token)
#         #    response = self.client.get(self.url)
#         response = self.client.get(f"{self.url}")
#         print(response.data)
#         self.assertEqual(response.status_code, 200)


#     def test_invalid_btitle(self):
#         """The reset password page loads properly"""

#         # url = self.url + "?token={}".format(self.token)
#         #    response = self.client.get(self.url)
#         response = self.client.get(f"{self.url}")
#         print(response.data)
#         self.assertEqual(response.status_code, 200)    

          

#     def test_invalid_bauthor(self):
#         """The reset password page loads properly"""

#         # url = self.url + "?token={}".format(self.token)
#         #    response = self.client.get(self.url)
#         response = self.client.get(f"{self.url}")
#         print(response.data)
#         self.assertEqual(response.status_code, 200)     

class PostTestCase(APITestCase):

    url = reverse("post-list")
      

    def setUp(self):
       
        self.student_setup = Post.objects.create(
            title="Post",
            content="django",
            date_posted="2019-04-05"
           
            
        )
        
        self.data={
            "title":"Post",
            "content":"django",
            "date_posted":"2022-05-04"
           
        }

    def test_invalid_ptitlep(self):
        """The reset password page loads properly"""

     
        response = self.client.post(self.url, data=self.data)
        #response = self.client.post(f"{self.url}", self.post)
        self.assertEqual(response.status_code, 201)



    def test_invalid_pcontentp(self):
        """The reset password page loads properly"""

     
        response = self.client.post(self.url, data=self.data)
        #response = self.client.post(f"{self.url}", self.post)
        self.assertEqual(response.status_code, 201)


    def test_invalid_pdatep(self):
        """The reset password page loads properly"""

     
        response = self.client.post(self.url, data=self.data)
        #response = self.client.post(f"{self.url}", self.post)
        self.assertEqual(response.status_code, 201)    
    


    def test_invalid_ptitleg(self):
        """The reset password page loads properly"""

        # url = self.url + "?token={}".format(self.token)
        #    response = self.client.get(self.url)
        response = self.client.get(f"{self.url}")
        # print(response.data)
        self.assertEqual(response.status_code, 200)


    def test_invalid_pcontentg(self):
        """The reset password page loads properly"""

        # url = self.url + "?token={}".format(self.token)
        #    response = self.client.get(self.url)
        response = self.client.get(f"{self.url}")
        # print(response.data)
        self.assertEqual(response.status_code, 200)    

          

    def test_invalid_pdateg(self):
        """The reset password page loads properly"""

        # url = self.url + "?token={}".format(self.token)
        #    response = self.client.get(self.url)
        response = self.client.get(f"{self.url}")
        # print(response.data)
        self.assertEqual(response.status_code, 200)  

      
class MusicianTestCase(APITestCase):

    

    def setUp(self):

            self.url = reverse("musician-list")              
            self.musician_setup = Musician.objects.create(
            first_name="Post",
            last_name="django",
           
           
            
        )
        
            self.data={
            "first_name":"Post",
            "last_name":"django",
         
           
        }        


    def test_invalid_firstname_get(self):
        """The reset password page loads properly"""

        response = self.client.get(f"{self.url}")
        self.assertEqual(response.status_code, 200)   


    def test_invalid_firstname_post(self):
        """The reset password page loads properly"""

     
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 400)      


    def test_invalid_lastname_get(self):
        """The reset password page loads properly"""

        response = self.client.get(f"{self.url}")
        self.assertEqual(response.status_code, 200)   


    def test_invalid_lasttname_post(self):
        """The reset password page loads properly"""

     
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 400)          