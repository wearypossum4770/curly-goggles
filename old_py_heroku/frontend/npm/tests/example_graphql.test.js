//~ I.sendQuery()
//~ I.sendMutation()


let postData = null;

Scenario('check post page', async (I)  => {
  // valid access token
  I.haveRequestHeaders({auth: '1111111'});
  // get the first user
  let response = await I.sendQuery('{ user(id:1) { id }}');
  let user = response.data;
  // create a post and save its Id
  response = await I.sendMutation(
    'mutation createPost($input: PostInput!) { createPost(input: $input) { id }}',
    {
      input : {
        author: user.data.id,
        body: 'some text',
      }
    },
  );
  postData = response.data.data['createPost'];
  // open browser page of new post
  I.amOnPage(`/posts/${postData.slug}.html`);
  I.see(postData.body, 'p.body');
});

// cleanup created data
After((I) => {
  I.sendMutation(
    'mutation deletePost($permalink: /ID!) { deletePost(permalink: /$id) }',
    { permalink: /postData.id},
  );
});
