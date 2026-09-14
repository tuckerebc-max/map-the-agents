# Set up enterprise SSO for camelAI

This guide explains how an organization administrator can connect camelAI to an
OpenID Connect (OIDC) identity provider. The main instructions use Google
Workspace; a provider-neutral reference is included at the end.

## Before you begin

You will need:

- A camelAI Enterprise organization.
- Owner or admin access to the camelAI organization.
- Permission to configure OAuth applications for your Google Workspace or
  other identity provider.
- A normal user in the identity provider that you can use for the connection
  test.

Decide who may join through SSO:

- **Allow uninvited SSO users on:** A regular camelAI member is created the
  first time any user allowed by the IdP and domain rules signs in. The user
  receives access to the organization's first active workspace. They do not
  automatically receive access to other or future workspaces.
- **Allow uninvited SSO users off:** Existing members and users with an active
  camelAI invitation may sign in. An invited user's tenant account is created
  automatically during their first SSO sign-in, and the invitation's role and
  workspace access are applied.

Users do not need to sign in twice. An existing organization member is matched
and linked during their first successful SSO sign-in.

## Part 1: Copy the camelAI callback URL

1. Sign in to camelAI as an organization owner or admin.
2. Open **Settings → Organization → Single sign-on**.
3. Copy the **Callback URL** shown on the page.

For the production camelAI service, it is currently:

```text
https://camelai.dev/api/auth/enterprise-oidc/callback
```

Always use the value displayed in camelAI. The URI must match exactly,
including its scheme, hostname, path, and trailing-slash behavior.

## Part 2: Create the Google Workspace OAuth client

Google Workspace SSO uses an OAuth 2.0 web application in a Google Cloud
project owned by your organization.

