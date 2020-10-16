Functional Testing: To make sure that all the API endpoints are up and working and doing what exactly they are supposed to so.

Reliability Testing: Making sure that the API works when connecting to various devices and doesn’t get disconnected.

Load Testing: When various servers send a request to an API, it is necessary to make sure that the API responds to all of them.

Stress Testing: When more than a set number of requests is received by the API, how does it behave? Does it send a message? It's mandatory to check whether it works as intended.

Security Testing: While giving authentication, it is important to make sure that no security breaches happen in between and that no more than the required data is shared. Have appropriate authentications, permissions, and access controls.

Integration Testing: Ensures that all the APIs connected to each other must communicate properly and the addition of features in the API does not cause bugs in other API modules.

Usability Testing: The API is functional, and on top of it, user-friendly.

Data type errors – Ensure only valid data can be entered for specific data types such as currency and dates. Field widths – If a certain text box permits a specified amount of characters, then make it clear on the user interface that the data entered shouldn’t exceed the character limit. ( For instance, a field that allows 50 characters in the application’s database should not allow users to enter more than 50 characters on the interface). Navigational elements – Verify all navigational buttons on the page are working correctly, and that they redirect users to the right page or screen. Progress bars – When displaying screens that take time to render results, a progress bar should be used to show the user that a process is still running. Type-ahead – If your UI uses drop-down lists, ensure you include type ahead. In a drop-down menu with hundreds of items, typing the first letter should skip the list to items beginning with that letter such that users will not have to check through a long list. Table scrolling – If data in your tables extends to another page, then the scroll function should allow users to scroll the data but keep all headers intact. Error logging – When the system experiences a fatal error, ensure the application writes the error details to an event viewer or log file for later review. Menu items – Ensure the application only displays valid menu items that are available at a particular state. Working shortcuts – For applications that support shortcuts, verify whether they work correctly, no matter the browser, platform, or device being used. Confirm action buttons – Ensure the UI has working confirm button every time the user wants to save or delete an item

Test scenarios on the Login module Enter the valid login details (Username, password), and check that the home page is displayed. Enter the invalid Username and password and check for the home page. Leave Username and password blank, and check for the error message displayed. Enter the valid Login, and click on the cancel, and check for the fields reset. Enter invalid Login, more than three times, and check that account blocked. Enter valid Login, and check that the Username is displayed on the home screen. Test scenarios on Compose module Checks that all users can enter email ides in the To, Cc, and Bcc. Check that the entire user can enter various email ids in To, Cc, and Bcc. Compose a mail, send it, and check for the confirmation message. Compose a mail, send it, and check in the sent item of the sender and the inbox. Compose a mail, send it, and check for invalid and valid email id (valid format), check the mail in sender inbox. Compose main, discard, and then check for conformation message and check-in draft. Compose mail click on save as draft and check for the confirmation message Compose mail click on close and check for conformation save as drafts. Test scenarios on Inbox module Click on the inbox, and verify all received mail are displayed and highlighted in the inbox. Check that a latest received mail has been displayed to the sender email id correctly. Select the mail, reply and forward send it; check in the sent item of sender and inbox of the receiver. Check for any attached attachments to the mail that are downloaded or not. Check that attachment is scanned correctly for any viruses before download. Select the mail, reply and forward save as draft, and check for the confirmation message and checks in the Draft section. Check all the emails are marked as read are not highlighted. Check all mail recipients in Cc are visible to all users. Checks all email recipients in Bcc are not visible to the users. Select mail, delete it, and then check in the Trash section. Test scenario on Trash module Open trash, check all deleted mail present. Restore mail from Trash; check-in the corresponding module. Select mail from trash, delete it, and check mail is permanently deleted.