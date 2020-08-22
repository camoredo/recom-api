## Register

**You send:** Your credentials.
**You get:** An account which you can use to log=on.

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
[
  {
    "id": 1,
    "username": "foo",
    "email": "foo@bar.com"
  }
]
```

**Failed Response:**

```json
{
  "username": ["A user with that username already exists."],
  "email": ["Email is already being used"],
  "password": ["Password should at least be 8 characters"]
}
```
