Feature: Authentication API - reqres.in

  Scenario: Register a new user
    When I register with email "eve.holt@reqres.in" and password "pistol"
    Then the response status should be 200
    And the response should contain a token

  Scenario: Login successfully
    When I login with email "eve.holt@reqres.in" and password "cityslicka"
    Then the response status should be 200
    And the response should contain a token

    Scenario: Login with missing password
    When I login with email "eve.holt@reqres.in" and no password
    Then the response status should be 400
    And the error message should mention "password"

  Scenario: Get paginated users list
    When I request reqres users page 1
    Then the response status should be 200
    And the response should contain a page number

  Scenario: Create a new user on reqres
    When I create a reqres user with name "John" and job "QA"
    Then the response status should be 201
    And the response should contain the created user details