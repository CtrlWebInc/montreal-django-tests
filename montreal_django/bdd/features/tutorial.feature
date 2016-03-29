Feature: Behave example
    In order to play with Behave
    As beginners
    We'll test Google Search

    Scenario: Find ctrlweb
        Given I search for "ctrlweb"
        Then the result page will include "CTRL+WEB"

    Scenario: Find Montreal-Django
        Given I search for "Montreal-Django"
        Then the result page will include "Django Meetups"
