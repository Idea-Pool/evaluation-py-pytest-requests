> Write test cases which test the following actions/checks:
> - [x] check GET
> - [x] check POST
> - [x] check DELETE
> - [ ] check authentication
> - [x] check query parameters: mandatory, optional
> - [ ] check schema

# Test cases

## `TC-1` The "GET movie by id" request should return with status code 200
1. **Given** the {movie_id} is added to the GET request
2. **When** the "GET movie by id" request is sent
3. **Then** the response should contain status code 200

## `TC-2` The "GET movie by id" response should contain the proper movie title
1. **Given** the {movie_id} is added to the GET request
2. **When** the "GET movie by id" request is sent
3. **Then** the response should contain the proper movie title

## `TC-3` The "POST movie rating" request should return with status code 201
1. **Give** the {movie_id} is added to the POST request
2. **And** the {"value": 8.0} is added to the POST request's body
3. **When** the "POST movie rating" request is sent
4. **Then** the response should contain status code 201

## `TC-4` The "POST movie rating" response should contain the proper status message
1. **Give** the {movie_id} is added to the POST request
2. **And** the {"value": 8.0} is added to the POST request's body
3. **When** the "POST movie rating" request is sent
4. **Then** the response should contain the "Success." status message

## `TC-5` The "POST movie rating" should handle the invalid rating
1. **Give** the {movie_id} is added to the POST request
2. **And** the {"value": 10.1} is added to the POST request's body
3. **When** the "POST movie rating" request is sent
4. **Then** the response should contain the proper status message

## `TC-6` The "DELETE movie rating by id" request should return with status code 200
1. **Given** the {movie_id} is added to the DELETE request
2. **When** the "DELETE movie rating by id" request is sent
3. **Then** the response should contain status code 200

## `TC-7` The "DELETE movie rating by id" response should contain the proper status message
1. **Given** the {movie_id} is added to the DELETE request
2. **When** the "DELETE movie rating by id" request is sent
3. **Then** the response should contain the "The item/record was deleted successfully." status message

## `TC-8` The "GET movie by id" request should return with status code 404 if the movie_id parameter is not added
1. **Given** the {movie_id} is not added to the GET request
2. **When** the "GET movie by id" request is sent
3. **Then** the response should contain status code 404