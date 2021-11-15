from enum import Enum


class Status(Enum):
    ACTIVE = "ACTIVE"
    IN_ACTIVE = "IN_ACTIVE"
    
    
class ROLES(Enum):
    ADMIN = 'ADMIN'
    REGULER_USER = 'REGULER_USER'
    


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# function to check file extension
def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# # function to check file extension
# def allowed_file(filename):
#     return '.' in filename and \
#         filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS    




