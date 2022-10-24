Feature: Home page
  Scenario: Redirect to Add/Remove Elements
    Given I am on the home page
    When I click the link for Add/Remove Elements
    And I click on Add element
    And The delete button appears
    And I click on the delete button
    Then I am redirected to the "forgot-password" page

