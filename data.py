class DataForOrderCreation:

    CREATE_ORDER_DATA = {
                        "ingredients":["61c0c5a71d1f82001bdaaa6d","61c0c5a71d1f82001bdaaa6f"]
                        }
    
    CREATE_ORDER_WRONG_DATA = {
                        "ingredients":["61c0c5a71d1f82001bdaaa6","61c0c5a71d1f82001bdaaa6fa"]
                        }
    
class DataForResponseMessages:

    SUCCESS = True
    USER_EXIST = 'User already exists'
    EMPTY_FIELD = 'Email, password and name are required fields'
    WRONG_FIELD = 'email or password are incorrect'
    ORDER_WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
