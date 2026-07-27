from services.auth_manager import AuthManager

USERNAME = "Admin"
PASSWORD = "Admin123456*"


auth = AuthManager()

auth.login(
    USERNAME,
    PASSWORD,
)

print("Usuario:", auth.username)
print("Roles:", auth.roles)

token = auth.get_access_token()

print(token[:50] + "...")