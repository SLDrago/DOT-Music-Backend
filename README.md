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

# DOT-Music Backend API Documentation

This document provides an overview of the available API endpoints for the DOT-Music Backend.

## Base URL

```
http://yourdomain.com/api/
```

## Authentication & User Management

### Register a New User

**Endpoint:** `POST /api/users/register/`  
**Description:** Registers a new user.  
**Request Body (JSON):**

```json
{
  "username": "example_user",
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response (Success):**

```json
{
  "message": "User registered successfully",
  "user_id": 1
}
```

### Login

**Endpoint:** `POST /api/users/login/`  
**Description:** Authenticates a user and returns a JWT token.  
**Request Body (JSON):**

```json
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

**Response (Success):**

```json
{
  "access": "jwt_access_token",
  "refresh": "jwt_refresh_token"
}
```

### Refresh Token

**Endpoint:** `POST /api/users/token/refresh/`  
**Description:** Refreshes the JWT access token.  
**Request Body (JSON):**

```json
{
  "refresh": "jwt_refresh_token"
}
```

### Edit User Profile

**Endpoint:** `PATCH /api/users/edit-user/`  
**Description:** Updates user profile details.

### Request Password Reset

**Endpoint:** `POST /api/users/request-password-reset/`  
**Description:** Sends a password reset link to the user's email.

### Reset Password

**Endpoint:** `POST /api/users/reset-password/`  
**Description:** Allows users to reset their password.

### Get User Profile

**Endpoint:** `GET /api/users/user-profile/`  
**Description:** Retrieves the logged-in user's profile details.

---

## Artist Management

### Artist Login

**Endpoint:** `POST /api/artist/login/`  
**Description:** Authenticates an artist.

### Get Artist Types

**Endpoint:** `GET /api/artist/types/`  
**Description:** Retrieves available artist types.

### Register an Artist

**Endpoint:** `POST /api/artist/register/`  
**Description:** Registers a new artist.

---

## Music Data & Content

### Get Recent Artists

**Endpoint:** `GET /api/artists/`  
**Description:** Retrieves the last five artists added.

### Get Recent Albums

**Endpoint:** `GET /api/albums/`  
**Description:** Retrieves the last five albums added.

### Get Popular Radio Stations

**Endpoint:** `GET /api/popular-radio/`  
**Description:** Retrieves the last five popular radio stations.

### Get "Today in Music" Highlights

**Endpoint:** `GET /api/today-in-music/`  
**Description:** Retrieves the last five "Today in Music" highlights.

### Get All Artists

**Endpoint:** `GET /api/full-artists/`  
**Description:** Retrieves all artists.

### Get All Albums

**Endpoint:** `GET /api/full-albums/`  
**Description:** Retrieves all albums.

### Get All Radio Stations

**Endpoint:** `GET /api/full-radio/`  
**Description:** Retrieves all radio stations.

### Get Songs by Artist

**Endpoint:** `GET /api/songs/artist/{artist_id}/`  
**Description:** Retrieves songs associated with a specific artist.  
**Path Parameter:**

- `artist_id` (integer) - The ID of the artist.

---

## Song Management

### Get All Songs

**Endpoint:** `GET /api/songs/`  
**Description:** Retrieves a list of all songs.

### Upload a New Song

**Endpoint:** `POST /api/songs/upload/`  
**Description:** Uploads a new song.  
**Request Body (JSON):**

```json
{
  "title": "Song Title",
  "artist": "Artist Name",
  "file": "song.mp3"
}
```

### Update a Song

**Endpoint:** `PATCH /api/songs/{song_id}/update/`  
**Description:** Updates a song's details.  
**Path Parameter:**

- `song_id` (integer) - The ID of the song to update.

### Delete a Song

**Endpoint:** `DELETE /api/songs/{song_id}/delete/`  
**Description:** Deletes a specific song.  
**Path Parameter:**

- `song_id` (integer) - The ID of the song to delete.

---

## Admin Panel

### Django Admin Access

**Endpoint:** `GET /admin/`  
**Description:** Provides access to the Django Admin panel for managing content and users (requires admin privileges).

---

## Media Files (Development Only)

If `DEBUG=True`, media files are served at:

```
/media/
```

---

### Notes:

- All API responses include appropriate HTTP status codes.
- JWT authentication is required for most endpoints.
- Ensure email server details are properly configured in `settings.py` before using password reset functionality.

## Contributing

Feel free to open issues and contribute to the project.
