# GitHub OAuth Application Setup Guide

This document will guide you through the steps to create and configure a GitHub OAuth application for using GitHub login functionality in your project.

## Step 1: Create a GitHub OAuth Application

1.  **Log in to your GitHub account**.
2.  Navigate to your developer settings page:
    *   Click on your profile avatar in the top right corner.
    *   Select **Settings**.
    *   In the left sidebar, select **Developer settings**.
3.  On the Developer settings page, select **OAuth Apps**, then click the **New OAuth App** button.

## Step 2: Fill in Application Information

On the "Register a new OAuth application" page, you need to fill in the following information:

*   **Application name**: Give your application a descriptive name, such as `Insforge Dev Login`.
*   **Homepage URL**: Your application's homepage URL. In development environment, you can set it to `http://localhost:7130` or your frontend development server address.
*   **Application description** (optional): Provide a brief description of your application.
*   **Authorization callback URL**: This is the URL where GitHub will redirect users after authorization. For local development, make sure to set it to:
    ```
    http://localhost:7130/api/auth/oauth/github/callback
    ```
    **Note**: This URL must exactly match the callback URL configured in your backend service, otherwise the OAuth flow will fail.

After filling in the information, click **Register application**.

## Step 3: Get Client ID and Client Secret

After creating the application, you will be redirected to the application's settings page. Here you can see the **Client ID**.

To get the **Client Secret**, click the **Generate a new client secret** button. GitHub will generate a secret and display it to you.

**Important**: The Client Secret will only be shown once. Please copy it immediately and keep it secure. If you lose it, you will need to generate a new one.

## Step 4: Configure Environment Variables

After obtaining the Client ID and Client Secret, you need to add them to your project's `.env` file. Make sure your `.env` file (or corresponding environment configuration file) contains the following two lines:

```env
GITHUB_CLIENT_ID=YOUR_GITHUB_CLIENT_ID
GITHUB_CLIENT_SECRET=YOUR_GITHUB_CLIENT_SECRET
GITHUB_REDIRECT_URI=http://localhost:7130/api/auth/oauth/github/callback
```

Replace `YOUR_GITHUB_CLIENT_ID` and `YOUR_GITHUB_CLIENT_SECRET` with the actual values you obtained in the previous step.

After completing the above steps, your application is ready to use GitHub OAuth for user authentication.
