## Register

**You send:** Your information.
**You get:** An account which you can use to login.

**Request:**

```json
POST /api/users/register/
Content-Type: application/json

{
    "username": "foo",
    "password": "free1234",
    "email": "foo@bar.com"
}
```

**Successful Response:**

```json
{
  "id": 1,
  "username": "foo",
  "email": "foo@bar.com"
}
```

**Failed Response:**

```json
{
  "username": ["A user with that username already exists."],
  "email": ["Email is already being used"],
  "password": ["Password should at least be 8 characters"]
}
```

## Login

**You send:** Your credentials.
**You get:** An authentication token.

**Request:**

```json
POST /api/users/login/
Content-Type: application/json

{
    "username": "foo",
    "password": "free1234",
}
```

**Successful Response:**

```json
{
    "token": "ef9390d38f85b67cf480bc43d6339b3d3ed1dbe4"
}
```

**Failed Response:**

```json
{
    "non_field_errors": [
        "Unable to log in with provided credentials."
    ]
}
```

## Logout

**You send:** Your authentication token.

**Request:**

```json
POST /api/users/login/
Content-Type: application/json
Authorization: Token ef9390d38f85b67cf480bc43d6339b3d3ed1dbe4
```

**Successful Response:**

```json
{}
```

**Failed Response:**

```json
{
    "detail": "Invalid token."
}
```

