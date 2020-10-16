let postId = null;

Scenario('check post page', async (I)  => {
  // valid access token
  I.haveRequestHeaders({auth: '1111111'});
  // get the first user
  let user = await I.sendGetRequest('/api/users/1');
  // create a post and save its Id
  postId = await I.sendPostRequest('/api/posts', { author: user.id, body: 'some text' });
  // open browser page of new post
  I.amOnPage('/posts/2.html');
  I.see('some text', 'p.body');
});

// cleanup created data
After((I) => {
  I.sendDeleteRequest('/api/posts/'+postId);
});

//~ I.sendGetRequest()
//~ I.sendPostRequest()
//~ I.sendPutRequest()
//~ I.sendPatchRequest()
//~ I.sendDeleteRequest()
