Feature: Login
    Identify the visitor and store their data

Scenario: Successful Login
    Given username and password
    When Log In button clicked
    Then select some products
    
    Then go to shopping cart
    Then click on checkout
   
    
