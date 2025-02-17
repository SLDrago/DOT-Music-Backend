# DOT-Music Backend

DOT-Music Backend is a Django-based system that provides APIs for managing users, playlists, and song streaming. It ensures secure authentication and efficient data management for the platform.

## Requirements

- Python (>= 3.x)
- Django

## Setup & Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/SLDrago/DOT-Music-Backend.git
   cd DOT-Music-Backend
   ```

2. **Activate the virtual environment:**

   ```bash
   dotmusicenv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure settings:**

   - Add your email server details in `settings.py`.
   - Set up the database configuration as needed.

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the server:**
   ```bash
   python manage.py runserver
   ```

# API Documentation

This document provides an overview of the available API endpoints for the DOT-Music Backend.

## Base URL (Develop Env. Default)

```
http://127.0.0.1:8000
```

## Artist Registration

### Endpoint: `POST /api/artist/register/`

**Description:** Registers a new artist user.

**Request Body:**

```json
{
  "username": "artist_name",
  "password": "securepassword",
  "email": "artist@example.com",
  "bio": "Short artist biography",
  "artist_type": "pop"
}
```

**Response:**

```json
{
  "message": "Registration successful",
  "artist": { ... },
  "access_token": "jwt_access_token",
  "refresh_token": "jwt_refresh_token"
}
```

---

## Artist Login

### Endpoint: `POST /api/artist/login/`

**Description:** Logs in an artist user and returns authentication tokens.

**Request Body:**

```json
{
  "email": "artist@example.com",
  "password": "securepassword"
}
```

**Response:**

```json
{
  "access_token": "jwt_access_token",
  "refresh_token": "jwt_refresh_token",
  "name": "artist_name",
  "artistId": 1,
  "artist": { ... }
}
```

---

## Fetch Artist Types

### Endpoint: `GET /api/artist/types/`

**Description:** Retrieves the available artist types.

**Response:**

```json
[
  { "value": "pop", "label": "Pop" },
  { "value": "rock", "label": "Rock" },
  { "value": "hip_hop", "label": "Hip-Hop" },
  ...
]
```

---

## Fetch Last Five Artists

### Endpoint: `GET /api/artists/last-five/`

**Description:** Retrieves the last five registered artists.

**Response:**

```json
{
  "artists": [
    {
      "id": 1,
      "bio": "Short artist biography",
      "genre": "pop",
      "profile_picture": "path/to/profile.jpg",
      "user__name": "Artist Name"
    },
    ...
  ]
}
```

---

## Fetch Songs by Artist

### Endpoint: `GET /api/songs/artist/{artist_id}/`

**Description:** Retrieves songs by a specific artist.

**Response:**

```json
{
  "artist_name": "Artist Name",
  "songs": [
    { "id": 1, "title": "Song Title", "duration": "3:45" },
    ...
  ]
}
```

---

## Upload Song

### Endpoint: `POST /api/songs/upload/`

**Description:** Uploads a new song for the authenticated artist.

**Request Body:**

```json
{
  "title": "Song Title",
  "genre": "pop",
  "duration": "3:45",
  "file": "song.mp3"
}
```

**Response:**

```json
{
  "id": 1,
  "title": "Song Title",
  "genre": "pop",
  "duration": "3:45",
  "artist": "Artist Name"
}
```

---

## User Registration

### Endpoint: `POST /api/user/register/`

**Description:** Registers a new user.

**Request Body:**

```json
{
  "name": "User Name",
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:**

```json
{
  "message": "User registered successfully",
  "user": {
    "name": "User Name",
    "email": "user@example.com",
    "access_token": "jwt_access_token",
    "refresh_token": "jwt_refresh_token"
  }
}
```

---

## User Login

### Endpoint: `POST /api/user/login/`

**Description:** Logs in a user and returns authentication tokens.

**Request Body:**

```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response:**

```json
{
  "message": "Login successful",
  "user": {
    "email": "user@example.com",
    "name": "User Name",
    "access_token": "jwt_access_token",
    "refresh_token": "jwt_refresh_token"
  }
}
```

---

## Password Reset Request

### Endpoint: `POST /api/user/request-password-reset/`

**Description:** Requests a password reset by email.

**Request Body:**

```json
{
  "email": "user@example.com"
}
```

**Response:**

```json
{
  "message": "Password reset email sent successfully."
}
```

---

## Reset Password

### Endpoint: `POST /api/user/reset-password/`

**Description:** Resets the user's password.

**Request Body:**

```json
{
  "uid": "encoded_user_id",
  "token": "reset_token",
  "password": "new_secure_password"
}
```

**Response:**

```json
{
  "message": "Password reset successful."
}
```

---

## Fetch User Profile

### Endpoint: `GET /api/user/profile/`

**Description:** Retrieves the authenticated user's profile.

**Response:**

```json
{
  "id": 1,
  "name": "User Name",
  "email": "user@example.com",
  "gender": "Male",
  "birthday": "1995-06-15"
}
```

### Notes:

- All API responses include appropriate HTTP status codes.
- JWT authentication is required for most endpoints.
- Ensure email server details are properly configured in `settings.py` before using password reset functionality.

## Contributing

Feel free to open issues and contribute to the project.

--- 
Made with ❤️ by [[Thanusian](https://github.com/Thanusiyan1007), [Lilaniya](https://github.com/LilaniRanjan), Rohana & [Oshada - Me](https://github.com/SLDrago/)]
