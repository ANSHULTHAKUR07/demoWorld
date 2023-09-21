from django.contrib.auth.models import Permission

class CustomePermissionCheck(Permission):
    print("custome permission check !@#$%")
    def has_perm(self, request, view):
        print("has permissions method 123456789 !!!!!!!")

        if request.method == 'GET':
            print("in request method Get")
            return True
        
        else:
            print("in else ")
            return request.user.is_authenticated
