# HTTP Status Codes — Quick Notes

## 2xx Success
- 200 OK: Generic success (GET/PUT/PATCH/DELETE)
- 201 Created: Resource created (POST)
- 204 No Content: Success without a body

## 4xx Client Errors
- 400 Bad Request: Invalid input
- 401 Unauthorized: Missing/invalid auth
- 403 Forbidden: Authenticated, but not allowed
- 404 Not Found: Resource doesn’t exist
- 409 Conflict: State conflict (e.g., duplicate)

## 5xx Server Errors
- 500 Internal Server Error: Unexpected failure
- 503 Service Unavailable: Temporary outage/overload
