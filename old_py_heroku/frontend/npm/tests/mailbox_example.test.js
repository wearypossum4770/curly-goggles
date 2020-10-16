const mailbox = await I.haveNewMailbox();
const mailbox1 = await I.haveNewMailbox();
const mailbox2 = await I.haveNewMailbox();
// mailbox2 is now default mailbox
// switch back to mailbox1
I.openMailbox(mailbox);

// to wait for default time (10 secs by default)
I.waitForLatestEmail();

// or specify number of time to wait
I.waitForLatestEmail(30);

// wait for an email with partial match in subject
I.waitForEmailMatching({ subject: 'Restore password' });

// wait 30 seconds for email with exact subject
I.waitForEmailMatching({ subject: '=Forgot password' }, 30);

// wait a last email from any address @mysite.com
I.waitForEmailMatching({
 from: '@mysite.com', // find anything from mysite
 subject: 'Restore password', // with Restore password in subject
});

const email = await I.waitForLatestEmail();
// extract a link by RegExp
const url = email.body.match(/http(s):\/\/(.*?)\s/)[0];
// open URL
I.amOnPage(url);

//~ I.waitForLatestEmail()
//~ I.seeEmailIsFrom('@mysite.com');
//~ I.seeInEmailSubject('Awesome Proposal!');
//~ I.seeInEmailBody('To unsubscribe click here');
// Listing all emails 
const emails = await I.grabAllEmailsFromMailbox();
// Sending an email
I.sendEmail({
  to: ['user@site.com'],
  subject: 'Hello',
  body: 'World'
});
