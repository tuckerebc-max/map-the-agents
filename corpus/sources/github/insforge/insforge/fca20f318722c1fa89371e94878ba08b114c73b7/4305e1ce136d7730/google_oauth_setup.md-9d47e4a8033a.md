# Google OAuth Login Setup Guide

## Overview

This project has integrated Google OAuth login functionality, supporting user authentication through Google accounts.

## Environment Variable Configuration

Add the following configuration to your `.env` file:

```env
# Google OAuth Configuration
GOOGLE_CLIENT_ID=your_google_client_id
GOOGLE_CLIENT_SECRET=your_google_client_secret
GOOGLE_REDIRECT_URI=http://localhost:7130/api/oauth/google/callback
```

## Google Cloud Console Setup

1. Visit [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing project
3. Enable Google+ API and Google Identity API
4. Create an OAuth 2.0 Client ID in the "Credentials" page
5. Configure authorized redirect URIs:
       - Development environment: `http://localhost:7130/api/auth/oauth/google/callback`
    - Production environment: `https://yourdomain.com/api/auth/oauth/google/callback`

## API Endpoints

### 1. Get Google OAuth Authorization URL

**Endpoint:** `GET /api/auth/v1/google-auth`

**Parameters:**
- `redirect_url`: Redirect URL after successful login

**Response:**
```json
{
  "success": true,
  "data": {
    "auth_url": "https://accounts.google.com/oauth/authorize?..."
  }
}
```

**Example:**
```bash
curl "http://localhost:7130/api/auth/v1/google-auth?redirect_url=http://localhost:7131/dashboard"
```

### 2. Google OAuth Callback Handling

**Endpoint:** `GET /api/auth/oauth/google/callback`

**Parameters:**
- `code`: Authorization code returned by Google
- `state`: State parameter (optional)

**Process:**
1. Receive Google authorization code
2. Exchange for access token and ID token
3. Verify ID token and retrieve user information
4. Find or create user record
5. Generate JWT token
6. Redirect to specified URL with token information

**Redirect URL Format:**
```
{redirect_url}?token={jwt_token}&user_id={user_id}&email={email}&name={name}
```

## User Flow

### New User Registration
1. User clicks "Sign in with Google"
2. Redirect to Google authorization page
3. After user authorization, system creates new user record:
   - Create basic authentication record in `auth` table
   - Create Google identity record in `identifies` table
   - Create user profile record in `profiles` table
4. Return JWT token and user information

### Existing User Login
1. User clicks "Sign in with Google"
2. Redirect to Google authorization page
3. After user authorization, system:
   - Searches for user in `identifies` table by `provider` and `provider_id`
   - Updates `last_login_at` timestamp
4. Return JWT token and user information

### Email Association
- If user already exists but not associated with Google account, system will automatically associate
- If Google account is already associated with another user, an error will be returned

## Frontend Integration Example

```javascript
// 1. Get authorization URL
const response = await fetch('/api/auth/v1/google-auth?redirect_url=/dashboard');
const { auth_url } = await response.json();

// 2. Redirect to Google authorization page
window.location.href = auth_url;

// 3. Handle returned token in callback page
const urlParams = new URLSearchParams(window.location.search);
const token = urlParams.get('token');
const userId = urlParams.get('user_id');

if (token) {
  // Store token
  localStorage.setItem('auth_token', token);
  // Navigate to main page
  window.location.href = '/dashboard';
}
```

## Error Handling

Common error codes:

- `MISSING_FIELD`: Missing required parameters
- `INVALID_CREDENTIALS`: Google token verification failed
- `ALREADY_EXISTS`: User already exists

## Security Considerations

1. Ensure `GOOGLE_CLIENT_SECRET` environment variable is stored securely
2. Use HTTPS in production environment
3. Validate redirect URL legitimacy
4. Regularly rotate JWT keys
5. Monitor abnormal login activities

## Troubleshooting

1. **"Invalid redirect_uri" Error**
   - Check redirect URI configuration in Google Cloud Console
   - Ensure it matches the `GOOGLE_REDIRECT_URI` environment variable

2. **"Invalid client" Error**
   - Verify `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET` are correct
   - Ensure necessary APIs are enabled in Google Cloud Console project

3. **"Token verification failed" Error**
   - Check network connectivity
   - Verify Google API service status
   - Confirm client ID configuration is correct