1. Open the
   [Google Auth Platform](https://console.cloud.google.com/auth/overview) and
   select or create a project under your Google Cloud organization.
2. Configure the app identity or branding if Google prompts you:
   - Use a recognizable name such as `camelAI SSO`.
   - Set a support email managed by your organization.
3. Under **Audience**, select **Internal**. This restricts authorization to
   accounts in your Google Workspace or Cloud Identity organization.
4. If the console asks you to configure data access, add the standard
   `openid`, `email`, and `profile` scopes. camelAI does not request Gmail,
   Drive, or other Workspace data.
5. Open **Clients**, select **Create client**, and choose **Web application**.
6. Give the client a recognizable name such as `camelAI production`.
7. Under **Authorized redirect URIs**, add the callback URL copied from
   camelAI.
8. You can leave **Authorized JavaScript origins** empty; the camelAI OIDC
   exchange is performed by its server.
9. Create the client, then securely copy its **Client ID** and
   **Client secret**.

Google may take several minutes to apply a newly added redirect URI.

## Part 3: Configure camelAI

Return to **Settings → Organization → Single sign-on** and enter:

| camelAI field                 | Google Workspace value                                                     |
| ----------------------------- | -------------------------------------------------------------------------- |
| Issuer URL                    | `https://accounts.google.com`                                              |
| Client ID                     | The Google OAuth client ID                                                 |
| Client secret                 | The Google OAuth client secret                                             |
| Token endpoint authentication | **Client secret POST**                                                     |
| Email claim                   | **email**                                                                  |
| Allowed email domains         | Usually leave blank for the first test                                     |
| Allow uninvited SSO users     | Enable only if every identity allowed by the IdP and domain rules may join |

### About allowed email domains

This field is an additional camelAI filter, not the primary source of access
control. Your identity provider controls who may authenticate or use the OAuth
application.

For Google Workspace, leaving the field blank is recommended for the first
test. camelAI validates Google's signed `email_verified` and hosted-domain
(`hd`) claims. When the test succeeds, camelAI automatically records the
verified hosted domain.

If your organization intentionally uses more than one Workspace domain, add
each permitted domain as a comma-separated value and test with the relevant
accounts:

```text
example.com, subsidiary.example.com
```

Do not add consumer domains such as `gmail.com`.

## Part 4: Test the connection

1. Select **Test connection** in camelAI.
2. Google will open in the browser. Sign in with a normal account from the
   Workspace organization being connected.
3. Approve the basic identity request if Google shows a consent screen.
4. Google redirects back to the camelAI SSO settings page.

The test should confirm:

- Discovery document found
- Authorization endpoint found
- Token endpoint found
- JWKS signing keys loaded
- Token exchange succeeded
- The signed-in user's email and domain
- Whether the provider verified the email

The test performs a real OIDC authorization and token exchange, but it does
**not** create a user, link an account, enable SSO, or replace the current
configuration.

If you edit any configuration field after a successful test, run the test
again.

## Part 5: Enable SSO

After the test passes:

1. Select **Enable SSO**.
2. Copy the **Organization sign-in URL** displayed by camelAI. It has this
   format:

   ```text
   https://camelai.dev/sso/your-organization-slug
   ```

3. Share that URL with users or add it to your internal application launcher.
4. Test the URL in a private browser window with a non-administrator user.

Do not disable the customer's existing sign-in method or announce a company-wide
cutover until at least one administrator and one regular user have completed this
end-to-end test.

## What happens on a user's first SSO sign-in

camelAI verifies the OIDC issuer, signature, audience, authorization
transaction, stable provider subject, email, and configured domain rules.

- If the provider identity is already linked, camelAI signs in that member.
- If an existing camelAI organization member has the asserted email, camelAI
  safely links that provider identity and signs them in.
- If no member exists but an active invitation matches the asserted email,
  camelAI creates a tenant-scoped account, consumes the invitation, and applies
  its role and workspace access.
- If no member or invitation exists and uninvited users are allowed, camelAI
  creates a tenant-scoped regular member and grants access to the first active
  workspace.
- If no member or invitation exists and uninvited users are not allowed,
  sign-in is denied.

Enterprise SSO sessions are restricted to the organization that issued them.

## Managing and removing access

### Add a user

- If uninvited users are allowed, permit the user in the identity provider and
  give them the organization sign-in URL.
- If uninvited users are not allowed, invite the exact email address in
  camelAI, choose its role and workspace access, and then give the user the
  organization sign-in URL. The user does not need to accept the email link or
  create a separate camelAI login first; the verified SSO identity consumes the
  invitation.

### Remove a user

Remove or disable the user in the identity provider **and** remove their camelAI
organization membership. Removing the camelAI membership immediately blocks
that SSO identity from re-provisioning itself.

Removing only the identity-provider assignment does not revoke a camelAI
session that has already been issued. The current camelAI SSO session duration
is eight hours.

### Disable the connection

In **Settings → Organization → Single sign-on**, select **Disable SSO**.
Disabling SSO immediately invalidates sessions issued through that connection.
It does not delete the organization or its users.

### Rotate the client secret

Update the client secret in the identity provider, enter the new secret in
camelAI, run **Test connection**, and apply the tested configuration.

If you change the issuer, client ID, or token authentication method, camelAI
requires the client secret to be entered again. This prevents an existing
secret from being sent to a newly entered endpoint.

## Troubleshooting

### “Could not validate the OIDC issuer and discovery document”

- For Google, use exactly `https://accounts.google.com`.
- Enter the issuer URL, not the discovery document URL. Do not append
  `/.well-known/openid-configuration`.
- Confirm that the issuer uses HTTPS and is publicly reachable.
- For another provider, verify that
  `<issuer>/.well-known/openid-configuration` returns a valid OIDC discovery
  document whose `issuer` value matches the configured issuer.

### Google reports `redirect_uri_mismatch`

- Copy the callback URL from camelAI again.
- Confirm it is listed under **Authorized redirect URIs** on the correct
  **Web application** client.
- Remove accidental trailing slashes, spaces, query parameters, or staging
  hostnames.
- Wait several minutes after changing the Google client, then retry.

### Google reports that access is blocked or the app is unavailable

- Confirm the Google Cloud project belongs to the customer's organization.
- Set the app audience to **Internal** for organization-only use.
- Confirm the test user belongs to that Workspace organization.
- If the app is configured for external testing instead, add the user as an
  OAuth test user and account for Google's testing restrictions.
- Check Google Admin Console OAuth application access controls if the
  organization blocks untrusted OAuth clients.

### “Google Workspace did not verify this email and hosted domain”

- Sign out of personal Google accounts and retry with the intended Workspace
  account.
- Confirm the user's primary Google identity belongs to the expected hosted
  domain.
- Confirm the domain in camelAI matches the identity returned by Google.

### “No organization member or active invitation matches this enterprise identity”

Uninvited SSO users are not allowed, and no active invitation has the exact
email asserted by the IdP. Send a new camelAI invitation to that address or
allow uninvited SSO users and retest the configuration.

### “This email is already bound to a different enterprise identity”

The same email has been presented with a different provider subject. This can
happen after deleting and recreating an identity-provider account or replacing
the OIDC connection. Do not repeatedly recreate the user. Contact camelAI
support to review the existing identity binding.

### The connection test passed, but “Enable SSO” is unavailable

One or more fields changed after the test. Run **Test connection** again and
enable the exact configuration that passed.

## Configuration reference for other OIDC providers

camelAI can connect to a standards-compliant OIDC provider that supplies:

- An HTTPS issuer with an OIDC discovery document
- Authorization, token, and JWKS endpoints in discovery
- Authorization Code flow
- A stable `sub` claim
- An `email` or `preferred_username` claim containing a valid email address
- The `openid`, `email`, and `profile` scopes
- Either `client_secret_post` or `client_secret_basic` token authentication

Register the callback URL shown in camelAI with the provider. Then select the
provider's documented token authentication method and email claim. Use
**preferred_username** only when the provider, commonly Microsoft Entra,
returns the user's email there rather than in `email`.

## Google references

- [Manage OAuth clients](https://support.google.com/cloud/answer/15549257)
- [Manage the app audience](https://support.google.com/cloud/answer/15549945)
- [Google OpenID Connect reference](https://developers.google.com/identity/openid-connect/reference)
