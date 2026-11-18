# ADR 0002: Custom Storage Driver Implementation for Supabase Storage

## Status

Accepted

## Context

Giselle uses Unstorage for storage and is designed to allow different storage drivers for each application. While migrating our cloud storage to Supabase[^1], we attempted to use Unstorage's official S3 driver with Supabase's S3 API, but discovered that the [getKeys](https://unstorage.unjs.io/guide#getkeysbase-opts) functionality (which retrieves a list of files in a specific path) did not work properly with Supabase's implementation.

## Decision

We decided to implement a custom driver specifically for Supabase Storage using Unstorage's extension mechanism for custom drivers.

## Alternatives Considered

We considered bypassing Unstorage and using the Supabase client directly. However, this approach would require Supabase authentication credentials for local development environments, which would degrade the developer experience. Therefore, we decided to continue with the multi-storage architecture using Unstorage.

## Consequences

We have implemented the Supabase Storage custom driver directly in both the playground app and the studio.giselles.ai app. In the future, we plan to either package this driver or contribute it as a pull request to the Unstorage project to create a more generalized solution.

[^1]: [ADR 0001: Migrate from Vercel Storage to Supabase Storage](./0001-migrate-from-vercel-storage-to-supabase-storage.md)