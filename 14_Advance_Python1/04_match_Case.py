#Match case is similar to switch case in cpp

def http_status(n):
    match n:
        case 200:


         return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal server error"
        case _:
            return "Unknown error"

print(http_status(200))


