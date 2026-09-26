Feature: User Management API - JSONPlaceholder

  Scenario: Get all users
    When I request the list of users
    Then the response status should be 200
    And the response should contain 10 users

  Scenario: Get a single user by ID
    When I request user with ID 1
    Then the response status should be 200
    And the user name should not be empty

  Scenario: Create a new user
    When I create a user with name "Test User" and email "test@example.com"
    Then the response status should be 201
    And the response should contain the created user details

  Scenario: Update a user with PUT
    When I update user 1 with name "Updated Name"
    Then the response status should be 200
    And the updated name should be "Updated Name"

  Scenario: Partially update a user with PATCH
    When I partially update user 1 with email "patch@example.com"
    Then the response status should be 200
    And the updated email should be "patch@example.com"

  Scenario: Delete a user
    When I delete user 1
    Then the response status should be 200